# Ejemplo 2: Transitorio de Circuito RC y Balance Energético

Este ejemplo ilustra la resolución detallada del proceso de carga de un condensador en serie con una resistencia y una fuente ideal de fem, detallando el balance de energía total del sistema.

---

## Enunciado

Un circuito en serie está constituido por una fuente ideal de fuerza electromotriz $\varepsilon$, una resistencia $R$, un condensador de capacitancia $C$ inicialmente descargado, y un interruptor $S$. En el instante $t = 0$ el interruptor se cierra.

1. Plantee la ecuación diferencial que gobierna la carga $q(t)$ en el capacitor y resuélvala usando condiciones de borde.
2. Determine la potencia instantánea entregada por la fuente, la disipada en la resistencia, y la almacenada en el capacitor.
3. Deduzca la energía total disipada como calor en la resistencia durante todo el proceso de carga ($t \to \infty$) y demuestre que corresponde a la mitad de la energía provista por la fuente.

---

## Resolución

### Parte 1: Ecuación Diferencial y Solución de la Carga

Recorriendo la malla única en el sentido de la corriente usando la Ley de Voltajes de Kirchhoff (KVL) obtenemos la relación:
$$\varepsilon - V_R(t) - V_C(t) = 0$$

Reemplazando las expresiones de voltaje en los terminales de la resistencia ($V_R = I R$) y del capacitor ($V_C = q/C$):
$$\varepsilon - I(t)R - \frac{q(t)}{C} = 0$$

Dado que la corriente instantánea se define como la tasa de acumulación de carga en las placas del condensador ($I = dq/dt$), reescribimos la ecuación como una ecuación diferencial lineal de primer orden para la carga:
$$\varepsilon - R\frac{dq(t)}{dt} - \frac{q(t)}{C} = 0$$

Dividiendo toda la ecuación por la resistencia $R$ para estandarizar su forma:
$$\frac{dq(t)}{dt} + \frac{q(t)}{RC} = \frac{\varepsilon}{R}$$

Esta ecuación se puede resolver mediante el método de separación de variables. Reordenando los términos:
$$\frac{dq}{dt} = \frac{C\varepsilon - q}{RC} \implies \frac{dq}{C\varepsilon - q} = \frac{dt}{RC}$$

Integrando a ambos lados de la ecuación entre el estado inicial ($t=0, q=0$) y un instante genérico $t$:
$$\int_{0}^{q} \frac{dq'}{C\varepsilon - q'} = \int_{0}^{t} \frac{dt'}{RC}$$

Evaluando la integral del lado izquierdo mediante sustitución simple y la del lado derecho:
$$-\ln\left(\frac{C\varepsilon - q}{C\varepsilon}\right) = \frac{t}{RC}$$

Multiplicando por $-1$ y aplicando la función exponencial a ambos lados para despejar el término logarítmico:
$$\frac{C\varepsilon - q}{C\varepsilon} = e^{-t/RC} \implies C\varepsilon - q = C\varepsilon e^{-t/RC}$$

Despejando finalmente la carga en función del tiempo $q(t)$:
$$q(t) = C\varepsilon\left(1 - e^{-t/RC}\right)$$

---

### Parte 2: Potencias Instantáneas del Sistema

Para caracterizar el flujo de energía en cada componente, primero derivamos la carga respecto al tiempo para obtener la corriente eléctrica del circuito:
$$I(t) = \frac{dq(t)}{dt} = \frac{\varepsilon}{R} e^{-t/RC}$$

A partir de la corriente, definimos la potencia entregada y consumida en cada parte del circuito:
- **Potencia entregada por la batería ($P_{\text{bat}}$):**
  $$P_{\text{bat}}(t) = \varepsilon I(t) = \frac{\varepsilon^2}{R} e^{-t/RC}$$
- **Potencia disipada en la resistencia por efecto Joule ($P_R$):**
  $$P_R(t) = I(t)^2 R = \frac{\varepsilon^2}{R} e^{-2t/RC}$$
- **Potencia almacenada en el capacitor ($P_C$):**
  $$P_C(t) = V_C(t) I(t) = \frac{q(t)}{C} I(t) = \varepsilon\left(1 - e^{-t/RC}\right) \frac{\varepsilon}{R} e^{-t/RC} = \frac{\varepsilon^2}{R}\left(e^{-t/RC} - e^{-2t/RC}\right)$$

Comprobando la conservación de la potencia instantánea sumando $P_R(t)$ y $P_C(t)$:
$$P_R(t) + P_C(t) = \frac{\varepsilon^2}{R} e^{-2t/RC} + \frac{\varepsilon^2}{R} e^{-t/RC} - \frac{\varepsilon^2}{R} e^{-2t/RC} = \frac{\varepsilon^2}{R} e^{-t/RC} = P_{\text{bat}}(t)$$

*El resultado verifica la conservación instantánea de la potencia.*

---

### Parte 3: Balance de Energía Total ($t \to \infty$)

La energía total transferida por la batería a lo largo del proceso completo de carga se obtiene integrando la potencia de la fuente desde $t=0$ hasta infinito:
$$W_{\text{bat}} = \int_{0}^{\infty} P_{\text{bat}}(t) dt = \int_{0}^{\infty} \frac{\varepsilon^2}{R} e^{-t/RC} dt$$

Evaluando la integral impropia resultante:
$$W_{\text{bat}} = \frac{\varepsilon^2}{R} \left[ -RC e^{-t/RC} \right]_{0}^{\infty} = \frac{\varepsilon^2}{R} (0 - (-RC)) = C\varepsilon^2$$

Por otro lado, la energía electrostática neta almacenada en el condensador al final de la carga completa ($q_f = C\varepsilon$) es:
$$U_C = \frac{1}{2}\frac{q_f^2}{C} = \frac{1}{2} C\varepsilon^2$$

Calculando la energía disipada en forma de calor en el resistor mediante la integración de la potencia Joule en el tiempo:
$$E_{\text{dis}} = \int_{0}^{\infty} P_R(t) dt = \int_{0}^{\infty} \frac{\varepsilon^2}{R} e^{-2t/RC} dt$$

Evaluando la integral impropia correspondiente:
$$E_{\text{dis}} = \frac{\varepsilon^2}{R} \left[ -\frac{RC}{2} e^{-2t/RC} \right]_{0}^{\infty} = \frac{\varepsilon^2}{R} \left(0 - \left(-\frac{RC}{2}\right)\right) = \frac{1}{2} C\varepsilon^2$$

Comparando los tres resultados energéticos:
$$W_{\text{bat}} = C\varepsilon^2$$
$$U_C = \frac{1}{2} C\varepsilon^2$$
$$E_{\text{dis}} = \frac{1}{2} C\varepsilon^2$$

Se cumple que:
$$U_C = E_{\text{dis}} = \frac{1}{2} W_{\text{bat}}$$

*Esto demuestra rigurosamente que exactamente el 50% de la energía provista por la fuente de alimentación se acumula como energía electrostática en el capacitor, mientras que el 50% restante se disipa inevitablemente como calor en el elemento resistivo, de forma independiente del valor específico de la resistencia $R$.*
