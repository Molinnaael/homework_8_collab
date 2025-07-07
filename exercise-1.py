def replace_last(numbers):
    ...
    if len (numbers) <= 1: 
        return numbers
    return [numbers[-1]]+ numbers [:-1]

print(replace_last([2, 3, 4, 1]))  
print(replace_last([1, 2, 3, 4]))  
print(replace_last([1]))        
print(replace_last([]))