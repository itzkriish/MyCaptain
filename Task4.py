numbers = list(map(int, input("Enter numbers separated by a space: ").split()))
print("Positive numbers:")
for num in numbers:
    if num >= 0:
        print(num, end=" ")
