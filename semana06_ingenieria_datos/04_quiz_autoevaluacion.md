# Actividad 4: Quiz de Autoevaluación - Fundamentos de Ingeniería de Datos

**Materia:** Optativa 3 - Ciencia de Datos  
**Semana 6:** Fundamentos de Ingeniería de Datos  
**Estudiante:** Samir Mares Benvenuto  
**Resultado:** 5/5 Correctas (100%)  

---

### Pregunta 1
**La diferencia clave entre ETL y ELT es:**
- a) ETL es para bases NoSQL y ELT para SQL.
- **b) El orden de la transformación: ETL transforma antes de cargar; ELT carga crudo y transforma después. [CORRECTA]**
- c) ELT no permite limpiar los datos.
- d) No hay ninguna diferencia real.

> **Justificación:**  
> En **ETL** (*Extract, Transform, Load*), las transformaciones, limpieza y agregaciones se realizan en un servidor intermedio antes de ingresar los datos al almacén de destino. En **ELT** (*Extract, Load, Transform*), los datos se extraen y se depositan crudos en el destino (comúnmente un Data Lake o Data Warehouse en la nube con cómputo elástico), aprovechando el poder de procesamiento del propio motor de destino (como Snowflake o BigQuery) para transformar los datos bajo demanda.

---

### Pregunta 2
**Para detectar un fraude en el instante en que ocurre una transacción, conviene:**
- a) Procesamiento por lotes cada 24 horas.
- b) Guardar todo y revisarlo el fin de semana.
- **c) Procesamiento en streaming (tiempo real). [CORRECTA]**
- d) No se puede detectar fraude con datos.

> **Justificación:**  
> La detección de fraude es un caso de uso de ultra-baja latencia donde el valor de la información decrece exponencialmente con el tiempo transcurrido. El procesamiento en **streaming** evalúa los eventos individualmente o en ventanas de pocos segundos conforme van arribando a la tubería (usando herramientas como Kafka y Flink), permitiendo bloquear la tarjeta o la transacción antes de que se autorice el pago ilegítimo.

---

### Pregunta 3
**Un data lake se caracteriza por:**
- **a) Almacenar datos crudos de cualquier tipo, de forma flexible y barata. [CORRECTA]**
- b) Guardar solo tablas estructuradas y ordenadas.
- c) Ser exclusivo para datos financieros.
- d) No poder almacenar imágenes ni video.

> **Justificación:**  
> Un **Data Lake** es un repositorio centralizado diseñado para almacenar datos masivos en su formato nativo o crudo (*as-is*), ya sean estructurados (tablas CSV/Parquet), semiestructurados (JSON, XML, logs) o no estructurados (imágenes, audio, video). Se fundamenta en almacenamiento de objetos de bajo costo (como Amazon S3 o Google Cloud Storage) aplicando el paradigma *schema-on-read*.

---

### Pregunta 4
**En un esquema estrella, la tabla de hechos (fact table) guarda principalmente:**
- a) Solo texto descriptivo.
- b) Los nombres completos de las categorías repetidos.
- c) Imágenes de los productos.
- **d) Las métricas numéricas y las claves que apuntan a las dimensiones. [CORRECTA]**

> **Justificación:**  
> Según la metodología de Ralph Kimball, la **tabla de hechos** modela un evento o proceso de negocio cuantitativo. Está compuesta por dos tipos de campos: **claves foráneas** que enlazan con las tablas de dimensiones circundantes (contexto: quién, cuándo, dónde) y **métricas numéricas aditivas o semiaditivas** (cantidades, ingresos, tiempos de duración, precios).

---

### Pregunta 5
**Se prefiere un esquema estrella (desnormalizado) sobre uno copo de nieve para un dashboard muy consultado porque:**
- a) Ocupa menos espacio en disco.
- **b) Requiere menos JOINs, por lo que las consultas son más rápidas. [CORRECTA]**
- c) No permite hacer consultas.
- d) Elimina la necesidad de tablas de hechos.

> **Justificación:**  
> En los entornos analíticos (OLAP) orientados a tableros de control y autoservicio, la velocidad de lectura es prioritaria sobre la optimización extrema del espacio en disco. El **esquema estrella desnormaliza** las dimensiones en una sola tabla directa por entidad, reduciendo drásticamente la cantidad de operaciones `JOIN` requeridas en las consultas SQL. Esto disminuye el costo computacional del motor de base de datos y acelera notablemente el tiempo de respuesta del dashboard.
