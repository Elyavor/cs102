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
        f1 = bool('a' <= c <= 'z')
        f2 = bool("A" <= c <= "Z")
        if f1:
            ciphertext = ciphertext + chr(ord('a') + (ord(c) - ord('a') + ord(keyword[i % len(keyword)]) - ord('a')) % 26)
        if f2:
            ciphertext = ciphertext + chr(ord('A') + (ord(c) - ord('A') + ord(keyword[i % len(keyword)]) - ord("A")) % 26)
        if not (f1 or f2):
            ciphertext = ciphertext + c
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
        f1 = bool('a' <= c <= 'z')
        f2 = bool("A" <= c <= "Z")
        if f1:
            plaintext = plaintext + chr(ord('a') + (ord(c) - ord('a') - ord(keyword[i % len(keyword)]) + ord('a')) % 26)
        if f2:
            plaintext = plaintext + chr(ord('A') + (ord(c) - ord('A') - ord(keyword[i % len(keyword)]) + ord("A")) % 26)
        if not (f1 or f2):
            plaintext = plaintext + c
    return plaintext    
