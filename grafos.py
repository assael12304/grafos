cat > grafos_ej1_b.py << 'EOF'
# Ejercicio 1 - Lista de adyacencia a partir del grafo
# Grafo NO DIRIGIDO
# Conexiones: A-B, A-C, B-D, B-E, C-F, E-G, E-H

red = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G', 'H'],
    'F': ['C'],
    'G': ['E'],
    'H': ['E'],
}

# Tabla resuelta:
# Nodo  Vecinos          Grado   Hoja
#  A    B, C               2     No
#  B    A, D, E            3     No
#  C    A, F               2     No
#  D    B                  1     Si
#  E    B, G, H            3     No
#  F    C                  1     Si
#  G    E                  1     Si
#  H    E                  1     Si

# Respuestas:
# Total nodos           : 8
# Total aristas         : 7
# Nodo con mayor grado  : B y E (grado 3)
# Nodos hoja (grado=1)  : D, F, G, H -> 4 nodos
# Ciclos                : No. Con 8 nodos y 7 aristas sin ciclos es un arbol.
# Tipo de grafo         : Arbol (grafo aciclico conexo)

print("Tabla de adyacencia:")
print(f"{'Nodo':<6} {'Vecinos':<20} {'Grado':<7} {'Hoja'}")
print("-" * 42)
for nodo, vecinos in red.items():
    grado = len(vecinos)
    hoja  = "Si" if grado == 1 else "No"
    print(f"{nodo:<6} {str(vecinos):<20} {grado:<7} {hoja}")
EOF

cat > grafos_ej2_b.py << 'EOF'
# Ejercicio 2 - Convertir lista de adyacencia a matriz
# Grafo NO DIRIGIDO

conexiones = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6'],
    '4': ['2', '5'],
    '5': ['2', '4'],
    '6': ['3'],
}

etiquetas = sorted(conexiones.keys())

# Construimos la matriz de ceros y marcamos con 1 donde hay arista
mat = [[0] * len(etiquetas) for _ in range(len(etiquetas))]
indice = {n: i for i, n in enumerate(etiquetas)}

for nodo, vecinos in conexiones.items():
    for vecino in vecinos:
        mat[indice[nodo]][indice[vecino]] = 1

# Resultado:
#     1  2  3  4  5  6
# 1 [ 0, 1, 1, 0, 0, 0 ]
# 2 [ 1, 0, 0, 1, 1, 0 ]
# 3 [ 1, 0, 0, 0, 0, 1 ]
# 4 [ 0, 1, 0, 0, 1, 0 ]
# 5 [ 0, 1, 0, 1, 0, 0 ]
# 6 [ 0, 0, 1, 0, 0, 0 ]

print("    " + "  ".join(etiquetas))
for i, fila_etiq in enumerate(etiquetas):
    print(f" {fila_etiq}  {mat[i]}")

# Respuestas:
# Simetrica porque es NO dirigido: mat[i][j] == mat[j][i] siempre
# Total de 1s : 14 (7 aristas x 2 por ser bidireccional)
# Cada arista genera 2 unos en la matriz simetrica
# Fila con mas 1s: fila 2 (3 unos) -> nodo de mayor grado
# Nodo hoja (grado 1): nodo 6 (solo conectado al nodo 3)
EOF

cat > grafos_ej3_b.py << 'EOF'
# Ejercicio 3 - Grafo dirigido
# Aristas: A->B, A->C, B->D, C->B, C->E, D->E, E->A

apunta_a = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['B', 'E'],
    'D': ['E'],
    'E': ['A'],
}

nodos = list(apunta_a.keys())

# Calculamos quien apunta a cada nodo (grado de entrada)
recibe_de = {n: [] for n in nodos}
for origen, destinos in apunta_a.items():
    for d in destinos:
        recibe_de[d].append(origen)

# Lista de adyacencia dirigida completa:
# Nodo  Sale hacia    Recibe de
#  A    B, C          E
#  B    D             A, C
#  C    B, E          A
#  D    E             B
#  E    A             C, D

print("Lista de adyacencia dirigida:")
for n in nodos:
    print(f"  {n} -> sale: {apunta_a[n]:<12} entra: {recibe_de[n]}")

