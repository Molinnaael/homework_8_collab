def remove_all_after(numbers, n):
    if not numbers:
        return numbers # If the list is empty, just return the empty list
    if n not in numbers:
        return numbers # If n is not in the list, just return the original list
    for i in range(len(numbers)):
        if numbers[i] == n:
        # If we find n, return the list from the beginning up to and includding n
            return numbers[:i + 1]
