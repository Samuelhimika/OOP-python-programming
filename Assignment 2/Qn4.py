

from dataclasses import replace
from pickletools import int4


Digits= input('Enter  the numbers.....')
for digit in Digits:
  if digit == "0":
    digit= Digits.replace('0', 'x')  
    break
             
print(digit )
  