import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(center, max_iter, width, height, scale):
    """
    Generate the Mandelbrot set.

    Parameters:
        center (complex): The center point of the image.
        max_iter (int): The maximum number of iterations.
        width (int): The width of the image in pixels.
        height (int): The height of the image in pixels.
        scale (float): The scale of the image.

    Returns:
        numpy.ndarray: The Mandelbrot set image.
    """
    # Initialize an empty array to store the Mandelbrot set
    result = np.zeros((height, width), int)
    
    # Loop through each pixel in the image
    for j in range(height):
        for i in range(width):
            # Calculate the complex number corresponding to the current pixel
            c = center + (i - width // 2 + (j - height // 2) * 1j) * scale
            z = 0
            # Iterate the Mandelbrot function for the current complex number
            for k in range(max_iter):
                z = z**2 + c
                # Check if the magnitude of z exceeds 2 (escape condition)
                if (z * z.conjugate()).real > 4.0:
                    break
            # Store the number of iterations it took for z to escape in the result array
            result[j, i] = k
    
    return result

# Define parameters for the Mandelbrot set
HEIGHT = 1080
WIDTH = 1080  # Adjust height for 16:9 aspect ratio
MAX_ITER = 4000
CENTER = -1.1195 + 0.2718j
EXTENT = 0.005 + 0.005j
SCALE = max((EXTENT / WIDTH).real * 0.75, (EXTENT / HEIGHT).imag * 0.75)
CMAP = "gray_r"

# Generate the Mandelbrot set
result = mandelbrot(CENTER, MAX_ITER, WIDTH, HEIGHT, SCALE)

# Set extent for desired cropping
plot_extent = (WIDTH + 1j * HEIGHT) * SCALE
z1 = CENTER - plot_extent / 2
z2 = z1 + plot_extent

# Plot the Mandelbrot set
fig, ax = plt.subplots(1, 1, figsize=(16, 9))  # Set figure size for 16:9 aspect ratio
ax.imshow(
    result**(1 / 3),
    origin='lower',
    extent=(z1.real, z2.real, z1.imag, z2.imag),
    cmap=CMAP,  # Use reversed grayscale colormap for white background
)
ax.set_axis_off()
# Optionally, save the plot as an image file
# plt.savefig("mandelbrot_set.png", dpi=1200)  # Save the plot as a PNG file with high resolution
plt.show()
