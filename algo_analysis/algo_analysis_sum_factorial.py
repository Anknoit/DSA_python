# 1st Method

my_list = []


def sum_fact(n):
    for i in range(1, n + 1):
        # i = i+1
        print(i)
        my_list.append(i)
    print("Sum of n values = ", sum(my_list))
    return i


sum_fact(3)

# 2nd Method
