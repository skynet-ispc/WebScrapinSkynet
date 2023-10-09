import json
from src import clParser, clProcesar, clScraping
from mongodb import insertarDatos

parserFunc = clParser.Parse()
scraping = clScraping.Scraping()
procesar = clProcesar.Porcesar()


inmuebles = []

# url de la pagina de la voz con filtros previos en cba, alquileres departamentos
url_ppal = "https://clasificados.lavoz.com.ar/inmuebles/todo?ciudad=cordoba&operacion=alquileres"

paginacion = '//a[@class="page-link h4"]/text()'
links_inmuebles = '//div[@class="col col-12 mx1 md-mx0 md-mr1 bg-white mb2 line-height-3 card relative safari-card "]/a[@class="text-decoration-none"]/@href'

parser = parserFunc.parser_func(url_ppal)

cantidad_de_paginas = parser.xpath(paginacion)

maximo = int(cantidad_de_paginas[-1])

for i in range(1, maximo):
    
    pagina = f"{url_ppal}&page={i}"
    parser = parserFunc.parser_func(pagina)
    links = parser.xpath(links_inmuebles)

    print(f"**********{pagina}**********\n")

    scraping.buscarInfo(links,inmuebles)    

    if (i == 160):
        break


#---------------------------------------------------------------------------------------------------------------------#


# Llama a tu función para obtener los datos procesados
datos_procesados = procesar.procesar_info(inmuebles)

# Abre un archivo JSON en modo escritura y guarda los datos en él
with open('datos_inmuebles.json', 'w' ,encoding='utf-8') as archivo_json:
    json.dump(datos_procesados, archivo_json, ensure_ascii=False, indent=4)

insertarDatos(datos_procesados)

