alphalist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def alphabet_position(letter):
    for position, item in enumerate(alphalist):
        if item == letter.lower():
            return position

def rotate_character(char, rot):

    if str(char).isalpha():
        char_pos = alphabet_position(char) + int(rot)
        if char_pos <= 25:
            # determine if char is in lower case
            if ord(char) in range(97,123):
                return alphalist[char_pos].lower()
            else:
                return alphalist[char_pos].upper()
        else:
            # if char_pos > 25 start from 0 again
            char_pos = (char_pos - 25) - 1
            # determine if char is in lower case
            if ord(char) in range(97,123):
                return alphalist[char_pos].lower()
            else:
                return alphalist[char_pos].upper()
    else:
        return char

def encrypt(text, rot):
    encrypt_text = ''

    for i in text:
        encrypt_text = encrypt_text + rotate_character(i, rot)

    return encrypt_text
