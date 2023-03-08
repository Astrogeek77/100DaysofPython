import string
import random


def random_chars(key):
    str = ''.join(random.choices(string.ascii_lowercase, k=key))
    return str


def encode_word(user_input, key):
    print("key: ", key, type(key))
    sentence = user_input.split()
    code_words = []
    for word in sentence:
        if (len(word) < 3):
            code_word = word[::-1]
        else:
            str = word[1:] + word[0]
            code_word = random_chars(key) + str + random_chars(key)
        code_words.append(code_word)

    code_words = ' '.join(code_words)
    return code_words


def dcode_word(user_input, key):
    print("key: ", key, type(key))
    coded_sentence = user_input.split()
    decode_words = []
    for word in coded_sentence:
        if (len(word) < 3):
            decode_word = word[::-1]
        else:
            decode_word = word[key: -key]
            try:
                decode_word = str[-1] + str[0:-1]
            except IndexError:
                print('Your encryption key is greater than message :(')

        decode_words.append(decode_word)
    decode_words = ' '.join(decode_words)
    return decode_words


while True:
    response = input('Enter Choice to Encode(1) or Decode(2) or Quit(0): ')
    if (response == "1"):
        user_input = input('Enter message to encode: ')
        try:
            key = int(input('Enter a key value:'))
        except Exception as e:
            print(e)
        try:
            print(encode_word(user_input, key))
        except Exception as e:
            print(e)

    elif (response == "2"):
        user_input = input('Enter message to be decoded: ')
        try:
            key = int(input('Enter the key used for encryption:'))
            if (key > len(user_input)):
                print('Your key is invalid :(')
            else:
                print(dcode_word(user_input, key))
        except Exception as e:
            print(e)

    elif (response == "0"):
        print("quiting...")
        break
