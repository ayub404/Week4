def next_collatz(n):
    if n % 2 == 0:
        print(f"Even: {n}")
        return n // 2
    else:
        print(n)
        return 3 * n + 1

def collatz_length(n):
    step = 0
    while n != 1:
        # print(n, end = ' > ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        step += 1
    # print(n)
    
    return step

def max_in_collatz(n):
    maxium = n
    while n != 1:
        
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        if n > maxium:
            maxium = n
    return maxium
    

    
def print_collatz_sequence(n, max_steps):
    steps = 0
    
    while n != 1 and steps < max_steps:
       
        print(f"  Step {steps}: {n}")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    
    return ' '
    


print("\nCollatz Sequence Analyzer")
print('-' * 40)


   



print(f"Steps to reach 1 from 6: {collatz_length(6)}")

print(f"Steps to reach 1 from 7: {collatz_length(7)}")
   
print(f"Steps to reach 1 from 27: {collatz_length(27)}\n")

print(f"Maxium value in sequence from 27: {max_in_collatz(27)}\n")

print(f"Collatz sequence starting from 19:")
print(f"{print_collatz_sequence(19, 11)}")

print('Sequence length comparison')

print(f"  Starting from 15: {collatz_length(15)} steps")
print(f"  Starting from 16: {collatz_length(16)} steps")
print(f"  Starting from 17: {collatz_length(17)} steps")