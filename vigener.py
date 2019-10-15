def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    for i in range(len(plaintext)):
        c = plaintext[i]
        if 'a' <= c <= 'z':
            ciphertext = ciphertext + chr(ord('a') + (ord(c) - ord('a') + ord(keyword[i % len(keyword)]) - ord('a')) % 26)
        elif "A" <= c <= "Z":
            ciphertext = ciphertext + chr(ord('A') + (ord(c) - ord('A') + ord(keyword[i % len(keyword)]) - ord("A")) % 26)
        else:
            ciphertext += c
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    for i in range(len(ciphertext)):
        c = ciphertext[i]
        if 'a' <= c <= 'z':
            plaintext = plaintext + chr(ord('a') + (ord(c) - ord('a') - ord(keyword[i % len(keyword)]) + ord('a')) % 26)
        elif "A" <= c <= "Z":
            plaintext = plaintext + chr(ord('A') + (ord(c) - ord('A') - ord(keyword[i % len(keyword)]) + ord("A")) % 26)
        else:
            plaintext += c
    return plaintext
