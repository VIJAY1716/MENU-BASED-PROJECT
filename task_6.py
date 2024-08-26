import cv2
import numpy as np

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

def overlay_image_alpha(img, img_overlay, pos, alpha_mask):
    x, y = pos

    # Image ranges
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    # Overlay ranges
    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if nothing to overlay
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return img

    # Blend overlay within the determined ranges
    img_crop = img[y1:y2, x1:x2]
    img_overlay_crop = img_overlay[y1o:y2o, x1o:x2o]
    alpha = alpha_mask[y1o:y2o, x1o:x2o, np.newaxis]

    img_crop[:] = alpha * img_overlay_crop + (1 - alpha) * img_crop
    return img

def apply_sunglasses_filter(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Failed to load the image.")
        return

    # Load the sunglasses image with transparency (alpha channel)
    sunglasses = cv2.imread(r'V:\OneDrive\Desktop\menu_based_project\ml\Sunglasses-PNG-File.png', cv2.IMREAD_UNCHANGED)
    if sunglasses is None:
        print("Failed to load the sunglasses image.")
        return

    # Check if the sunglasses image has an alpha channel
    if sunglasses.shape[2] != 4:
        print("Sunglasses image does not have an alpha channel.")
        return

    sunglasses_alpha = sunglasses[:, :, 3] / 255.0
    sunglasses_rgb = sunglasses[:, :, :3]

    # Resize sunglasses if larger than the image
    if sunglasses.shape[0] > image.shape[0] or sunglasses.shape[1] > image.shape[1]:
        scale = min(image.shape[0] / sunglasses.shape[0], image.shape[1] / sunglasses.shape[1]) * 0.5
        sunglasses = cv2.resize(sunglasses, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        sunglasses_alpha = sunglasses[:, :, 3] / 255.0
        sunglasses_rgb = sunglasses[:, :, :3]

    # Place the sunglasses roughly over the center
    center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
    image_with_sunglasses = overlay_image_alpha(image, sunglasses_rgb, (center_x - sunglasses.shape[1] // 2, center_y - sunglasses.shape[0] // 2), sunglasses_alpha)

    # Save and display the image with sunglasses
    cv2.imwrite('abc_with_sunglasses.jpg', image_with_sunglasses)
    cv2.imshow('Image with Sunglasses', image_with_sunglasses)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def apply_star_filter(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Failed to load the image.")
        return

    # Load the star image with transparency (alpha channel)
    star = cv2.imread(r'V:\OneDrive\Desktop\menu_based_project\ml\R.png', cv2.IMREAD_UNCHANGED)
    if star is None:
        print("Failed to load the star image.")
        return

    # Check if the star image has an alpha channel
    if star.shape[2] != 4:
        print("Star image does not have an alpha channel.")
        return

    star_alpha = star[:, :, 3] / 255.0
    star_rgb = star[:, :, :3]

    # Resize star if larger than the image
    if star.shape[0] > image.shape[0] or star.shape[1] > image.shape[1]:
        scale = min(image.shape[0] / star.shape[0], image.shape[1] / star.shape[1]) * 0.5
        star = cv2.resize(star, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        star_alpha = star[:, :, 3] / 255.0
        star_rgb = star[:, :, :3]

    # Place multiple stars in random locations
    np.random.seed(0)  # For reproducibility
    for _ in range(5):
        rand_x = np.random.randint(0, image.shape[1] - star.shape[1])
        rand_y = np.random.randint(0, image.shape[0] - star.shape[0])
        image = overlay_image_alpha(image, star_rgb, (rand_x, rand_y), star_alpha)

    # Save and display the image with stars
    cv2.imwrite('abc_with_stars.jpg', image)
    cv2.imshow('Image with Stars', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main function to run the entire process
def main():
    # Capture and save the image
    capture_image()

    # Apply sunglasses filter and save result
    apply_sunglasses_filter('abc.jpg')

    # Apply star filter and save result
    apply_star_filter('abc.jpg')

if __name__ == "__main__":
    main()
