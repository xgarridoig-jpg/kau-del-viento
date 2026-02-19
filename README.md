
# 🦅 Kau del Viento

### Plataforma E-Commerce con Django ORM y Administración CRUD

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![Modulo](https://img.shields.io/badge/Módulo-7-purple)
![ORM](https://img.shields.io/badge/Django-ORM-important)
![Status](https://img.shields.io/badge/Estado-Completo-success)

---

# 📌 Proyecto Académico – Módulo 7

## Acceso a Datos en Aplicaciones Python Django

Este repositorio corresponde a la evolución del proyecto desarrollado en el **Módulo 6**, extendido y mejorado en el **Módulo 7** para implementar correctamente la capa de acceso a datos utilizando **Django ORM**, relaciones entre modelos, migraciones y operaciones CRUD completas.

El proyecto simula la administración interna de un e-commerce, permitiendo gestionar el catálogo de productos mediante un módulo exclusivo de administración.

---

# 🎯 Objetivo del Módulo 7

Implementar un módulo de administración de productos que permita:

* ✅ Uso completo de **Django ORM**
* ✅ Modelado de entidades del dominio
* ✅ Relaciones entre modelos (Producto–Categoría)
* ✅ Migraciones aplicadas correctamente
* ✅ CRUD completo funcional
* ✅ Integración de modelos con vistas y templates
* ✅ Registro del modelo en Django Admin
* ✅ Sistema de mensajes para feedback al usuario

---

# 🏗️ Modelo de Datos Implementado

## 📂 Categoria

```python
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
```

---

## 🛍️ Producto

```python
class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    precio = models.DecimalField(...)
    imagen = models.ImageField(...)
    activo = models.BooleanField(default=True)
```

---

## 🔗 Relación ORM Implementada

**Producto → Categoria (ForeignKey real)**

* Relación protegida (`on_delete=PROTECT`)
* Uso de `related_name`
* Consultas ORM funcionales
* Migraciones aplicadas correctamente



---

# 🔁 CRUD Completo de Productos

Se implementó un módulo de administración funcional accesible solo para usuarios `staff`.

## 📌 Rutas Implementadas

| Ruta                     | Funcionalidad        |
| ------------------------ | -------------------- |
| `/products/`             | Listado de productos |
| `/products/create/`      | Crear producto       |
| `/products/edit/<id>/`   | Editar producto      |
| `/products/delete/<id>/` | Eliminar producto    |

---

## ✔ Funcionalidades del CRUD

* Validación de campos obligatorios
* Precio validado con `MinValueValidator`
* Verificación de existencia antes de editar/eliminar
* Mensajes de éxito y error con `Django messages`
* Integración completa con templates
* Uso exclusivo del ORM (sin SQL crudo)



---

# 🛡️ Django Admin Integrado

El modelo `Producto` está registrado en el panel administrativo de Django:

```
/admin/
```

Desde allí se pueden:

* Crear productos
* Editar productos
* Filtrar por categoría
* Activar/desactivar productos



---

# 🛒 Funcionalidades Complementarias del Proyecto

Aunque el foco del Módulo 7 es la administración de productos, el sistema incluye:

* 🔐 Autenticación completa (login / registro / logout)
* 👥 Roles diferenciados (Usuario / Staff)
* 🛒 Carrito persistente por sesión
* 📦 Sistema de pedidos asociado a usuario autenticado
* 🎨 Interfaz personalizada y responsive



---

# 🛠️ Instalación del Proyecto

## 1️⃣ Clonar repositorio

```bash
git clone https://github.com/xgarridoig-jpg/kau-del-viento.git
cd kau-del-viento
```

---

## 2️⃣ Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Aplicar migraciones

```bash
python manage.py migrate
```

---

## 5️⃣ Crear superusuario

```bash
python manage.py createsuperuser
```

---

## 6️⃣ Ejecutar servidor

```bash
python manage.py runserver
```

Ir a:

👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

# 📸 Evidencias 

Se incluyen capturas de:

* ✔ Listado de productos
* ✔ Formulario de creación
* ✔ Edición de producto
* ✔ Eliminación de producto
* ✔ Panel Admin
* ✔ Migraciones aplicadas
* ✔ Base de datos poblada


# 🏁 Conclusión Académica

El proyecto cumple con los requerimientos del **Módulo 7 – Acceso a Datos en Django**, implementando correctamente:

* Arquitectura MVT
* ORM de Django
* Relaciones entre modelos
* Migraciones funcionales
* CRUD completo
* Integración con vistas y templates
* Administración desde Django Admin

Representa la evolución de un sistema e-commerce básico hacia una aplicación con gestión estructurada de datos utilizando buenas prácticas del framework.

---

**Desarrollado por:** Ximena Garrido
Bootcamp Full Stack Python
Módulo 7 – Acceso a Datos en Django 🚀
