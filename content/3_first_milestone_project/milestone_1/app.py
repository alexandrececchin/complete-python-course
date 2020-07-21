# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({'title': title, 'director': director, 'year': year})


def list_movies():
    print(movies)


def find_by_title():
    title = input("Enter the movie title to search: ")
    print(list(filter(lambda x: x['title'] == title, movies)))


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add();
        elif selection == "l":
            list_movies()
        elif selection == "f":
            find_by_title()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu();
