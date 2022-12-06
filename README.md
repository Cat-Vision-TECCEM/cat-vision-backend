# CatVision: Documentación del Backend

**Integrantes:** _David Rodríguez Fragoso, Diego Armando Ulibarri Hernández, Eduardo Rodríguez López, Erick Hernández Silva, Israel Sánchez Miranda, Liam Garay Monroy, María Fernanda Ramírez Barragán, Octavio Andrick Sánchez Perusquia, Raúl Youthan Irigoyen Osorio, Renata de Luna Flores, Roberto Valdez Jasso._

05 de noviembre de 2022

_Inteligencia artificial avanzada para la ciencia de datos II_

## Este documento contiene la información sobre las rutas que existen para la aplicación de CatVision.

# Rutas

## Compañía

### /company/create

Ruta para crear una nueva compañía.

**Método:**

- POST

**Parámetros:**

- name: nombre de la compañía
- email: email de la compañía

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200

### /company/get-all

Ruta para cargar todas las compañías.

**Método:**

- GET

**Parámetros:**

- no aplica

**Formato:**

- no aplica

**Regresa:**

- Una excepción o un estatus 200

## NUC

### /nuc/sendData

Ruta para mandar desde la NUC datos codificados en bytes al backend.

**Método:**

- POST

**Parámetros:**

- Una lista de bytes que contiene un JSON codificado

**Formato:**

- RAW

**Regresa:**

- Una excepción o un estatus 200

### /nuc/get-products

Ruta usada por la NUC para cargar todos los productos de una compañía.

**Método:**

- POST

**Parámetros:**

- company_id: id numérico de la compañía

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200

## Orden

### /order/create

Ruta para crear una nueva orden.

**Método:**

- POST

**Parámetros:**

- company_id: id numérico de la compañía
- store_id: id numérico de la tienda
- products: una lista de diccionarios que contienen el id del producto y la cantidad
- total: precio total de los productos

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200

### /order/getSalesProduct

Ruta que recibe cuantas veces se ha pedido un producto, el total de productos pedidos y el total de ingresos en un intervalo de tiempo.\
Si no se proporciona un store_id, se supone que se solicitan estadísticas globales.\
Si no se proporciona una fecha de finalización, se supone que la fecha de finalización deseada es la fecha actual.

**Método:**

- GET

**Parámetros:**

- store_id (opcional): id numérico de la tienda
- start_month: mes en forma numérica
- start_year: año en forma numérica
- end_month(opcional): mes en forma numérica
- end_year(opcional): año en forma numérica

**Formato:**

- QueryParams

**Regresa:**

- Una excepción o un estatus 200

### /order/getOrders

Ruta que recibe store_id y company_id, regresa todos los pedidos activos. Regresa los productos del pedido, la fecha y el total a pagar.

**Método:**

- GET

**Parámetros:**

- store_id (opcional): id numérico de la tienda
- company_id (opcional): id numérico de la compañía

**Formato:**

- QueryParams

**Regresa:**

- Una excepción o un estatus 200

## Producto

### /product/create

Ruta para crear un nuevo producto.

**Método:**

- POST

**Parámetros:**

- company_id: id numérico de la compañía
- sku: sku del producto
- name: nombre del producto
- selling_price: precio de venta del producto
- image: url de la imagen del producto

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200

### /product/getProduct

Ruta para cargar la información de un producto.

**Método:**

- GET

**Parámetros:**

- product_id: id numérico del producto

**Formato:**

- QueryParams

**Regresa:**

- Una excepción o un estatus 200

### /product/get-all

Ruta para cargar todos los productos de una compañía.

**Método:**

- GET

**Parámetros:**

- company_id: id numérico de la compañía

**Formato:**

- QueryParams

**Regresa:**

- Una excepción o un estatus 200

## Tienda

### /store/create

Ruta para crear una nueva tienda.

**Método:**

- POST

**Parámetros:**

- name: nombre de la tienda
- state: estado donde está localizada la tienda
- street: calle donde está localizada la tienda
- number: número exterior de la tienda
- city: ciudad donde está localizada la tienda
- lat: latitud de la localización de la tienda
- lng: longitud de la localización de la tienda
- company_id: id numérico de la compañía

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200

### /store/getProducts

Ruta para cargar todos los productos de una tienda.

**Método:**

- GET

**Parámetros:**

- store_id: id numérico de la tienda

**Formato:**

- QueryParams

**Regresa:**

- Una excepción o un estatus 200

### /store/getAllStores

Ruta para cargar todas las tiendas.

**Método:**

- GET

**Parámetros:**

- no aplica

**Formato:**

- no aplica

**Regresa:**

- Una excepción o un estatus 200

## Ticket

### /ticket/create

Ruta para crear un nuevo ticket.

**Método:**

- POST

**Parámetros:**

- company_id: id numérico de la compañía
- body: contenido del ticket
- status: estatus del ticket
- name: nombre del cliente
- username: usuario del cliente que creó el ticket

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200

### /ticket/get

Ruta para cargar la información de un ticket.

**Método:**

- GET

**Parámetros:**

- ticket_id: id numérico del ticket

**Formato:**

- QueryParams

**Regresa:**

- Una excepción o un estatus 200

## Usuario

### /user/create

Ruta para crear un nuevo ticket.

**Método:**

- POST

**Parámetros:**

- store_or_company_id: id numérico de la compañía o de la tienda
- username: nombre del usuario
- password: contraseña para el login del usuario
- is*admin: \_true* si el usuario es administrador, de lo contrario _false_
- type: tipo de la cuenta, _company_ o _store_
- email: email del usuario

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200

### /user/login

Ruta para hacer login a la aplicación.

**Método:**

- POST

**Parámetros:**

- username: nombre del usuario
- password: contraseña para el login del usuario

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200

### /user/recover-password

Ruta para enviar al usuario un correo electrónico de recuperación de contraseña.

**Método:**

- POST

**Parámetros:**

- email: email del usuario

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200

### /user/reset-password

Ruta para cambiar la contraseña del usuario.

**Método:**

- POST

**Parámetros:**

- email: email del usuario
- token: token que se envió en el correo electrónico de recuperación de contraseña
- password: nueva contraseña del usuario

**Formato:**

- JSON

**Regresa:**

- Una excepción o un estatus 200
