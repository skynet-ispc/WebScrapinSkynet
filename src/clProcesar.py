from src import clExtraerNumero , clTipoMoneda
class Porcesar:

    def procesar_info(self, info):
        extraer = clExtraerNumero.ExtraerNumero()
        moneda = clTipoMoneda.TipoMoneda()
        lista_de_diccionarios = []
        contadorId = 1
        for data_list in info:
            tipoInmueble, tipo_operacion, dormitorios, precio, zona, fecha_actualizacion, descripcion = data_list

            # Convierte los valores encontrados a enteros
            precioEntero = extraer.ExtraerValorNumerico(precio)
            habitaciones = extraer.ExtraerValorNumerico(dormitorios)
            tipoMoneda = moneda.identificarMoneda(precio)

            # Crear un diccionario con los datos de la propiedad actual
            propiedad = {
                'id': contadorId,
                'TipoDeInmueble': tipoInmueble,
                'TipoDeOperacion' : tipo_operacion,
                'Dormitorios': habitaciones,
                'Precio': precioEntero,
                'Moneda': tipoMoneda,
                'Zona': zona,
                'FechaDeActualización': fecha_actualizacion,
                'Descripcion': descripcion
            }

            contadorId = contadorId + 1
            lista_de_diccionarios.append(propiedad)


        return lista_de_diccionarios