# Matriz dirigida (fila=origen, columna=destino)
#     A  B  C  D  E
# A [ 0, 1, 1, 0, 0 ]
# B [ 0, 0, 0, 1, 0 ]
# C [ 0, 1, 0, 0, 1 ]
# D [ 0, 0, 0, 0, 1 ]
# E [ 1, 0, 0, 0, 0 ]

idx = {n: i for i, n in enumerate(nodos)}
mat = [[0] * len(nodos) for _ in range(len(nodos))]
for origen, destinos in apunta_a.items():
    for d in destinos:
        mat[idx[origen]][idx[d]] = 1

print("\nMatriz dirigida:")
print("    " + "  ".join(nodos))
for i, n in enumerate(nodos):
    print(f" {n}  {mat[i]}")

# Respuestas:
# No es simetrica: la direccion de la arista importa (A->B != B->A)
# Mayor grado de salida : A y C (2 destinos cada uno)
# Mayor grado de entrada: B y E (2 nodos apuntan a ellos)
# Ciclo detectado       : E -> A -> B -> D -> E
# Nodo sin entrada      : ninguno. A recibe de E,
#   pero si ignoramos el ciclo, A es el punto de partida logico.
EOF

cat > grafos_ej4_b.py << 'EOF'
# Ejercicio 4 - Grafo ponderado: matriz de pesos
# Grafo NO DIRIGIDO
# Aristas: S-A:4, S-B:2, A-B:5, A-C:10, B-C:3, B-D:8, C-T:7, D-T:6, D-C:1

INF   = float('inf')
nodos = ['S', 'A', 'B', 'C', 'D', 'T']
n     = len(nodos)
idx   = {nd: i for i, nd in enumerate(nodos)}

# Inicializamos con INF y diagonal en 0
pesos = [[INF] * n for _ in range(n)]
for i in range(n):
    pesos[i][i] = 0

# Cargamos aristas de forma simetrica
rutas = [
    ('S','A',4), ('S','B',2),
    ('A','B',5), ('A','C',10),
    ('B','C',3), ('B','D',8),
    ('C','T',7), ('D','T',6),
    ('D','C',1),
]
for u, v, w in rutas:
    pesos[idx[u]][idx[v]] = w
    pesos[idx[v]][idx[u]] = w

# Matriz resultante:
#      S    A    B    C    D    T
# S [  0,   4,   2, INF, INF, INF ]
# A [  4,   0,   5,  10, INF, INF ]
# B [  2,   5,   0,   3,   8, INF ]
# C [INF,  10,   3,   0,   1,   7 ]
# D [INF, INF,   8,   1,   0,   6 ]
# T [INF, INF, INF,   7,   6,   0 ]

print("Matriz de pesos:")
print("     " + "    ".join(nodos))
for i, nd in enumerate(nodos):
    fila = ["INF" if pesos[i][j] == INF else f"{pesos[i][j]:3}" for j in range(n)]
    print(f" {nd}  [ {', '.join(fila)} ]")

# Respuestas:
# Arista menor peso  : S-B con peso 2
# Arista mayor peso  : A-C con peso 10
# INF en fila S      : 3 (S no conecta con C, D ni T)
# Ruta optima S->T   : S->B->C->D->T = 2+3+1+6 = 12
# Dijkstra aplicable : Si, todos los pesos son positivos

camino = [('S','B',2), ('B','C',3), ('C','D',1), ('D','T',6)]
costo  = sum(w for _, _, w in camino)
ruta   = ' -> '.join(u for u, _, _ in camino) + ' -> T'
print(f"\nRuta optima: {ruta} = {costo} minutos")
EOF

cat > grafos_ej5_b.py << 'EOF'
# Ejercicio 5 - Identificar tipo de grafo

# Grafo 5A - Grafo completo K5
g5A = {
    'P': ['Q', 'R', 'S', 'T'],
    'Q': ['P', 'R', 'S', 'T'],
    'R': ['P', 'Q', 'S', 'T'],
    'S': ['P', 'Q', 'R', 'T'],
    'T': ['P', 'Q', 'R', 'S'],
}
nodos_A   = len(g5A)
aristas_A = sum(len(v) for v in g5A.values()) // 2
print("5A - Grafo completo K5")
print(f"  Nodos         : {nodos_A}")
print(f"  Aristas       : {aristas_A}  (formula: n*(n-1)/2 = {nodos_A*(nodos_A-1)//2})")
print(f"  Tipo          : Completo. Todo par de nodos tiene arista directa.")
print(f"  Grado de cada nodo: {nodos_A - 1}")

