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
