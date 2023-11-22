#Definición de la Clase Matriz:
#La clase tiene un constructor __init__ que recibe el número de filas y columnas y crea una matriz vacía.
#La matriz se representa como una lista de listas.

class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        
#Método llenarMatriz:
#Este método solicita al usuario que ingrese valores para cada posición de la matriz
#Utiliza dos bucles anidados para recorrer las filas y columnas.

    def llenarMatriz(self):
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                valor = int(input("Ingrese el valor para [{i + 1}][{j + 1}]: "))
                fila.append(valor)
                self.matriz.append(fila)

#Método mostrarMatriz:
#Este método imprime la matriz en la consola, mostrando cada fila en una línea y separando las filas con guiones.

    def mostrarMatriz(self):
        for fila in self.matriz:
            print(fila)
        print("-----------")
        
#Método sumarMatrices:
#Este método recibe otra matriz como parámetro y devuelve una nueva matriz que es el resultado de la suma de las dos matrices.
#Verifica que las matrices tengan la misma dimensión antes de realizar la suma.

    def sumarMatrices(self, otra_matriz):
        if self.filas != otra_matriz.filas or self.columnas != otra_matriz.columnas:
            print("No se pueden sumar las matrices. Deben tener la misma dimensión.")
            return None

        matriz_resultante = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            fila_resultado = []
            for j in range(self.columnas):
                suma = self.matriz[i][j] + otra_matriz.matriz[i][j]
                fila_resultado.append(suma)
            matriz_resultante.matriz.append(fila_resultado)

        return matriz_resultante

# Programa principal
#Se crean dos objetos de la clase Matriz (matriz1 y matriz2).
#Se solicita al usuario ingresar valores para ambas matrices.
#Se muestran las matrices ingresadas.
#Se realiza la suma de las matrices y se muestra el resultado si es posible.

matriz1 = Matriz(2, 2)
matriz2 = Matriz(2, 2)

print("Ingrese valores para la primera matriz:")
matriz1.llenarMatriz()
print("\nIngrese valores para la segunda matriz:")
matriz2.llenarMatriz()

print("\nMatriz 1:")
matriz1.mostrarMatriz()

print("\nMatriz 2:")
matriz2.mostrarMatriz()

# Sumar las matrices
matriz_resultante = matriz1.sumarMatrices(matriz2)

if matriz_resultante:
    print("\nMatriz resultante de la suma:")
    matriz_resultante.mostrarMatriz()
