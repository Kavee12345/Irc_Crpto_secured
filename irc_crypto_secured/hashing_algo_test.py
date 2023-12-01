import hashlib

def sha256_encrypt(input_string):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes of the input string
    sha256_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    encrypted_string = sha256_hash.hexdigest()

    return encrypted_string

# Example usage
input_string = "Hello, World!"
encrypted_string = sha256_encrypt(input_string)

print(f"Input String: {input_string}")
print(f"SHA-256 Encrypted String: {encrypted_string}")
