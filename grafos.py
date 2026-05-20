cat > ej01_b.py << 'EOF'
# Ejercicio 1 - Mi primer nodo

class Vertice:
    def __init__(self, valor):
        self.valor      = valor   # informacion que contiene el nodo
        self.izq        = None    # rama izquierda (sin hijo al inicio)
        self.der        = None    # rama derecha  (sin hijo al inicio)

# Parte A - Preguntas conceptuales
# 1. self.izq = None quiere decir que el nodo no tiene
#    conexion hacia la izquierda; ese espacio esta disponible
#    para un futuro hijo.
# 2. Si escribo nodo = Vertice(42), entonces nodo.valor es 42.
# 3. Un arbol donde solo existe la raiz tiene 1 nodo en total.

# Parte B - Esquema del nodo con valor 25:
#
#   [ izq: None | valor: 25 | der: None ]
#         |                       |
#       (vacio)                (vacio)

# Parte C - Tres nodos conectados manualmente
central     = Vertice(10)
central.izq = Vertice(5)
central.der = Vertice(15)

print("central:", central.valor)
print("rama izq:", central.izq.valor)
print("rama der:", central.der.valor)
EOF

cat > ej02_b.py << 'EOF'
# Ejercicio 2 - Construyendo un arbol paso a paso

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

# construimos el arbol nivel por nivel

# nivel 0: raiz
central = Vertice(10)

# nivel 1
central.izq = Vertice(5)
central.der = Vertice(15)

# nivel 2: hijos de 5
central.izq.izq = Vertice(3)
central.izq.der = Vertice(7)

# nivel 2: hijos de 15
central.der.izq = Vertice(12)
central.der.der = Vertice(20)

# verificacion del punto e)
# central.izq.valor         deberia imprimir 5
# central.der.izq.valor     deberia imprimir 12
print(central.izq.valor)         # 5
print(central.der.izq.valor)     # 12
EOF

cat > ej03_b.py << 'EOF'
# Ejercicio 3 - Regla de ordenamiento BST
#
# Parte A
# 1. Insertar [8, 3, 10] en orden:
#    - 8 entra primero -> se convierte en raiz
#    - 3 < 8 -> va a la izquierda de 8
#    - 10 > 8 -> va a la derecha de 8
#
# 2. Arbol con raiz 20, insertar 15:
#    15 es menor que 20, por lo tanto va a la IZQUIERDA.
#    Regla: valores menores siempre a la izquierda del nodo actual.
#
# 3. Insertar un duplicado: simplemente se ignora.
#    El BST no almacena valores repetidos.
#
# Parte B - Insertar 6 en el arbol dado:
#    Paso 1: 6 vs 8  -> 6 < 8  -> bajar izquierda
#    Paso 2: 6 vs 3  -> 6 > 3  -> bajar derecha
#    Paso 3: 6 vs 5  -> 6 > 5  -> bajar derecha (None -> insertar aqui)
#
#    Arbol final:
#        8
#       / \
#      3   10
#       \
#        5
#         \
#          6
#
# Parte C
# Arbol A (10 con izq=5, y 5 con der=12):
#    NO es BST valido. El nodo 12 esta en el subarbol izquierdo
#    de 10, pero 12 > 10. Viola la propiedad fundamental del BST.
#
# Arbol B (10 con izq=5, y 5 con izq=12):
#    NO es BST valido. El 12 esta a la izquierda del 5
#    pero 12 > 5 (deberia ir a la derecha). Doble violacion.

print("Ver comentarios para respuestas del ejercicio 3")
EOF

cat > ej04_b.py << 'EOF'
# Ejercicio 4 - Completa el metodo insertar

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

class BST:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            # primer elemento: se convierte en la raiz del arbol
            self.raiz = Vertice(valor)
        else:
            self._agregar_rec(self.raiz, valor)

    def _agregar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                # encontramos el lugar: insertamos a la izquierda
                nodo.izq = Vertice(valor)
            else:
                # seguimos buscando hacia abajo por la izquierda
                self._agregar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                # encontramos el lugar: insertamos a la derecha
                nodo.der = Vertice(valor)
            else:
                # seguimos buscando hacia abajo por la derecha
                self._agregar_rec(nodo.der, valor)
        # valor igual al nodo: duplicado, no se agrega

arbol = BST()
for n in [10, 5, 15, 3, 7, 12, 20]:
    arbol.agregar(n)

print(arbol.raiz.valor)       # 10
print(arbol.raiz.izq.valor)   # 5
print(arbol.raiz.der.valor)   # 15
EOF

cat > ej05_b.py << 'EOF'
# Ejercicio 5 - Buscar, altura y contar nodos

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

