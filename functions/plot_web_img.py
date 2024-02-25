import numpy as np
import matplotlib.pyplot as plt

def plot_web_img(images):
    """
    Plot a list of images with their corresponding labels.

    Args:
    images: List of images to plot
    labels: List of labels corresponding to the images
    """
    
    num_images = len(images)
    rows = int(np.ceil(num_images / 5.0))  # Use np.ceil to round up to the nearest whole number
    fig, axes = plt.subplots(rows, 5, figsize=(15, rows*3))
    axes = axes.ravel()  # Flatten the axes array

    # Hide axes for unused subplots
    for ax in axes[num_images:]:
        ax.axis('off')

    for i, image in enumerate(images):
        axes[i].imshow(image, cmap='gray')
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()