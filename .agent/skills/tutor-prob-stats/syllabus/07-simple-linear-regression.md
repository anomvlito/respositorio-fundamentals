# Tema 7 — Regresión Lineal Simple

**Referencias**: Devore, *Probability and Statistics for Engineering and the Sciences* (9th ed.), Ch. 12–13; Wackerly, Mendenhall & Scheaffer, *Mathematical Statistics with Applications* (7th ed.), Ch. 11.

---

## 7.1 El Modelo

El **Modelo de Regresión Lineal Simple** (SLR) es:
$$Y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad i = 1, \ldots, n$$

**Supuestos (LINE)**:
- **L**inealidad: $E[Y \mid x] = \beta_0 + \beta_1 x$ (la relación media es lineal).
- **I**ndependencia: los errores $\varepsilon_i$ son independientes entre sí.
- **N**ormalidad: $\varepsilon_i \sim N(0, \sigma^2)$.
- **E**qual variance (homocedasticidad): $\text{Var}(\varepsilon_i) = \sigma^2$ constante para todo $i$.

> En el modelo SLR, $x_i$ son **valores fijos** (no aleatorios). Solo $Y_i$ es aleatoria.

---

## 7.2 Estimación por Mínimos Cuadrados (OLS)

Los estimadores OLS minimizan la **Suma de Cuadrados del Error**:
$$\text{SSE} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 = \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2$$

**Solución OLS**:
$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}}, \qquad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$$

donde:
$$S_{xx} = \sum_{i=1}^n (x_i - \bar{x})^2 = \sum x_i^2 - n\bar{x}^2$$
$$S_{xy} = \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) = \sum x_i y_i - n\bar{x}\bar{y}$$
$$S_{yy} = \sum_{i=1}^n (y_i - \bar{y})^2 = \sum y_i^2 - n\bar{y}^2$$

**Nota**: La recta de regresión siempre pasa por el punto $(\bar{x}, \bar{y})$.

---

## 7.3 Residuos y Estimación de $\sigma^2$

**Residuo**: $e_i = y_i - \hat{y}_i = y_i - (\hat{\beta}_0 + \hat{\beta}_1 x_i)$.

Propiedades de los residuos OLS:
- $\sum e_i = 0$
- $\sum x_i e_i = 0$
- $\sum \hat{y}_i e_i = 0$

**Estimador insesgado de $\sigma^2$** (Error Estándar del Modelo):
$$S^2 = \hat{\sigma}^2 = \frac{\text{SSE}}{n-2} = \frac{\sum(y_i - \hat{y}_i)^2}{n-2}, \qquad S = \sqrt{S^2}$$

El divisor es $n-2$ porque se estiman 2 parámetros ($\beta_0$, $\beta_1$).

---

## 7.4 Descomposición ANOVA

$$\underbrace{\sum(y_i - \bar{y})^2}_{\text{SST}} = \underbrace{\sum(\hat{y}_i - \bar{y})^2}_{\text{SSR}} + \underbrace{\sum(y_i - \hat{y}_i)^2}_{\text{SSE}}$$

| Fuente | Suma de Cuadrados | Grados de Libertad | Cuadrado Medio |
|---|---|---|---|
| Regresión | SSR | $1$ | MSR = SSR |
| Error | SSE | $n-2$ | MSE = SSE/$n-2$ |
| Total | SST | $n-1$ | |

**Coeficiente de Determinación**:
$$R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}} \in [0,1]$$

$R^2$ es la proporción de variabilidad en $Y$ explicada por el modelo lineal con $x$.

**Relación con la correlación**:
$$R^2 = r^2_{xy} = \left(\frac{S_{xy}}{\sqrt{S_{xx}\,S_{yy}}}\right)^2$$

donde $r_{xy}$ es el coeficiente de correlación de Pearson muestral.

---

## 7.5 Distribución de los Estimadores

Bajo los supuestos LINE, con $\varepsilon_i \sim N(0,\sigma^2)$:

$$\hat{\beta}_1 \sim N\!\left(\beta_1,\, \frac{\sigma^2}{S_{xx}}\right), \qquad \hat{\beta}_0 \sim N\!\left(\beta_0,\, \sigma^2\!\left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right)\right)$$

