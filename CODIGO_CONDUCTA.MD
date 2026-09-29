# 🤝 CÓDIGO DE CONDUCTA Y FUNDAMENTOS TÉCNICOS

Este documento establece las directrices éticas, operativas y de arquitectura para toda persona, agente o colaborador que participe en este repositorio.

Su propósito es **formar personas éticas** que usen la automatización para promover el **bienestar y el beneficio real** de otras personas, con un **criterio científico recto**: afirmar solo lo que se puede verificar, mostrar la evidencia y corregir cuando los datos lo exigen.

La inteligencia artificial alivia cargas de trabajo pesadas, pero **no tiene criterio propio**. La responsabilidad y las decisiones finales recaen única y exclusivamente en los `CODEOWNERS`.

---

## 📐 Cómo leer este documento

Cada cláusula declara siempre dos compromisos:

| Declaración | Significado |
|---|---|
| 🛡️ **CODEOWNERS** | Qué responsabilidad asumen las personas que revisan y aprueban el código. |
| 🌱 **USERS BENEFIT** | Qué beneficio concreto y verificable recibe quien usa o depende del sistema. |

Una cláusula que no puede justificar su beneficio para las personas usuarias no forma parte de este proyecto.

---

## 1. CONVIVENCIA

**1.1 Espacio respetuoso e inclusivo.** Este equipo es un espacio seguro para todas las personas, sin importar su experiencia, identidad, origen o forma de trabajar.
- 🛡️ **CODEOWNERS:** dan el ejemplo y atienden cualquier situación de exclusión en cuanto la detectan.
- 🌱 **USERS BENEFIT:** reciben herramientas creadas por un equipo diverso, que considera más necesidades y comete menos errores por puntos ciegos.

**1.2 Crítica al código, nunca a las personas.** La comunicación es amable y directa, y cada observación se argumenta con evidencia.
- 🛡️ **CODEOWNERS:** revisan con sugerencias concretas, a tiempo y con la razón técnica de cada cambio que piden.
- 🌱 **USERS BENEFIT:** reciben código que mejoró por argumentos verificables, no por jerarquía ni preferencias personales.

**1.3 Conocimiento compartido.** Las preguntas técnicas se hacen en los canales compartidos de Discord y las soluciones se sustentan en el foro.
- 🛡️ **CODEOWNERS:** responden en público para que todo el equipo aprenda de cada respuesta.
- 🌱 **USERS BENEFIT:** se benefician de soluciones revisadas por muchas personas, no por una sola.

**1.4 Respeto por el trabajo ajeno.** Nadie modifica el agente ni la carpeta de otra persona sin su acuerdo, y quien vaya a retrasarse con una tarea avisa a tiempo.
- 🛡️ **CODEOWNERS:** protegen la autoría de cada colaborador y planifican según los avisos recibidos.
- 🌱 **USERS BENEFIT:** reciben entregas predecibles, con responsables identificables para cada parte.

**1.5 Conductas no aceptadas.** No se aceptan el acoso, los insultos, las burlas ni los comentarios discriminatorios. Tampoco se permite compartir información privada sin permiso ni intentar saltarse las reglas del repositorio o las protecciones de `main`.
- 🛡️ **CODEOWNERS:** aplican las consecuencias de forma proporcional y con confidencialidad.
- 🌱 **USERS BENEFIT:** sus datos y su confianza se protegen dentro de un entorno donde las reglas se cumplen.

---

## 2. PRINCIPIOS CLAVE

**2.1 Usuario al centro.** Todo proceso de validación, *parsing* e ingesta de datos prioriza la claridad, la precisión y la experiencia de quien gestiona la información final. Los datos se tratan con ética, optimismo y altruismo, sin intenciones dobles ni maliciosas.
- 🛡️ **CODEOWNERS:** rechazan cualquier cambio que sacrifique la claridad o la honestidad hacia las personas usuarias a cambio de conveniencia técnica.
- 🌱 **USERS BENEFIT:** reciben herramientas que les apoyan de verdad, con resultados comprensibles y datos tratados de buena fe.

**2.2 Criterio humano intransferible.** La IA y los flujos automatizados no tienen criterio ni intención propios. El juicio crítico y la validación final son exclusivos de las personas.
- 🛡️ **CODEOWNERS:** firman y responden por cada decisión aprobada, y ninguna se delega a un modelo.
- 🌱 **USERS BENEFIT:** siempre hay una persona responsable a quien acudir, no una "caja negra".

**2.3 Cero tolerancia a la ambigüedad.** Ante una discrepancia, una anomalía o un dato que no cumpla el esquema esperado, el sistema se detiene o escala el caso en lugar de suponer un valor por defecto.
- 🛡️ **CODEOWNERS:** definen reglas explícitas de escalamiento y revisan cada caso detenido.
- 🌱 **USERS BENEFIT:** evitan decisiones silenciosas tomadas sobre datos dudosos que afecten su dinero o su información.

**2.4 Criterio científico recto.** Toda afirmación sobre el sistema, como "funciona", "es válido" o "está corregido", se respalda con evidencia reproducible: pruebas, reportes o datos de entrada y salida.
- 🛡️ **CODEOWNERS:** exigen evidencia antes de aprobar, reconocen públicamente los errores y corrigen cuando los datos contradicen una suposición.
- 🌱 **USERS BENEFIT:** confían en resultados comprobables y reciben la verdad aunque no sea la respuesta esperada.

