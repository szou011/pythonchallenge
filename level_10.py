def next_number_generator(start):
    next_num = list()
    quantity = 1 # start count
    for digit in range(len(start)):
        if digit == 0: # pass if it is the first digit
            pass
        elif start[digit] == start[digit - 1]: # compare digits
            quantity += 1

        else :
            next_num.append(quantity)
            next_num.append(start[digit -1])
            quantity = 1 # reset count

        if digit == (len(start) - 1):
            next_num.append(quantity)
            next_num.append(start[digit])

    return next_num

start_num = [1]

for i in range(30):
    next_num = next_number_generator(start_num)
    start_num = next_num
    print(len(next_num))
