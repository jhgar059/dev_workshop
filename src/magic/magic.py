class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """
        if n<=0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) +self.fibonacci (n -2)
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        sec = [0 ,1]
        for i in range(2, n):
            sec.append(sec[-1] + sec[-2])
        return sec[:n]    
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        if n < 2:
            return []
        gen = [True] * (n + 1)
        gen [0] = gen[1] = False
        for j in range(2, int(n ** 0.5) + 1):
            if gen[j]:
                for i in range(j * j, n + 1, j):
                    gen[i] = False
        return [j for j in range(n + 1) if gen]

    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """
        if n < 2:
            return False
        sum_div = sum(i for i in range(1, n // 2 + 1)if n % i == 0)
        return sum_div == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        if filas < 0:
            raise ValueError("Las filas no deben ser negativo")
        if filas == 0:
            return []
        triangulo = [[1]]
        for i in range(1, filas):
            prev = triangulo[-1]
            nueva_fila = [1]
            for j in range(1, i):
                nueva_fila.append(prev[j-1] + prev[j])
            nueva_fila.append(1)
            triangulo.append(nueva_fila)
        return triangulo




    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        while b:
            a, b = b, a % b
        return a 
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """
        return abs (a * b) // self.mcd (a, b)
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """
        return sum (int(digito)for digito in str(n))
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        digitos = [int(d) for d in str(n)]
        return n == sum(d**len(digitos) for d in digitos)
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        if not matriz:
            return False
        x = len(matriz)
        suma_ref = sum (matriz[0])

        for fila in matriz:
            if sum(fila) != suma_ref:
                return False

        for col in range(x):
            if sum(matriz[fila][col] for fila in range(x)) !=suma_ref:
                return False

        if sum(matriz[i][i] for i in range(x)) != suma_ref:
            return False
        if sum(matriz[i][x - 1 - i] for i in range(x)) != suma_ref:
            return False
        return True    

