def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))

# Swap values if start is greater than end
if start > end:
    start, end = end, start

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num,end=" " )





