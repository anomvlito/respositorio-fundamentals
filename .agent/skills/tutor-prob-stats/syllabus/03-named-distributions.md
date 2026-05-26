# Tema 3 — Distribuciones Nombradas

**Referencias**: Ross, *A First Course in Probability* (10th ed.), Ch. 4–5; Devore, *Probability and Statistics for Engineering and the Sciences* (9th ed.), Ch. 3–4; DeGroot & Schervish, *Probability and Statistics* (4th ed.), Ch. 5.

---

## 3.1 Distribuciones Discretas

### Bernoulli($p$)
Un único ensayo con resultado "éxito" ($X=1$) o "fracaso" ($X=0$).

| PMF | $E[X]$ | $\text{Var}(X)$ | MGF |
|---|---|---|---|
| $p^x(1-p)^{1-x}$, $x \in \{0,1\}$ | $p$ | $p(1-p)$ | $(1-p) + pe^t$ |

---

### Binomial($n, p$)
Número de éxitos en $n$ ensayos Bernoulli **independientes** con probabilidad de éxito $p$.

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

| $E[X]$ | $\text{Var}(X)$ | MGF |
|---|---|---|
| $np$ | $np(1-p)$ | $\left[(1-p) + pe^t\right]^n$ |

**Suma de Bernoullis**: Si $X_i \overset{iid}{\sim} \text{Bern}(p)$, entonces $\sum X_i \sim \text{Bin}(n,p)$.

**Reproductividad**: Si $X \sim \text{Bin}(n,p)$ y $Y \sim \text{Bin}(m,p)$ independientes, entonces $X+Y \sim \text{Bin}(n+m, p)$.

---

### Geométrica($p$)
Número de ensayos hasta el **primer éxito** (inclusive).

$$P(X = k) = (1-p)^{k-1} p, \quad k = 1, 2, 3, \ldots$$

| $E[X]$ | $\text{Var}(X)$ | MGF |
|---|---|---|
| $\frac{1}{p}$ | $\frac{1-p}{p^2}$ | $\frac{pe^t}{1-(1-p)e^t}$, $t < -\ln(1-p)$ |

**Propiedad de falta de memoria**: $P(X > m+n \mid X > m) = P(X > n)$.
> La Geométrica es la **única** distribución discreta con esta propiedad.

---

### Binomial Negativa($r, p$)
Número de ensayos hasta obtener el **$r$-ésimo éxito**.

$$P(X = k) = \binom{k-1}{r-1} p^r (1-p)^{k-r}, \quad k = r, r+1, \ldots$$

| $E[X]$ | $\text{Var}(X)$ |
|---|---|
| $\frac{r}{p}$ | $\frac{r(1-p)}{p^2}$ |

**Relación**: Suma de $r$ variables Geométricas($p$) independientes.

---

### Poisson($\lambda$)
Número de eventos en un intervalo fijo cuando: los eventos son raros, independientes, y ocurren a tasa constante $\lambda > 0$.

$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots$$

| $E[X]$ | $\text{Var}(X)$ | MGF |
|---|---|---|
| $\lambda$ | $\lambda$ | $e^{\lambda(e^t - 1)}$ |

**Reproductividad**: Si $X \sim \text{Poi}(\lambda_1)$ y $Y \sim \text{Poi}(\lambda_2)$ independientes, entonces $X+Y \sim \text{Poi}(\lambda_1 + \lambda_2)$.

**Aproximación Poisson a Binomial**: Cuando $n$ es grande, $p$ pequeño, y $\lambda = np$ fijo:
$$\text{Bin}(n,p) \approx \text{Poisson}(\lambda)$$
Regla práctica: $n \ge 20$ y $p \le 0.05$.

---

### Hipergeométrica($N, K, n$)
Número de éxitos al extraer $n$ objetos **sin reemplazo** de una población de $N$ objetos con $K$ éxitos.

$$P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}, \quad \max(0, n-(N-K)) \le k \le \min(n,K)$$

