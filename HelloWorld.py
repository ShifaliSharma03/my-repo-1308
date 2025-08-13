import time
import sys

message = "Hello World"
for char in message:
    print(char, end='', flush=True)
    time.sleep(0.2)
print()  # Move to next line after animation

#Write a code to generate a star like pattern
def print_star_pattern(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))            
print_star_pattern(5)   

print("Hello World")
