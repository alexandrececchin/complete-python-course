file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    data = line.split(',')
    name = data[0].title()
    age = data[1]
    university = data[2].title()
    degree = data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}.')
