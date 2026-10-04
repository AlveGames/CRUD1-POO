from models import Cliente

ana = Cliente(1, "ana", "pérez", "ana@gmail.com", "0987654321", "guayaquil")

print(ana)
print(ana.nombre_completo)
print(ana.dominio_email)

d = ana.a_diccionario()
print(d)

copia = Cliente.desde_diccionario(d)
print(copia)
print(copia is ana)