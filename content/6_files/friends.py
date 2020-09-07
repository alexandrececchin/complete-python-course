friends_names = input('Enter your friends comma separated: ').split(',')

file = open('people.txt', 'r')
people_list = set([line.strip() for line in file.readlines()])
file.close()

near_friends = people_list.intersection(set(friends_names))

file = open('nearby_friends.txt', 'w')
for name in near_friends:
    print(f'{name} is nearby you, go and meet them !')
    file.write(f'{name}\n')
file.close()