---

## 3. IDENTIDAD DISTINTIVA

**3.1 Validación estricta y defensiva.** Todo documento externo (facturas, extractos o cotizaciones) se considera no confiable por defecto y pasa filtros rigurosos antes de tocar la base de datos.
- 🛡️ **CODEOWNERS:** mantienen y amplían las reglas de validación, y ninguna excepción se aprueba sin justificación escrita.
- 🌱 **USERS BENEFIT:** sus registros quedan protegidos frente a datos falsos, mal formados o manipulados.

**3.2 Transparencia y trazabilidad.** Cada archivo procesado deja una huella clara y auditable, como el `reporte.md`, de su paso por las capas de validación.
- 🛡️ **CODEOWNERS:** aseguran que cada rechazo o alerta explique el motivo en lenguaje comprensible.
- 🌱 **USERS BENEFIT:** pueden saber qué pasó con sus datos, por qué pasó y quién lo aprobó.

**3.3 Calidad antes que velocidad.** La velocidad de procesamiento nunca compromete la calidad de los datos.
- 🛡️ **CODEOWNERS:** frenan cualquier automatización que aumente el volumen a costa de la exactitud.
- 🌱 **USERS BENEFIT:** reciben información correcta, aunque tarde un poco más.

---

## 4. ARQUITECTURA

**4.1 Prevención de fraude por diseño.** Los módulos de lectura y validación trabajan en una capa aislada (*staging/ingress*) y bloquean inyecciones, formatos alterados e intentos de fraude antes de llegar a las estructuras persistentes. Las descripciones que dan órdenes, como "ignorar validación", se marcan como 🚨 **SOSPECHOSO**.
- 🛡️ **CODEOWNERS:** revisan cada alerta de fraude y nunca desactivan una protección para "hacer pasar" un dato.
- 🌱 **USERS BENEFIT:** quedan protegidos frente a instrucciones maliciosas escondidas en los datos.

**4.2 Mitigación rigurosa de alucinaciones.** Los modelos y analizadores de documentos se limitan con esquemas tipados y reglas deterministas. Ninguna interpretación probabilística modifica registros financieros o críticos.
- 🛡️ **CODEOWNERS:** verifican que toda salida de IA pase por reglas deterministas antes de aceptarse.
- 🌱 **USERS BENEFIT:** sus registros reflejan hechos verificados, no suposiciones de un modelo.

**4.3 Desacoplamiento de flujos externos.** La lectura de archivos externos (Markdown, PDF, XML, CSV o JSON) vive separada del motor de persistencia, con un diseño modular, seguro y fácil de auditar.
- 🛡️ **CODEOWNERS:** mantienen esa separación y rechazan los atajos que mezclen las capas.
- 🌱 **USERS BENEFIT:** una falla en la lectura de un archivo no compromete el resto de sus datos.

**4.4 Solo lectura sobre las fuentes.** Los robots revisores **leen** los datos de origen, nunca los modifican.
- 🛡️ **CODEOWNERS:** rechazan cualquier cambio que permita a un robot alterar los archivos de entrada.
- 🌱 **USERS BENEFIT:** conservan siempre el original intacto para comparar y auditar.

---

## 5. COORDINACIÓN DE AGENTES

**5.1 Subordinación estricta al control humano.** Todo agente automatizado o asistente de código asiste en tareas repetitivas y está subordinado a las revisiones, pruebas y aprobaciones manuales.
- 🛡️ **CODEOWNERS:** supervisan a cada agente y responden por lo que hace en el repositorio.
- 🌱 **USERS BENEFIT:** reciben la eficiencia de la automatización con la garantía del juicio humano.

**5.2 Validación cruzada de cambios.** Los agentes no pueden hacer *push* directo a `main` ni modificar configuraciones críticas de seguridad o validación sin un *Pull Request* aprobado por personas.
- 🛡️ **CODEOWNERS:** son las únicas personas que aprueban y fusionan esos *Pull Requests*.
- 🌱 **USERS BENEFIT:** ningún cambio llega a producción sin que al menos una persona lo haya revisado.

**5.3 Prevención de sesgos y errores sistémicos.** La coordinación entre agentes se basa en contratos de datos estrictos y pruebas automatizadas, para no propagar errores de interpretación.
- 🛡️ **CODEOWNERS:** diseñan esos contratos y pruebas, y los revisan cuando aparece un error nuevo.
- 🌱 **USERS BENEFIT:** un error de un agente se detecta a tiempo y no se multiplica en cadena.

---

## 6. CÓMO REPORTAR

Escribe en privado a la administradora (**@saorionline**). Los reportes se tratan con confidencialidad. Las consecuencias van desde un aviso hasta la retirada del acceso al repositorio, según la gravedad.

- 🛡️ **CODEOWNERS:** atienden cada reporte con confidencialidad, imparcialidad y proporcionalidad.
- 🌱 **USERS BENEFIT:** cuentan con un canal seguro para señalar cualquier riesgo, y su reporte ayuda a proteger a todas las personas.
