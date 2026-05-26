# Referencia de Dieléctricos y Electrostática

Este documento reúne las formulaciones matemáticas y conceptos teóricos esenciales del manual de fórmulas de la NCEES FE y la cátedra de Electromagnetismo (FIS1533).

---

## 1. Dipolo Eléctrico

Un dipolo eléctrico consiste en dos cargas de igual magnitud $q$ pero de signos opuestos ($+q$ y $-q$) separadas por una distancia vectorial pequeña $\vec{d}$ (que apunta de la carga negativa a la positiva).

### Magnitudes Fundamentales:
* **Momento Dipolar Eléctrico ($\vec{p}$):**
  $$\vec{p} = q\vec{d} \quad [\text{C}\cdot\text{m}]$$
* **Torque sobre un Dipolo en un Campo Externo Uniforme ($\vec{\tau}$):**
  $$\vec{\tau} = \vec{p} \times \vec{E}$$
  *El torque tiende a alinear el dipolo con las líneas de campo eléctrico.*
* **Energía Potencial Electrostática de un Dipolo ($U$):**
  $$U = -\vec{p} \cdot \vec{E}$$
  * $U_{\text{mín}} = -pE$ (alineado, $\theta=0^\circ$, equilibrio estable).
  * $U_{\text{máx}} = pE$ (anti-alineado, $\theta=180^\circ$, equilibrio inestable).

---

## 2. Dieléctricos y Polarización en Medios Materiales

Los dieléctricos son materiales aislantes que se polarizan en presencia de un campo eléctrico externo, creando momentos dipolares inducidos en sus átomos o moléculas.

### Polarización y Constantes Físicas:
* **Vector Polarización ($\vec{P}$):** Momento dipolar neto por unidad de volumen. Para un medio lineal e isotrópico:
  $$\vec{P} = \chi_e \epsilon_0 \vec{E}$$
  Donde $\chi_e$ es la susceptibilidad eléctrica del material.
* **Vector Desplazamiento Eléctrico ($\vec{D}$):**
  $$\vec{D} = \epsilon_0 \vec{E} + \vec{P} = \epsilon \vec{E} = \kappa \epsilon_0 \vec{E}$$
  Donde:
  * $\kappa = 1 + \chi_e$ es la constante dieléctrica del medio.
  * $\epsilon = \kappa \epsilon_0$ es la permitividad absoluta del medio.
* **Ley de Gauss en Medios Dieléctricos:**
  * **Forma Integral:**
    $$\oint_S \vec{D} \cdot d\vec{A} = Q_{f,\text{enc}}$$
    Donde $Q_{f,\text{enc}}$ representa únicamente las cargas **libres** encerradas por la superficie gaussiana.
  * **Forma Diferencial:**
    $$\vec{\nabla} \cdot \vec{D} = \rho_f$$

### Densidades de Carga Ligada (Carga de Polarización):
La polarización molecular acumula carga neta en las superficies y el volumen del dieléctrico:
* **Densidad Superficial de Carga Ligada ($\sigma_b$):**
  $$\sigma_b = \vec{P} \cdot \hat{n}$$
  Donde $\hat{n}$ es el vector unitario normal exterior a la superficie del dieléctrico.
* **Densidad Volumétrica de Carga Ligada ($\rho_b$):**
  $$\rho_b = -\vec{\nabla} \cdot \vec{P}$$
* **Relación con la Carga Libre en Interfaces Conductoras:**
  Para placas de conductores cargadas con densidad libre $\sigma_f$:
  $$\sigma_b = -\sigma_f \left(1 - \frac{1}{\kappa}\right)$$
  La carga total en la interfaz es $\sigma_{\text{total}} = \sigma_f + \sigma_b = \sigma_f / \kappa$.

---

## 3. Energía Potencial Electroestática en Medios

La presencia del dieléctrico modifica la densidad de energía acumulada en el campo:
* **Densidad de Energía Electroestática ($u_e$):**
  $$u_e = \frac{1}{2} \vec{D} \cdot \vec{E} = \frac{1}{2} \kappa \epsilon_0 E^2$$
* **Energía Total Almacenada ($U$):**
  $$U = \int_V u_e dV = \int_V \frac{1}{2} \kappa \epsilon_0 E^2 dV$$

---

## 4. Capacitores con Dieléctricos

Al llenar totalmente el espacio de un capacitor de capacitancia en vacío $C_0$ con un dieléctrico, su capacitancia aumenta por un factor $\kappa$:
$$C = \kappa C_0$$

### Comparación de Escenarios Críticos:

| Variable | Caso A: Capacitor Aislado ($Q$ Constante) | Caso B: Conectado a Fuente ($V$ Constante) |
| :--- | :--- | :--- |
| **Carga ($Q$)** | $Q = Q_0$ (por conservación de carga) | $Q = \kappa Q_0$ (la fuente inyecta carga) |
| **Voltaje ($V$)** | $V = \frac{V_0}{\kappa}$ (cae la tensión) | $V = V_0$ (fijado por la fuente) |
| **Campo ($E$)** | $E = \frac{E_0}{\kappa}$ (el dieléctrico debilita el campo) | $E = E_0$ (el voltaje y la distancia no varían) |
| **Energía ($U$)** | $U = \frac{U_0}{\kappa}$ (el capacitor pierde energía electroestática al succionar el dieléctrico) | $U = \kappa U_0$ (el capacitor absorbe energía neta de la batería) |

### Particiones Dieléctricas Parciales (Modelado Equivalente):
* **Caso Serie (Dieléctrico por Capas apiladas perpendicularmente al campo):**
  Las placas se dividen en capas. Los capacitores resultantes comparten la misma carga libre.
  $$\frac{1}{C_{\text{eq}}} = \frac{1}{C_1} + \frac{1}{C_2} = \frac{d_1}{\kappa \epsilon_0 A} + \frac{d_2}{\epsilon_0 A}$$
* **Caso Paralelo (Dieléctrico Lateral apilado paralelamente al campo):**
  Las placas se dividen lateralmente. Los capacitores resultantes comparten la misma diferencia de potencial.
  $$C_{\text{eq}} = C_1 + C_2 = \kappa \epsilon_0 \frac{A_1}{d} + \epsilon_0 \frac{A_2}{d}$$
