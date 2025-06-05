import time
from faker import Faker


#Algoritmos de ordenamiento
def bubble_sort(lista):
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]: 
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia

def selection_sort(lista):
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista_copia[j] < lista_copia[min_idx]: 
                min_idx = j
        if min_idx != i:
            lista_copia[i], lista_copia[min_idx] = lista_copia[min_idx], lista_copia[i]
    
    return lista_copia

def insertion_sort(lista):
    lista_copia = lista.copy()
    
    for i in range(1, len(lista_copia)):
        key = lista_copia[i]
        j = i - 1
        while j >= 0 and lista_copia[j] > key:
            lista_copia[j + 1] = lista_copia[j]
            j -= 1
        lista_copia[j + 1] = key
    
    return lista_copia

#Algoritmos de busqueda
def busqueda_lineal(lista, nombre_buscado):
    posiciones = []
    for i, nombre in enumerate(lista):
        if nombre.lower() == nombre_buscado.lower(): 
            posiciones.append(i)
    return posiciones

def busqueda_binaria(lista, nombre_buscado):
    lista_ordenada = sorted(lista)
    low = 0
    high = len(lista_ordenada) - 1
    posiciones = []
    
    while low <= high:
        mid = (low + high) // 2
        if lista_ordenada[mid].lower() == nombre_buscado.lower():
            posiciones.append(mid)
            left = mid - 1
            while left >= 0 and lista_ordenada[left].lower() == nombre_buscado.lower():
                posiciones.append(left)
                left -= 1
            right = mid + 1
            while right < len(lista_ordenada) and lista_ordenada[right].lower() == nombre_buscado.lower():
                posiciones.append(right)
                right += 1
            break
        elif lista_ordenada[mid].lower() < nombre_buscado.lower():
            low = mid + 1
        else:
            high = mid - 1
    
    return posiciones, lista_ordenada

#Carga de datos
def cargar_datos_manual():
    print("\n=== CARGA DE DATOS ===")
    try:
        cantidad = int(input("¿Cuántos nombres desea ingresar? "))
        personas = [] 
        
        for i in range(cantidad):
            print(f"\nPersona {i + 1}:")
            nombre = input("Nombre: ").strip()
            while not nombre:
                nombre = input("Por favor, ingrese un nombre válido: ").strip()
            
            personas.append(nombre)
        
        print(f"\n✓ Se cargaron {len(personas)} nombres correctamente.")
        return personas
    except ValueError:
        print("Error: Ingrese un número válido.")

def cargar_datos_ejemplo():
    n = int(input("Ingrese la cantidad de datos de ejemplo a cargar: "))
    personas = Faker()
    print(f"✓ Se cargaron {n} nombres de ejemplo.")
    return [personas.first_name() for _ in range(n)]

#Muestra de datos
def mostrar_lista(personas):
    if not personas:
        print("No hay nombres cargados.")
        return
    
    print("\n=== LISTA DE NOMBRES ===")
    for i, nombre in enumerate(personas):
        print(f"{i + 1}. {nombre}")

def medir_tiempo_ejecucion(func, *args):
    inicio = time.perf_counter()
    resultado = func(*args)
    fin = time.perf_counter()
    tiempo = (fin - inicio) * 1000000  # Convertir a microsegundos
    return resultado, tiempo

def mostrar_lista_ordenada(lista_ordenada, titulo):
    print(f"\n{titulo}:")
    for i, nombre in enumerate(lista_ordenada):
        print(f"{i + 1}. {nombre}")

