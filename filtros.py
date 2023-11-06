import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import re

# Filtros
def url_filtros():

    # Extraer provincias
    def extraer_provincias():
        url = 'https://clasificados.lavoz.com.ar/inmuebles/todo?'

        html_text_provincias = requests.get(url).text
        soup = BeautifulSoup(html_text_provincias, 'lxml')

        div_provincias = soup.find_all('div', id='provincias')
        alquileres_provincias = []

        for i, div in enumerate(div_provincias):
            provincias = div.find('a')
            if provincias:
                cant_provincias = provincias.text.strip()
                alquileres_provincias.append(cant_provincias)
            else:
                print(f'No se encontró la etiqueta <a> dentro del div {i}.')

        return alquileres_provincias

    print('\nProvincias:')
    print(extraer_provincias())
    provincia_filtro = extraer_provincias()

    def convertir_lista(lista):
        lista_nueva = []
        for string in lista:
            string_modificado = unidecode(string.lower().replace(' ', '-'))
            string_modificado = re.sub(r'\([^)]*\)', '', string_modificado)
            string_modificado = string_modificado.rstrip('-')
            lista_nueva.append(string_modificado)
        return lista_nueva

    p_lista = extraer_provincias()
    lista_provincias = convertir_lista(p_lista)

    def seleccionar(lista, indice):
        if indice.isdigit():
            indice = int(indice)
            if 0 <= indice < len(lista):
                seleccionado = lista[indice]
                return seleccionado
            else:
                return 'El índice está fuera del rango de la lista.'
        else:
            return 'Ingrese un valor numérico válido para el índice.'

    seleccionar_provincia = input('\nSeleccione la provincia: ')
    print(provincia_filtro[int(seleccionar_provincia)])
    provincia = seleccionar(lista_provincias, seleccionar_provincia)

    def construir_url_provincia(provincia):
        url = f'https://clasificados.lavoz.com.ar/inmuebles/todo?provincia={provincia}'
        return url

    url_provincia = construir_url_provincia(provincia)

    # Extraer Ciudades
    def extraer_ciudades(url):

        html_text_ciudades = requests.get(url).text
        soup = BeautifulSoup(html_text_ciudades, 'lxml')

        div_ciudades = soup.find_all('div', id='ciudades')
        alquileres_ciudades = []

        for i, div in enumerate(div_ciudades):
            ciudades = div.find('a')
            if ciudades:
                cant_ciudades = ciudades.text.strip()
                alquileres_ciudades.append(cant_ciudades)
            else:
                print(f'No se encontró la etiqueta <a> dentro del div {i}.')

        return alquileres_ciudades

    print('\nCiudades:')
    print(extraer_ciudades(url_provincia))
    ciudad_filtro = extraer_ciudades(url_provincia)

    c_lista = extraer_ciudades(url_provincia)
    lista_ciudades = convertir_lista(c_lista)

    seleccionar_ciudad = input('\nSeleccione la ciudad: ')
    print(ciudad_filtro[int(seleccionar_ciudad)])
    ciudad = seleccionar(lista_ciudades, seleccionar_ciudad)

    def construir_url_ciudad(provincia, ciudad):
        url = f'https://clasificados.lavoz.com.ar/inmuebles/todo?provincia={provincia}&ciudad={ciudad}'
        return url

    url_ciudad = construir_url_ciudad(provincia, ciudad)

    def extraer_operaciones(url, palabras_clave):
        html_text_operaciones = requests.get(url).text
        soup = BeautifulSoup(html_text_operaciones, 'lxml')

        operaciones = soup.find_all('div', class_='mx1 px2 py05')
        operaciones_seleccionados = []

        for i, operacion in enumerate(operaciones):
            tipo_operacion = operacion.find('a')
            if tipo_operacion:
                operacion_texto = tipo_operacion.text.strip()
                for palabra_clave in palabras_clave:
                    if palabra_clave in operacion_texto:
                        operaciones_seleccionados.append(operacion_texto)
                        break
            else:
                print(f'No se encontró la etiqueta <a> dentro del div {i}.')

        return operaciones_seleccionados

    palabras_clave = ['Alquileres', 'Venta', 'Compra']

    print('\nOperaciones:')
    print(extraer_operaciones(url_ciudad, palabras_clave))
    operacion_filtro = extraer_operaciones(url_ciudad, palabras_clave)

    o_lista = extraer_operaciones(url_ciudad, palabras_clave)
    lista_operaciones = convertir_lista(o_lista)

    seleccionar_operacion = input('\nSeleccione la operación: ')
    print(operacion_filtro[int(seleccionar_operacion)])
    operacion = seleccionar(lista_operaciones, seleccionar_operacion)

    def construir_url_operacion(provincia, ciudad, operacion):
        url = f'https://clasificados.lavoz.com.ar/inmuebles/todo?provincia={provincia}&ciudad={ciudad}&operacion={operacion}'
        return url

    url_inmuebles = construir_url_operacion(provincia, ciudad, operacion)

    return url_inmuebles

url = url_filtros()
print(url)