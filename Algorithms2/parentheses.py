# Parentheses
# Illustrates basic stack in operation, checks if open parentheses match close ones
import sys

read_input = sys.stdin
# read_input = input()
# print(read_input)
OPEN_PRTH = ['(', '[', '{']
CLOSE_PRTH = [')', ']', '}']
prth_stack = []
SUCCSESS = 'Success'
inp_str = read_input.read()
# inp_str = read_input
was_answered = False
for number, char in enumerate(inp_str, start=1):
    if char in OPEN_PRTH:
        prth_stack.append((char, number))
    elif char in CLOSE_PRTH:
        if not prth_stack:
            print(number)
            was_answered = True
            break
        index_cl = CLOSE_PRTH.index(char)
        if OPEN_PRTH.index(prth_stack[-1][0]) == index_cl:
            prth_stack.pop()
        else:
            print(number)
            was_answered = True
            break
if not was_answered:
    if prth_stack:
        print(prth_stack[0][1])
    else:
        print(SUCCSESS)

