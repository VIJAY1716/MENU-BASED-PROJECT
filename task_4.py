import cv2

# Step 1: Capture an Image from the Webcam
def capture_image():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        return None

    ret, frame = cap.read()

    if ret:
        # Save the captured frame as 'abc.jpg'
        cv2.imwrite('abc.jpg', frame)
        print("Image saved as abc.jpg")
    else:
        print("Failed to capture image")
        frame = None

    cap.release()
    cv2.destroyAllWindows()
    
    return frame

# Step 2: Apply Filters to the Saved Image
def apply_filters(image_path):
    # Load the saved image
    image = cv2.imread(image_path)

    if image is None:
        print(f"Failed to load image from {image_path}")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray_abc.jpg', gray)

    # Apply Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imwrite('gaussian_blur_abc.jpg', gaussian_blur)

    # Apply Median Blur
    median_blur = cv2.medianBlur(image, 15)
    cv2.imwrite('median_blur_abc.jpg', median_blur)

    # Apply Bilateral Filter
    bilateral_filter = cv2.bilateralFilter(image, 15, 75, 75)
    cv2.imwrite('bilateral_filter_abc.jpg', bilateral_filter)

    # Apply Edge Detection (Canny)
    edges = cv2.Canny(image, 100, 200)
    cv2.imwrite('edges_abc.jpg', edges)

    # Display the original and filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale', gray)
    cv2.imshow('Gaussian Blur', gaussian_blur)
    cv2.imshow('Median Blur', median_blur)
    cv2.imshow('Bilateral Filter', bilateral_filter)
    cv2.imshow('Edge Detection', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main Function
def main():
    # Capture and save the image
    capture_image()

    # Apply filters to the saved image
    apply_filters('abc.jpg')

if __name__ == "__main__":
    main()
