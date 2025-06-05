import functions 

#Menu funciones
def menu_ordenamiento(personas):
    if not personas:
        print("No hay datos cargados. Cargue datos primero.")
        return
    
    print("\n=== ALGORITMOS DE ORDENAMIENTO ===")
    print("1. Bubble Sort (alfabético)")
    print("2. Selection Sort (alfabético)")
    print("3. Insertion Sort (alfabético)")
    print("0. Volver al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 0:
            return
        
        if opcion == 1:
            lista_ordenada, tiempo = functions.medir_tiempo_ejecucion(functions.bubble_sort, personas)
            personas = lista_ordenada
            print(f"\n✓ Bubble Sort completado:")
            functions.mostrar_lista_ordenada(lista_ordenada, "Lista ordenada alfabéticamente")
            
        elif opcion == 2:
            lista_ordenada, tiempo = functions.medir_tiempo_ejecucion(functions.selection_sort, personas)
            personas = lista_ordenada
            print(f"\n✓ Selection Sort completado:")
            functions.mostrar_lista_ordenada(lista_ordenada, "Lista ordenada alfabéticamente")
            
        elif opcion == 3:
            lista_ordenada, tiempo = functions.medir_tiempo_ejecucion(functions.insertion_sort, personas)
            personas = lista_ordenada
            print(f"\n✓ Insertion Sort completado:")
            functions.mostrar_lista_ordenada(lista_ordenada, "Lista ordenada alfabéticamente")
            
        else:
            print("Opción no válida.")
            return
        
        print(f"\nTiempo de ejecución: {tiempo:.2f} μs")
        
    except ValueError:
        print("Error: Ingrese un número válido.")

def menu_busqueda(personas):
    if not personas:
        print("No hay datos cargados. Cargue datos primero.")
        return
    
    print("\n=== ALGORITMOS DE BÚSQUEDA ===")
    print("1. Búsqueda lineal por nombre")
    print("2. Búsqueda binaria por nombre")
    print("0. Volver al menú principal")
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 0:
            return
        
        if opcion == 1:
            nombre = input("Ingrese el nombre a buscar: ").strip()
            if not nombre:
                print("Nombre no válido.")
                return
            
            posiciones, tiempo = functions.medir_tiempo_ejecucion(functions.busqueda_lineal, personas, nombre)
            print(f"\n✓ Búsqueda lineal por nombre completada:")
            print(f"Tiempo de ejecución: {tiempo:.2f} μs")
            
            if posiciones:
                print(f"Encontrado en {len(posiciones)} posición(es):")
                for pos in posiciones:
                    print(f"Posición {pos + 1}: {personas[pos]}")
            else:
                print(f"No se encontró ninguna persona con el nombre '{nombre}'.")
        
        elif opcion == 2:
            nombre = input("Ingrese el nombre a buscar: ").strip()
            if not nombre:
                print("Nombre no válido.")
                return
            
            resultado, tiempo = functions.medir_tiempo_ejecucion(functions.busqueda_binaria, personas, nombre)
            posiciones, lista_ordenada = resultado
            print(f"\n✓ Búsqueda binaria por nombre completada:")
            print(f"Tiempo de ejecución: {tiempo:.2f} μs")
            print("(Nota: La lista fue ordenada automáticamente para la búsqueda binaria)")
            
            if posiciones:
                print(f"Encontrado en {len(posiciones)} posición(es) en la lista ordenada:")
                for pos in sorted(posiciones):
                    print(f"Posición {pos + 1}: {lista_ordenada[pos]}")
            else:
                print(f"No se encontró ninguna persona con el nombre '{nombre}'.")
        
        else:
            print("Opción no válida.")
            
    except ValueError:
        print("Error: Ingrese un número válido.")

def menu_principal():
    personas = []
    while True:
        print("\n" + "="*50)
        print(" ALGORITMOS DE BÚSQUEDA Y ORDENAMIENTO")
        print("="*50)
        print("1. Cargar datos manualmente")
        print("2. Cargar datos de ejemplo")
        print("3. Mostrar lista actual")
        print("4. Algoritmos de ordenamiento")
        print("5. Algoritmos de búsqueda")
        print("0. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion == 0:
                print("¡Gracias por usar el programa!")
                break
            elif opcion == 1:
                personas = functions.cargar_datos_manual()
            elif opcion == 2:
                personas = functions.cargar_datos_ejemplo()
            elif opcion == 3:
                functions.mostrar_lista(personas)
            elif opcion == 4:
                menu_ordenamiento(personas)
            elif opcion == 5:
                menu_busqueda(personas)
            else:
                print("Opción no válida. Intente nuevamente.")
                
        except ValueError:
            print("Error: Ingrese un número válido.")
        
        input("\nPresione Enter para continuar...")