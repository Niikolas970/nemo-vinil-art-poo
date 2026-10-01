# Nemo Vinil Art – POO

Proyecto académico de **Programación Orientada a Objetos** desarrollado para el proyecto Nemo Vinil Art.

El proyecto busca aplicar los conceptos de programación orientada a objetos al desarrollo de una solución de software relacionada con el catálogo y la gestión de clientes de Nemo Vinil Art.

Durante el desarrollo se han trabajado progresivamente conceptos como clases, objetos, encapsulamiento, CRUD, herencia, polimorfismo, relaciones entre clases, persistencia de datos con SQLite e interfaz gráfica con Tkinter.

---

## Objetivo del proyecto

Aplicar los principios y conceptos de Programación Orientada a Objetos mediante el desarrollo progresivo de una solución para **Nemo Vinil Art**, utilizando Python.

El proyecto parte de las necesidades reales del negocio y permite modelar elementos como productos y clientes mediante clases y objetos.

La solución evoluciona desde operaciones realizadas en memoria hasta una aplicación con:

- Persistencia de datos.
- Base de datos SQLite.
- Operaciones CRUD.
- Interfaz gráfica.
- Integración de las diferentes clases del proyecto.

---

## Contexto de Nemo Vinil Art

Nemo Vinil Art es un negocio relacionado con la comercialización y personalización mediante materiales de vinilo.

Dentro del proyecto académico se contemplan diferentes tipos de materiales, entre ellos:

- Vinilos reflectivos.
- Vinilos tornasol.
- Polarizados.
- PPF.
- Otros materiales utilizados para personalización de vehículos y diferentes superficies.

El proyecto busca representar mediante programación las entidades y operaciones relacionadas con este contexto.

---

## Tecnologías utilizadas

- Python
- Programación Orientada a Objetos
- SQLite
- `sqlite3`
- Tkinter
- Git
- GitHub
- DB Browser for SQLite

---

## Conceptos de Programación Orientada a Objetos

Durante el desarrollo del proyecto se han aplicado los principales conceptos de POO:

### Clases y objetos

Se utilizan clases para representar elementos del negocio y objetos para crear instancias concretas de dichas clases.

Entre las clases trabajadas se encuentran:

- `Producto`
- `Cliente`
- `ViniloReflectivo`
- `ViniloTornasol`

### Encapsulamiento

Se utilizan atributos y métodos para controlar el acceso y modificación de la información de los objetos.

### Herencia

Se desarrollaron clases especializadas a partir de `Producto`.

