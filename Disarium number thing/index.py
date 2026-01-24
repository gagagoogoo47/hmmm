def disarium_number(n):
    num_str = str(n)
    digit_sum = 0
    
    # Iterate through digits with their positions (starting from 1)
    for i, digit in enumerate(num_str, start=1):
        digit_sum += int(digit) ** i
        
    return digit_sum == n

num = int(input("Enter a number => "))
if disarium_number(num):
    print(f"{num} is a Disarium number 😃 .")
else:
    print(f"{num} i1s not a Disarium number 😱 .")
