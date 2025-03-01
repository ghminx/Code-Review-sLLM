# Find the largest number in the list
def find_max_number(lst):
    max_num = lst[0]  
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j] > max_num:
                max_num = lst[j] 
    return max_num 

data = [3, 1, 7, 2, 5, 10, 6]
max_value = find_max_number(data)
print("최대값:", max_value)
