def encrypt_caesar(plaintext, shift):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for elem in plaintext:
        if ord(elem) < 97:
            ciphertext += chr(65 + (ord(elem) + shift - 65) % 26)
        else:
            ciphertext += chr(97 + (ord(elem) + 3 - 97) % 26)
    return ciphertext


def decrypt_caesar(ciphertext, shift):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for elem in ciphertext:
        if ord(elem) < 97:
            plaintext += chr(65 + (ord(elem) - shift - 65 + 26) % 26)
        else:
            plaintext += chr(97 + (ord(elem) - shift - 97 + 26) % 26)
    return plaintext
