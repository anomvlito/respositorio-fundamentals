# Ejemplo 1: Capacitor parcialmente relleno con Dieléctrico

Este ejemplo muestra la resolución paso a paso de un problema típico de certamen sobre capacitores con dieléctricos, aplicando rigurosamente el protocolo de flujo semántico en español y desarrollo continuo.

---

## Enunciado

Un capacitor de placas paralelas de área de placas $A$ y separación de placas $d$ se llena hasta la mitad con un dieléctrico de constante dieléctrica $\kappa$, de modo que las dos capas resultantes quedan apiladas una sobre la otra (cada capa tiene un espesor $d/2$). 

1. Encuentre la capacitancia equivalente $C_{\text{eq}}$ del sistema.
2. Si el capacitor está cargado inicialmente con una carga de magnitud $Q_0$ y luego se aísla, determine la diferencia de potencial final $V_f$ en términos de la diferencia de potencial en vacío $V_0$.
3. Si en lugar de aislarse, el capacitor se mantiene conectado a una batería de voltaje $V_0$, determine la carga final $Q_f$ del capacitor en términos de la carga inicial en vacío $Q_0$.

---

## Resolución

### Parte 1: Obtención de la Capacitancia Equivalente

Para modelar este capacitor parcialmente relleno, representamos el sistema como una conexión en serie de dos capacitores independientes: el capacitor inferior de espesor $d_1 = d/2$ relleno con dieléctrico $\kappa$, y el capacitor superior de espesor $d_2 = d/2$ en vacío ($\kappa_2 = 1$). 

Las capacitancias de estas dos porciones están dadas por:
$$C_1 = \kappa \epsilon_0 \frac{A}{d/2} = \frac{2\kappa\epsilon_0 A}{d}$$
y
$$C_2 = \epsilon_0 \frac{A}{d/2} = \frac{2\epsilon_0 A}{d}$$

Como ambos sub-capacitores se encuentran en serie debido al apilamiento perpendicular al campo eléctrico, la capacitancia equivalente se calcula mediante la relación inversa:
$$\frac{1}{C_{\text{eq}}} = \frac{1}{C_1} + \frac{1}{C_2}$$

Sustituyendo los valores de $C_1$ y $C_2$ en la ecuación anterior obtenemos:
$$\frac{1}{C_{\text{eq}}} = \frac{d}{2\kappa\epsilon_0 A} + \frac{d}{2\epsilon_0 A}$$

Factorizando el término común de la derecha:
$$\frac{1}{C_{\text{eq}}} = \frac{d}{2\epsilon_0 A} \left( \frac{1}{\kappa} + 1 \right) = \frac{d}{2\epsilon_0 A} \left( \frac{\kappa + 1}{\kappa} \right)$$

Invirtiendo ambos miembros para despejar la capacitancia equivalente del sistema:
$$C_{\text{eq}} = \frac{2\kappa}{\kappa + 1} \frac{\epsilon_0 A}{d}$$

Identificando la capacitancia original en vacío $C_0 = \epsilon_0 A / d$, reescribimos el resultado final como:
$$C_{\text{eq}} = \left(\frac{2\kappa}{\kappa + 1}\right) C_0$$

---

### Parte 2: Escenario Aislado ($Q$ constante)

En el escenario donde el capacitor se aísla de toda fuente antes de introducir la placa dieléctrica, la carga acumulada en las placas no puede variar, por lo que:
$$Q_f = Q_0$$

Relacionando la carga, la diferencia de potencial y la capacitancia mediante la definición macroscópica del capacitor:
$$V_f = \frac{Q_f}{C_{\text{eq}}}$$

Reemplazando los resultados de la carga constante y de la capacitancia equivalente:
$$V_f = \frac{Q_0}{\left(\frac{2\kappa}{\kappa+1}\right) C_0}$$

Dado que la diferencia de potencial en vacío es $V_0 = Q_0/C_0$, simplificamos para obtener la relación pedida:
$$V_f = \left(\frac{\kappa + 1}{2\kappa}\right) V_0$$

---

### Parte 3: Escenario Conectado ($V$ constante)

Si el capacitor permanece conectado a la batería durante la introducción del dieléctrico, la diferencia de potencial se mantiene fija por la fuente de tensión:
$$V_f = V_0$$

Calculando la nueva carga libre acumulada en las placas:
$$Q_f = C_{\text{eq}} V_f$$

Reemplazando el valor de la capacitancia equivalente obtenida en la Parte 1:
$$Q_f = \left(\frac{2\kappa}{\kappa + 1}\right) C_0 V_0$$

Sustituyendo el valor de la carga en vacío $Q_0 = C_0 V_0$ en la expresión anterior, concluimos la relación de carga final:
$$Q_f = \left(\frac{2\kappa}{\kappa + 1}\right) Q_0$$