# Grafo 5B - Camino lineal / arbol
g5B = {
    'X': ['Y'],
    'Y': ['X', 'Z'],
    'Z': ['Y', 'W'],
    'W': ['Z', 'V'],
    'V': ['W'],
}
nodos_B   = len(g5B)
aristas_B = sum(len(v) for v in g5B.values()) // 2
print("\n5B - Camino lineal")
print(f"  Nodos         : {nodos_B}")
print(f"  Aristas       : {aristas_B}")
print(f"  Tipo          : Path graph (camino). Cadena lineal sin ramificaciones.")
print(f"  Ciclos        : No. No hay forma de regresar al punto de inicio.")
print(f"  Es arbol      : {aristas_B == nodos_B - 1} (verifica N-1={nodos_B-1} aristas)")

# Grafo 5C - Grafo bipartito
g5C = {
    '1': ['A', 'C'],
    '2': ['B', 'C', 'D'],
    '3': ['A', 'D'],
    'A': ['1', '3'],
    'B': ['2'],
    'C': ['1', '2'],
    'D': ['2', '3'],
}
grupo_num  = {'1', '2', '3'}
grupo_alfa = {'A', 'B', 'C', 'D'}

# Verificar que ningun nodo conecta dentro de su propio grupo
arista_interna = False
for nodo, vecinos in g5C.items():
    for vecino in vecinos:
        if (nodo in grupo_num and vecino in grupo_num) or \
           (nodo in grupo_alfa and vecino in grupo_alfa):
            arista_interna = True

print("\n5C - Grafo bipartito")
print(f"  Grupos        : {sorted(grupo_num)} y {sorted(grupo_alfa)}")
print(f"  Aristas internas al mismo grupo: {arista_interna}")
print(f"  Tipo          : Bipartito. Las aristas solo cruzan entre los dos grupos.")
print(f"  Aplicacion    : Emparejamiento de candidatos con puestos de trabajo,")
print(f"                  o asignacion de estudiantes a materias.")
EOF

cat > grafos_b1_b.py << 'EOF'
# Ejercicio B1 - Red de transporte urbano
# Grafo ponderado NO DIRIGIDO

# B1.2 - Lista de adyacencia (vecino, tiempo_min)
# CTR: (NTE,12), (SUR,8), (EST,15)
# NTE: (CTR,12), (OCC,10), (NOR,7)
# SUR: (CTR,8), (SOR,9)
# EST: (CTR,15), (NOR,5), (SOR,11)
# OCC: (NTE,10), (TRM,18)
# NOR: (NTE,7), (EST,5), (TRM,6)
# SOR: (SUR,9), (EST,11), (TRM,13)
# TRM: (OCC,18), (NOR,6), (SOR,13)

# B1.3 - Codigo Python
red_urbana = {
    'CTR': [('NTE', 12), ('SUR', 8),  ('EST', 15)],
    'NTE': [('CTR', 12), ('OCC', 10), ('NOR', 7)],
    'SUR': [('CTR', 8),  ('SOR', 9)],
    'EST': [('CTR', 15), ('NOR', 5),  ('SOR', 11)],
    'OCC': [('NTE', 10), ('TRM', 18)],
    'NOR': [('NTE', 7),  ('EST', 5),  ('TRM', 6)],
    'SOR': [('SUR', 9),  ('EST', 11), ('TRM', 13)],
    'TRM': [('OCC', 18), ('NOR', 6),  ('SOR', 13)],
}

# B1.4 - Analisis
num_estaciones = len(red_urbana)
num_rutas      = sum(len(v) for v in red_urbana.values()) // 2
mas_conexiones = max(red_urbana, key=lambda e: len(red_urbana[e]))
todas          = [(t, a, b) for a, lst in red_urbana.items() for b, t in lst]
mas_rapida     = min(todas)
mas_lenta      = max(todas)

