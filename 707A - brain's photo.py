rows, columns = map(int, input().split())

color_dict = {}
for i in range(rows):
    values = list(input().split())
    for val in values:
        if val in color_dict:
            temp = color_dict[val]
            color_dict[val] = temp + 1
        else:
            color_dict[val] = 1

if len(color_dict) <= 3 and ('C' not in color_dict and 'M' not in color_dict and 'Y' not in color_dict):
    print("#Black&White")
else:
    print("#Color")
