# Referencia de Circuitos de Corriente Directa y RC

Este documento reúne las formulaciones matemáticas y métodos sistemáticos de circuitos eléctricos basados en la convención de FIS1533 y el manual NCEES FE.

---

## 1. Corriente, Resistividad y Ley de Ohm

### Magnitudes Fundamentales:
* **Corriente Eléctrica ($I$):** Tasa de flujo neto de carga libre por unidad de tiempo.
  $$I = \frac{dQ}{dt} \quad [\text{A} = \text{C}/\text{s}]$$
* **Densidad de Corriente ($\vec{J}$):** Corriente por unidad de área normal al flujo.
  $$\vec{J} = nq\vec{v}_d \quad [\text{A}/\text{m}^2]$$
  Donde $n$ es la densidad de portadores, $q$ es la carga de cada portador, y $\vec{v}_d$ es la velocidad de deriva.
* **Ley de Ohm Microscópica:**
  $$\vec{J} = \sigma \vec{E} = \frac{1}{\rho}\vec{E}$$
  Donde $\sigma$ es la conductividad eléctrica y $\rho = 1/\sigma$ es la resistividad del material.
* **Ley de Ohm Macroscópica:**
  $$V = I R \quad [\text{V} = \text{A}\cdot\Omega]$$

### Parámetros de la Resistencia:
* **Dependencia Geométrica (Resistencia Cilíndrica):**
  $$R = \rho \frac{L}{A}$$
  Donde $L$ es el largo del conductor y $A$ es su área de sección transversal.
* **Dependencia Térmica:**
  $$\rho(T) = \rho_0 [1 + \alpha(T - T_0)] \implies R(T) = R_0 [1 + \alpha(T - T_0)]$$
  Donde $\alpha$ es el coeficiente térmico de resistividad.

---

## 2. Potencia Eléctrica y Efecto Joule

* **Potencia Eléctrica Generada/Absorbida ($P$):**
  $$P = I V \quad [\text{W} = J/\text{s}]$$
* **Efecto Joule (Disipación en una Resistencia):** Toda la energía eléctrica se disipa irreversiblemente en forma de calor.
  $$P_{\text{disipada}} = I^2 R = \frac{V^2}{R}$$

---

## 3. Circuitos de Corriente Directa (DC)

* **Baterías Reales (con Resistencia Interna $r$):**
  El voltaje terminal de la fuente es menor que su fuerza electromotriz (fem) $\varepsilon$ debido a la caída de tensión en su resistencia interna cuando circula corriente:
  $$V_{\text{terminal}} = \varepsilon - I r$$
* **Simplificación Serie / Paralelo:**
  * **Serie:** Las corrientes son iguales; los voltajes se suman.
    $$R_{\text{eq}} = \sum_{i} R_i$$
  * **Paralelo:** Los voltajes son iguales; las corrientes se suman.
    $$\frac{1}{R_{\text{eq}}} = \sum_{i} \frac{1}{R_i}$$

---

## 4. Leyes de Kirchhoff

Son consecuencia directa de las leyes de conservación de carga y energía:
* **1ª Ley (Ley de Nodos - KCL):** La suma de las corrientes que entran a un nodo es igual a la suma de las corrientes que salen.
  $$\sum I_{\text{entran}} = \sum I_{\text{salen}}$$
* **2ª Ley (Ley de Mallas - KVL):** La suma algebraica de los cambios de potencial eléctrico a lo largo de cualquier malla cerrada es igual a cero.
  $$\sum_{\text{lazo cerrado}} V = 0$$

### Método Sistemático de Mallas:
1. Identifica las mallas independientes del circuito y asígnales una corriente de malla ficticia (habitualmente en sentido horario).
2. Para cada malla, escribe la KVL sumando las caídas de potencial:
   - Al pasar por una resistencia en el sentido de la corriente, resta $IR$.
   - Al pasar por una resistencia en sentido opuesto a otra malla vecina, suma $I_{\text{vecina}}R$.
   - Al pasar por una fuente de voltaje de la placa negativa (línea corta) a la positiva (línea larga), suma $+\varepsilon$. De lo contrario, resta $-\varepsilon$.
3. Resuelve el sistema lineal resultante de ecuaciones para obtener las corrientes.

---

## 5. Circuitos transitorios RC

### A. Proceso de Carga
Se conecta una fuente de fem $\varepsilon$ en serie con una resistencia $R$ y un capacitor inicialmente descargado ($q(0)=0$).
* **Ecuación Diferencial:**
  $$\varepsilon - R\frac{dq}{dt} - \frac{q}{C} = 0 \implies \frac{dq}{dt} + \frac{q}{RC} = \frac{\varepsilon}{R}$$
