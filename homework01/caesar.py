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

        if ('a' <= c <= 'z'):
            ciphertext = ciphertext + chr(ord('a') + (ord(c) - ord('a') + 3) % 26)
        if ('A' <= c <= 'Z'):
            ciphertext = ciphertext + chr(ord('A') + (ord(c) - ord('A') + 3) % 26)
    return ciphertext

y= encrypt_caesar('python')
print(y)
k= encrypt_caesar('privet')
print(k)


def decrypt_caesar(ciphertext: str) -> str:
    """
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
        if 'a' <= c <= 'z':
            plaintext = plaintext + chr((ord(c) - ord('a') - 3) % 26 + ord('a'))
        if 'A' <= c <= 'Z':
             plaintext = plaintext + chr((ord(c) - ord('A') - 3) % 26 + ord('A'))

    return plaintext
x = decrypt_caesar('SBWKRQ')
print(x)
u= decrypt_caesar('sulyhw')
print(u)
