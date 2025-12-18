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
    for u in usuarios:
        datos_limpios.append({
            'ID': usuarios['id'],
            'Nombre': usuarios['name'],
            'Email': usuarios['email'],
            'Ciudad': usuarios['address']['city'],
            'Empresa':usuarios['company']['name']
        })
    return pd.DataFrame(datos_limpios)
    
def main():
        usuarios = obtener_usuarios()
        df = procesamiento_datos(usuarios)
        df.to_excel("usuarios.xlsx", index=False)
        print("Archivo usuarios.xlsx generado correctamente")
        
        if __name__ == "__main__":
            main()