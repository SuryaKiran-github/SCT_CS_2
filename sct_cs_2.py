from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def encrypt_image(image_path, operation, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    if operation == "swap":
        encrypted_pixels = swap_pixels(pixels, key)
    elif operation == "math":
        encrypted_pixels = apply_math_operation(pixels, key)
    else:
        raise ValueError("Unsupported operation. Use 'swap' or 'math'.")

    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    return encrypted_image

def swap_pixels(pixels, key):
    np.random.seed(key)
    shape = pixels.shape
    flat_pixels = pixels.flatten()
    indices = np.arange(flat_pixels.size)
    np.random.shuffle(indices)
    flat_pixels = flat_pixels[indices]
    return flat_pixels.reshape(shape)

def apply_math_operation(pixels, key):
    return (pixels * key) % 256

def display_image(image):
    plt.imshow(image)
    plt.axis('off')
    plt.show()

def main():
    while True:
        try:
            image_path = input("Enter the path to the image: ")
            operation = input("Enter the operation (swap/math): ").lower()
            if operation not in ['swap', 'math']:
                print("Invalid operation. Please choose 'swap' or 'math'.")
                continue

            key = int(input("Enter the key value (integer): "))

            result_image = encrypt_image(image_path, operation, key)
            print("Encrypted Image:")
            display_image(result_image)
            break

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
