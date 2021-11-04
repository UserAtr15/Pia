# Manual Técnico

#### Método HTTP del request

| Modulo  | Métodos HTTP  |
| :------------ |:---------------:|
| Usuarios   |  Get, Post, Update, Delete|
| Productos    | Get, Post, Update, Delete        |
| Categorias |  Get, Post, Update, Delete       |
|Pedidos | Get, Post, Delete|
|Login| Post|


#### Parámetros del URL
- Usuarios
	- Get
	http://127.0.0.1:8000/users/
	- Update y Delete
	http://127.0.0.1:8000/users/id/
- Productos
	- Get 
	http://127.0.0.1:8000/products/products/
	- Update y Delete
	http://127.0.0.1:8000/products/products/id/
- Categorias
	- Get
	http://127.0.0.1:8000/products/category/
	- Update y Delete
	http://127.0.0.1:8000/products/category/id/
- Pedidos
	- Get
	http://127.0.0.1:8000/orders/
	- Delete
	http://127.0.0.1:8000/orders/id/

#### Parámetros del body
- Usuarios
```javascript
{
  "password": "",
  "is_superuser": false,
  "username": "",
  "email": "",
  "name": "",
  "lastname": "",
  "is_active": true,
  "is_staff": false
}
```
- Productos
```javascript
{
  "name": "",
  "description": "",
  "image": null,
  "category_product": null
}
```
- Categorias
```javascript
{
  "name": ""
}
```
- Pedidos
```javascript
{
  "order_user": "",
  "order_product": [],
  "address": "",
  "time": ""
}
```
- Login
```javascript
{
  "username":"",
  "password": ""
}
```

#### Pruebas en Postman
