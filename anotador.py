from nota import Nota


class Anotador:
    '''Representa una coleccion de notas que pueden ser tageadas, modificadas y buscadas.'''

    def __init__(self):
        '''Inicializa un cuaderno sin notas.'''
        self.notas = []

    def nuevaNota(self, texto, tags=''):
        '''Crea una nueva nota y la agrega a la lista.'''
        self.notas.append(Nota(texto, tags))

    def buscarNota(self, notaId):
        '''Busca la nota segun el id.'''
        for nota in self.notas:
            if nota.id == notaId:
                return nota
        return None

    def modificarTexto(self, notaId, texto):
        '''Busca la nota con el id dado y modifica el texto con el texto argumento.'''
        self.buscarNota(notaId).texto = texto

    def modificarTags(self, notaId, tags):
        '''Busca la nota con el id dado y modifica los tags con el tags dado.'''
        self.buscarNota(notaId).tags = tags

    def buscar(self, filtro):
        '''Busca todas las notas que coincidan con el argumento filter.'''
        return [nota for nota in self.notas if nota.match(filtro)]
