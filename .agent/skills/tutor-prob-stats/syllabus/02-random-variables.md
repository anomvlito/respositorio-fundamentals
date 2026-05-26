# Tema 2 — Variables Aleatorias

**Referencias**: Ross, *A First Course in Probability* (10th ed.), Ch. 4–5; DeGroot & Schervish, *Probability and Statistics* (4th ed.), Ch. 3–4; Devore, *Probability and Statistics for Engineering and the Sciences* (9th ed.), Ch. 3–4.

---

## 2.1 Definición Formal

Una **variable aleatoria** (v.a.) $X$ es una función medible $X: \Omega \to \mathbb{R}$ que asigna un número real a cada resultado del espacio muestral.

- **Discreta**: toma valores en un conjunto finito o numerable $\{x_1, x_2, \ldots\}$.
- **Continua**: toma valores en un intervalo (o unión de intervalos) de $\mathbb{R}$.

---

## 2.2 Variables Aleatorias Discretas

### Función de Masa de Probabilidad (PMF)
$$p_X(x) = P(X = x), \qquad p_X(x) \ge 0, \qquad \sum_{\text{todos } x} p_X(x) = 1$$

### Función de Distribución Acumulada (CDF)
$$F_X(x) = P(X \le x) = \sum_{k \le x} p_X(k)$$

Propiedades de la CDF (discretas y continuas):
1. No decreciente: $x_1 < x_2 \Rightarrow F(x_1) \le F(x_2)$.
2. Límites: $\lim_{x \to -\infty} F(x) = 0$, $\lim_{x \to \infty} F(x) = 1$.
3. Continua por la derecha: $\lim_{h \to 0^+} F(x+h) = F(x)$.

### Valor Esperado (Esperanza Matemática)
$$E[X] = \sum_{x} x \cdot p_X(x)$$

**Propiedades**:
- **Linealidad**: $E[aX + b] = a\,E[X] + b$
- **Linealidad para suma**: $E[X + Y] = E[X] + E[Y]$ (siempre, sin importar dependencia)
- **Independencia**: Si $X \perp Y$, entonces $E[XY] = E[X]\,E[Y]$

### LOTUS — Ley del Estadístico Inconsciente
Para $g: \mathbb{R} \to \mathbb{R}$:
$$E[g(X)] = \sum_{x} g(x)\, p_X(x)$$

### Varianza y Desviación Estándar
$$\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$$
$$\sigma_X = \sqrt{\text{Var}(X)}$$

**Propiedades**:
- $\text{Var}(aX + b) = a^2\,\text{Var}(X)$
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ **solo si** $X \perp Y$

### Momentos
- **$k$-ésimo momento**: $\mu_k' = E[X^k]$
- **$k$-ésimo momento central**: $\mu_k = E[(X - \mu)^k]$
- **Asimetría** (*skewness*): $\gamma_1 = \frac{\mu_3}{\sigma^3}$
- **Curtosis**: $\gamma_2 = \frac{\mu_4}{\sigma^4} - 3$

### Función Generadora de Momentos (MGF)
$$M_X(t) = E[e^{tX}] = \sum_x e^{tx} p_X(x)$$

Si $M_X(t)$ existe en un entorno de $0$:
- $E[X^k] = M_X^{(k)}(0)$ (la $k$-ésima derivada evaluada en $t=0$).
- **Unicidad**: Si $M_X(t) = M_Y(t)$ para todo $t$ en un entorno de $0$, entonces $X \overset{d}{=} Y$.
- **Independencia**: Si $X \perp Y$, entonces $M_{X+Y}(t) = M_X(t)\cdot M_Y(t)$.

---

## 2.3 Variables Aleatorias Continuas

### Función de Densidad de Probabilidad (PDF)
$f_X(x)$ es la PDF de $X$ si:
$$P(a \le X \le b) = \int_a^b f_X(x)\, dx$$
con $f_X(x) \ge 0$ y $\int_{-\infty}^{\infty} f_X(x)\, dx = 1$.

> **Nota**: $P(X = x) = 0$ para cualquier punto específico. La probabilidad está definida sobre intervalos.

### CDF Continua
$$F_X(x) = \int_{-\infty}^x f_X(t)\, dt$$
Relación inversa (Teorema Fundamental del Cálculo):
$$f_X(x) = F_X'(x) \quad \text{en los puntos donde } F_X \text{ es diferenciable}$$

### Valor Esperado (Continuo)
$$E[X] = \int_{-\infty}^{\infty} x\, f_X(x)\, dx$$

**LOTUS** (continuo):
$$E[g(X)] = \int_{-\infty}^{\infty} g(x)\, f_X(x)\, dx$$

### Varianza (Continua)
$$\text{Var}(X) = \int_{-\infty}^{\infty} (x - E[X])^2 f_X(x)\, dx = E[X^2] - (E[X])^2$$

### MGF Continua
$$M_X(t) = E[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} f_X(x)\, dx$$

---

## 2.4 Percentiles y Mediana

El **percentil $p$** (o cuantil de orden $p$) de $X$ es el valor $x_p$ tal que:
$$F_X(x_p) = P(X \le x_p) = p$$

- **Mediana**: $x_{0.5}$ (percentil 50).
- **Cuartiles**: $Q_1 = x_{0.25}$, $Q_3 = x_{0.75}$; $\text{IQR} = Q_3 - Q_1$.

---

## 2.5 Transformaciones de Variables Aleatorias

### Método de la CDF (General)
1. Escribir $F_Y(y) = P(Y \le y) = P(g(X) \le y)$.
2. Reescribir en términos de $X$ usando la función inversa.
3. Derivar para obtener $f_Y(y) = F_Y'(y)$.

### Fórmula Directa (g Monotóna)
Si $Y = g(X)$ con $g$ estrictamente monótona y diferenciable:
$$f_Y(y) = f_X\!\left(g^{-1}(y)\right) \cdot \left|\frac{d}{dy} g^{-1}(y)\right|$$

**Ejemplo**: Si $X \sim \text{Exp}(\lambda)$ e $Y = \ln X$, aplicar la fórmula con $g^{-1}(y) = e^y$.

### Transformación Lineal
Si $Y = aX + b$:
$$f_Y(y) = \frac{1}{|a|} f_X\!\left(\frac{y-b}{a}\right)$$

### Estandarización
Si $X \sim (\mu, \sigma^2)$, entonces $Z = \frac{X - \mu}{\sigma}$ tiene media $0$ y varianza $1$.

---

## 2.6 Errores Comunes en este Tema

- **Confundir PMF con CDF**: la CDF es acumulada y siempre no decreciente; la PMF puede tomar cualquier valor positivo en los puntos del soporte.
- **LOTUS sin el peso**: calcular $E[g(X)]$ evaluando $g$ en la media, en lugar de ponderar con la distribución.
- **Varianza de suma**: $\text{Var}(X + Y) \ne \text{Var}(X) + \text{Var}(Y)$ en general; hay que sumar $2\,\text{Cov}(X,Y)$.
- **Olvidar el Jacobiano** en transformaciones: el término $\left|\frac{d}{dy} g^{-1}(y)\right|$ es obligatorio.
- **Confundir continuidad de $F$ con diferenciabilidad**: la CDF de una v.a. continua es continua, pero no necesariamente diferenciable en todos los puntos.
