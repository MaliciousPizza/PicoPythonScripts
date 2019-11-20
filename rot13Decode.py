import pyperclip
import codecs

rottenCode = input('Input the Code: ')

ripeCode = codecs.encode(rottenCode,'rot_13')


print(ripeCode)

pyperclip.copy(ripeCode)

