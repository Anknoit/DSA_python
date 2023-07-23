T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    arr = list(input().split())
    print(type(N), type(K), type(arr))
    # print(len(arr))
    if len(arr) <= N:
        # Write shit here
        new_arr = arr[-K:] + arr[:-K]

print(" ".join(new_arr))