* **Soluciones Temporales ($\tau = RC$):**
  * **Carga en el Capacitor:**
    $$q(t) = C\varepsilon\left(1 - e^{-t/\tau}\right)$$
  * **Corriente en el Circuito:**
    $$I(t) = \frac{\varepsilon}{R} e^{-t/\tau}$$
* **Balance Energético ($t \to \infty$):**
  - Energía total entregada por la batería: $W_{\text{batería}} = \int_{0}^{\infty} \varepsilon I(t) dt = C\varepsilon^2$.
  - Energía almacenada en el capacitor: $U_C = \frac{1}{2} C\varepsilon^2$.
  - Energía disipada en la resistencia: $E_{\text{disipada}} = \int_{0}^{\infty} I^2(t) R dt = \frac{1}{2} C\varepsilon^2$.
  - *La eficiencia de carga es exactamente del 50%, independientemente del valor de $R$.*

### B. Proceso de Descarga
Un capacitor inicialmente cargado con carga $Q_0$ se descarga a través de una resistencia $R$ sin fuentes externas.
* **Ecuación Diferencial:**
  $$R\frac{dq}{dt} + \frac{q}{C} = 0$$
* **Soluciones Temporales ($\tau = RC$):**
  * **Carga en el Capacitor:**
    $$q(t) = Q_0 e^{-t/\tau}$$
  * **Corriente en el Circuito (sentido opuesto):**
    $$I(t) = -\frac{Q_0}{RC} e^{-t/\tau}$$

---

## 6. Puente de Wheatstone

El puente de Wheatstone es un circuito de medición diseñado para determinar valores de resistencia desconocidos mediante el equilibrio de dos brazos divisores de tensión.

### Condición de Equilibrio:
Cuando la corriente que pasa por el detector o galvanómetro central es nula ($I_G = 0$), los potenciales de los nodos intermedios se igualan, lo que da lugar a la relación:
$$R_1 R_x = R_2 R_3 \implies R_x = \frac{R_2 R_3}{R_1}$$
Donde:
* $R_x$ es la resistencia desconocida.
* $R_1, R_2$ son resistencias fijas conocidas.
* $R_3$ es una resistencia variable ajustada para lograr el equilibrio (anulación de $I_G$).

---

## 7. Conceptos de Corriente Alterna (AC) y Filtros

En circuitos excitados por fuentes sinusoidales del tipo $v(t) = V_{\text{max}} \cos(\omega t + \phi)$:

### Impedancia Compleja ($Z$):
La oposición al flujo de corriente alterna se mide en ohmios ($\Omega$) mediante la impedancia $Z = R + jX$:
* **Resistor:** $Z_R = R$ (Reactancia $X_R = 0$)
* **Inductor:** $Z_L = j\omega L$ (Reactancia inductiva $X_L = \omega L$)
* **Capacitor:** $Z_C = \frac{1}{j\omega C} = -j\frac{1}{\omega C}$ (Reactancia capacitiva $X_C = \frac{1}{\omega C}$)
* **Frecuencia Angular:** $\omega = 2\pi f$ (rad/s), donde $f$ es la frecuencia en Hz.

### Circuitos RLC en Serie:
* **Impedancia Equivalente:**
  $$Z = R + j\left(\omega L - \frac{1}{\omega C}\right)$$
  $$|Z| = \sqrt{R^2 + \left(\omega L - \frac{1}{\omega C}\right)^2}$$
* **Resonancia en Serie:** Ocurre cuando la impedancia compleja es puramente real ($X_L = X_C$), minimizando $|Z| = R$ y maximizando la corriente.
  $$\omega_0 = \frac{1}{\sqrt{LC}} \implies f_0 = \frac{1}{2\pi \sqrt{LC}}$$

### Filtros Analógicos de Primer Orden:
* **Filtro Pasa Bajos:** Permite el paso de bajas frecuencias y atenúa las altas.
  - *Ejemplo RC:* La salida se toma en bornes del capacitor $C$. A frecuencias altas, el capacitor actúa como cortocircuito ($Z_C \to 0$), atenuando la salida.
* **Filtro Pasa Altos:** Permite el paso de altas frecuencias y atenúa las bajas.
  - *Ejemplo RC:* La salida se toma en bornes del resistor $R$. A frecuencias bajas, el capacitor actúa como circuito abierto ($Z_C \to \infty$), bloqueando la señal.