```text
Producto
├── ViniloReflectivo
└── ViniloTornasol

Las clases hijas reutilizan atributos y métodos de la clase Producto mediante super().
Polimorfismo
El proyecto contempla el uso de métodos con comportamientos diferentes cuando las clases especializadas lo requieren.
Relaciones entre clases
Se implementaron relaciones entre objetos del proyecto.
Una de las relaciones trabajadas es:
Cliente ───────────→ Producto
       asociación

Un cliente puede consultar productos, mientras que ambos objetos pueden existir independientemente.
CRUD
El proyecto ha trabajado las cuatro operaciones fundamentales de un CRUD:
- Create – Crear.
- Read – Leer.
- Update – Actualizar.
- Delete – Eliminar.
Inicialmente estas operaciones fueron desarrolladas utilizando listas de Python.
Posteriormente se migraron a una base de datos SQLite para conseguir persistencia de la información.
Persistencia con SQLite
A partir del Corte 3, el proyecto incorpora persistencia de datos utilizando SQLite.
La base de datos utilizada es:
nemo_vinil_art.db

La información de los clientes se almacena en la tabla:
clientes

Actualmente la tabla contiene los siguientes campos:
Campo	Tipo
nombre	TEXT
cedula	TEXT
telefono	TEXT


La cédula se utiliza como identificador único de cada cliente.
Operaciones de persistencia
La clase Cliente incorpora métodos para trabajar con la base de datos:
guardar()
listar_todos()
actualizar()
eliminar()

Estos métodos utilizan las operaciones SQL correspondientes:
Operación	Método	SQL
Crear	guardar()	INSERT
Leer	listar_todos()	SELECT
Actualizar	actualizar()	UPDATE
Eliminar	eliminar()	DELETE


La conexión se realiza mediante el módulo sqlite3, incluido en Python.
Interfaz gráfica
El proyecto incorpora una interfaz gráfica desarrollada con Tkinter.
La interfaz permite trabajar con los clientes mediante:
- Campo de nombre.
- Campo de cédula.
- Campo de teléfono.
- Botón Guardar.
- Botón Actualizar.
- Botón Eliminar.
- Botón Limpiar.
- Lista visual de clientes.
La interfaz utiliza los mismos métodos de persistencia de la clase Cliente, evitando duplicar la lógica de la base de datos.
La arquitectura trabajada hasta este punto puede representarse de la siguiente manera:
Usuario
   │
   ▼
Tkinter
   │
   ▼
Clase Cliente
   │
   ▼
SQLite
   │
   ▼
nemo_vinil_art.db

Talleres desarrollados
El proyecto se ha construido progresivamente mediante los talleres de la asignatura.
Taller 1 – De mi negocio a objetos
Se identificaron elementos del negocio que podían convertirse en clases.
Entre las clases conceptuales identificadas se encuentran:
- Producto.
- Cliente.
- Cotización.
- Catálogo.
- Servicio.
También se definieron atributos y métodos iniciales para las clases principales.
Taller 2 – Primera clase en Python
Se llevó una de las clases conceptuales a Python.
Se trabajaron:
- Definición de clases.
- Constructor __init__.
- Atributos.
- Métodos.
- Creación de objetos.
La clase principal utilizada fue Producto.
Taller 3 – Trabajo con objetos
Se trabajó con varios objetos de la clase Producto, una lista de productos y diferentes métodos para consultar y modificar su información.
Este taller permitió avanzar desde una única instancia hacia el manejo de colecciones de objetos.
Taller 4 – Primer CRUD
Se implementó un CRUD básico utilizando una lista de objetos Producto.
Se trabajaron las operaciones:
Create
Read
Update
Delete

También se incorporó el método especial:
__str__()


para facilitar la representación de los objetos al imprimirlos.
Taller 5 – Herencia
Se implementó una jerarquía de clases basada en Producto.
Producto
├── ViniloReflectivo
└── ViniloTornasol

Las clases especializadas utilizan:
super().__init__()


para reutilizar el constructor de la clase padre.
Cada clase hija incorpora además características y métodos propios.
Taller 6 – CRUD de Clientes
Se creó la clase:
Cliente


y se implementó un segundo CRUD para gestionar clientes.
La clase incluye información como:
- Nombre.
- Teléfono.
- Correo.
- Compras totales.
Se trabajaron nuevamente las operaciones de crear, leer, actualizar y eliminar.
Taller 7 – Relaciones entre clases y UML
Se trabajaron las relaciones entre las clases del proyecto.
Se implementó una relación de asociación entre:
Cliente → Producto

El cliente puede consultar productos sin que ninguno dependa de la existencia del otro.
También se construyó el modelo UML acumulando:
- Clases.
- Atributos.
- Métodos.
- Herencia.
- Relaciones entre clases.
Taller 8 – Persistencia con SQLite
Se migró el CRUD de clientes desde una lista en memoria hacia una base de datos SQLite.
Se creó:
nemo_vinil_art.db

con la tabla:
clientes

Se implementaron los métodos:
guardar()listar_todos()actualizar()eliminar()


La base de datos fue comprobada utilizando DB Browser for SQLite.
Taller 9 – Interfaz gráfica con Tkinter
Se desarrolló una interfaz gráfica para trabajar con la clase Cliente.
La interfaz permite:
- Registrar clientes.
- Visualizar clientes.
- Seleccionar un cliente.
- Actualizar información.
- Eliminar clientes.
- Limpiar los campos.
La interfaz utiliza la misma base de datos SQLite desarrollada en el Taller 8.
Estructura del proyecto
La estructura del repositorio se organiza progresivamente por talleres:
nemo-vinil-art-poo/
│
├── README.md
│
├── taller-02/
│   └── producto.py
│
├── taller-03/
│   └── productos.py
│
├── taller-04/
│   └── crud_productos.py
│
├── taller-05/
│   └── herencia_productos.py
│
├── taller-06/
│   └── crud_clientes.py
│
├── taller-07/
│   └── relaciones_uml.py
│
├── taller-08/
│   └── taller_08_sqlite.py
│
├── taller-09/
│   └── taller_09_tkinter.py
│
└── nemo_vinil_art.db

La estructura puede continuar evolucionando durante las siguientes sesiones de la asignatura.
Herramientas de apoyo
DB Browser for SQLite
Se utiliza DB Browser for SQLite para visualizar y comprobar la base de datos SQLite.
Permite verificar:
- Tablas.
- Columnas.
- Registros.
- Cambios realizados desde Python.
La herramienta no reemplaza a SQLite. SQLite es el motor de base de datos utilizado por Python mediante sqlite3, mientras que DB Browser funciona como herramienta gráfica de visualización y administración.
Control de versiones
El proyecto utiliza Git y GitHub para controlar las diferentes versiones del código desarrollado durante la asignatura.
El repositorio principal del proyecto es:
nemo-vinil-art-poo
La rama principal utilizada es:
main

Durante el desarrollo pueden utilizarse ramas de funcionalidad para trabajar cambios específicos antes de integrarlos a la rama principal.
Ejemplo:
main
 │
 └── feature/taller-09-tkinter
          │
          ├── desarrollo
          ├── commit
          └── merge → main

Estado actual del proyecto
Actualmente el proyecto cuenta con:
- Modelo inicial del negocio.
- Clases y objetos en Python.
- CRUD de productos.
- CRUD de clientes.
- Herencia.
- Relaciones entre clases.
- Modelo UML.
- Persistencia mediante SQLite.
- Base de datos nemo_vinil_art.db.
- Tabla clientes.
- Métodos guardar(), listar_todos(), actualizar() y eliminar().
- Interfaz gráfica inicial con Tkinter.
- Visualización de la base de datos mediante DB Browser for SQLite.
- Repositorio GitHub para controlar el desarrollo.
Próximos pasos
Los siguientes pasos del proyecto están orientados a integrar las diferentes partes desarrolladas durante la asignatura.
Entre ellos se encuentran:
- Integrar las diferentes clases del proyecto.
- Completar la interfaz gráfica.
- Conectar las diferentes funcionalidades con la base de datos.
- Mejorar la interacción entre las clases.
- Consolidar la aplicación final.
- Realizar las pruebas correspondientes.
- Preparar la entrega y sustentación del proyecto.
Autor
Nicolás Piraján
Proyecto académico de Ingeniería de Software
Programación Orientada a Objetos – Uniempresarial
