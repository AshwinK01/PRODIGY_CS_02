from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice, please choose 'e' for encryption or 'd' for decryption.")
        return

    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the key (an integer): "))
    output_path = input("Enter the path to save the output image: ")

    if choice == 'e':
        encrypt_image(image_path, key, output_path)
    else:
        decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()
