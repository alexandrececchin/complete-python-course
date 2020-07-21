MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({'title': title, 'director': director, 'year': year})


def print_movie(movie):
    print(f"Title: {movie['title']} ")
    print(f"Director: {movie['director']} ")
    print(f"Year: {movie['year']} ")


def list_movies():
    for movie in movies:
        print_movie(movie)


def find_by_title():
    title = input("Enter the movie title to search: ")
    for movie in filter(lambda x: x['title'] == title, movies):
        print_movie(movie)


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


menu()
