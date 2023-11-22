import easygui as eg

Lista = ["Pedro", "Juan", "Guillermo", "Samuel"]

def main():
    while True:
        msg = "Lista de nombres"
        titulo = "Opciones a realizar"
        opciones = ["Agregar nombre", "Eliminar nombre", "Recorrer Lista", "Buscar en Lista", "Mostrar Lista", "Salir"]
        menu = eg.indexbox(msg, titulo, opciones)
        
        if menu == 0:
            msg1 = "Agrega nombre"
            titulo1 = "Agregar algun nombre"
            opciones1 = ["Agregar", "Salir"]
            agrega = eg.indexbox(msg1, titulo1, opciones1)
            if agrega == 0:
                dato = eg.enterbox(msg="Agrega un nombre cualquiera", title="Agrega un nombre")
                indice = eg.enterbox(msg="En que posicion de la lista iria?", title="Posicion en donde se inserta")
                Lista.insert(int(indice), dato)

        elif menu == 1:
            msg1 = "Eliminar nombre"
            titulo1 = "Elimina algun nombre segun su posición"
            opciones1 = ["Eliminar", "Salir"]
            eliminar = eg.indexbox(msg1, titulo1, opciones1)
            if eliminar == 0:
                elimina = eg.enterbox(msg="En que posicion de la lista esta?", title="Posicion en donde se encuentra")
                del Lista[int(elimina)]
                eg.msgbox(msg="Dato eliminado", title="Eliminado")

        elif menu == 2:
            msg3 = "Recorre la lista 1 por 1 los elementos"
            titulo3 = "Recorre la lista"
            opciones3 = ["Recorre", "Salir"]
            recorrer = eg.indexbox(msg3, titulo3, opciones3)
            if recorrer == 0:
                for n in Lista:
                    eg.msgbox(msg=n, title="Nombre en la lista")
                eg.msgbox(msg="Lista recorrida!!", title="Terminado")

        elif menu == 3:
            msg4 = "Busca algun nombre"
            titulo4 = "Busqueda"
            opciones4 = ["Buscar", "Salir"]
            busqueda = eg.enterbox(msg="Cual nombre busca", title="Nombre a buscar")
            if busqueda == 0:
                buscar = eg.enterbox(msg="Cual nombre busca?", title="Nombre a buscar")
                if buscar in Lista:
                    puntero = Lista.index(buscar)
                    eg.msgbox(msg="Nombre encontrado con el puntero: " + str(puntero), title="Nombre encontrado en la lista")
                else:
                    eg.msgbox(msg="No existe el nombre en la lista", title="No encontrado")

        elif menu == 4:
            msg5 = "Lista en su estado actual"
            titulo5 = "Lista guardada"
            opciones5 = ["Lista", "Salir"]
            if menu == 4:
                eg.msgbox(msg=str(Lista), title="Lista actual")

        elif menu == 5:
            break

if __name__ == '__main__':
    main()
