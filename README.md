Detailed Explanation

Image Loading and Conversion:

The image is loaded using PIL.Image.open(). The image is then converted into a NumPy array for pixel manipulation.

Encryption Operations:

Swapping Pixels: Randomly shuffles pixel values based on a seed derived from the provided key. Mathematical Operation: Adds a key value to each pixel and ensures the values wrap around using modulo 256.

Image Display:

Utilizes matplotlib.pyplot to display the encrypted image directly in the output window.

User Interaction:

The script prompts the user for the image path, operation type, and key value. After encryption, the resulting image is displayed, allowing the user to see the encrypted image immediately. This simplified version focuses solely on the encryption process and real-time visualization of the encrypted image.
