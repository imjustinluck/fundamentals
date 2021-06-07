# 1
def countdown(num):
    for x in range (num, -1, -1):
        print(x)

countdown(10)

# 2
def print_and_return(lis):
    print(lis[0])
    return lis[1]

x = print_and_return([3,4])
print(x)

# 3
def first_plus_length(lis):
    sum = lis[0] + len(lis)
    return sum

print(first_plus_length([1,2,3,4,5]))

# 4
def values_greater_than_second(lis):
    if len(lis) < 2:
        return False
    else:
        newlist = []
        num = 0
        for i in range (0, len(lis)):
            if lis[i] > lis[1]:
                num += 1
                newlist.append(lis[i])
        print(num)
        return newlist

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5
def length_and_value(num1, num2):
    newlist = []
    for i in range (0, num1):
        newlist.append(num2)
    return newlist

print(length_and_value(4,7))
print(length_and_value(6,2))