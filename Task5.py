def most_frequent(string):
    d = {}
    for letter in string:
        d[letter] = string.count(letter)
    values = list(d.values())
    while len(values) != 0:
        for key, value in d.items():
            if value == max(values):
                print(f"{key}: {value}")
                values.remove(value)
            if len(values) == 0:
                break

s = input("Enter a string: ")
most_frequent(s)
