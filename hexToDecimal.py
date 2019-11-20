import pyperclip

hexString = input('What is the hex value to convert to decimal? ')

hexString  = int(hexString,16)

stringHex = 'picoCTF{' + str(hexString) + '}'

print(stringHex)

pyperclip.copy(stringHex)