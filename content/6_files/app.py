file = open('data.txt', 'r')
file_content = file.read()

print(f'content: {file_content}')

file.close()

user_name = input("Enter your name: ")
file_writing = open('data.txt', 'w')
file_writing.write(user_name)

file.close()
