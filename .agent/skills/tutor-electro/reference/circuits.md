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
