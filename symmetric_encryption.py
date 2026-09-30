import base64
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(bit_length=256)
aes = AESGCM(key)


def encrypt(message: str) -> str:
    nonce = os.urandom(12)
    ciphertext = aes.encrypt(nonce, message.encode("utf-8"), None)
    return base64.urlsafe_b64encode(nonce + ciphertext).decode("ascii")


def decrypt(message: str) -> str:
    encrypted_message = base64.urlsafe_b64decode(message.encode("ascii"))
    nonce, ciphertext = encrypted_message[:12], encrypted_message[12:]
    plaintext = aes.decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")