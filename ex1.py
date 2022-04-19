def print_numbers():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0 and i % 5 != 0:
            print("Three")
        elif i % 3 != 0 and i % 5 == 0:
            print("Five")
        else:
            print(i)

print_numbers()