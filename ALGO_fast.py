import json

file_path = 'base.json'
new_data = {'KONIKA c6085 4+0': 'c6085 4+0'}


def start_app(f_path):
    try:
        with open(f_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_new_data(data, n_data):
    data.update(n_data)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


info_data = start_app(file_path)
save_new_data(info_data, new_data)