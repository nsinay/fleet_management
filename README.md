# Fleet Management Module

## Descripción

Módulo personalizado de Odoo desarrollado para la gestión de vehículos asociados a contactos.

El módulo permite:

- Registrar y administrar vehículos.
- Asociar vehículos a contactos.
- Transferir vehículos entre contactos.
- Llevar historial de transferencias.
- Generar reportes PDF de vehículos.
- Consumir un endpoint REST para consultar vehículos por contacto.

---

## Tecnologías y Herramientas Utilizadas

El desarrollo fue realizado utilizando las herramientas permitidas definidas en la prueba técnica:

- Odoo Community 18
- Python
- XML
- PostgreSQL
- Git y GitHub
- Visual Studio Code
- Máquina virtual Linux utilizada como entorno de desarrollo y pruebas

<img width="1912" height="983" alt="image" src="https://github.com/user-attachments/assets/0657215b-b941-450d-a9b5-bec9985e9e48" />
<img width="1402" height="557" alt="image" src="https://github.com/user-attachments/assets/844a6b01-a9fe-4b64-b939-cd9b592bf72f" />

---

## Funcionalidades

### Gestión de Vehículos

Registro de vehículos con:

- Matrícula
- Marca
- Modelo
- Año
- Tipo de vehículo
- Color

### Integración con Contactos

Los vehículos están relacionados con contactos de Odoo (`res.partner`).

<img width="478" height="631" alt="image" src="https://github.com/user-attachments/assets/eada3c4b-1ae4-4969-8b7b-b6fa997c7ade" />
<img width="1918" height="336" alt="image" src="https://github.com/user-attachments/assets/fe1124ff-5d8c-4ccf-955b-70db93325213" />
<img width="1902" height="442" alt="image" src="https://github.com/user-attachments/assets/79230edd-1468-4b6e-98cf-6e061289c9ad" />




### Wizard de Transferencia

Permite transferir vehículos entre contactos.

Incluye:

- Contacto origen
- Contacto destino
- Registro automático del historial

  <img width="620" height="411" alt="image" src="https://github.com/user-attachments/assets/914e4fba-41a1-46be-b6ea-852bea140f40" />
  <img width="1062" height="408" alt="image" src="https://github.com/user-attachments/assets/6e85110d-640b-4a5c-ba7c-f06f7852f653" />
  <img width="1920" height="931" alt="image" src="https://github.com/user-attachments/assets/50f4e09b-5957-4ad5-80c1-b35eb95c33b4" />


### Historial de Transferencias

Se almacena:

- Propietario anterior
- Nuevo propietario
- Fecha de transferencia
- Usuario que realizó la acción

<img width="1903" height="578" alt="image" src="https://github.com/user-attachments/assets/f8f13786-7cd8-45d7-9b4f-176d7ef93a63" />

### Reporte PDF

Generación de reporte PDF con información del vehículo.

[Vehiculos - Acme Corporation (1).pdf](https://github.com/user-attachments/files/27987262/Vehiculos.-.Acme.Corporation.1.pdf)
<img width="1902" height="921" alt="image" src="https://github.com/user-attachments/assets/d47de00d-14f0-4ed9-9745-3a6f69d9dedf" />

### Seguridad y Permisos

El módulo incluye configuración de seguridad mediante grupos y reglas de acceso.

Se implementaron permisos para:

- Gestión de vehículos
- Acceso al historial de transferencias
- Uso del wizard de transferencia
- Acceso a reportes

Además, se configuraron archivos de seguridad utilizando:

- `ir.model.access.csv`
- Grupos de seguridad
- Reglas de acceso por modelo

Esto permite controlar qué usuarios pueden visualizar, crear, modificar o eliminar registros dentro del módulo.

<img width="1506" height="448" alt="image" src="https://github.com/user-attachments/assets/1ec074b9-b4bc-4ff8-a0d4-9056886ecebb" />

usuario
<img width="934" height="445" alt="image" src="https://github.com/user-attachments/assets/e9af488a-da00-4e6c-8267-9c0a602c5b3e" />

admin
<img width="924" height="444" alt="image" src="https://github.com/user-attachments/assets/13ddab12-3f41-4001-bfc2-18e20b851dad" />


### Endpoint REST API

Permite consultar vehículos asociados a un contacto.

#### Endpoint

```http
GET /api/vehicles/contact/<partner_id>
```

#### Ejemplo

```http
http://192.168.0.13:8069/api/vehicles/contact/10
```

#### Respuesta JSON

```json
{
    "success": true,
    "partner_id": 10,
    "partner_name": "Acme Corporation",
    "total_vehicles": 3,
    "vehicles": [
        {
            "id": 1,
            "license_plate": "10RTY",
            "brand": "TOYOTA",
            "model": "2050",
            "year": 2011,
            "vehicle_type": "pickup",
            "color": "Negro"
        }
    ]
}
```

<img width="757" height="737" alt="image" src="https://github.com/user-attachments/assets/724d93f8-c87b-47ac-99a9-a09d6c95dcee" />


---

## Instalación

### Opción 1: Clonar el repositorio

Clonar el repositorio dentro de la carpeta de addons personalizados de Odoo


### Opción 2: Archivo ZIP

Descargar el módulo `.zip` y copiar la carpeta `fleet_management` dentro del directorio de addons personalizados de Odoo.

---

### Pasos de instalación

1. Reiniciar el servidor de Odoo.

2. Actualizar la lista de aplicaciones.

3. Instalar el módulo:
   - Fleet Management

4. Verificar que los menús y funcionalidades estén disponibles correctamente.
   
<img width="921" height="474" alt="image" src="https://github.com/user-attachments/assets/c19a0924-8277-4056-bea1-2db7ed702f92" />

---

## Dependencias

- base
- contacts
- web

---

## Versión de Odoo

Desarrollado y probado en:

- Odoo Community 18

---

## Estructura del Proyecto

```text
fleet_management/
├── controllers/
├── models/
├── report/
├── security/
├── static/
├── views/
├── wizard/
├── README.md
├── __init__.py
└── __manifest__.py
```

---

## Autor

Nery Sinay
