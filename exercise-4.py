def chunking_by(numbers, chunck):
    ...
    split_list = []
    while numbers:
        split_list.append(numbers[:chunck]) 
        numbers = numbers[chunck:] 
    return split_list

assert chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]], "Test failed"
assert chunking_by([3, 4, 5], 1) == [[3], [4], [5]], "Test failed"
assert chunking_by([], 3) == [], "Test failed"