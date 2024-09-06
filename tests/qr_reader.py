import cv2
import numpy as np
from pyzbar import pyzbar

def adjust_brightness(image, brightness=30):
    # Add a constant to increase brightness or subtract to decrease brightness
    image_bright = cv2.convertScaleAbs(image, alpha=1, beta=brightness)
    return image_bright

def adjust_contrast(image):
    # Compute the 1st and 99th percentile intensity values
    lower_percentile = np.percentile(image, 1)
    upper_percentile = np.percentile(image, 99)
    
    # Clip the image intensity values based on these percentiles
    image_adjusted = np.clip(image, lower_percentile, upper_percentile)
    
    # Normalize the image to span the full 0-255 range of grayscale intensities
    image_adjusted = ((image_adjusted - lower_percentile) / (upper_percentile - lower_percentile)) * 255
    image_adjusted = np.uint8(image_adjusted)
    
    return image_adjusted

def decode_qr_codes(frame):
    # Decode QR codes in the grayscale frame
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        # Extract data and the position of the QR code
        qr_data = obj.data.decode('utf-8')
        rect_points = obj.polygon

        # Draw the bounding box around the QR code (on the original frame for visualization)
        if len(rect_points) == 4:
            pts = [(point.x, point.y) for point in rect_points]
            cv2.polylines(frame, [np.array(pts)], True, (0, 255, 0), 3)
        
        # Put the decoded QR code data on the frame
        cv2.putText(frame, qr_data, (rect_points[0].x, rect_points[0].y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

def process_video_frame(frame, brightness=30):
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Adjust the brightness of the grayscale frame
    bright_frame = adjust_brightness(gray_frame, brightness)
    
    # Adjust the grayscale image for 1% saturation at low and high intensities
    adjusted_frame = adjust_contrast(bright_frame)
    
    # Scan for QR codes in the adjusted grayscale frame
    frame_with_qr = decode_qr_codes(adjusted_frame)
    
    return frame_with_qr

def video_capture_with_qr_and_brightness_adjustment():
    cap = cv2.VideoCapture(2)
    
    brightness = 30  # Initial brightness value

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process the frame to adjust brightness, grayscale, and QR scan
        adjusted_frame = process_video_frame(frame, brightness=brightness)
        
        # Display the adjusted grayscale image with QR code bounding boxes and data
        cv2.imshow('Video with QR Code Scanning and Brightness Adjustment', adjusted_frame)
        
        # Adjust brightness with keyboard input: '+' to increase, '-' to decrease
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('+'):
            brightness += 5
        elif key == ord('-'):
            brightness -= 5
    
    cap.release()
    cv2.destroyAllWindows()


video_capture_with_qr_and_brightness_adjustment()