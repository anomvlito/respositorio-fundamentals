# Ejemplo 3: Conductores Esféricos Concéntricos con Densidad de Carga Variable

Este ejemplo detalla la aplicación de la Ley de Gauss para distribuciones de carga radialmente no uniformes en presencia de cascarones conductores concéntricos y el cálculo del potencial electrostático por superposición.

---

## Enunciado

Una esfera conductora maciza de radio $R_1$ posee una carga neta $+Q_1$. Concéntrico con ella, se ubica un casquete esférico conductor de radio interno $R_2$ y radio externo $R_3$, el cual posee una carga neta $+Q_2$. El espacio intermedio ($R_1 < r < R_2$) está ocupado por una distribución continua de carga con densidad volumétrica variable $\rho(r) = q r$, donde $q$ es una constante conocida.

1. Encuentre el campo eléctrico $\vec{E}(r)$ en todas las regiones del espacio ($r < R_1$, $R_1 < r < R_2$, $R_2 < r < R_3$, y $r > R_3$).
2. Calcule el potencial electrostático en el punto medio del espacio intermedio, es decir, en $r_m = \frac{R_1 + R_2}{2}$.

---

## Resolución

### Parte 1: Cálculo del Campo Eléctrico en todas las Regiones

Para determinar el campo eléctrico en cada región, aplicamos la Ley de Gauss sobre superficies esféricas concéntricas de radio variable $r$. Por la simetría esférica del sistema, el flujo eléctrico a través de una de estas superficies gaussiana es $E(r) \cdot 4\pi r^2$.

* **Región 1 ($r < R_1$):**
  Como esta región se encuentra en el interior del conductor esférico central en equilibrio electrostático, la carga encerrada es nula, por lo que el campo eléctrico se anula idénticamente:
  $$\vec{E}(r) = 0$$

