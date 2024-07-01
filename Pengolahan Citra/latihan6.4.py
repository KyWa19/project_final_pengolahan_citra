import cv2
import numpy as np

# Load image
image = cv2.imread('ky2.jpg', cv2.IMREAD_GRAYSCALE)

# Define homogeneity operator
homogeneity_operator = np.array([[1, 1, 1],
                                  [1, -8, 1],
                                  [1, 1, 1]])

# Define difference operator
difference_operator = np.array([[0, 1, 0],
                                [1, -4, 1],
                                [0, 1, 0]])

# Apply homogeneity operator
edges_homogeneity = cv2.filter2D(image, -1, homogeneity_operator)

# Apply difference operator
edges_difference = cv2.filter2D(image, -1, difference_operator)

# Display original image and edges
cv2.imshow('Original Image', image)
cv2.imshow('Edges (Homogeneity Operator)', edges_homogeneity)
cv2.imshow('Edges (Difference Operator)', edges_difference)
cv2.waitKey(0)
cv2.destroyAllWindows()