def encrypt(text, shift):
    '''
    Create a function that takes in two parameters
    Text and Shift. text is is an string and shift is a int
    shifts the text by given int.
    '''
    result = ''
    for char in text:
        if char.isalpha() and char.isupper():
            result += chr((ord(char) - ord('A') + shift ) % 26 + ord('A'))
        elif char.isalpha() and char.islower():
            result += chr((ord(char) - ord('a') + shift ) % 26 + ord('a'))
        else:
            result += char
    return result
    
        
def decrypt(result, shift):
    '''
    this funtion will decrypt by calling encrypt and reversing the shift.
    '''
    return encrypt(result, -shift)



    
