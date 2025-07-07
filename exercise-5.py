def reverse_ascending(numbers):
    if not numbers:
        return []
    
    result = []
    current = [numbers[0]]
    for i in range(1,len(numbers)):
        if numbers [i] > numbers[i-1]:
            current.append(numbers[i])
        else:
            result.extend(reversed(current))
            current = [numbers[i]]

    result.extend(reversed(current))
    return result
