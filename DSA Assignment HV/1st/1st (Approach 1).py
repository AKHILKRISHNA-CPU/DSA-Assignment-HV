def count_duplicates(arr, n, ele):
    if n == 0:
        return 0
    if arr[n-1] == ele:
        return 1 + count_duplicates(arr, n-1, ele)
    else:
        return count_duplicates(arr, n-1, ele)

def find_duplicates(arr, n):
    result=[]
    for i in range(n):
        count = count_duplicates(arr, n, arr[i])
        if (count > 1):
            result.append((arr[i],count))
            print("The frequency of", arr[i], "is -", count)

input_array =list(map(int, input("Enter the array elements separated by space: ").split()))
n = len(input_array)
find_duplicates(input_array, n)
