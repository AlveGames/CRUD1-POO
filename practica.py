from views import ClienteController

print(ClienteController.crear({"nombre": "ana", "apellido": "pérez", "email": "ana@gmail.com"}))
print(ClienteController.crear({"nombre": "luis", "apellido": "", "email": "luis@gmail.com"}))
print(ClienteController.crear({"nombre": "sol", "apellido": "ruiz", "email": "ANA@gmail.com"}))
print(ClienteController.crear({"nombre": "marco", "apellido": "díaz", "email": "marco@gmail"}))
print(ClienteController.siguiente_id())