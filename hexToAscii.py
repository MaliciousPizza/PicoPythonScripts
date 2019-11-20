import codecs


hexInput = input('What is the hex value to convert? ')

ascii_out = codecs.decode(hexInput,'hex').decode('utf-8')



print('picoCTF{' + str(ascii_out) + '}')