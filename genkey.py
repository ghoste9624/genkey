import argparse
import random
import string
from cryptography.fernet import Fernet # Requires: pip install cryptography

def generate_key():
    """Generates a random key for encryption."""
    key = Fernet.generate_key()
    return key.decode() # Return key as string

def encode_message(message, key):
    """Encodes a message using the provided key."""
    f = Fernet(key.encode())
    encoded_message = f.encrypt(message.encode())
    return encoded_message

def decode_message(encoded_message, key):
    """Decodes an encoded message using the provided key."""
    f = Fernet(key.encode())
    decoded_message = f.decrypt(encoded_message)
    return decoded_message.decode()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hidden Message Encoder/Decoder")

    parser.add_argument(
        "--key",
        action="store_true",
        help="Generate a new encryption key"
    )

    parser.add_argument(
        "--encode",
        nargs=2,
        metavar=("message", "key"),
        help="Encode a message with a given key. Example: --encode 'Hello world' <your_key>"
    )

    parser.add_argument(
        "--decode",
        nargs=2,
        metavar=("encoded_message", "key"),
        help="Decode an encoded message with the key. Example: --decode <encoded_message> <your_key>"
    )

    args = parser.parse_args()

    if args.key:
        print("Generated Key:", generate_key())
    elif args.encode:
        message_to_encode, key = args.encode
        encoded = encode_message(message_to_encode, key)
        print("Encoded Message:", encoded)
    elif args.decode:
        encoded_message, key = args.decode
        decoded = decode_message(encoded_message, key)
        print("Decoded Message:", decoded)
    else:
        parser.print_help() # Show help if no arguments are provided
