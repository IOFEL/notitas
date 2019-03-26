import sys
from anotador import Anotador


class Menu:
    def __init__(self):
        self.anotador = Anotador()
        self.opciones = {
            "1": self.mostrarNotas,
            "2": self.buscarNotas,
            "3": self.agregarNota,
            "4": self.modificarNota,
            "5": self.salir
        }

    def display_menu(self):
        print("""
        Anotador-Menu:
        1. Mostrar las notas
        2. Buscar notas
        3. Agregar nota
        4. Modificar nota
        5. Salir
         """)

    def run(self):
        '''Muestra el menu y responde a las opciones.'''
        while True:
            self.display_menu()
            opcion = input("Ingrese una opcion: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es valido.")

    def mostrarNotas(self, notas=None):
        if not notas:
            notas = self.anotador.notas
        for nota in notas:
            print(f"{nota.id}: {nota.tags} \n{nota.texto}")

    def buscarNotas(self):
        filtro = input("Busqueda: ")
        notas = self.anotador.buscar(filtro)
        self.mostrarNotas(notas)

    def agregarNota(self):
        texto = input("Escriba la nota: ")
        tags = input("Ingrese sus tags: ")
        self.anotador.nuevaNota(texto, tags)
        print("Su nota ha sido agregada.")

    def modificarNota(self):
        id = int(input("Ingrese el id de la nota: "))
        nota = self.anotador.buscarNota(id)
        if nota:
            texto = input("Ingrese el texto: ")
            tags = input("Ingrese sus tags: ")
            if texto:
                nota.texto = texto
            if tags:
                nota.tags = tags
            print("Se a modificado la nota con exito.")
        else:
            print(f"No existe la nota de id:{id}")

    def salir(self):
        print("Gracias por usar el cuaderno de notas.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
