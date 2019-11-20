import pyperclip

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ciphertext = 'ynkooejcpdanqxeykjrubvtagp'

"""for i in range(0,26):
    newMessage = ''
    for character in ciphertext:
        position = alphabet.find(character)
        newPosition = (position + i) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    print( str(i) + ' ' + newMessage + '\n')"""

newMessage = ''
for character in ciphertext:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + 4 ) % 26
        newCharacter= alphabet[newPosition]
        newMessage += newCharacter

flag = 'picoCTF{'+ newMessage + '}')

print(flag)

pyperclip.copy(flag)
