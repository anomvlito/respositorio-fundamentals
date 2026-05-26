# Ejemplo 4: Puente de Wheatstone en Equilibrio y Disipación de Potencia

Este ejemplo ilustra el modelamiento circuital del Puente de Wheatstone, deduciendo la condición analítica de equilibrio para la medición de resistencias y calculando la potencia disipada en la resistencia incógnita.

---

## Enunciado

Considere el circuito de un Puente de Wheatstone alimentado por una fuente de voltaje continua ideal $V$. El puente consta de dos ramas paralelas conectadas a la fuente:
- La rama izquierda está compuesta por las resistencias $R_1$ (superior) y $R_2$ (inferior) en serie.
- La rama derecha está compuesta por las resistencias $R_3$ (superior) y $R_x$ (inferior) en serie.
- Un galvanómetro detector $G$ conecta el nodo intermedio izquierdo $a$ (entre $R_1$ y $R_2$) con el nodo intermedio derecho $b$ (entre $R_3$ y $R_x$).

1. Demuestre que si la corriente por el galvanómetro es nula ($I_G = 0$), entonces la resistencia desconocida se expresa como $R_x = \frac{R_2 R_3}{R_1}$.
2. Bajo esta misma condición de equilibrio, calcule la potencia disipada $P_x$ por la resistencia $R_x$ en términos de la tensión de la fuente $V$ y las resistencias conocidas.

---

## Resolución

### Parte 1: Deducción de la Condición de Equilibrio

La corriente nula por el galvanómetro ($I_G = 0$) implica que no hay transferencia de carga entre los nodos intermedios $a$ y $b$. Esto exige que ambos nodos se encuentren exactamente al mismo potencial eléctrico respecto de la referencia de tierra (el terminal negativo de la fuente):
$$V_a = V_b$$

Dado que $I_G = 0$, la corriente de la rama izquierda fluye por completo a través de $R_1$ y $R_2$. Aplicando la regla del divisor de voltaje para obtener el potencial en el nodo $a$:
$$V_a = V \frac{R_2}{R_1 + R_2}$$

De igual manera, puesto que no entra ni sale corriente en el nodo $b$, las resistencias $R_3$ y $R_x$ están en serie ideal. El potencial del nodo $b$ es:
$$V_b = V \frac{R_x}{R_3 + R_x}$$

Igualando los potenciales de ambos nodos para cumplir la condición de equilibrio:
$$V \frac{R_2}{R_1 + R_2} = V \frac{R_x}{R_3 + R_x}$$

Cancelando el voltaje común $V$ a ambos lados de la ecuación:
$$\frac{R_2}{R_1 + R_2} = \frac{R_x}{R_3 + R_x}$$

Multiplicando cruzado para eliminar los denominadores:
$$R_2 (R_3 + R_x) = R_x (R_1 + R_2)$$

Distribuyendo los productos algebraicos:
$$R_2 R_3 + R_2 R_x = R_1 R_x + R_2 R_x$$

Restando el término común $R_2 R_x$ a ambos lados de la expresión:
$$R_2 R_3 = R_1 R_x$$

Despejando finalmente la resistencia incógnita $R_x$:
$$R_x = \frac{R_2 R_3}{R_1}$$

---

### Parte 2: Potencia Disipada por la Resistencia Incógnita

La potencia disipada en un resistor debido a la corriente que circula por él está dada por la Ley de Joule:
$$P_x = I_x^2 R_x$$

Debido a que el puente está en equilibrio, la corriente $I_x$ que circula por la resistencia $R_x$ es idéntica a la corriente de toda la rama derecha. Aplicando la Ley de Ohm para dicha rama conectada a la fuente $V$:
$$I_x = \frac{V}{R_3 + R_x}$$

Sustituyendo el valor obtenido de la resistencia incógnita en equilibrio $R_x = \frac{R_2 R_3}{R_1}$ en el denominador:
$$I_x = \frac{V}{R_3 + \frac{R_2 R_3}{R_1}}$$

Factorizando la resistencia $R_3$ en el denominador:
$$I_x = \frac{V}{R_3 \left(1 + \frac{R_2}{R_1}\right)} = \frac{V}{R_3 \left(\frac{R_1 + R_2}{R_1}\right)}$$

Reordenando los términos para simplificar la corriente:
$$I_x = \frac{V R_1}{R_3(R_1 + R_2)}$$

Sustituyendo ahora la corriente $I_x$ y la resistencia $R_x$ en la fórmula de la potencia:
$$P_x = \left[ \frac{V R_1}{R_3(R_1 + R_2)} \right]^2 \left( \frac{R_2 R_3}{R_1} \right)$$

Desarrollando el término cuadrático:
$$P_x = \frac{V^2 R_1^2}{R_3^2 (R_1 + R_2)^2} \frac{R_2 R_3}{R_1}$$

Simplificando los factores comunes $R_1$ y $R_3$ en el numerador y denominador:
$$P_x = \frac{V^2 R_1 R_2}{R_3 (R_1 + R_2)^2}$$

Este resultado expresa la potencia disipada en $R_x$ utilizando únicamente variables conocidas del circuito.