print("Analisis de la red de transporte:")
print(f"  Estaciones (nodos)       : {num_estaciones}")
print(f"  Rutas directas (aristas) : {num_rutas}")
print(f"  Estacion mas conectada   : {mas_conexiones}")
print(f"  Ruta directa mas rapida  : {mas_rapida[1]}-{mas_rapida[2]} ({mas_rapida[0]} min)")
print(f"  Ruta directa mas lenta   : {mas_lenta[1]}-{mas_lenta[2]} ({mas_lenta[0]} min)")
print(f"  Ruta directa CTR->TRM    : No existe (son extremos opuestos de la red)")
print(f"  Ruta posible CTR->TRM    : CTR->NTE->NOR->TRM = {12+7+6} min")
print(f"  Tipo de grafo            : No dirigido (las rutas van en ambas direcciones)")

print("\nLista completa de adyacencia:")
for est, conex in red_urbana.items():
    print(f"  {est}: {conex}")
EOF

cat > grafos_b2_b.py << 'EOF'
# Ejercicio B2 - Red social de seguidores
# Grafo DIRIGIDO ponderado (interacciones/mes como peso)

# B2.1 y B2.4 - Lista de adyacencia y codigo
seguidores = {
    'Ana':    [('Luis', 45),   ('Maria', 30)],
    'Luis':   [('Maria', 60),  ('Pedro', 25)],
    'Maria':  [('Ana', 50),    ('Sofia', 40)],
    'Pedro':  [('Ana', 15),    ('Carlos', 35)],
    'Sofia':  [('Luis', 20),   ('Pedro', 10)],
    'Carlos': [('Maria', 55),  ('Sofia', 22)],
}

usuarios = list(seguidores.keys())

# B2.2 - Matriz dirigida (1 si fila sigue a columna)
#          Ana  Lui  Mar  Ped  Sof  Car
# Ana    [  0,   1,   1,   0,   0,   0 ]
# Luis   [  0,   0,   1,   1,   0,   0 ]
# Maria  [  1,   0,   0,   0,   1,   0 ]
# Pedro  [  1,   0,   0,   0,   0,   1 ]
# Sofia  [  0,   1,   0,   1,   0,   0 ]
# Carlos [  0,   0,   1,   0,   1,   0 ]

mat = {u: {v: 0 for v in usuarios} for u in usuarios}
for u, lista in seguidores.items():
    for v, _ in lista:
        mat[u][v] = 1

print("Matriz de adyacencia dirigida:")
cab = [u[:3] for u in usuarios]
print("        " + "    ".join(cab))
for u in usuarios:
    fila = [str(mat[u][v]) for v in usuarios]
    print(f"  {u:7} [{', '.join(fila)}]")

# Grados
g_salida  = {u: len(seguidores[u]) for u in usuarios}
g_entrada = {u: 0 for u in usuarios}
for u, lista in seguidores.items():
    for v, _ in lista:
        g_entrada[v] += 1

print(f"\nGrado salida : {g_salida}")
print(f"Grado entrada: {g_entrada}")
print(f"Mayor salida : {max(g_salida,  key=g_salida.get)}")
print(f"Mayor entrada: {max(g_entrada, key=g_entrada.get)}")

# Relaciones mutuas
print("\nRelaciones mutuas:")
encontradas = set()
for u in usuarios:
    for v, _ in seguidores[u]:
        par = tuple(sorted([u, v]))
        if par not in encontradas and any(x == u for x, _ in seguidores[v]):
            print(f"  {u} <-> {v}")
            encontradas.add(par)

# Respuestas de analisis:
# La matriz NO es simetrica: seguir en redes sociales es unidireccional
# Mayor grado salida  : todos tienen grado 2 (misma cantidad)
# Mayor grado entrada : Maria (la siguen Ana, Luis y Carlos -> 3)
# Relacion mutua      : Ana <-> Maria (Ana->Maria y Maria->Ana)
# Ciclo               : Ana -> Luis -> Maria -> Ana
# Alguien sin seguidores: no, todos tienen al menos 1 seguidor
# Recomendacion para Ana: Pedro o Sofia (seguidos por quienes Ana sigue)
# Diferencia con B1   : B1 no dirigido (rutas van en ambos sentidos),
#                       B2 dirigido (seguir es una accion de una sola via)
EOF

echo ""
echo "Archivos generados:"
ls -lh grafos_*_b.py