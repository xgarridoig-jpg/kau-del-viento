# Kau del Viento — E-commerce (Django + PostgreSQL) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-6.x-092E20?style=flat-square&logo=django&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=flat-square&logo=postgresql&logoColor=white)

Aplicación web de comercio desarrollada con **Python**, **Django** y **PostgreSQL**.  
Incluye catálogo persistente (ORM), carrito por sesión, flujo de compra completo y gestión administrativa de productos con control de acceso por rol.

Repositorio: https://github.com/xgarridoig-jpg/kau-del-viento  
Portafolio: https://xgarridoig-jpg.github.io/

---

## Funcionalidades

### Autenticación y acceso
- Registro de usuarios
- Login / Logout
- Control de acceso por rol:
  - **Cliente**: navega catálogo, opera carrito y realiza compras
  - **Administrador (staff)**: gestiona productos (CRUD)

### Catálogo y persistencia (ORM + PostgreSQL)
- Productos persistidos en PostgreSQL
- Relación **Producto → Categoría**
- Catálogo público con:
  - búsqueda por nombre
  - filtro por categoría
  - orden por precio / nombre
  - paginación

### Carrito y compra (flujo completo)
- Carrito basado en sesión:
  - agregar productos
  - actualizar cantidades
  - quitar productos
  - vaciar carrito
  - subtotal por ítem y total general
- Checkout:
  - crea **Pedido** y **PedidoItem**
  - asocia pedido al usuario autenticado
  - limpia carrito al confirmar

### Pedidos
- Vista “Mis pedidos” para clientes autenticados
- Estados de pedido gestionables desde admin

---

## Stack técnico
- **Python**
- **Django**
- **PostgreSQL**
- Django ORM
- HTML/CSS (estilos propios) + Bootstrap (parcial)
- Git / GitHub

---

## Requisitos
- Python 3.x
- PostgreSQL 14+ (recomendado)
- Git

---

## Instalación y ejecución local

> Importante: el proyecto Django se ejecuta desde la carpeta `kau/` (ahí vive `manage.py`).

### 1) Clonar repositorio
```bash
git clone https://github.com/xgarridoig-jpg/kau-del-viento.git
cd kau-del-viento
```

### 2) Crear y activar entorno virtual

**Windows (PowerShell)**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Instalar dependencias

```bash
cd kau
pip install -r requirements.txt
```

### 4) Configurar base de datos PostgreSQL

Crea una base de datos y un usuario en PostgreSQL (ejemplo):

* DB: `kau_del_viento`
* USER: `kau_user`
* PASSWORD: (la que definas)
* HOST: `localhost`
* PORT: `5432`

Luego ajusta la configuración en `kau/settings.py` (bloque `DATABASES`) si tu entorno usa otros valores.

### 5) Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6) Crear usuario administrador (si no existe)

```bash
python manage.py createsuperuser
```

### 7) Ejecutar servidor

```bash
python manage.py runserver
```

App disponible en:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Rutas principales

### Público

* `/` → Home (catálogo público en sección colección)
* `/contacto/` → Contacto

### Autenticación

* `/accounts/signup/` → Registro
* `/accounts/login/` → Login
* `/accounts/logout/` → Logout

### Carrito y compra

* `/cart/` → Carrito (Tu Kau)
* `/orders/checkout/` → Checkout (requiere login)
* `/orders/success/<order_id>/` → Confirmación (requiere login, acceso restringido por usuario)
* `/orders/mis-pedidos/` → Historial del usuario

### Administración (solo staff)

* `/products/` → Listado de productos (admin)
* `/products/create/` → Crear producto
* `/products/edit/<id>/` → Editar producto
* `/products/delete/<id>/` → Eliminar producto
* `/admin/` → Admin Django (gestión completa)

---

## Credenciales de prueba

> Para evaluación/demostración se recomienda mantener **1 ADMIN** y **1 CLIENTE** listos.

### Administrador (staff)

* usuario: `admin`
* contraseña: `admin123`

### Cliente

* usuario: `cliente_test`
* contraseña: `Pass1234`

Si en tu entorno no existen, créalos desde:

* `/admin/` (como superuser) o
* `python manage.py createsuperuser` (para admin)

---

## Evidencias

Capturas del flujo principal y administración en:

* `kau/docs/`

Sugeridas:

* Home / catálogo
* Carrito (Tu Kau)
* Checkout / confirmación
* Administración de productos (CRUD)
* Pedidos (admin / mis pedidos)

---

## Nota de seguridad (entorno local)

Este repositorio está pensado para ejecución local y demostración.
Para despliegue productivo se recomienda:

* `DEBUG=False`
* variables de entorno para secretos
* `ALLOWED_HOSTS` configurado
* almacenamiento de media separado

---

## Proyección del proyecto

La estructura actual permite extender el sistema hacia funcionalidades como:

* gestión de inventario (stock por producto) y disponibilidad
* catálogo con búsqueda avanzada y filtros por rango de precio
* cupones y reglas de descuento (por categoría o por total de compra)
* seguimiento de pedidos (tracking) y notificaciones por correo
* reportes administrativos (ventas por periodo, productos más vendidos)

---

## Autora

**Ximena Garrido** — Backend Developer

Portafolio: [https://xgarridoig-jpg.github.io/](https://xgarridoig-jpg.github.io/)
LinkedIn: [https://www.linkedin.com/in/xpgarrido/](https://www.linkedin.com/in/xpgarrido/)