* **Región 2 ($R_1 < r < R_2$):**
  Para evaluar la carga total encerrada por una superficie gaussiana de radio $r$ en esta zona, sumamos la carga de la esfera central y la porción de la nube de carga no uniforme acumulada desde el radio límite $R_1$ hasta $r$:
  $$Q_{\text{enc}} = Q_1 + \int_{R_1}^{r} \rho(r') (4\pi r'^2) dr'$$
  Sustituyendo el modelo de la densidad variable $\rho(r') = q r'$:
  $$Q_{\text{enc}} = Q_1 + 4\pi q \int_{R_1}^{r} r'^3 dr' = Q_1 + 4\pi q \left[ \frac{r'^4}{4} \right]_{R_1}^{r} = Q_1 + \pi q \left( r^4 - R_1^4 \right)$$
  Aplicando la Ley de Gauss para despejar la magnitud del campo eléctrico en este intervalo:
  $$E(r) \cdot 4\pi r^2 = \frac{Q_1 + \pi q \left( r^4 - R_1^4 \right)}{\epsilon_0} \implies E(r) = \frac{Q_1 + \pi q (r^4 - R_1^4)}{4\pi \epsilon_0 r^2}$$
  Escrito vectorialmente en dirección radial:
  $$\vec{E}(r) = \frac{1}{4\pi\epsilon_0 r^2}\left[ Q_1 + \pi q (r^4 - R_1^4) \right] \hat{r}$$

* **Región 3 ($R_2 < r < R_3$):**
  Debido a que esta zona se localiza en el interior del casquete esférico conductor exterior en equilibrio electrostático, el campo eléctrico en el medio conductor debe ser nulo:
  $$\vec{E}(r) = 0$$

* **Región 4 ($r > R_3$):**
  Una superficie gaussiana que encierra todo el sistema abarca la carga libre de la esfera central, la totalidad de la carga de la nube dieléctrica y la carga del casquete conductor externo.
  Calculando primero la carga total acumulada de la nube volumétrica:
  $$Q_{\text{nube}} = \pi q (R_2^4 - R_1^4)$$
  De este modo, la carga encerrada total es:
  $$Q_{\text{total}} = Q_1 + \pi q (R_2^4 - R_1^4) + Q_2$$
  Aplicando la Ley de Gauss para esta región exterior:
  $$\vec{E}(r) = \frac{Q_1 + Q_2 + \pi q (R_2^4 - R_1^4)}{4\pi\epsilon_0 r^2} \hat{r}$$

---

### Parte 2: Potencial Electrostático en el Punto Medio $r_m$

Para calcular el potencial $V(r_m)$, integramos el campo eléctrico desde una referencia infinitamente alejada ($V(\infty) = 0$) hasta la posición de interés $r_m$. La trayectoria de integración se divide en tramos correspondientes a las diferentes regiones del campo:
$$V(r_m) = -\int_{\infty}^{r_m} E(r) dr = -\int_{\infty}^{R_3} E(r) dr - \int_{R_3}^{R_2} E(r) dr - \int_{R_2}^{r_m} E(r) dr$$

* **Primer Tramo ($r > R_3$):**
  El potencial en la superficie exterior del casquete conductor ($R_3$) es igual al potencial de una carga puntual equivalente a la carga total del sistema:
  $$V(R_3) = \frac{Q_1 + Q_2 + \pi q (R_2^4 - R_1^4)}{4\pi\epsilon_0 R_3}$$

* **Segundo Tramo ($R_2 < r < R_3$):**
  Como el campo eléctrico en el interior de la pared del casquete conductor es nulo, no hay caída de tensión a través de él. Por ende, el potencial en la superficie interior $R_2$ es idéntico al potencial en su superficie exterior:
  $$V(R_2) = V(R_3) = \frac{Q_1 + Q_2 + \pi q (R_2^4 - R_1^4)}{4\pi\epsilon_0 R_3}$$

* **Tercer Tramo ($r_m < r < R_2$):**
  Integramos la magnitud del campo eléctrico en la región intermedia desde el radio de la pared interna del casquete $R_2$ hasta el punto de medición $r_m$:
  $$V(r_m) - V(R_2) = -\int_{R_2}^{r_m} E(r) dr = \int_{r_m}^{R_2} \frac{Q_1 + \pi q (r^4 - R_1^4)}{4\pi \epsilon_0 r^2} dr$$
  Separando los términos de la integral para facilitar su cálculo algebraico:
  $$V(r_m) - V(R_2) = \frac{1}{4\pi\epsilon_0} \int_{r_m}^{R_2} \left[ \frac{Q_1 - \pi q R_1^4}{r^2} + \pi q r^2 \right] dr$$
  Integrando directamente cada término:
  $$V(r_m) - V(R_2) = \frac{1}{4\pi\epsilon_0} \left[ -\frac{Q_1 - \pi q R_1^4}{r} + \frac{\pi q r^3}{3} \right]_{r_m}^{R_2}$$
  Evaluando los límites de integración:
  $$V(r_m) - V(R_2) = \frac{1}{4\pi\epsilon_0} \left[ \left( -\frac{Q_1 - \pi q R_1^4}{R_2} + \frac{\pi q R_2^3}{3} \right) - \left( -\frac{Q_1 - \pi q R_1^4}{r_m} + \frac{\pi q r_m^3}{3} \right) \right]$$
  Agrupando y sumando el valor constante de $V(R_2)$ calculado previamente:
  $$V(r_m) = \frac{Q_1 + Q_2 + \pi q (R_2^4 - R_1^4)}{4\pi\epsilon_0 R_3} + \frac{1}{4\pi\epsilon_0} \left[ \left( \frac{1}{r_m} - \frac{1}{R_2} \right) (Q_1 - \pi q R_1^4) + \frac{\pi q}{3} (R_2^3 - r_m^3) \right]$$

Sustituyendo finalmente la definición del punto medio $r_m = \frac{R_1 + R_2}{2}$ obtenemos el valor exacto del potencial para el punto del enunciado.
