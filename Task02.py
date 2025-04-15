from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open the image and convert to a numpy array
    image = Image.open(input_path)
    image_array = np.array(image)
    
    # Encrypt the pixels
    encrypted_array = (image_array + key) % 256
    
    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # Open the image and convert to a numpy array
    image = Image.open(input_path)
    image_array = np.array(image)
    
    # Decrypt the pixels
    decrypted_array = (image_array - key) % 256
    
    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# User input for paths and key
print("IMAGE ENCRYPTION TOOL")
mode = input("Choose mode (encrypt/decrypt): ").lower()
input_path = input("Enter the path of the input image: ")
output_path = input("Enter the path to save the output image: ")
key = int(input("Enter the encryption/decryption key (a number): "))

# Perform encryption or decryption
if mode == "encrypt":
    encrypt_image(input_path, output_path, key)
elif mode == "decrypt":
    decrypt_image(input_path, output_path, key)
else:
    print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")


"""
CS Task 2 Description
Develop a simple image encryption tool using pixel manipulation. 
You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. 
Allow users to encrypt and decrypt images.

"""