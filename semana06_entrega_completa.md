# Entrega Integral: Semana 6 - Fundamentos de Ingeniería de Datos

**Materia:** Optativa 3 - Ciencia de Datos  
**Alumno:** Samir Mares Benvenuto  
**Repositorio GitHub:** [https://github.com/maresamir/optativa3-ciencia-datos](https://github.com/maresamir/optativa3-ciencia-datos)  
**Directorio del Proyecto:** `semana06_ingenieria_datos/`  

---

## 📑 Tabla de Contenidos
1. [Actividad 1: Foro de Mediación - Reflexión Crítica](#actividad-1-foro-de-mediación---reflexión-crítica)
2. [Actividad 2: Práctica en Python - Pipeline ETL y Esquema Estrella](#actividad-2-práctica-en-python---pipeline-etl-y-esquema-estrella)
3. [Actividad 3: Caso Práctico - Plataforma de Streaming de Música](#actividad-3-caso-práctico---plataforma-de-streaming-de-música)
4. [Actividad 4: Quiz de Autoevaluación Resuelto y Argumentado](#actividad-4-quiz-de-autoevaluación-resuelto-y-argumentado)

---

# Actividad 1: Foro de Mediación - Reflexión Crítica

### Pregunta Detonadora:
> *"Se dice que un científico de datos dedica hasta el 80% de su tiempo a preparar y mover datos, no a construir modelos. Si la ingeniería de datos es tan determinante, ¿por qué crees que suele recibir menos reconocimiento que el modelado o la inteligencia artificial? ¿Qué consecuencias tiene para una organización descuidar su infraestructura de datos?"*

### Respuesta Inicial (224 palabras):
Considero que la ingeniería de datos padece del "sesgo de invisibilidad": cuando las tuberías funcionan a la perfección, el flujo de datos es transparente y los directivos atribuyen el éxito comercial al algoritmo predictivo o a la interfaz del dashboard, ignorando el cimiento que lo sostiene. Tal como señalan Reis y Housley (2022) en *Fundamentals of Data Engineering*, la ingeniería de datos constituye la base insustituible de la jerarquía de necesidades de la IA; sin ingestión confiable, almacenamiento estructurado y gobernanza, cualquier modelo carece de validez. El modelado analítico se percibe como la "magia visible", mientras que la ingeniería es tratada erróneamente como fontanería operativa.

Descuidar la infraestructura de datos acarrea consecuencias críticas para cualquier organización: silos informativos, costos descontrolados de almacenamiento en la nube, latencias inaceptables y, sobre todo, la proliferación del axioma *Garbage In, Garbage Out*. Un ejemplo concreto ocurre en el comercio electrónico: si un pipeline ETL no implementa resolución de identidades ni manejo de transacciones duplicadas entre la aplicación móvil y el punto de venta físico, la tabla de hechos registrará compras dobles o clientes inconsistentes. En consecuencia, un modelo de predicción de abandono (*churn*) o el reporte financiero diario de la gerencia proyectará métricas infladas, provocando decisiones estratégicas millonarias basadas en datos ilusorios.

### Referencias Bibliográficas:
- Reis, J., & Housley, M. (2022). *Fundamentals of Data Engineering: Plan and Build Robust Data Systems*. O'Reilly Media.
- Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3rd ed.). John Wiley & Sons.

### Réplicas a Compañeros (Listas para el Foro de Classroom):

#### Réplica 1: Sobre Deuda Técnica y Contratos de Datos
> **Aporte al compañero:** Coincido plenamente con tu apreciación sobre el marketing tecnológico. Me gustaría complementar tu argumento señalando que la falta de reconocimiento también se debe a que la deuda técnica en infraestructura no se manifiesta de inmediato, sino como una erosión silenciosa. Cuando una organización prioriza contratar únicamente científicos de datos y omite a los ingenieros de datos, fuerza a los primeros a diseñar scripts *ad-hoc* frágiles para extraer datos. Un caso emblemático es cuando la fuente operacional cambia un tipo de dato (por ejemplo, de `INT` a `VARCHAR`) y los scripts sin validación de esquemas rompen los dashboards de toma de decisiones en plena temporada alta. La ingeniería de datos no solo mueve bytes; implementa contratos de datos (*data contracts*) que salvaguardan la integridad de la organización.

#### Réplica 2: Sobre la Ilusión del "Data Lake Mágico" (ETL vs. ELT)
> **Aporte al compañero:** Agradezco mucho tu perspectiva, ya que toca el auge del paradigma ELT y las herramientas modernas de autoservicio. No obstante, quisiera poner sobre la mesa una objeción: adoptar la postura de "subir todo crudo al Data Lake y resolver después" sin una ingeniería rigurosa suele derivar en un *Data Swamp* (pantano de datos). Sin un modelado dimensional adecuado (como los principios de Kimball) y sin pipelines que garanticen linaje y particionamiento, las consultas analíticas sobre grandes volúmenes de datos crudos se vuelven lentas y extremadamente costosas en nubes como Snowflake o BigQuery. El poder de cómputo en la nube es abundante, pero no gratuito ni infinito; una tubería descuidada convierte un lago de datos en un pasivo financiero y de cumplimiento normativo.

---

# Actividad 2: Práctica en Python - Pipeline ETL y Esquema Estrella

### 1. Descripción de las Fases del Pipeline (`etl.py`)
1. **EXTRACT:** Extracción de 15 transacciones comerciales desde `ventas.csv` con columnas: `producto`, `categoria`, `precio`, `cantidad`.
2. **TRANSFORM:**
   - **Feature Engineering:** Cálculo del ingreso total por registro ($\text{total} = \text{precio} \times \text{cantidad}$).
   - **Modelado Dimensional (Star Schema):** Descomposición en dimensión `dim_categoria` (con clave subrogada `cat_id`) y tabla de hechos central `fact_ventas` (con `venta_id`, `cat_id` como clave foránea, `producto`, `precio`, `cantidad` y `total`).
3. **LOAD:** Persistencia relacional en base de datos SQLite (`almacen.db`) mediante `.to_sql()` de Pandas.
4. **CONSULTA ANALÍTICA (OLAP):** Consulta SQL con agregación (`JOIN`, `GROUP BY`, `SUM`, `AVG`, `ORDER BY`) para obtener el rendimiento por categoría.

### 2. Código Fuente del Pipeline (`etl.py`)

```python
import os
import sys
import pandas as pd
import sqlite3

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_etl():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "ventas.csv")
    db_path = os.path.join(base_dir, "almacen.db")

    print("=" * 65)
    print(">>> INICIANDO PIPELINE ETL - SEMANA 6: INGENIERIA DE DATOS <<<")
    print("=" * 65)

    # ===== 1. EXTRACT =====
    print("\n[1/3] FASE EXTRACT (Extraccion)")
    df = pd.read_csv(csv_path)
    print(f"-> Datos extraidos exitosamente desde '{csv_path}'")
    print(f"-> Total de filas extraidas: {len(df)}")

    # ===== 2. TRANSFORM =====
    print("\n[2/3] FASE TRANSFORM (Transformacion y Modelado Dimensional)")
    df["total"] = df["precio"] * df["cantidad"]

    # Modelado dimensional: Esquema Estrella
    dim_categoria = pd.DataFrame({"categoria": sorted(df["categoria"].unique())})
    dim_categoria["cat_id"] = range(1, len(dim_categoria) + 1)
    dim_categoria = dim_categoria[["cat_id", "categoria"]]

    fact = df.merge(dim_categoria, on="categoria")
    fact["venta_id"] = range(1, len(fact) + 1)
    fact_ventas = fact[["venta_id", "producto", "cat_id", "precio", "cantidad", "total"]]

    # ===== 3. LOAD =====
    print("\n[3/3] FASE LOAD (Carga)")
    conn = sqlite3.connect(db_path)
    dim_categoria.to_sql("dim_categoria", conn, if_exists="replace", index=False)
    fact_ventas.to_sql("fact_ventas", conn, if_exists="replace", index=False)
    print(f"-> Tablas 'dim_categoria' y 'fact_ventas' persistidas exitosamente en '{db_path}'")

    # ===== 4. QUERY ANALITICA =====
    print("\n" + "=" * 65)
    print("CONSULTA ANALITICA SQL (JOIN DE HECHOS Y DIMENSION)")
    print("=" * 65)
    query = """
    SELECT 
        d.categoria, 
        COUNT(f.venta_id) AS num_ventas,
        SUM(f.cantidad) AS unidades_vendidas,
        ROUND(AVG(f.precio), 2) AS precio_promedio,
        ROUND(SUM(f.total), 2) AS ingresos_totales
    FROM fact_ventas f 
    JOIN dim_categoria d ON f.cat_id = d.cat_id 
    GROUP BY d.categoria 
    ORDER BY ingresos_totales DESC;
    """
    res_df = pd.read_sql(query, conn)
    print(res_df.to_string(index=False))
    print("=" * 65)

    conn.close()
    return res_df

if __name__ == "__main__":
    run_etl()
```

### 3. Salida de la Ejecución y Verificación de Resultados
```text
=================================================================
CONSULTA ANALITICA SQL (JOIN DE HECHOS Y DIMENSION)
=================================================================
           categoria  num_ventas  unidades_vendidas  precio_promedio  ingresos_totales
Alimentos Preparados           3                  6            78.33             466.0
       Bebidas Frias           3                  7            51.67             352.0
     Snacks y Dulces           3                 12            26.00             304.0
   Bebidas Calientes           3                  6            45.00             253.0
           Panaderia           3                  7            35.00             221.0
=================================================================
>>> Pipeline ETL completado con exito. <<<
```

---

# Actividad 3: Caso Práctico - Plataforma de Streaming de Música

### Contexto:
Tres fuentes de datos: (1) Eventos de reproducción (millones/minuto), (2) Catálogo de canciones (cambia varias veces al día), y (3) Suscripciones de pago (mensuales).  
Objetivos: Dashboard de tendencias musicales actualizado + Detección inmediata en tiempo real de cuentas compartidas desde varios países simultáneamente.

---

### a) Decisión de Paradigma por Fuente (Batch vs. Streaming):
1. **Eventos de reproducción (Millones/minuto): STREAMING (Híbrido con micro-batching)**  
   - *Justificación:* Los eventos de reproducción son continuos y de altísimo volumen. El paradigma streaming (ej. Apache Kafka + Apache Flink) es imperativo para alimentar de inmediato el algoritmo de detección de fraude geográfico y calcular métricas de tendencias en ventanas de tiempo deslizantes (*sliding windows*). Paralelamente, se van asentando en micro-lotes para el histórico analítico.
2. **Catálogo de canciones (Cambia varias veces al día): BATCH (Micro-lotes programados)**  
   - *Justificación:* Los metadatos de artistas, álbumes y canciones cambian a intervalos discretos. Mantener un consumidor de streaming activo 24/7 generaría un costo computacional injustificado. Un job programado por lotes cada pocas horas (o por eventos CDC) sincroniza los cambios de forma eficiente.
3. **Suscripciones de pago (Mensuales): BATCH (Procesamiento por lotes)**  
   - *Justificación:* Las renovaciones, cobros y liquidaciones bancarias se rigen por ciclos contables fijos. El procesamiento por lotes mensual garantiza transaccionalidad ACID, auditoría bancaria y reportes financieros sin desperdiciar recursos computacionales.

---

### b) Estrategia de Almacenamiento:
1. **Eventos de reproducción crudos:** Se deben almacenar en un **Lakehouse / Data Lake** (por ejemplo, AWS S3 o Azure ADLS con formato abierto **Delta Lake** o **Apache Iceberg**). Esto permite almacenar petabytes de datos semiestructurados (JSON de telemetría) a una fracción del costo de un warehouse, manteniendo capacidades transaccionales ACID y linaje para reentrenar modelos o realizar re-procesamientos.
2. **Catálogo estructurado y métricas del Dashboard:** Se deben almacenar en un **Data Warehouse** (ej. Snowflake, Google BigQuery o capa Gold del Lakehouse). Este almacenamiento columnar relacional está altamente optimizado para consultas SQL concurrentes, indexación y agregaciones analíticas con tiempos de respuesta en milisegundos.

---

### c) Diseño del Esquema Estrella para Tendencias Musicales:

```text
               +-----------------------+
               |      DIM_TIEMPO       |
               +-----------------------+
               | PK  tiempo_id         |
               |     fecha_hora        |
               |     hora_del_dia      |
               |     dia_semana        |
               |     mes, anio         |
               +-----------+-----------+
                           |
+-------------------+      |      +---------------------+
|    DIM_CANCION    |      |      |     DIM_USUARIO     |
+-------------------+      |      +---------------------+
| PK  cancion_id    |      |      | PK  usuario_id      |
|     titulo        |      |      |     tipo_suscripc   |
|     artista       |      |      |     rango_edad      |
|     genero        |      |      |     genero_usuario  |
+---------+---------+      |      +----------+----------+
          |                |                 |
          |       +--------+-------+         |
          +------>|  FACT_REPROD   |<--------+
                  +----------------+
                  | PK reproducc_id|
                  | FK cancion_id  |
                  | FK usuario_id  |
                  | FK tiempo_id   |
                  | FK ubicacion_id|
                  |    segundos_rep|
                  |    completada  |
                  |    fue_saltada |
                  +--------+-------+
                           |
               +-----------+-----------+
               |     DIM_UBICACION     |
               +-----------------------+
               | PK  ubicacion_id      |
               |     pais, ciudad      |
               |     zona_horaria      |
               +-----------------------+
```

- **Tabla de Hechos (`fact_reproducciones`):** Claves foráneas (`cancion_id`, `usuario_id`, `tiempo_id`, `ubicacion_id`) y métricas cuantitativas (`segundos_reproducidos`, indicador booleano `completada`, indicador booleano `fue_saltada`).
- **Tablas de Dimensiones:**
  - `dim_cancion`: Atributos descriptivos (título, artista, álbum, género musical, duración, sello).
  - `dim_usuario`: Perfil del oyente (nivel de suscripción *Free/Premium*, segmento de edad, país de origen).
  - `dim_tiempo`: Jerarquía temporal (año, mes, día, hora, día de la semana, festivo).
  - `dim_ubicacion`: Ubicación geográfica del evento (país, región, ciudad, coordenadas aproximadas).

---

### d) Inadecuación del Pipeline Batch Nocturno para Cuentas Compartidas:
La detección de anomalías geográficas concurrentes (por ejemplo, reproducir música en México y en Japón a los 5 minutos) exige cálculo inmediato:
1. **Pérdida de Ventana Crítica:** Un job batch que corre a la medianoche procesará la infracción hasta 24 horas después. Para entonces, la sesión fraudulenta ya finalizó, el servicio ya fue explotado y el costo en regalías ya se devengó.
2. **Imposibilidad de Intervención en Tiempo Real:** En streaming, un motor de reglas (Complex Event Processing con Kafka + Flink) calcula la velocidad de desplazamiento ($\text{distancia} / \text{tiempo}$); si supera la velocidad física plausible de un vuelo comercial (> 900 km/h), suspende la sesión simultánea o solicita autenticación en dos factores (2FA) en ese preciso instante. El procesamiento batch no ofrece capacidad reactiva.

---

# Actividad 4: Quiz de Autoevaluación

| # | Pregunta | Respuesta Seleccionada | Justificación Técnica |
| :--- | :--- | :--- | :--- |
| **1** | La diferencia clave entre ETL y ELT es: | **b) El orden de la transformación: ETL transforma antes de cargar; ELT carga crudo y transforma después.** | ETL limpia y estructura en un servidor intermedio antes de cargar; ELT almacena en crudo en el destino (Data Lake/Warehouse) y transforma aprovechando la potencia del motor de destino. |
| **2** | Para detectar un fraude en el instante en que ocurre una transacción, conviene: | **c) Procesamiento en streaming (tiempo real).** | Casos de ultra-baja latencia donde la decisión debe tomarse en milisegundos para bloquear la transacción antes de que finalice. |
| **3** | Un data lake se caracteriza por: | **a) Almacenar datos crudos de cualquier tipo, de forma flexible y barata.** | Se sustenta en almacenamiento de objetos elástico y de bajo costo (ej. S3), admitiendo datos estructurados, semiestructurados y no estructurados (*schema-on-read*). |
| **4** | En un esquema estrella, la tabla de hechos guarda principalmente: | **d) Las métricas numéricas y las claves que apuntan a las dimensiones.** | Modela los eventos del proceso de negocio conteniendo métricas cuantitativas aditivas y claves foráneas que referencian a las dimensiones contextuales. |
| **5** | Se prefiere un esquema estrella sobre uno copo de nieve para dashboards porque: | **b) Requiere menos JOINs, por lo que las consultas son más rápidas.** | Al desnormalizar dimensiones, reduce radicalmente el número de operaciones `JOIN`, maximizando el rendimiento analítico (OLAP) en tableros de control. |
