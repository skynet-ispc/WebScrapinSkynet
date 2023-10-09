from . import clParser

class Scraping:
    def buscarInfo(self, urls_inmueble, inmueble):
        parserFunc = clParser.Parse()
        for i in urls_inmueble:
            title = '//div[@class="bg-darken-1 px3 py2"]/h1/text()'
            price = '//div[@class="bg-darken-1 px3 py2"]//div[@class="h2 mt0 main bolder"]/text()'
            tipo_ope_dor = '//div[@class="inline-flex align-baseline2 col-10"]/a/text()'
            zona = '//div[@class="col col-12 md-pt2"]/p[@class="mt0 h4"]/text()'
            date = '//div[@class="bg-darken-1 px3 py2"]//div[@class="h5 center"]/text()'

            parser = parserFunc.parser_func(i)

            precio = parser.xpath(price)  #Precio
            data_list= parser.xpath(tipo_ope_dor) #casa o departamento
            barrio=parser.xpath(zona) #Barrio
            titulo = parser.xpath(title) #Titulo
            aux_fecha = parser.xpath(date) #Fecha

            if aux_fecha:
                aux_fecha = aux_fecha[0].lstrip('Fecha de actualización: ')
            else:
                aux_fecha = "Fecha no disponible"

            if(len(barrio)!=1):
                barrio.append("null")

            if (len(data_list)==1):
                data_list.insert(0,"Comercio")
                data_list.append("N/A")
            elif(len(data_list)==2):
                data_list.append("N/A")
            elif(len(data_list)<1):
                data_list.append("null")
                data_list.append("null")
                data_list.append("null")


            if precio:
                data_list.append(precio[0])
            else:
                data_list.append("Precio no disponible")

            if barrio:
                data_list.append(barrio[0])
            else:
                data_list.append("Barrio no disponible")

            data_list.append(aux_fecha)

            if titulo:
                data_list.append(titulo[0])
            else:
                data_list.append("Titulo no disponible")

            inmueble.append(data_list) # Guardar
