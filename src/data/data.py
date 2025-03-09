class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        lista_modificada = []
        for i in range(len(lista) - 1, -1, -1):
            lista_modificada.append(lista[i])
        return lista_modificada
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i, valor in enumerate(lista):
            if valor == elemento:
              return i 
        return -1
    
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        lista_normal = []
        componentes_revisados = []
        for elemento in lista:
            if (elemento, type(elemento)) not in componentes_revisados:
                lista_normal.append(elemento)
                componentes_revisados.append ((elemento, type(elemento))) 
                return componentes_revisados
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        x = 0
        y = 0
        total = []
        while x < len(lista1) and y < len(lista2):
            if lista1[x] <= lista2[y]:
                total.append(lista1[x])
                x += 1
            else:
                total.append (lista2[y])
                y +=1 
                total.extend(lista1[x:])
                total.extend(lista2[y:])  

    
    def rotar_lista(self, lista, h):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        if not lista:
            return []
        h = h % len(lista)
        return lista[-h:] + lista[-h:] 

    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        l = len(lista) + 1
        suma_guardada = n * (n + 1) // 2
        suma_actualizada = sum(lista) 
        return suma_guardada - suma_actualizada 
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for element in conjunto1:
              if element not in conjunto2:
                  return False
        return True
        
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila = []
        return {
            "Push": lambda x: pila.append(x),
            "pop": lambda: pila.pop () if pila else None,
        "peek": lambda: pila[-1] if pila else None,
        "is_empty": lambda: len(pila) == 0
        }

    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass