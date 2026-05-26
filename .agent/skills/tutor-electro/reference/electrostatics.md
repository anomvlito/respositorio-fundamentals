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

---

## 5. Conductores Esféricos Concéntricos y Superposición

Para un sistema de cascarones o esferas conductoras concéntricas, el potencial eléctrico $V(r)$ es un escalar que cumple con el principio de superposición.

### Reglas de Potencial para una Esfera Conductora de Radio $R$ y Carga $Q$:
* **Punto Exterior ($r \ge R$):** La esfera se comporta electrostáticamente como si toda su carga estuviera concentrada en el centro geométrico.
  $$V(r) = \frac{1}{4\pi\epsilon} \frac{Q}{r}$$
* **Punto Interior ($r < R$):** Como el campo eléctrico neto en el interior de un conductor en equilibrio es cero ($E = 0$), el potencial permanece constante en todo su volumen e igual al valor en la superficie.
  $$V(r) = \frac{1}{4\pi\epsilon} \frac{Q}{R}$$

---

## 6. Ley de Gauss con Densidades Volumétricas Variables

Cuando la densidad de carga no es uniforme sino radialmente simétrica, e.g., $\rho(r) = q r^n$, la carga encerrada $Q_{\text{enc}}$ debe calcularse integrando en coordenadas esféricas:
$$Q_{\text{enc}} = \int_V \rho(r') dV = \int_{r_i}^{r} \rho(r') (4\pi r'^2) dr'$$

### Aplicación del Flujo Eléctrico:
Para simetría esférica:
$$\oint_S \vec{E} \cdot d\vec{A} = E(r) \cdot 4\pi r^2 = \frac{Q_{\text{enc}}}{\epsilon_0}$$
$$E(r) = \frac{Q_{\text{enc}}(r)}{4\pi \epsilon_0 r^2}$$

---

## 7. Inducción Magnética (Ley de Faraday) y Transformadores

* **Fuerza Electromotriz (FEM) Inducida:**
  $$\varepsilon = -\frac{d\Phi_B}{dt}$$
  Donde $\Phi_B = \int \vec{B} \cdot d\vec{A}$ es el flujo del campo magnético a través de la superficie delimitada por el espira.
* **Fuerza Electromotriz de Movimiento (Motional EMF):**
  Para un conductor recto de longitud $l$ moviéndose con velocidad constante $\vec{v}$ perpendicular a un campo magnético uniforme y estacionario $\vec{B}$:
  $$\varepsilon = v B l$$
* **Inducción Mutua ($M$):**
  Indica el flujo magnético enlazado en una bobina debido a la corriente en otra:
  $$M = \frac{N_2 \Phi_{21}}{I_1}$$
* **Transformadores Ideales:**
  Dispositivos que cambian el voltaje y corriente de alterna mediante acoplamiento magnético cerrado:
  $$\frac{V_p}{V_s} = \frac{N_p}{N_s} = a$$
  $$\frac{I_p}{I_s} = \frac{N_s}{N_p} = \frac{1}{a}$$
  Donde $a$ es la relación de transformación, e indexados por primario ($p$) y secundario ($s$).

