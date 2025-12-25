import cv2

# 1. Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# 2. Check if camera opened successfully
if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

while True:
    # 3. Read one frame from the camera
    ret, frame = cap.read()

    # ret = True if frame is read correctly
    if not ret:
        print("❌ Can't receive frame (stream end?). Exiting ...")
        break

    # 4. Flip frame horizontally (mirror view)
    frame = cv2.flip(frame, 1)

    # 5. Display the frame
    cv2.imshow("Air Drums - Camera Test", frame)

    # 6. Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 7. Release resources
cap.release()
cv2.destroyAllWindows()