class BST:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Vertice(valor)
        else:
            self._ag(self.raiz, valor)

    def _ag(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Vertice(valor)
            else:
                self._ag(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Vertice(valor)
            else:
                self._ag(nodo.der, valor)

    def existe(self, valor):
        return self._existe_rec(self.raiz, valor)

    def _existe_rec(self, nodo, valor):
        # si llegamos a None el valor no esta en el arbol
        if nodo is None:
            return False
        # lo encontramos
        if nodo.valor == valor:
            return True
        # valor mas pequeno: buscar en rama izquierda
        elif valor < nodo.valor:
            return self._existe_rec(nodo.izq, valor)
        # valor mas grande: buscar en rama derecha
        else:
            return self._existe_rec(nodo.der, valor)


def profundidad(nodo):
    # nodo vacio no aporta nivel
    if nodo is None:
        return 0
    rama_izq = profundidad(nodo.izq)
    rama_der = profundidad(nodo.der)
    # tomamos la rama mas profunda y sumamos el nodo actual
    return 1 + max(rama_izq, rama_der)


def total_nodos(nodo):
    if nodo is None:
        return 0
    # nodo actual + todos los de sus dos subarboles
    return 1 + total_nodos(nodo.izq) + total_nodos(nodo.der)


# Sin el caso base 'if nodo is None', la recursion no sabria
# cuando parar y terminaria con un error al intentar leer
# atributos de un objeto que no existe.

arbol = BST()
for n in [10, 5, 15, 3, 7, 12, 20]:
    arbol.agregar(n)

print(arbol.existe(7))          # True
print(arbol.existe(99))         # False
print(profundidad(arbol.raiz))  # 3
print(total_nodos(arbol.raiz))  # 7
EOF

cat > ej06_b.py << 'EOF'
# Ejercicio 6 - Recorrido inorden, minimo y maximo

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

class BST:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Vertice(valor)
        else:
            self._ag(self.raiz, valor)

    def _ag(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Vertice(valor)
            else:
                self._ag(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Vertice(valor)
            else:
                self._ag(nodo.der, valor)


def inorden(nodo, acumulado=None):
    if acumulado is None:
        acumulado = []   # lista nueva en cada llamada principal
    if nodo is not None:
        inorden(nodo.izq, acumulado)    # visitar izquierda primero
        acumulado.append(nodo.valor)    # registrar nodo actual
        inorden(nodo.der, acumulado)    # visitar derecha al final
    return acumulado


def minimo(nodo):
    # el valor mas pequeno siempre esta en el extremo izquierdo
    if nodo.izq is None:
        return nodo.valor
    return minimo(nodo.izq)


def maximo(nodo):
    # el valor mas grande siempre esta en el extremo derecho
    if nodo.der is None:
        return nodo.valor
    return maximo(nodo.der)


# El inorden siempre da orden ascendente en un BST porque
# la regla de insercion garantiza que la rama izquierda
# contiene solo menores y la rama derecha solo mayores.
# Visitar izquierda primero equivale a listar de menor a mayor.

arbol = BST()
for n in [10, 5, 15, 3, 7, 12, 20]:
    arbol.agregar(n)

print(inorden(arbol.raiz, []))  # [3, 5, 7, 10, 12, 15, 20]
print(minimo(arbol.raiz))       # 3
print(maximo(arbol.raiz))       # 20
EOF

cat > ej07_b.py << 'EOF'
# Ejercicio 7 - Analisis: metodo insertar
#
# ERROR IDENTIFICADO:
# En el bloque que maneja valores MENORES que el nodo actual,
# cuando el hijo izquierdo ya existe, la llamada recursiva
# pasa nodo.derecho en lugar de nodo.izquierdo:
#
#   else:
#       self._insertar_rec(nodo.derecho, dato)  <- incorrecto
#
# Si el valor es menor, la busqueda debe continuar por la
# izquierda. Al pasar nodo.derecho se baja por el lado
# contrario, insertando el valor en una posicion incorrecta.
#
# IMPACTO:
# El arbol pierde la propiedad BST silenciosamente.
# No hay error de ejecucion, pero los valores quedan mal
# ubicados y operaciones como buscar o recorrer darian
# resultados incorrectos.

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Vertice(valor)
        else:
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Vertice(valor)
            else:
                # correccion: bajar por izq, no por der
                self._insertar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Vertice(valor)
            else:
                self._insertar_rec(nodo.der, valor)

arbol = BST()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(3)
print(arbol.raiz.izq.izq.valor)  # 3
EOF

cat > ej08_b.py << 'EOF'
# Ejercicio 8 - Analisis: funcion buscar
#
# ERROR IDENTIFICADO:
# Falta el caso base para cuando nodo es None.
# La funcion asume que siempre recibe un nodo valido,
# pero cuando el valor buscado no existe, la recursion
# eventualmente llega a None e intenta leer None.dato,
# lo que genera AttributeError.
#
# TRAZA buscando 99 en arbol [10, 5, 15]:
#   buscar(raiz=10, 99) -> 99 > 10 -> buscar(15, 99)
#   buscar(nodo=15, 99) -> 99 > 15 -> buscar(None, 99)
#   buscar(nodo=None, 99) -> None.dato -> AttributeError
#
# CORRECCION: verificar si nodo es None antes de acceder
# a sus atributos y retornar False en ese caso.

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

class BST:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Vertice(valor)
        else:
            self._ag(self.raiz, valor)

    def _ag(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Vertice(valor)
            else:
                self._ag(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Vertice(valor)
            else:
                self._ag(nodo.der, valor)


def buscar(nodo, valor):
    # caso base corregido: nodo vacio significa que no existe
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    if valor < nodo.valor:
        return buscar(nodo.izq, valor)
    else:
        return buscar(nodo.der, valor)


arbol = BST()
for n in [10, 5, 15]:
    arbol.agregar(n)

print(buscar(arbol.raiz, 5))   # True
print(buscar(arbol.raiz, 99))  # False
EOF

cat > ej09_b.py << 'EOF'
# Ejercicio 9 - Analisis: funcion altura
#
# ERROR IDENTIFICADO:
# La funcion suma las alturas de ambas ramas en lugar de
# tomar la mayor:
#   return 1 + altura(nodo.izquierdo) + altura(nodo.derecho)
#
# La altura de un arbol es la longitud del camino mas largo
# desde la raiz hasta una hoja, no la suma de todos los caminos.
#
# TRAZA en arbol [10, 5, 15, 3]:
#   altura(3)  = 1 + 0 + 0 = 1
#   altura(5)  = 1 + 1 + 0 = 2
#   altura(15) = 1 + 0 + 0 = 1
#   altura(10) = 1 + 2 + 1 = 4  <- incorrecto
#
# La altura real es 3 (camino: 10 -> 5 -> 3).
# CORRECCION: reemplazar la suma por max().

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

class BST:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Vertice(valor)
        else:
            self._ag(self.raiz, valor)

    def _ag(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Vertice(valor)
            else:
                self._ag(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Vertice(valor)
            else:
                self._ag(nodo.der, valor)


def altura(nodo):
    if nodo is None:
        return 0
    # correccion: max en lugar de suma
    return 1 + max(altura(nodo.izq), altura(nodo.der))


arbol = BST()
for n in [10, 5, 15, 3]:
    arbol.agregar(n)

print(altura(arbol.raiz))  # 3
EOF

cat > ej10_b.py << 'EOF'
# Ejercicio 10 - Aplicacion real: organigrama universitario
#
# Parte A - Explicacion:
# Una universidad tiene una jerarquia natural de autoridad.
# La raiz es el rector, los nodos internos son decanos
# y directores de programa, y las hojas son los docentes.
# El recorrido inorden permite listar todos los miembros
# en orden alfabetico. La busqueda permite ubicar a una
# persona dentro del organigrama rapidamente.
#
# Parte B - Codigo

class Cargo:
    def __init__(self, nombre, rol):
        self.nombre = nombre   # nombre de la persona
        self.rol    = rol      # cargo que ocupa
        self.izq    = None
        self.der    = None


def listar_personal(nodo):
    if nodo is None:
        return
    listar_personal(nodo.izq)
    print(f"  {nodo.rol:25} -> {nodo.nombre}")
    listar_personal(nodo.der)


def buscar_cargo(nodo, nombre):
    if nodo is None:
        return None
    if nodo.nombre == nombre:
        return nodo.rol
    resultado = buscar_cargo(nodo.izq, nombre)
    if resultado:
        return resultado
    return buscar_cargo(nodo.der, nombre)


# construccion del organigrama
rector              = Cargo("Dr. Ramirez",  "Rector")
rector.izq          = Cargo("Dra. Torres",  "Decana Ingenieria")
rector.der          = Cargo("Dr. Morales",  "Decano Ciencias")

rector.izq.izq      = Cargo("Ing. Perez",   "Director Sistemas")
rector.izq.der      = Cargo("Ing. Gomez",   "Director Civil")
rector.der.izq      = Cargo("Dr. Vargas",   "Director Biologia")

print("Personal de la universidad:")
listar_personal(rector)

print()
nombre_buscar = "Ing. Gomez"
cargo = buscar_cargo(rector, nombre_buscar)
print(f"{nombre_buscar} ocupa el cargo: {cargo}")
EOF

echo ""
echo "Archivos generados:"
ls -lh ej*_b.py