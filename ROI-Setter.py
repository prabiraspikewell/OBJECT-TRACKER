import cv2

# Initialize a list to store points
points = []

# Mouse callback function
def select_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left click
        points.append((x, y))
        print(f"Point selected: ({x}, {y})")
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)  # Draw a small circle on the selected point
        cv2.imshow("Frame", frame)
    elif event == cv2.EVENT_RBUTTONDOWN:  # Right click
        print("Right click detected. Exiting...")
        cv2.destroyAllWindows()
        exit()

# Open the video
cap = cv2.VideoCapture(r"C:\Users\Prabira\Downloads\people.mp4")

# Read the first frame
ret, frame = cap.read()

if not ret:
    print("Failed to read video.")
    cap.release()
    cv2.destroyAllWindows()
    exit()

# Display the frame
cv2.imshow("Frame", frame)

# Set the mouse callback function
cv2.setMouseCallback("Frame", select_points)

# Wait until any key is pressed or the window is closed
cv2.waitKey(0)

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
