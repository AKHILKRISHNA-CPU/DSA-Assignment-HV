# Write a program (W.A.P) to find out the unique elements in the array by implementing the sorting technique. 
# Sample Input - [5, 4, 7, 5, 1, 3, 4]
# Sample Output - [1, 3, 4, 5, 7]


def unique_elements(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    unique_list = []
    for i in range(n):
        if i == 0 or arr[i] != arr[i-1]:
            unique_list.append(arr[i])

    return unique_list

input_array = list(map(int, input("Enter the array elements separated by space: ").split()))
print(unique_elements(input_array))
