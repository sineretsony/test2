d = "Casablanca 1942, Gone with the Wind 1939, The Godfather 1972, Psycho 1960"

list_now = d.split(",")

dictionary = {}
results = ""
year = 0


def fil_mov():
    global results, year, dictionary
    for i in list_now:
        temp = i.strip().rsplit(" ", 1)
        dictionary[temp[0]] = int(temp[1])
        if year == 0:
            year = int(temp[1])
            results = temp[0]
        if int(temp[1]) < year:
            year = int(temp[1])
            results = temp[0]
    return results


fil_mov()

print(dictionary)
print("Найстаріший фільм:", results)
