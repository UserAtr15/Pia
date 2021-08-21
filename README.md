# Pia
# PIA - Desarrollo Web Back-end

LARA REYNA ARTURO

1554973

#### Introducción:
Un señor de la tercera edad tiene una tienda de abarrotes en el brinda el servicio de envíar sus productos por medio de otra persona que viaja en motocicleta, toma la petición por medio de una llamada y le da las indicaciones a su empleado. Esto causa un problema ya que si varias personas llaman a la vez el solo podrá contestar una, además de que puede haber error al anotar el producto o dirección del cliente.

#### Propuesta Técnica:
Entidades
- Usuario
- Pedido
- Producto
- Categoria

Atributos:
- Usuario
	- Id
	- Nombre
	- Primer Apellido
	- Segundo Apellido
	- Contraseña
	- Teléfono
- Pedido
	- Id
	- Id de usuario
	- Hora del pedido
	- Hora de entrega
	- Dirección
- Producto
	- Id
	- Nombre de producto
	- Descripción 
	- Precio
	- Imagen
- Categoria
	- Id
	- Nombre de categoria
	- Descripción

Funcionalidades:
- Uso de login
- El usuario podra ver/ordenar los productos sin necesidad de realizar la llamada
- El usuario y el dueño podran saber el estado del pedido (Completado, Cancelado, En Progreso)
- Tener un registro de sus ventas

Base de datos:
Se utilizara La base de datos PostgresSQL ya que es facil de configurar, trabaja con datos relacionales y esta orientado a objetos

#### Diagrama UML
![](images/Diagrama%20UML.png)

#### Diagrama Entidad-Relación
![](images/Diagrama%20BD.png)
