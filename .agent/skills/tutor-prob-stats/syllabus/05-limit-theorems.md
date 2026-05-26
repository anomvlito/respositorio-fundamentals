# Tema 5 — Teoremas Límite

**Referencias**: Ross, *A First Course in Probability* (10th ed.), Ch. 8; DeGroot & Schervish, *Probability and Statistics* (4th ed.), Ch. 6.

---

## 5.1 Tipos de Convergencia

Sea $\{X_n\}$ una sucesión de variables aleatorias y $X$ una v.a. límite.

| Tipo | Notación | Definición |
|---|---|---|
| **Casi segura** (a.s.) | $X_n \xrightarrow{a.s.} X$ | $P(\lim_{n\to\infty} X_n = X) = 1$ |
| **En probabilidad** | $X_n \xrightarrow{P} X$ | $\forall\, \varepsilon > 0$: $\lim P(\|X_n - X\| > \varepsilon) = 0$ |
| **En distribución** ($L$) | $X_n \xrightarrow{d} X$ | $F_{X_n}(x) \to F_X(x)$ en puntos de continuidad de $F_X$ |
| **En media cuadrática** ($L^2$) | $X_n \xrightarrow{L^2} X$ | $E[(X_n - X)^2] \to 0$ |

**Jerarquía**:
$$X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{P} X \implies X_n \xrightarrow{d} X$$
$$X_n \xrightarrow{L^2} X \implies X_n \xrightarrow{P} X$$

> La convergencia en distribución es la más débil: solo describe el comportamiento asintótico de la CDF, no de las v.a. mismas.

---

## 5.2 Desigualdades de Concentración

### Desigualdad de Markov
Para $X \ge 0$ y $a > 0$:
$$P(X \ge a) \le \frac{E[X]}{a}$$

**Derivación**: $E[X] = \int_0^\infty x\, f(x)\, dx \ge \int_a^\infty x\, f(x)\, dx \ge a \cdot P(X \ge a)$.

### Desigualdad de Chebyshev
Para cualquier $X$ con $E[X] = \mu$ y $\text{Var}(X) = \sigma^2 < \infty$, y $k > 0$:
$$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2} \qquad \text{equivalentemente} \qquad P(|X - \mu| \ge \varepsilon) \le \frac{\sigma^2}{\varepsilon^2}$$

Provee cotas **sin necesidad de conocer la distribución**. Es cruda; en la práctica la Normal es mucho más concentrada.

**Corolario**: $P(|X - \mu| < k\sigma) \ge 1 - \frac{1}{k^2}$.

---

## 5.3 Ley de los Grandes Números

### Ley Débil (WLLN)
Sean $X_1, X_2, \ldots$ v.a. **iid** con $E[X_i] = \mu < \infty$. Sea $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$. Entonces:
$$\bar{X}_n \xrightarrow{P} \mu \quad \text{cuando } n \to \infty$$

**Demostración vía Chebyshev** (si además $\text{Var}(X_i) = \sigma^2 < \infty$):
$$P(|\bar{X}_n - \mu| \ge \varepsilon) \le \frac{\text{Var}(\bar{X}_n)}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \to 0$$

### Ley Fuerte (SLLN)
Bajo las mismas condiciones (solo requiere $E[|X|] < \infty$):
$$\bar{X}_n \xrightarrow{a.s.} \mu$$

**Interpretación**: La media muestral converge a la media poblacional con probabilidad 1. Justifica la frecuencia relativa como aproximación de la probabilidad.

---

## 5.4 Teorema Central del Límite (CLT)

### Versión Clásica (iid)
Sean $X_1, \ldots, X_n \overset{iid}{\sim} (\mu, \sigma^2)$ con $0 < \sigma^2 < \infty$. Sea $\bar{X}_n = \frac{1}{n}\sum X_i$. Entonces:

$$Z_n = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1)$$

**Notación**: $\bar{X}_n \overset{aprox}{\sim} N\!\left(\mu,\, \frac{\sigma^2}{n}\right)$ para $n$ grande.

**Regla práctica**: El CLT es una buena aproximación para $n \ge 30$ en general. Si la distribución original es muy asimétrica, se puede necesitar $n$ mayor.

### Aplicación a la Binomial
Si $X \sim \text{Bin}(n,p)$, entonces $\frac{X - np}{\sqrt{np(1-p)}} \xrightarrow{d} N(0,1)$.

**Corrección de Continuidad** (mejora la aproximación):
$$P(X \le k) \approx \Phi\!\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right)$$
$$P(X = k) \approx \Phi\!\left(\frac{k + 0.5 - np}{\sqrt{np(1-p)}}\right) - \Phi\!\left(\frac{k - 0.5 - np}{\sqrt{np(1-p)}}\right)$$

Condición para aplicar: $np \ge 5$ y $n(1-p) \ge 5$.

### Aplicación a la Poisson
Si $X \sim \text{Poi}(\lambda)$, entonces $\frac{X - \lambda}{\sqrt{\lambda}} \xrightarrow{d} N(0,1)$ cuando $\lambda \to \infty$.

---

## 5.5 Método Delta

Si $\sqrt{n}(X_n - \mu) \xrightarrow{d} N(0, \sigma^2)$ y $g$ es diferenciable en $\mu$ con $g'(\mu) \ne 0$:
$$\sqrt{n}(g(X_n) - g(\mu)) \xrightarrow{d} N(0,\, [g'(\mu)]^2 \sigma^2)$$

**Uso típico**: Encontrar la distribución asintótica de una función de la media muestral o de un MLE.

**Ejemplo**: Si $\hat{p}$ es la proporción muestral con $\sqrt{n}(\hat{p} - p) \xrightarrow{d} N(0, p(1-p))$, y $g(p) = \ln(p/(1-p))$ (logit), entonces:
$$\sqrt{n}(g(\hat{p}) - g(p)) \xrightarrow{d} N\!\left(0,\, \frac{1}{p^2(1-p)^2} \cdot p(1-p)\right) = N\!\left(0,\, \frac{1}{p(1-p)}\right)$$

---

## 5.6 Convergencia de la MGF (Teorema de Continuidad de Momentos)

Si $M_{X_n}(t) \to M_X(t)$ para todo $t$ en un entorno de $0$, entonces $X_n \xrightarrow{d} X$.

**Uso en la demostración del CLT**: Se demuestra que la MGF de $Z_n$ converge a $e^{t^2/2}$ (la MGF de $N(0,1)$) usando la expansión de Taylor de $e^{tX}$.

---

## 5.7 Errores Comunes en este Tema

- **Confundir WLLN y CLT**: La LGN dice que $\bar{X}_n \to \mu$ (convergencia puntual). El CLT dice *con qué velocidad* converge y cuál es la distribución del error.
- **Aplicar CLT sin verificar condiciones**: Requiere $\sigma^2 < \infty$ y $n$ suficientemente grande.
- **Olvidar la corrección de continuidad**: Omitirla subestima o sobreestima probabilidades de colas.
- **$\bar{X}_n$ no es Normal exactamente**: Solo aproximadamente Normal para $n$ grande, a menos que la distribución original sea Normal.
- **Método Delta**: Requiere que $g'(\mu) \ne 0$; si $g'(\mu) = 0$, se necesita el Método Delta de segundo orden.
