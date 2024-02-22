import numpy as np
import matplotlib.pyplot as plt

def plot_images(images, labels):
    num_images = len(images)
    rows = int(np.ceil(num_images / 5.0))  # Use np.ceil to round up to the nearest whole number
    fig, axes = plt.subplots(rows, 5, figsize=(15, rows*3))
    # axes = axes.ravel()  # Flatten the axes array

    # Hide axes for unused subplots
    for ax in axes[num_images:]:
        ax.axis('off')

    for i, (image, label) in enumerate(zip(images, labels)):
        axes[i].imshow(image, cmap='gray')
        axes[i].axis('off')
        axes[i].set_title(f'Label: {label}')

    plt.tight_layout()
    plt.show()