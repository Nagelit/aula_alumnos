import requests

def get_json_from(uri):
    r = requests.get(uri)

    return r.json()

def generar_correo_nombre():
    results = "1"  # input("Cuantos quieres? ")
    uri = f'https://randomuser.me/api/?results=1{results}'
    dict = get_json_from(uri)

    for user in dict["results"]:
        fullname = f'{user["name"]["first"]} {user["name"]["last"]}'
        email = user["email"]
        datos_usuario = {
            "nombre": fullname,
            "correo": email
        }
        print("")
        return datos_usuario

