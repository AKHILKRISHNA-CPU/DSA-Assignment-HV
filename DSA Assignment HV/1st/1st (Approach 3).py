# User-defined Function

def check_ele(arr):
    dict = {}
    for i in arr:
        dict[i] = dict.get(i, 0) + 1
    for key in dict:
        if dict[key] > 1:
            print("The frequency of", key, "element is -", dict[key])
Array1= list(map(int, input("Enter the array elements separated by space: ").split()))
duplicate_entries(Array1)