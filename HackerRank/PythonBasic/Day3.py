#Task 5: Find the Runner-Up Score! -- 힌트보고 해결

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    sc = None

    for num in arr:
        if num == mx:
            pass
        elif sc == None:
            sc = num
        elif num > sc:
            sc = num

    print(sc)

'''Reference code
n = int(input())
A = list(map(int, input().split()))
A = list(set(A))
A.sort()
print(A[-2]) #[-2]: next to last'''
