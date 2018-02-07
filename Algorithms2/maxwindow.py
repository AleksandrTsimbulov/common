# Maxwindow
# Calculates and prints max number in sliding window lenght m along massive length n
import sys

reader = sys.stdin
n = int(reader.readline().strip())
A = [int(item) for item in reader.readline().strip().split()]
m = int(reader.readline().strip())

# realisation of queue with two stacks and max/min stacks for each part
stack_in = [-1]
stack_out = [-1]
max_in = [-1]
max_out = [-1]
ans_list = []
A.reverse()

def fill_it():
    # filling the queue with first m numbers
    for i in range(m):
        number = A.pop()
        stack_in.append(number)
    for j in range(m):
        resend_number = stack_in.pop()
        stack_out.append(resend_number)
        if max_out[-1] >= resend_number:
            max_out.append(max_out[-1])
        else:
            max_out.append(resend_number)

def refill():
    # resending all of the numbers from inc to out stack after the last is out of numbers
    for i in range(m):
        resend_number = stack_in.pop()
        max_in.pop()
        stack_out.append(resend_number)
        if max_out[-1] >= resend_number:
            max_out.append(max_out[-1])
        else:
            max_out.append(resend_number)


fill_it()
while A:
    maxi = max_in[-1]
    maxo = max_out[-1]
    ans_max = max(maxi, maxo)
    ans_list.append(ans_max)
    incoming_number = A.pop()
    stack_in.append(incoming_number)
    if max_in[-1] >= incoming_number:
        max_in.append(max_in[-1])
    else:
        max_in.append(incoming_number)
    gone_number = stack_out.pop()
    max_out.pop()
    if stack_out[-1] == -1:
        refill()
# after A is empty have to add last 'window'
maxi = max_in[-1]
maxo = max_out[-1]
ans_max = max(maxi, maxo)
ans_list.append(ans_max)

print(' '.join(str(i) for i in ans_list))