| $E[X]$ | $\text{Var}(X)$ |
|---|---|
| $n\frac{K}{N}$ | $n\frac{K}{N}\cdot\frac{N-K}{N}\cdot\frac{N-n}{N-1}$ |

El factor $\frac{N-n}{N-1}$ se llama **factor de corrección para población finita**. Cuando $n/N \to 0$, la Hipergeométrica se aproxima a la Binomial$(n, K/N)$.

---

## 3.2 Distribuciones Continuas

### Uniforme($a, b$)
Todo valor en $[a,b]$ es igualmente probable.

$$f_X(x) = \frac{1}{b-a}, \quad x \in [a,b]$$

| $E[X]$ | $\text{Var}(X)$ | MGF |
|---|---|---|
| $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | $\frac{e^{tb} - e^{ta}}{t(b-a)}$ |

**Método de la transformada inversa**: Si $U \sim \text{Unif}(0,1)$, entonces $X = F_X^{-1}(U)$ tiene CDF $F_X$ (base de simulación Monte Carlo).

---

### Exponencial($\lambda$)
Tiempo de espera entre eventos Poisson. Parámetro de tasa $\lambda > 0$ (o equivalentemente, escala $\beta = 1/\lambda$).

$$f_X(x) = \lambda e^{-\lambda x}, \quad x \ge 0 \qquad F_X(x) = 1 - e^{-\lambda x}$$

| $E[X]$ | $\text{Var}(X)$ | MGF |
|---|---|---|
| $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | $\frac{\lambda}{\lambda - t}$, $t < \lambda$ |

**Propiedad de falta de memoria** (continua): $P(X > s+t \mid X > s) = P(X > t)$.
> La Exponencial es la **única** distribución continua con esta propiedad.

**Relación con Poisson**: Si los tiempos entre eventos son $\text{Exp}(\lambda)$, el conteo de eventos en $[0,T]$ es $\text{Poisson}(\lambda T)$.

---

### Normal($\mu, \sigma^2$)
La distribución más importante en estadística, central en el CLT.

$$f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad x \in \mathbb{R}$$

| $E[X]$ | $\text{Var}(X)$ | MGF |
|---|---|---|
| $\mu$ | $\sigma^2$ | $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ |

**Normal Estándar**: $Z = \frac{X-\mu}{\sigma} \sim N(0,1)$. CDF: $\Phi(z) = P(Z \le z)$.

**Regla Empírica** (68-95-99.7):
- $P(\mu - \sigma \le X \le \mu + \sigma) \approx 0.6827$
- $P(\mu - 2\sigma \le X \le \mu + 2\sigma) \approx 0.9545$
- $P(\mu - 3\sigma \le X \le \mu + 3\sigma) \approx 0.9973$

**Cálculo de probabilidades**:
$$P(a \le X \le b) = \Phi\!\left(\frac{b-\mu}{\sigma}\right) - \Phi\!\left(\frac{a-\mu}{\sigma}\right)$$

**Reproductividad**: Si $X_i \overset{ind}{\sim} N(\mu_i, \sigma_i^2)$, entonces $\sum a_i X_i \sim N\!\left(\sum a_i \mu_i,\, \sum a_i^2 \sigma_i^2\right)$.

---

### Gamma($\alpha, \beta$)
Tiempo hasta el $\alpha$-ésimo evento Poisson. $\alpha > 0$ (forma), $\beta > 0$ (escala).

$$f_X(x) = \frac{x^{\alpha-1} e^{-x/\beta}}{\beta^\alpha\,\Gamma(\alpha)}, \quad x > 0$$

donde $\Gamma(\alpha) = \int_0^\infty t^{\alpha-1}e^{-t}\,dt$ (función Gamma de Euler). Para $\alpha \in \mathbb{Z}^+$: $\Gamma(\alpha) = (\alpha-1)!$.

| $E[X]$ | $\text{Var}(X)$ | MGF |
|---|---|---|
| $\alpha\beta$ | $\alpha\beta^2$ | $(1 - \beta t)^{-\alpha}$, $t < 1/\beta$ |

