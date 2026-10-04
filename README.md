# Optativa 3 - Ciencia de Datos

Repositorio oficial para las actividades y prácticas de la materia **Optativa 3: Ciencia de Datos**.

---

## 📌 Estructura del Repositorio

### 📂 Semana 1: Entorno Profesional y Exploración Inicial
- `semana01_exploracion.ipynb`: Jupyter Notebook con la carga, exploración estadística y visualización de un dataset de ventas globales de videojuegos (Kaggle).
- `distribucion.png`: Gráfico generado durante la exploración inicial.

### 📂 Semana 2: Estadística Avanzada y Probabilidad Aplicada (I)
- `semana02_estadistica.ipynb`: Jupyter Notebook que contiene:
  1. Cálculo de medidas de tendencia central (media, mediana, moda) y dispersión (desviación estándar, varianza).
  2. Ajuste de histograma empírico frente a la densidad Normal teórica ($N(\mu, \sigma)$).
  3. Simulación y comparación visual de distribuciones **Binomial** y **Poisson** con `scipy.stats`.
  4. Clasificador conceptual de Spam implementando el **Teorema de Bayes**.
- `distribucion_normal_vs_empirica.png`: Gráfico comparativo entre los datos reales y la curva normal teórica.
- `distribuciones_discretas.png`: Gráficos de PMF de las distribuciones Binomial y Poisson.
- `semana02_teorema_bayes_hospital.docx`: Documento de entrega formal sobre Teorema de Bayes y falsos positivos.
- `semana02_teorema_bayes_hospital.md`: Versión Markdown del análisis del Teorema de Bayes.

### 📂 Semana 6: Fundamentos de Ingeniería de Datos (ETL, Modelado y Arquitecturas)
- **Directorio del Proyecto:** [`semana06_ingenieria_datos/`](semana06_ingenieria_datos/)
  - `etl.py`: Pipeline ETL ejecutable en Python (`EXTRACT` -> `TRANSFORM` -> `LOAD` a SQLite).
  - `ventas.csv`: Dataset transaccional fuente (15 ventas detalladas).
  - `almacen.db`: Base de datos relacional SQLite con el modelo dimensional estrella (`dim_categoria` y `fact_ventas`).
  - `semana06_pipeline_etl.ipynb`: Jupyter Notebook interactivo con ejecución paso a paso, análisis SQL y visualizaciones.
  - `ingresos_por_categoria.png`: Gráfico analítico de barras e ingresos/unidades por categoría.
  - `01_foro_mediacion.md`: Respuesta argumentada al foro de mediación (224 palabras), citas bibliográficas y 2 réplicas a compañeros.
  - `03_caso_practico.md`: Análisis arquitectónico y diseño de modelo estrella para la plataforma de streaming de música (Batch vs. Streaming, Lakehouse vs. Warehouse, CEP anti-fraude en tiempo real).
  - `04_quiz_autoevaluacion.md`: Cuestionario de 5 preguntas resuelto y fundamentado con rigor conceptual.
  - `entrega_semana06.md`: Documento unificado y completo de entrega con las cuatro actividades.
  - `entrega_semana06.docx`: Documento formal en Word listo para entrega en Google Classroom.
  - `README.md`: Documentación técnica especializada del pipeline ETL y del esquema estrella.
- **Acceso Directo en Raíz:**
  - `semana06_pipeline_etl.ipynb`: Cuaderno Jupyter de la práctica.
  - `semana06_entrega_completa.md`: Documento consolidado en Markdown.
  - `semana06_entrega_completa.docx`: Documento consolidado en Microsoft Word.

---

## 🛠️ Requisitos e Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/maresamir/optativa3-ciencia-datos.git
   cd optativa3-ciencia-datos
   ```
2. Crear y activar entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows PowerShell:
   .venv\Scripts\activate
   # En macOS/Linux:
   # source .venv/bin/activate
   ```
3. Instalar librerías:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Ejecución del Pipeline ETL (Semana 6)

Para ejecutar el pipeline ETL de la Semana 6 y verificar la persistencia en SQLite y la consulta analítica:

```bash
python semana06_ingenieria_datos/etl.py
```
