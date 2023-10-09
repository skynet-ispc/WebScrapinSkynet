import re
class TipoMoneda:
    def identificarMoneda(self, cadena):
        # Define patrones para buscar el tipo de moneda en la cadena
        patronDolares = r'U\$\S'
        patronPesos = r'\$'

        # Busca el tipo de moneda en la cadena
        if re.search(patronDolares, cadena):
            return "Dólares"
        elif re.search(patronPesos, cadena):
            return "Pesos"
        else:
            return "Moneda no identificada"