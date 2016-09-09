import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

binary = list()
for char in message:
    ascii = bin( ord(char) )[2:]
    # Complete to 7-bit
    binary += "0" * (7  - len(ascii)) + ascii

answer = ""
start = 0
if binary[start] == "0":
    answer += "00 "
elif binary[start] == "1":
    answer += "0 "
        
for i in range(len(binary)):
    if binary[i] == binary[start]:
        answer += "0"
    else:
        start = i
        if binary[i] == "0":
            answer += " 00 0"
        elif binary[i] == "1":
            answer += " 0 0"

print(answer)

# Decoder
def decode(message):
    answer = ''
    binary = ''
    value = ''
    valueSet = False
    counter = 0
    for char in message:
        if valueSet:
            if char == '0':
                binary += value
            elif char == ' ':
                value = ''
                valueSet = False
        else:
            if char == '0':             
                if value == '':
                    value = '1'
                elif value == '1':
                    value = '0'
                elif value == '0':
                    raise Exception()
            elif char == ' ':
                valueSet = True
    for chunk in [binary[i:i + 7] for i in range(0, len(binary), 7)]:
        n = int('0b' + str(chunk), 2)
        answer += n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return answer