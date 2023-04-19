import cv2
import numpy as np

class FingerprintImageEnhancer:
    def __init__(self):
        self.b1 = 0.03
        self.b2 = 0.03
        self.c1 = 10
        self.c2 = 10
        self.alpha = 0.1
        self.beta = 0.1
        self.iterations = 1

    def enhance(self, img):
        img = np.double(img)
        rows, cols = img.shape

        for i in range(self.iterations):
            mu = cv2.boxFilter(img, cv2.CV_64F, (self.c1, self.c1))
            mu_sq = mu * mu
            sigma = cv2.boxFilter(img * img, cv2.CV_64F, (self.c2, self.c2)) - mu_sq
            sigma[sigma < 0] = 0
            sigma = np.sqrt(sigma)
            structdis = (img - mu) / (sigma + 1.0 / 255)
            img = img + self.alpha * structdis
            img = img + self.beta * (img - cv2.boxFilter(img, cv2.CV_64F, (self.c1, self.c1)))

            lap = cv2.Laplacian(img, cv2.CV_64F)
            img = img + self.b1 * lap
            img = img + self.b2 * (img - cv2.boxFilter(img, cv2.CV_64F, (self.c1, self.c1)))
            img[img > 255] = 255
            img[img < 0] = 0

        img = np.uint8(np.round(img))
        return img

if __name__ == '__main__':
    enhancer = FingerprintImageEnhancer()
    img_path = input("Enter image path: ")
    img = cv2.imread(img_path, 0)
    
    # Enhance the fingerprint image
    enhanced_img = enhancer.enhance(img)
    
    # Apply unsharp masking to sharpen the image
    gaussian_img = cv2.GaussianBlur(enhanced_img, (0, 0), 5)
    sharpened_img = cv2.addWeighted(enhanced_img, 1.5, gaussian_img, -0.5, 0)

    # Display the enhanced and sharpened fingerprint image
    cv2.imshow('Enhanced and Sharpened Image', sharpened_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
