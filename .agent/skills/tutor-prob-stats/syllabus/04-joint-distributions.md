# Tema 4 — Distribuciones Conjuntas e Independencia

**Referencias**: DeGroot & Schervish, *Probability and Statistics* (4th ed.), Ch. 3; Ross, *A First Course in Probability* (10th ed.), Ch. 6.

---

## 4.1 Distribución Conjunta

### Caso Discreto
La **PMF conjunta** de $(X, Y)$:
$$p_{X,Y}(x,y) = P(X=x, Y=y) \ge 0, \qquad \sum_x \sum_y p_{X,Y}(x,y) = 1$$

### Caso Continuo
La **PDF conjunta** $f_{X,Y}(x,y)$:
$$f_{X,Y}(x,y) \ge 0, \qquad \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f_{X,Y}(x,y)\, dx\, dy = 1$$
$$P\!\left((X,Y) \in A\right) = \iint_A f_{X,Y}(x,y)\, dx\, dy$$

### CDF Conjunta
$$F_{X,Y}(x,y) = P(X \le x,\, Y \le y)$$
Para variables continuas: $f_{X,Y}(x,y) = \frac{\partial^2}{\partial x \partial y} F_{X,Y}(x,y)$.

---

## 4.2 Distribuciones Marginales

Se obtienen integrando (o sumando) sobre la otra variable:

**Continuas**:
$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)\, dy, \qquad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)\, dx$$

**Discretas**:
$$p_X(x) = \sum_y p_{X,Y}(x,y), \qquad p_Y(y) = \sum_x p_{X,Y}(x,y)$$

> **Atención**: Conocer las marginales **no** determina la distribución conjunta (a menos que haya independencia).

---

## 4.3 Distribuciones Condicionales

**PDF Condicional** de $Y$ dado $X = x$ (con $f_X(x) > 0$):
$$f_{Y \mid X}(y \mid x) = \frac{f_{X,Y}(x,y)}{f_X(x)}$$

Propiedades:
- $f_{Y \mid X}(y \mid x) \ge 0$
- $\int f_{Y \mid X}(y \mid x)\, dy = 1$ (para cada $x$ fijo)

**Esperanza Condicional**:
$$E[Y \mid X = x] = \int y\, f_{Y \mid X}(y \mid x)\, dy$$

**Ley de la Esperanza Total**:
$$E[Y] = E_X[E[Y \mid X]] = \int E[Y \mid X=x]\, f_X(x)\, dx$$

**Ley de la Varianza Total**:
$$\text{Var}(Y) = E[\text{Var}(Y \mid X)] + \text{Var}(E[Y \mid X])$$

---

## 4.4 Independencia

$X$ e $Y$ son **independientes** ($X \perp Y$) si y solo si:
$$f_{X,Y}(x,y) = f_X(x)\cdot f_Y(y) \quad \text{para todo } (x,y)$$

Equivalentemente:
- $F_{X,Y}(x,y) = F_X(x)\cdot F_Y(y)$
- $f_{Y \mid X}(y \mid x) = f_Y(y)$ para todo $x$ con $f_X(x) > 0$
- $E[g(X)h(Y)] = E[g(X)] \cdot E[h(Y)]$ para cualesquiera funciones $g$, $h$.

**Test práctico de independencia**: Si $f_{X,Y}(x,y)$ se puede escribir como $g(x)\cdot h(y)$ **y** el soporte es un rectángulo (producto cartesiano), entonces $X \perp Y$.

> **Trampa**: El soporte debe ser un rectángulo. Si el soporte es un triángulo (e.g., $0 < x < y < 1$), $X$ e $Y$ **no** pueden ser independientes.

---

## 4.5 Covarianza y Correlación

### Covarianza
$$\text{Cov}(X,Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]\,E[Y]$$

**Propiedades**:
- $\text{Cov}(X,X) = \text{Var}(X)$
- $\text{Cov}(aX + b,\, cY + d) = ac\,\text{Cov}(X,Y)$
- $\text{Cov}(X + Y, Z) = \text{Cov}(X,Z) + \text{Cov}(Y,Z)$ (bilinealidad)
- $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X,Y)$
- $\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + 2\sum_{i < j} \text{Cov}(X_i, X_j)$

