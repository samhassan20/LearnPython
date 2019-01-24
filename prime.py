# To return a list of only PRIME NUMBERS in a given range of numbers
def prime(s, e):
    primelist = []
    for num in range(s, e + 1):
        flag = 0
        if num > 1 and flag == 0:
            for i in range(2, num):
                if num % i == 0:
                    flag = 1
                # else:
                #     continue
            if flag == 0:
                primelist.append(num)
    print(primelist)


prime(1, 100)