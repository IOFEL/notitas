from datetime import date

#Variable de clase que registra la cantidad de notas creadas y en funcion de eso asigna id
ultimo_id = 0

class Nota:
    '''Representa una nota en el cuaderno. Coincide con un string en las busquedas y guarda tags para cada nota.'''

    def __init__(self, texto,tags=''):
        '''Inicializa una nota con un texto y opcionalmente un tag.
        Automaticamente pone una fecha de creacion y id.'''
        self.texto = texto
        self.tags = tags
        self.fecha_creacion = date.today()
        global ultimo_id
        ultimo_id += 1
        self.id = ultimo_id

    def match(self, filter):
        '''Determina si la nota coincide con el filtro.
        Retorna True si coincide, sino False.

        La busqueda es caseSensitive y iguala texto y tags.'''
        return filter in self.texto or filter in self.tags