
def calculate(a):
    sum = 0
    for i in a:
        try:
            if i.isdigit():
                sum += int(i)
            elif i[0] == '-' and i[1:].isdigit():
                sum -= int(i[1:])
        except:
            pass
    return sum

print(calculate(['4', '3', '-2']))
print(calculate(['nothing', 3, '8', 2, '1']))