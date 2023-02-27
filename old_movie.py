# import datetime
d = "Casablanca 1942, Gone with the Wind 1939, The Godfather 1972, Psycho 1960"

list_now = d.split(",")
year = 2023  # datetime.datetime.now().year

dictionary = {}
results = ""

for i in list_now:
    temp = i.strip().rsplit(" ", 1)
    dictionary[temp[0]] = int(temp[1])
    if int(temp[1]) < year:
        year = int(temp[1])
        results = temp[0]

print(dictionary)
print("Найстаріший фільм:", results)
