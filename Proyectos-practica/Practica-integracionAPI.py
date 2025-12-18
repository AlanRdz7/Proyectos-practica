import urllib.request
import json
import pandas as pd
import os
import platform

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
    for u in usuarios:
        datos_limpios.append({
            'ID': u['id'],
            'Nombre': u['name'],
            'Email': u['email'],
            'Ciudad': u['address']['city'],
            'Empresa':u['company']['name']
            
        })
    return pd.DataFrame(datos_limpios)

def main():
    usuarios = obtener_usuarios()
    df = procesamiento_datos(usuarios)
    
    print("\nLista de usuarios:\n")
    print(df.to_string(index=False)) 
       
if __name__ == "__main__": 
        main()
    