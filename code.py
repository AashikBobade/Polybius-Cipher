# function to display polybius cipher text
def polybiusCipher(s, mode):
    cipher_text = ""
    i = 0
    # convert each character to its encrypted code or decrypted text
    while i < len(s):
        if s[i] == ' ':
            cipher_text += ' '
            i += 1
            continue
        if mode == 'encrypt':
            # Convert character to corresponding row and column numbers
            row = int((ord(s[i]) - ord('a')) / 5) + 1
            col = ((ord(s[i]) - ord('a')) % 5) + 1
            # if character is 'k'
            if s[i] == 'k':
                row = row - 1
                col = 5 - col + 1
            # if character is greater than 'j'
            elif ord(s[i]) >= ord('j'):
                if col == 1:
                    col = 6
                    row = row - 1
                col = col - 1
            cipher_text += str(row) + str(col)
            i += 1
        elif mode == 'decrypt':
            # Extract row and column numbers from the cipher text
            row = int(s[i])
            col = int(s[i + 1])
            # Calculate corresponding letter
            letter_index = (row - 1) * 5 + col - 1
            if letter_index >= 9:
                letter_index += 1  # Adjust for 'j'
            letter = chr(letter_index + ord('a'))
            cipher_text += letter
            i += 2  # Move to the next pair of digits
    return cipher_text

# Driver's Code
if __name__ == "__main__":
    text = input("Enter the text: ").lower()

    # Encrypt the text
    encrypted_text = polybiusCipher(text, 'encrypt')
    print("Encrypted Text:", encrypted_text)

    # Decrypt the text
    decrypted_text = polybiusCipher(encrypted_text, 'decrypt')
    print("Decrypted Text:", decrypted_text)
