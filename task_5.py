import numpy as np
import matplotlib.pyplot as plt

# Dimensions of the image
width = 400
height = 300

# Create a NumPy array for the image with RGB channels
image = np.zeros((height, width, 3), dtype=np.uint8)

# Set the color (RGB values)
color = (255, 0, 0)  # Red color

# Fill the image with the specified color
image[:, :] = color

# Display the image using matplotlib
plt.imshow(image)
plt.axis('off')  # Hide axis ticks and labels
plt.show()