Si $X \perp Y$, entonces $\text{Cov}(X,Y) = 0$ (pero el recíproco **no es** cierto en general).

### Correlación de Pearson
$$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X\,\sigma_Y} \in [-1, 1]$$

- $\rho = 1$: relación lineal perfecta positiva.
- $\rho = -1$: relación lineal perfecta negativa.
- $\rho = 0$: no hay relación **lineal** (puede haber relación no lineal).
- **Invarianza de escala**: $\rho$ no cambia con transformaciones lineales afines $aX+b$, $cY+d$ (con $a,c > 0$).

---

## 4.6 Distribución Normal Bivariada

$(X, Y)$ tiene distribución **Normal Bivariada** $N(\mu_X, \mu_Y, \sigma_X^2, \sigma_Y^2, \rho)$ si:
$$f_{X,Y}(x,y) = \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}} \exp\!\left(-\frac{Q}{2(1-\rho^2)}\right)$$
donde
$$Q = \left(\frac{x-\mu_X}{\sigma_X}\right)^2 - 2\rho\left(\frac{x-\mu_X}{\sigma_X}\right)\left(\frac{y-\mu_Y}{\sigma_Y}\right) + \left(\frac{y-\mu_Y}{\sigma_Y}\right)^2$$

**Propiedad clave**: Si $(X,Y)$ es Normal Bivariada:
$$\rho_{X,Y} = 0 \iff X \perp Y$$
> Esto es **exclusivo** de la Normal conjunta. Para otras distribuciones, $\rho = 0$ **no** implica independencia.

**Condicional**: $Y \mid X = x \sim N\!\left(\mu_Y + \rho\frac{\sigma_Y}{\sigma_X}(x - \mu_X),\; \sigma_Y^2(1-\rho^2)\right)$.

---

## 4.7 Estadísticas de Orden

Sean $X_1, \ldots, X_n \overset{iid}{\sim} f_X$ con CDF $F_X$. Ordenadas: $X_{(1)} \le X_{(2)} \le \cdots \le X_{(n)}$.

**PDF de la $k$-ésima estadística de orden** $X_{(k)}$:
$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!\,(n-k)!}\,[F_X(x)]^{k-1}\,[1-F_X(x)]^{n-k}\,f_X(x)$$

**Casos notables**:
- Mínimo ($k=1$): $f_{X_{(1)}}(x) = n\,[1-F_X(x)]^{n-1} f_X(x)$
- Máximo ($k=n$): $f_{X_{(n)}}(x) = n\,[F_X(x)]^{n-1} f_X(x)$

---

## 4.8 Suma de Variables Aleatorias (Convolución)

Si $X \perp Y$ con PDFs $f_X$ y $f_Y$, la PDF de $Z = X + Y$ es la **convolución**:
$$f_Z(z) = (f_X * f_Y)(z) = \int_{-\infty}^{\infty} f_X(z-y)\, f_Y(y)\, dy$$

**Vía MGF**: $M_{X+Y}(t) = M_X(t)\cdot M_Y(t)$ (más eficiente que convolución directa).

**Reproductividades importantes** (caso independiente):
- $\text{Bin}(n,p) + \text{Bin}(m,p) = \text{Bin}(n+m, p)$
- $\text{Poi}(\lambda_1) + \text{Poi}(\lambda_2) = \text{Poi}(\lambda_1+\lambda_2)$
- $N(\mu_1,\sigma_1^2) + N(\mu_2,\sigma_2^2) = N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2)$
- $\Gamma(\alpha_1,\beta) + \Gamma(\alpha_2,\beta) = \Gamma(\alpha_1+\alpha_2,\beta)$
- $\chi^2(d_1) + \chi^2(d_2) = \chi^2(d_1+d_2)$

---

## 4.9 Errores Comunes en este Tema

- **Marginal ≠ Conjunta**: Las distribuciones marginales no determinan la distribución conjunta.
- **Covarianza cero ≠ Independencia**: Solo cuando el vector es Normal Bivariado implica independencia.
- **Soporte no rectangular**: Verificar el soporte antes de declarar independencia.
- **Ley de la Varianza Total**: No confundir con $\text{Var}(X+Y)$; son conceptos distintos.
- **Convolución en soporte acotado**: Los límites de integración dependen del soporte de $f_X$ y $f_Y$; no siempre son $(-\infty, \infty)$.
