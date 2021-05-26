first_term = 0
second_term = 1
print(first_term, second_term, end=" ")
for i in range(11):
    term = first_term + second_term
    print(term, end=" ")
    first_term = second_term
    second_term = term
