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







#ayuda complementaria si se desea modificar o agregar algo al menu funcionalmente:
# ============================================================
# RECETA PARA AGREGAR UNA FUNCION NUEVA AL MENU
# Siempre 3 pasos, de abajo hacia arriba:
#   1. MODELO: si usa los datos de UN estudiante -> metodo en Estudiante
#   2. CONTROLADOR: junta el resultado de TODOS, sin print
#   3. VISTA: metodo que muestra + linea en self._opciones
#
# EJEMPLO: materia con mas puntos de cada estudiante
#
# --- PASO 1: models.py, dentro de Estudiante (debajo de notas_de) ---
#     def mejor_materia(self):
#         mejor = None
#         mejor_promedio = -1
#         for materia, notas in self.__notas.items():
#             promedio = sum(notas) / len(notas)
#             if promedio > mejor_promedio:
#                 mejor = materia
#                 mejor_promedio = promedio
#         if mejor is None:
#             return None
#         return mejor, round(mejor_promedio, 2)
#
#   Si piden la SUMA en vez del promedio:
#   cambiar  sum(notas) / len(notas)  por  sum(notas)
#
# --- PASO 2: views.py, al final de EstudianteController ---
#     @classmethod
#     def mejores_materias(cls):
#         return {e.nombre_completo: e.mejor_materia() for e in cls.listar()}
#
# --- PASO 3a: main.py, en __init__ de MenuEstudiantes ---
#   Debajo de la opcion "10" y ANTES de self._opciones["0"] = salir:
#         self._opciones["11"] = ("Materia con más puntos", self.mejores_materias)
#
# --- PASO 3b: main.py, metodo nuevo en MenuEstudiantes ---
#     def mejores_materias(self):
#         imprimir_titulo("MATERIA CON MÁS PUNTOS")
#         for nombre, resultado in self._controlador.mejores_materias().items():
#             if resultado is None:
#                 print(f"  {nombre}: sin notas")
#             else:
#                 materia, promedio = resultado
#                 print(f"  {nombre}: {materia} ({promedio})")
#         self.pausa()
# ============================================================


#======================
# si se requiere implementsr un campo nuevo pero simple 
#debe ir asi
# ===== AGREGAR CAMPO NUEVO (ej. carrera) =====
# OJO: "..." = lo que ya está escrito, no se copia

# --- models.py > class Estudiante ---

# 1. Agregar al FINAL de las tuplas:
#     CAMPOS = (..., "carrera")
#     OBLIGATORIOS = (..., "carrera")

# 2. En __init__, agregar al FINAL de los parámetros:
#     def __init__(self, ..., carrera=""):

# 3. En __init__, PEGAR debajo de self.carnet = carnet:
#         self.carrera = carrera

# 4. PEGAR debajo del setter de carnet:
#     @property
#     def carrera(self):
#         return self.__carrera
#
#     @carrera.setter
#     def carrera(self, valor):
#         self.__carrera = Estudiante.limpiar(valor).title()

# 5. En a_diccionario, PEGAR debajo de "carnet": self.__carnet,
#             "carrera": self.__carrera,

# 6. En desde_diccionario, PEGAR debajo de materias=...
#             carrera=datos.get("carrera", ""),

# --- OPCIONAL: views.py > class EstudianteController ---
#     CAMPOS_BUSCABLES = (..., "carrera")

# --- OPCIONAL: main.py > class MenuEstudiantes (NO MenuClientes) ---
# REEMPLAZAR mostrar_tabla completo:
#     def mostrar_tabla(self, estudiantes):
#         print(f"{'ID':<5}{'NOMBRE':<25}{'CARNET':<12}{'CARRERA':<20}{'PROMEDIO':<10}{'ESTADO':<12}")
#         print("-" * self.ANCHO)
#         for e in estudiantes:
#             print(f"{e.id:<5}{e.nombre_completo:<25}{e.carnet:<12}"
#                   f"{e.carrera:<20}{e.promedio:<10}{e.estado:<12}")
#         print("-" * self.ANCHO)
#         imprimir_info(f"Total: {len(estudiantes)} estudiante(s)")

# =============================================
