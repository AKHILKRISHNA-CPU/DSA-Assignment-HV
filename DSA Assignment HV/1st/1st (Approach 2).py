# Iterative Method

def duplicate_entries(arr):
    arr.sort()
    n = len(arr)
    present = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] == present:
            cnt += 1
        else:
            if cnt != 1:
                print("The frequency of", present, "element is -", cnt)
            present = arr[i]
            cnt = 1
    print("The frequency of", present, "element is -", cnt)
Array1= list(map(int, input("Enter the array elements separated by space: ").split()))
duplicate_entries(Array1)