#Reverse a List
def reverse_list(list):
    result = []
    for i in range(len(list)-1, -1, -1):  # from last index to 0
        result.append(list[i])
    return result

print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]