**Casos especiales**:
- $\text{Gamma}(1, 1/\lambda) = \text{Exponential}(\lambda)$
- $\text{Gamma}(k/2, 2) = \chi^2(k)$
- $\text{Gamma}(\alpha, \beta)$: suma de $\alpha$ variables $\text{Exp}(1/\beta)$ independientes (si $\alpha \in \mathbb{Z}^+$).

---

### Beta($\alpha, \beta$)
Distribución en $(0,1)$, usada para modelar proporciones y como distribución a priori Bayesiana.

$$f_X(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}, \quad x \in (0,1)$$

donde $B(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$.

| $E[X]$ | $\text{Var}(X)$ |
|---|---|
| $\frac{\alpha}{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ |

**Casos especiales**: Beta$(1,1) = \text{Unif}(0,1)$.

---

### Chi-cuadrado $\chi^2(k)$
Si $Z_1, \ldots, Z_k \overset{iid}{\sim} N(0,1)$, entonces $\sum_{i=1}^k Z_i^2 \sim \chi^2(k)$.

Caso especial de Gamma$\left(\frac{k}{2}, 2\right)$.

| $E[X]$ | $\text{Var}(X)$ |
|---|---|
| $k$ | $2k$ |

**Uso principal**: Pruebas de varianza ($\chi^2$ test), tablas de contingencia (prueba de independencia).

---

### $t$ de Student($\nu$)
Si $Z \sim N(0,1)$, $W \sim \chi^2(\nu)$, independientes:
$$T = \frac{Z}{\sqrt{W/\nu}} \sim t(\nu)$$

Simétrica alrededor de $0$, con colas más pesadas que la Normal. Converge a $N(0,1)$ cuando $\nu \to \infty$.

| $E[T]$ | $\text{Var}(T)$ |
|---|---|
| $0$ ($\nu > 1$) | $\frac{\nu}{\nu-2}$ ($\nu > 2$) |

**Uso principal**: Inferencia sobre $\mu$ con $\sigma$ desconocida (muestras pequeñas).

---

### $F$($d_1, d_2$)
Si $W_1 \sim \chi^2(d_1)$, $W_2 \sim \chi^2(d_2)$, independientes:
$$F = \frac{W_1/d_1}{W_2/d_2} \sim F(d_1, d_2)$$

| $E[F]$ | Relación |
|---|---|
| $\frac{d_2}{d_2-2}$ ($d_2>2$) | Si $T \sim t(\nu)$, entonces $T^2 \sim F(1,\nu)$ |

**Uso principal**: Pruebas de razón de varianzas, ANOVA.

---

## 3.3 Aproximaciones entre Distribuciones

```
Hipergeométrica(N,K,n) ──(n/N→0)──→ Binomial(n, K/N)
                                              │
                               (n grande, p pequeña, λ=np fijo)
                                              ↓
                                        Poisson(λ)
                                              │
                               (λ grande, aprox. normal)
                                              ↓
                                     Normal(λ, λ)
Binomial(n,p) ──(n grande, np y n(1-p) ≥5)──→ Normal(np, np(1-p))
```

**Corrección de Continuidad** (discreta → continua):
$$P(X \le k) \approx \Phi\!\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$$

---

## 3.4 Errores Comunes en este Tema

- **Geométrica indexada desde 0 vs 1**: Algunos textos definen $P(X=k)$ con $k=0,1,2,\ldots$ (número de fracasos antes del primer éxito). Confirmar la convención.
- **Parámetro de la Exponencial**: $\lambda$ es la **tasa** (no la media). La media es $1/\lambda$.
- **Parámetros de Gamma**: Distintos textos usan (forma, tasa) vs. (forma, escala). Verificar.
- **Poisson approximation**: No aplicar cuando $p$ no es pequeña aunque $n$ sea grande.
- **$t$ vs. $z$**: Usar $t_{n-1}$ cuando $\sigma$ es desconocida, sin importar el tamaño muestral. Solo se usa $z$ cuando $\sigma$ es conocida.
- **Curtosis de la Normal**: $\gamma_2 = 0$ (curtosis excedente). Colas más pesadas implican $\gamma_2 > 0$.
