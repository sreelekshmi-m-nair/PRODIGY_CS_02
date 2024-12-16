from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Converting the image to a NumPy array
    img_array = np.array(img)

    # Ensure key has the same shape as img_array
    key = np.resize(key, img_array.shape)

    # Encrypting each pixel using XOR with the key
    encrypted_array = np.bitwise_xor(img_array, key)
    
    # Converting the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")


def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Converting the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_img)

    # Ensure key has the same shape as encrypted_array
    key = np.resize(key, encrypted_array.shape)

    # Decrypting each pixel using XOR with the key
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    
    # Converting the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")


def main():
    print("Image Encryption and Decryption using Pixel Manipulation")

    #image_path = enter image path in your system
    image_path = input("Enter the path to the image file: ")
    # Generate a random key (you can use any integer as the key)
    key = np.random.randint(0, 256, size=(3,), dtype=np.uint8)
    
    # Encrypt the image
    encrypt_image(image_path, key)
    
    # Decrypt the image
    decrypt_image("encrypted_image.png", key)

if __name__ == "__main__":
    main()
