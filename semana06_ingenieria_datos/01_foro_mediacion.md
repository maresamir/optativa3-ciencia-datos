# Actividad 1: Foro de Mediación - Reflexión Crítica

**Materia:** Optativa 3 - Ciencia de Datos  
**Semana 6:** Fundamentos de Ingeniería de Datos  
**Estudiante:** Samir Mares Benvenuto  

---

## 📌 Pregunta Detonadora

> *"Se dice que un científico de datos dedica hasta el 80% de su tiempo a preparar y mover datos, no a construir modelos. Si la ingeniería de datos es tan determinante, ¿por qué crees que suele recibir menos reconocimiento que el modelado o la inteligencia artificial? ¿Qué consecuencias tiene para una organización descuidar su infraestructura de datos?"*

---

## ✍️ Respuesta Inicial (224 palabras)

Considero que la ingeniería de datos padece del "sesgo de invisibilidad": cuando las tuberías funcionan a la perfección, el flujo de datos es transparente y los directivos atribuyen el éxito comercial al algoritmo predictivo o a la interfaz del dashboard, ignorando el cimiento que lo sostiene. Tal como señalan Reis y Housley (2022) en *Fundamentals of Data Engineering*, la ingeniería de datos constituye la base insustituible de la jerarquía de necesidades de la IA; sin ingestión confiable, almacenamiento estructurado y gobernanza, cualquier modelo carece de validez. El modelado analítico se percibe como la "magia visible", mientras que la ingeniería es tratada erróneamente como fontanería operativa.

Descuidar la infraestructura de datos acarrea consecuencias críticas para cualquier organización: silos informativos, costos descontrolados de almacenamiento en la nube, latencias inaceptables y, sobre todo, la proliferación del axioma *Garbage In, Garbage Out*. Un ejemplo concreto ocurre en el comercio electrónico: si un pipeline ETL no implementa resolución de identidades ni manejo de transacciones duplicadas entre la aplicación móvil y el punto de venta físico, la tabla de hechos registrará compras dobles o clientes inconsistentes. En consecuencia, un modelo de predicción de abandono (*churn*) o el reporte financiero diario de la gerencia proyectará métricas infladas, provocando decisiones estratégicas millonarias basadas en datos ilusorios.

---

## 📚 Referencia Bibliográfica

* Reis, J., & Housley, M. (2022). *Fundamentals of Data Engineering: Plan and Build Robust Data Systems*. O'Reilly Media.
* Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling* (3rd ed.). John Wiley & Sons.

---

## 💬 Réplicas a Compañeros (Interacción en Foro)

### Réplica 1 (Aporte sobre deuda técnica y gobierno del dato)
> **Compañero 1 (Idea central comentada):** Plantea que los ingenieros de datos reciben menos reconocimiento debido a que la mercadotecnia tecnológica vende el concepto de "Inteligencia Artificial" como sinónimo de solución mágica directa.

**Mi réplica:**  
> "Coincido plenamente con tu apreciación sobre el marketing tecnológico. Me gustaría complementar tu argumento señalando que la falta de reconocimiento también se debe a que la deuda técnica en infraestructura no se manifiesta de inmediato, sino como una erosión silenciosa. Cuando una organización prioriza contratar únicamente científicos de datos y omite a los ingenieros de datos, fuerza a los primeros a diseñar scripts *ad-hoc* frágiles para extraer datos. Un caso emblemático es cuando la fuente operacional cambia un tipo de dato (por ejemplo, de `INT` a `VARCHAR`) y los scripts sin validación de esquemas rompen los dashboards de toma de decisiones en plena temporada alta. La ingeniería de datos no solo mueve bytes; implementa contratos de datos (*data contracts*) que salvaguardan la integridad de la organización."

---

### Réplica 2 (Objeción y matiz sobre costos y escalabilidad: ETL vs ELT)
> **Compañero 2 (Idea central comentada):** Sugiere que en la actualidad las herramientas *no-code* y los Data Lakes en la nube hacen innecesario invertir tanto tiempo en ingeniería previa, ya que "se puede subir todo y luego ver cómo se procesa".

**Mi réplica:**  
> "Agradezco mucho tu perspectiva, ya que toca el auge del paradigma ELT y las herramientas modernas de autoservicio. No obstante, quisiera poner sobre la mesa una objeción: adoptar la postura de 'subir todo crudo al Data Lake y resolver después' sin una ingeniería rigurosa suele derivar en un *Data Swamp* (pantano de datos). Sin un modelado dimensional adecuado (como los principios de Kimball) y sin pipelines que garanticen linaje y particionamiento, las consultas analíticas sobre grandes volúmenes de datos crudos se vuelven lentas y extremadamente costosas en nubes como Snowflake o BigQuery. El poder de cómputo en la nube es abundante, pero no gratuito ni infinito; una tubería descuidada convierte un lago de datos en un pasivo financiero y de cumplimiento normativo."
