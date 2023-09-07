# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

for n in range(1,11):
    s = n + (n-1)
    print(f"Current number {n} Sum: {s}")