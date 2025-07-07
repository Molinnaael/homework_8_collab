def index_power(numbers, n):
    if n <= len(numbers):
        return numbers[n] ** n
    else:
        return -1

while True:  
    try:
        user_input = input(f"Enter the numbers with commas: ")
        numbers = [int(x.strip()) for x in user_input.split(",")]
        
        break
    except ValueError:
        print(f"Please enter numbers separated by commas.")
        continue
while True:
    try:   
        n = int(input(f"Enter the number 'N': "))
        break
    except ValueError:
        print(f"Invalid. Please try again.")
        continue

print(f"The answer is: {index_power(numbers, n)}")

  



