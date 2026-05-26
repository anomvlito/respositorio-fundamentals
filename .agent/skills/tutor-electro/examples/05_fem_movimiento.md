# Ejemplo 5: Fuerza Electromotriz de Movimiento y Balance de Energía

Este ejemplo expone la resolución de un problema clásico de inducción electromagnética (Ley de Faraday) donde una barra conductora desliza sobre rieles en presencia de un campo magnético, ilustrando la equivalencia entre el trabajo mecánico y la disipación eléctrica.

---

## Enunciado

Una barra conductora recta de longitud $l$ y resistencia despreciable desliza sin fricción con velocidad constante $v$ hacia la derecha sobre dos rieles conductores paralelos también de resistencia despreciable. Los rieles están conectados en un extremo por un resistor de resistencia $R$, formando un lazo cerrado. Un campo magnético uniforme y estacionario $\vec{B}$ apunta perpendicularmente hacia adentro de la página (entrando al plano del lazo).

1. Determine la fuerza electromotriz (FEM) inducida $\varepsilon$ y la corriente inducida $I$ en el circuito, especificando su sentido físico de rotación.
2. Calcule la magnitud y sentido de la fuerza magnética $\vec{F}_B$ ejercida sobre la barra deslizante.
3. Demuestre la conservación de la energía comprobando que la potencia mecánica suministrada por el agente externo para mantener la barra a velocidad constante es idéntica a la potencia térmica disipada en el resistor por efecto Joule.

---

## Resolución

### Parte 1: FEM y Corriente Inducida

Al deslizarse la barra hacia la derecha una distancia $x(t)$, el área del lazo cerrado aumenta continuamente, lo que incrementa el flujo magnético que atraviesa el circuito. Definiendo el área instantánea del lazo como $A(t) = l \cdot x(t)$, calculamos el flujo de campo magnético $\Phi_B$:
$$\Phi_B = \vec{B} \cdot \vec{A} = B A(t) = B l x(t)$$

Aplicando la Ley de Faraday para determinar la fuerza electromotriz inducida en magnitud:
$$\varepsilon = \left| -\frac{d\Phi_B}{dt} \right| = \frac{d}{dt} (B l x(t))$$

Dado que los parámetros $B$ y $l$ son constantes en el tiempo:
$$\varepsilon = B l \frac{dx}{dt}$$

Reemplazando la tasa de cambio de la posición por la velocidad constante de la barra ($v = dx/dt$):
$$\varepsilon = v B l$$

Aplicando la Ley de Ohm para calcular la intensidad de la corriente eléctrica inducida:
$$I = \frac{\varepsilon}{R} = \frac{v B l}{R}$$

*De acuerdo con la Ley de Lenz, la corriente inducida debe generar un campo magnético inducido que se oponga al incremento de flujo entrante. Por lo tanto, el campo inducido debe apuntar hacia afuera de la página, lo que requiere, según la regla de la mano derecha, que la corriente circule en **sentido antihorario** por el circuito.*

---

### Parte 2: Fuerza Magnética sobre la Barra

Toda corriente eléctrica $I$ inmersa en un campo magnético experimenta una fuerza dada por la ley de fuerza magnética sobre conductores:
$$\vec{F}_B = I (\vec{l} \times \vec{B})$$

Como la corriente fluye hacia arriba por la barra deslizante (en dirección $+\hat{j}$) y el campo magnético entra al plano (en dirección $-\hat{k}$), evaluamos el producto cruz:
$$\hat{j} \times (-\hat{k}) = -\hat{i}$$

*La dirección de la fuerza magnética es hacia la **izquierda** (oponiéndose al movimiento de la barra).*

Calculando la magnitud de esta fuerza magnética:
$$F_B = I l B$$

Sustituyendo el valor de la corriente inducida $I = \frac{v B l}{R}$ en la expresión anterior:
$$F_B = \left(\frac{v B l}{R}\right) l B = \frac{v B^2 l^2}{R}$$

---

### Parte 3: Balance de Potencia y Conservación de Energía

Para sostener el movimiento de la barra hacia la derecha con velocidad constante $v$, un agente externo debe aplicar una fuerza motora externa $\vec{F}_{\text{ext}}$ de igual magnitud pero sentido opuesto a la fuerza de retención magnética:
$$F_{\text{ext}} = F_B = \frac{v B^2 l^2}{R}$$

Calculando la potencia mecánica $P_{\text{mec}}$ desarrollada por dicho agente externo:
$$P_{\text{mec}} = F_{\text{ext}} \cdot v = \left( \frac{v B^2 l^2}{R} \right) v = \frac{v^2 B^2 l^2}{R}$$

Por otra parte, calculamos la potencia eléctrica disipada como calor en el resistor $R$ debido a la corriente inducida:
$$P_{\text{Joule}} = I^2 R$$

Reemplazando la expresión de la corriente obtenida en la Parte 1:
$$P_{\text{Joule}} = \left( \frac{v B l}{R} \right)^2 R = \frac{v^2 B^2 l^2}{R^2} R = \frac{v^2 B^2 l^2}{R}$$

Comparando ambas expresiones:
$$P_{\text{mec}} = P_{\text{Joule}} = \frac{v^2 B^2 l^2}{R}$$

*El trabajo mecánico realizado por el agente externo se transforma íntegramente en energía eléctrica que es disipada en el resistor en forma de calor por efecto Joule. Esto demuestra la consistencia termodinámica del sistema y la conservación de la energía.*
