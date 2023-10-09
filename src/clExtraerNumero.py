import re
class ExtraerNumero:
    def ExtraerValorNumerico(self,cadena):
        # Utiliza una expresión regular para encontrar valores numéricos
        match = re.search(r'(\d+(\.\d+)?)', cadena)

        if match:
            # Obtiene el primer valor numérico encontrado
            valor_numerico = match.group()
            valor_numerico = valor_numerico.replace(".", "")  # Elimina los puntos de miles
            valor_numerico = int(valor_numerico)
            return valor_numerico
        else:
            return None  # No se encontraron valores numéricos en la cadena