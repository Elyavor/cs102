def encrypt_caesar(plaintext: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        c = plaintext[i]
        f1 = bool('a' <= c <= 'z')
        f2 = bool('A' <= c <= 'Z')
        if f1:
            ciphertext = ciphertext + chr(ord('a') + (ord(c) - ord('a') + 3) % 26)
        if f2:
            ciphertext = ciphertext + chr(ord('A') + (ord(c) - ord('A') + 3) % 26)
        if not (f1 or f2):
             ciphertext = ciphertext + c
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        c = ciphertext[i]
        f1 = bool('a' <= c <= 'z')
        f2 = bool('A' <= c <= 'Z')
        if f1:
            plaintext = plaintext + chr((ord(c) - ord('a') - 3) % 26 + ord('a'))
        if f2:
             plaintext = plaintext + chr((ord(c) - ord('A') - 3) % 26 + ord('A'))
        if not (f1 or f2):
            plaintext = plaintext + c
    return plaintext
if __name__ == '__main__':
    print(encrypt_caesar("python2.5"))
