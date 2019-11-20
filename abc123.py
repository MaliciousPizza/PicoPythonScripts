import pyperclip

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

pico = [16,9,3,15,3,20,6]

flag = [20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]

picoPrint = ''
flagPrint = ''

for num in pico:
    num = num -1
    picoPrint += alphabet[num]

for num in flag:
    num = num -1
    flagPrint += alphabet[num]

picoFlag = picoPrint + '{' + flagPrint + '}'

print(picoFlag)

pyperclip.copy(picoFlag)