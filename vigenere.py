def encrypt_vigenere(plaintext, keyword):
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    keyword = keyword.upper()
    length = len(keyword)
    for i in range(len(plaintext)):
        elem = plaintext[i]
        if ord(elem) < 97:
            ciphertext += chr(65 + (ord(elem) + ord(keyword[i % length]) -
                                    65 - 65 + 26) % 26)
        else:
            ciphertext += chr(97 + (ord(elem) + ord(keyword[i % length]) -
                                    65 - 97 + 26) % 26)
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    keyword = keyword.upper()
    length = len(keyword)
    for i in range(len(ciphertext)):
        elem = ciphertext[i]
        if ord(elem) < 97:
            plaintext += chr(65 + (ord(elem) - ord(keyword[i % length]) +
                                   65 - 65 + 26) % 26)
        else:
            plaintext += chr(97 + (ord(elem) - ord(keyword[i % length]) +
                                   65 - 97 + 26) % 26)
    return plaintext
