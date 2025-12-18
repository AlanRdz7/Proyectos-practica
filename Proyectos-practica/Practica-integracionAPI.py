import urllib.request
import json
import pandas as pd

def obtener_usuarios():
    """ Obtiene la lista de usuarios desde una API pública y la devuelve como una lista de diccionarios. """
    
    url="https://jsonplaceholder.typicode.com/users"
    
    with urllib.request.urlopen(url) as response:
        data = response.read()
        usuarios = json.loads(data)
        
        return usuarios
    
def procesamiento_datos(usuarios):
    """ Procesa la lista de usuarios obtenida de la Api """
    datos_limpios = []
    for usuario in usuarios:
        datos_limpios.append({
            'ID': usuario['id'],
            'Nombre': usuario['name'],
            'Email': usuario['email'],
            'Ciudad': usuario['address']['city'],
            'Empresa': usuario['company']['name']
        })