d = "Casablanca 1942, Gone with the Wind 1939, The Godfather 1972, Psycho 1960"

list_now = d.split(",")

def fil_mov():
    dictionary = {}
    min_year = None
    oldest_movie = ""
    for i in list_now:
        temp = i.strip().rsplit(" ", 1)
        dictionary[temp[0]] = int(temp[1])
        year = int(temp[1])
        if min_year is None or year < min_year:
            min_year = year
            oldest_movie = temp[0]
    results = f"Найстаріший фільм: {oldest_movie}"
    return dictionary, results

result = fil_mov()
print(result[0], result[1])
