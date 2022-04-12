num_list = []
num = int(input("Enter a number: "))
num_list.append(num)
while num != 1:
    ### if even
    if num % 2 == 0:
        num = num // 2
        num_list.append(num)
    ### if odd
    else:
        num = 3 * num + 1
        num_list.append(num)
print(num_list)



