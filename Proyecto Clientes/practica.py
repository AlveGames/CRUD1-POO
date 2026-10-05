"""
practica.py - Ejercicios de la seccion 14 (Guia 1 CRUD Python POO)

Ejercicios 1 a 3: se resuelven aqui mismo.
Ejercicios 4 a 8: el codigo va dentro de models.py, views.py y main.py.
Aqui solo se PRUEBAN (ver la parte de abajo).
"""

# =====================================================================
# EJERCICIO 1 - Quitar duplicados conservando el orden
# =====================================================================
print("=== Ejercicio 1 ===")

ciudades = ["Quito", "Guayaquil", "Quito", "Cuenca", "Guayaquil"]

vistas = set()      # SET de control: pregunta "ya la vi?" al instante
unicas = []         # LISTA de resultado: conserva el orden de aparicion
for ciudad in ciudades:
    if ciudad not in vistas:
        vistas.add(ciudad)
        unicas.append(ciudad)

print(unicas)       # ['Quito', 'Guayaquil', 'Cuenca']
# Nota: set(ciudades) tambien quita repetidos, pero pierde el orden.


# =====================================================================
# EJERCICIO 2 - Contar con un diccionario
# =====================================================================
print("\n=== Ejercicio 2 ===")

conteo = {}
for ciudad in ciudades:
    # .get(ciudad, 0): si la ciudad aun no esta, empieza en 0
    conteo[ciudad] = conteo.get(ciudad, 0) + 1

print(conteo)                        # {'Quito': 2, 'Guayaquil': 2, 'Cuenca': 1}
print(max(conteo, key=conteo.get))   # 'Quito' (la primera con el valor mas alto)


# =====================================================================
# EJERCICIO 3 - Conjuntos en accion
# =====================================================================
print("\n=== Ejercicio 3 ===")

matematica = {"Ana", "Luis", "Sol", "Marco"}
ingles = {"Luis", "Marco", "Ruth"}

ambas = matematica & ingles          # INTERSECCION: en los dos
solo_mate = matematica - ingles      # DIFERENCIA: solo en matematica
total = len(matematica | ingles)     # UNION: personas distintas

print("En las dos:", sorted(ambas))          # ['Luis', 'Marco']
print("Solo en matematica:", sorted(solo_mate))  # ['Ana', 'Sol']
print("Personas distintas:", total)          # 5


# =====================================================================
# PRUEBAS DE LOS EJERCICIOS 4 A 8
# (solo funcionan despues de pegar el codigo en models.py, views.py y main.py)
# =====================================================================
from models import Cliente
from views import ClienteController

# --- Ejercicio 4: propiedad calculada 'iniciales' ---
print("\n=== Ejercicio 4 ===")
ana = Cliente(1, "Ana", "Perez", "ana@x.com")
print(ana.iniciales)                 # 'A.P.'  (sin parentesis: es propiedad)

# --- Ejercicio 5: metodo estatico 'es_telefono_valido' ---
print("\n=== Ejercicio 5 ===")
print(Cliente.es_telefono_valido(""))            # True  (vacio es valido)
print(Cliente.es_telefono_valido("0987654321"))  # True  (10 digitos)
print(Cliente.es_telefono_valido("123"))         # False (pocos digitos)
try:
    Cliente(2, "Luis", "Torres", "luis@x.com", "123")
except ValueError as error:
    print("Error:", error)           # El setter de telefono ya usa la regla

# --- Ejercicio 6: metodo de clase 'desde_texto' ---
print("\n=== Ejercicio 6 ===")
sol = Cliente.desde_texto("3, Sol, Ruiz, sol@x.com")
print(sol)                           # [3] Sol Ruiz - sol@x.com

# --- Ejercicio 7: atributo de clase + 'resumen()' ---
print("\n=== Ejercicio 7 ===")
print(Cliente.resumen())             # Se han creado N clientes
# RESPUESTA: resumen() no puede ser metodo de instancia porque la respuesta
# no es sobre UN cliente, sino sobre TODOS. Usa el atributo de clase
# total_creados y se puede llamar sin haber creado ningun objeto.

# --- Ejercicio 8: 'agrupar_por_ciudad()' en el Controlador ---
print("\n=== Ejercicio 8 ===")
print(ClienteController.agrupar_por_ciudad())
# Para verlo en el menu: ejecutar main.py y elegir la opcion 8.