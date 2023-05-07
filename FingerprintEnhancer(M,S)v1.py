import cv2
import numpy as np
from cv2 import ximgproc
import os

# Set input and output directories
input_dir = 'Images'
output_dir = 'EnhancedImages'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize PSNR variable
total_psnr = 0

# Loop through input images and extract features
for filename in os.listdir(input_dir):
    # Load image in grayscale
    image = cv2.imread(os.path.join(input_dir, filename), cv2.IMREAD_GRAYSCALE)

    # Binarization using Otsu's method
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Skeletonization using the Zhang-Suen algorithm
    skeleton = cv2.ximgproc.thinning(binary_image)

    # Minutiae detection using the Crossing Number method
    minutiae_image = cv2.ximgproc.thinning(binary_image)
    minutiae_image = cv2.ximgproc.thinning(minutiae_image)
    minutiae_image = cv2.ximgproc.thinning(minutiae_image)
    minutiae_image = cv2.ximgproc.thinning(minutiae_image)
    minutiae_image = cv2.ximgproc.thinning(minutiae_image)

    rows, cols = skeleton.shape
    minutiae = []
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if skeleton[i][j] == 0:
                continue
            values = [skeleton[i - 1][j - 1], skeleton[i - 1][j], skeleton[i - 1][j + 1], skeleton[i][j - 1],
                      skeleton[i][j + 1], skeleton[i + 1][j - 1], skeleton[i + 1][j], skeleton[i + 1][j + 1]]
            if values.count(255) == 1:
                minutiae.append((j, i))

    # Draw minutiae on skeleton image
    minutiae_image = np.zeros_like(minutiae_image)
    for minutia in minutiae:
        cv2.circle(minutiae_image, minutia, 1, 255, -1)

    # Concatenate input image and enhanced image horizontally
    enhanced_image = cv2.hconcat([image, binary_image, skeleton, minutiae_image])

    # Calculate PSNR
    psnr = cv2.PSNR(image, binary_image)
    total_psnr += psnr

    # Save output images
    cv2.imwrite(os.path.join(output_dir, 'skeleton_' + filename), skeleton)
    cv2.imwrite(os.path.join(output_dir, 'minutiae_' + filename), minutiae_image)
    cv2.imwrite(os.path.join(output_dir, 'enhanced_' + filename), enhanced_image)

    # Display output image
    cv2.imshow('Input and Enhanced Image', enhanced_image)
    cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

# Calculate average PSNR across all images
num_images = len(os.listdir(input_dir))
average_psnr = total_psnr / num_images
print('Average PSNR: {:.2f}'.format(average_psnr))
