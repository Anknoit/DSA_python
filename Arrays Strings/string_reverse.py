def arr_rev(N):
    newArr = []
    for i in range((len(N) - 1), -1, -1):
        newArr += N[i]
    # print(newArr)
    print(" ".join(newArr))
    return " ".join(newArr)


arr_rev("Hi Iam Ankit Jha!")