$$\frac{(n-2)S^2}{\sigma^2} \sim \chi^2_{n-2} \quad \text{(independiente de }\hat{\beta}_0\text{ y }\hat{\beta}_1\text{)}$$

---

## 7.6 Inferencia sobre $\beta_1$

**Prueba de hipótesis** $H_0: \beta_1 = 0$ (no hay relación lineal):
$$T = \frac{\hat{\beta}_1}{S/\sqrt{S_{xx}}} \sim t_{n-2} \quad \text{bajo } H_0$$

Rechazar $H_0$ si $|T| > t_{\alpha/2,\, n-2}$.

**Intervalo de confianza** para $\beta_1$:
$$\hat{\beta}_1 \pm t_{\alpha/2,\, n-2} \cdot \frac{S}{\sqrt{S_{xx}}}$$

**Inferencia sobre $\beta_0$**:
$$T = \frac{\hat{\beta}_0}{S\sqrt{1/n + \bar{x}^2/S_{xx}}} \sim t_{n-2}$$

---

## 7.7 Predicción

Sea $x^*$ un nuevo valor del predictor.

**Estimación de la media de $Y$ dado $X = x^*$** (IC para $E[Y \mid x^*]$):
$$\hat{y}^* \pm t_{\alpha/2,\, n-2} \cdot S\sqrt{\frac{1}{n} + \frac{(x^*-\bar{x})^2}{S_{xx}}}$$

**Intervalo de Predicción** para una nueva observación $Y^*$ (más ancho):
$$\hat{y}^* \pm t_{\alpha/2,\, n-2} \cdot S\sqrt{1 + \frac{1}{n} + \frac{(x^*-\bar{x})^2}{S_{xx}}}$$

> **Distinción clave**: El IC de la media tiene varianza $\text{Var}(\hat{Y}^*)$; el IP adiciona $\sigma^2$ (incertidumbre de la nueva observación individual).

**Extrapolación**: Predecir fuera del rango de los datos $x_i$ observados es estadísticamente peligroso; la relación lineal puede no mantenerse.

---

## 7.8 Verificación de Supuestos (Análisis de Residuos)

| Supuesto | Verificación gráfica | Prueba formal |
|---|---|---|
| **Linealidad** | Gráfico $e_i$ vs $\hat{y}_i$ (sin patrón) | — |
| **Homocedasticidad** | Gráfico $e_i$ vs $\hat{y}_i$ (varianza constante) | Prueba de Breusch-Pagan |
| **Normalidad** | Q-Q plot de residuos | Shapiro-Wilk, Kolmogorov-Smirnov |
| **Independencia** | Gráfico $e_i$ vs orden temporal | Prueba de Durbin-Watson |

**Outliers e influencia**:
- **Outlier**: observación con residuo estandarizado $|r_i| > 2$ o $3$.
- **High Leverage**: observación con $h_{ii} > 2(p+1)/n$ (palanca de la diagonal de la matriz hat $H = X(X'X)^{-1}X'$).
- **Distancia de Cook**: mide la influencia total de la $i$-ésima observación sobre todos los $\hat{\beta}$. Valores $D_i > 1$ (o $> 4/n$) indican influencia alta.

---

## 7.9 Errores Comunes en este Tema

- **Confundir IC de la media con IP**: El intervalo de predicción siempre es más ancho; incluye la incertidumbre de la nueva observación.
- **$R^2$ alto ≠ modelo válido**: Un $R^2$ cercano a 1 no garantiza que el modelo sea lineal ni que los supuestos se cumplan. Revisar residuos siempre.
- **Causalidad vs correlación**: Una correlación significativa no implica causalidad.
- **Divisor $n-2$ en $S^2$**: No $n$, no $n-1$. Se pierden 2 grados de libertad por $\hat{\beta}_0$ y $\hat{\beta}_1$.
- **Extrapolación**: Nunca predecir fuera del rango de $x$ sin justificación del dominio.
- **Prueba $F$ vs. Prueba $t$ en SLR**: En SLR con un solo predictor, $F = T^2$ bajo $H_0: \beta_1 = 0$; son equivalentes.
- **Interpretar $\beta_0$**: El intercepto es el valor esperado de $Y$ cuando $x=0$; si $x=0$ no está en el rango de los datos, $\hat{\beta}_0$ no tiene interpretación práctica directa.
