# Entrega: Aplicación del Teorema de Bayes y Análisis de Falsos Positivos

**Materia:** Optativa 3 - Ciencia de Datos | Semana 2  
**Tema:** Probabilidad Aplicada y Razonamiento Bayesiano  

---

## Planteamiento del Problema
Un hospital implementa una prueba rápida para una enfermedad:
- **Sensibilidad:** $P(+ \mid E) = 0.99$ (99% de verdaderos positivos).
- **Especificidad:** $P(- \mid S) = 0.95$ (95% de verdaderos negativos).
- **Prevalencia de la enfermedad:** $P(E) = 0.01$ (1% de la población).
- **Tasa de falsos positivos:** $P(+ \mid S) = 1 - 0.95 = 0.05$ (5%).

---

### a) Aplicando el teorema de Bayes, calcula la probabilidad real de que el paciente esté enfermo dado que dio positivo. Muestra el procedimiento.

#### 1. Variables y Eventos
- $E$: El paciente padece la enfermedad.
- $S$: El paciente está sano ($P(S) = 1 - 0.01 = 0.99$).
- $+$: La prueba resulta positiva.

#### 2. Probabilidad Total de Dar Positivo $P(+)$
Utilizando la Ley de Probabilidad Total:
$$P(+) = P(+ \mid E) \cdot P(E) + P(+ \mid S) \cdot P(S)$$
$$P(+) = (0.99 \times 0.01) + (0.05 \times 0.99)$$
$$P(+) = 0.0099 + 0.0495 = 0.0594 \quad (5.94\%)$$

#### 3. Aplicación del Teorema de Bayes para $P(E \mid +)$
$$P(E \mid +) = \frac{P(+ \mid E) \cdot P(E)}{P(+)}$$
$$P(E \mid +) = \frac{0.99 \times 0.01}{0.0594} = \frac{0.0099}{0.0594} = \frac{1}{6} \approx 0.166666...$$

#### Resultado Final:
$$\mathbf{P(E \mid +) \approx 16.67\%}$$

**Conclusión:** La probabilidad real de que el paciente esté efectivamente enfermo tras recibir un resultado positivo es de **solo el 16.67%** (aproximadamente 1 de cada 6 personas con resultado positivo).

---

### b) Explica con tus palabras por qué una prueba "99 % precisa" produce tantos falsos positivos en este escenario.

El resultado resulta contraintuitivo debido a que la atención suele centrarse en la alta precisión de la prueba (99%) omitiendo el volumen masivo del grupo de personas sanas.

Imaginemos una muestra representativa de **10,000 personas**:
1. **100 personas están enfermas** (1%). La prueba detecta a **99** de ellas (verdaderos positivos).
2. **9,900 personas están sanas** (99%). La prueba genera un 5% de falsos positivos:  
   $$5\% \times 9,900 = \mathbf{495 \text{ falsos positivos}}$$

**Resumen de Pruebas Positivas Totales ($99 + 495 = 594$):**
- Verdaderos enfermos detectados: **99**
- Sanos diagnosticados erróneamente como positivos: **495**

Dado que el grupo de personas sanas es 99 veces mayor que el de enfermos, el 5% de error sobre la población sana produce **5 veces más falsos positivos que la totalidad de enfermos reales**.

---

### c) ¿Qué papel juega la probabilidad previa (el 1 % de prevalencia) en el resultado? ¿Qué pasaría si la enfermedad afectara al 30 % de la población?

#### 1. Rol de la Probabilidad Previa $P(E)$:
La probabilidad previa establece la certeza inicial antes de realizar la medición. Al ser la enfermedad sumamente rara (1%), la hipótesis por defecto de que el paciente está sano es muy fuerte; la evidencia de un solo test positivo actualiza la probabilidad, pero no alcanza para convertirla en una certeza absoluta.

#### 2. Recálculo con Prevalencia del 30% ($P(E) = 0.30$):
- $P(E) = 0.30 \quad \implies \quad P(S) = 0.70$
- $P(+) = (0.99 \times 0.30) + (0.05 \times 0.70) = 0.297 + 0.035 = 0.332$
- $P(E \mid +) = \frac{0.297}{0.332} \approx \mathbf{89.46\%}$

**Comparación:**
- Con **1% de prevalencia**, dar positivo da un **16.67%** de probabilidad real de estar enfermo.
- Con **30% de prevalencia**, dar positivo eleva la probabilidad real al **89.46%**.

---

### d) Relaciona este caso con el diseño de un sistema automático de detección (antivirus, filtro de fraude): ¿por qué minimizar falsos positivos es un problema de ingeniería y no solo de matemáticas?

En sistemas computacionales reales (ej. detección de fraude bancario o antivirus), los eventos maliciosos tienen una prevalencia extremadamente baja (ej. 0.01% de transacciones son fraudulentas).

Minimizar los falsos positivos es un problema crítico de ingeniería por:

1. **Experiencia de Usuario (UX) e Impacto Financiero:** Un 5% de falsos positivos en un banco significaría bloquear miles de compras legítimas de clientes honestos, destruyendo la confianza y generando pérdidas económicas.
2. **Estabilidad de Infraestructura (Antivirus):** Si un antivirus detecta por error como virus un archivo `.dll` legítimo del sistema operativo (falso positivo), puede inhabilitar miles de servidores de una empresa.
3. **Fatiga de Alertas (*Alert Fatigue*):** En centros de monitoreo de seguridad, una avalancha de falsos positivos insensibiliza a los analistas, lo que puede provocar que pasen por alto un ciberataque real.
4. **Trade-offs de Ingeniería:** Mientras que en matemáticas se optimizan métricas puras, en ingeniería se deben calibrar los umbrales de decisión (*decision thresholds*) evaluando la matriz de costos reales del negocio y equilibrando la **Precisión** vs. la **Sensibilidad** (F-beta score).
