import cv2

def capture_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return None

    ret, frame = cap.read()

    if ret:
        cv2.imwrite('abc.jpg', frame)
        print("Image saved as abc.jpg")
    else:
        print("Failed to capture image")
        frame = None

    cap.release()
    cv2.destroyAllWindows()
    
    return frame

def detect_and_crop_face(image):
    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("No faces detected.")
        return None, None

    # Assuming the first detected face is the target
    (x, y, w, h) = faces[0]
    face = image[y:y+h, x:x+w]
    
    return face, (x, y, w, h)

def overlay_face_on_image(original_image, face, face_position):
    x, y, w, h = face_position
    # Resize face to fit within the original image
    face = cv2.resize(face, (w, h), interpolation=cv2.INTER_AREA)

    # Place the face back onto the original image
    original_image[y:y+h, x:x+w] = face

    return original_image

def main():
    # Capture and save the image
    image = capture_image()
    if image is None:
        return

    # Detect and crop the face
    face, face_position = detect_and_crop_face(image)
    if face is None:
        print("No face detected, skipping overlay.")
        return

    # Save the cropped face separately
    cv2.imwrite('def.jpg', face)
    print("Cropped face saved as def.jpg")

    # Overlay the cropped face back onto the original image
    result_image = overlay_face_on_image(image, face, face_position)

    # Save and display the result
    cv2.imwrite('abc_with_cropped_face.jpg', result_image)
    cv2.imshow('Image with Cropped Face', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
