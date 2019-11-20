
baseNum = int(input('What is the base number? '))

binary = bin(baseNum)

binary = binary[2:]

print('picoCTF{' + binary + '}')


