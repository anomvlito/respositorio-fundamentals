# Tema 6 — Inferencia Estadística

**Referencias**: Devore, *Probability and Statistics for Engineering and the Sciences* (9th ed.), Ch. 6–9; DeGroot & Schervish, *Probability and Statistics* (4th ed.), Ch. 7–9; Wackerly, Mendenhall & Scheaffer, *Mathematical Statistics with Applications* (7th ed.), Ch. 8–10.

---

## 6.1 Marco de la Inferencia

Un **modelo estadístico** supone que los datos $X_1, \ldots, X_n$ provienen de una distribución indexada por un parámetro desconocido $\theta \in \Theta$.

- **Estadístico**: cualquier función de los datos $T = T(X_1,\ldots,X_n)$ que **no** depende de $\theta$.
- **Estimador**: estadístico usado para aproximar $\theta$.
- **Estimado**: el valor numérico $T(x_1,\ldots,x_n)$ observado.

---

## 6.2 Estimación Puntual

### Propiedades de los Estimadores

| Propiedad | Definición | Consecuencia |
|---|---|---|
| **Insesgadez** | $E[\hat{\theta}] = \theta$ para todo $\theta$ | El sesgo es cero |
| **Sesgo** | $\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$ | Puede ser positivo o negativo |
| **Eficiencia** | MSE mínimo entre los insesgados | Óptimo en varianza |
| **Consistencia** | $\hat{\theta}_n \xrightarrow{P} \theta$ | Mejora con $n$ |
| **Suficiencia** | $T$ captura toda la info sobre $\theta$ | No se pierde info al resumir |

**Error Cuadrático Medio**:
$$\text{MSE}(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = \text{Var}(\hat{\theta}) + \text{Bias}^2(\hat{\theta})$$

**Estimadores estándar**:
- Media muestral: $\bar{X} = \frac{1}{n}\sum X_i$ — insesgado para $\mu$.
- Varianza muestral: $S^2 = \frac{1}{n-1}\sum(X_i - \bar{X})^2$ — insesgado para $\sigma^2$ (corrección de Bessel).
- Proporción muestral: $\hat{p} = X/n$ — insesgado para $p$.

### Cota de Cramér–Rao

Para cualquier estimador **insesgado** $\hat{\theta}$ de $\theta$:
$$\text{Var}(\hat{\theta}) \ge \frac{1}{n\,\mathcal{I}(\theta)}$$

donde $\mathcal{I}(\theta)$ es la **información de Fisher**:
$$\mathcal{I}(\theta) = E\!\left[\left(\frac{\partial}{\partial\theta}\ln f(X;\theta)\right)^2\right] = -E\!\left[\frac{\partial^2}{\partial\theta^2}\ln f(X;\theta)\right]$$

Un estimador que alcanza esta cota se llama **UMVUE** (Uniformly Minimum Variance Unbiased Estimator).

---

### Método de los Momentos (MOM)

1. Calcular los momentos poblacionales: $\mu_k(\theta) = E[X^k]$.
2. Igualar con los momentos muestrales: $\hat{\mu}_k = \frac{1}{n}\sum X_i^k$.
3. Resolver el sistema para obtener $\hat{\theta}_{\text{MOM}}$.

**Ejemplo**: Para $X \sim \text{Gamma}(\alpha, \beta)$:
- $\mu_1 = \alpha\beta$, $\mu_2 - \mu_1^2 = \alpha\beta^2$
- $\hat{\beta}_{\text{MOM}} = \frac{S^2}{\bar{X}}$, $\hat{\alpha}_{\text{MOM}} = \frac{\bar{X}^2}{S^2}$

---

### Estimación por Máxima Verosimilitud (MLE)

**Definición**: $\hat{\theta}_{\text{MLE}} = \arg\max_\theta L(\theta; \mathbf{x})$, donde la **función de verosimilitud** es:
$$L(\theta; x_1,\ldots,x_n) = \prod_{i=1}^n f(x_i;\, \theta)$$

**Procedimiento**:
1. Escribir $L(\theta) = \prod f(x_i; \theta)$.
2. Tomar log: $\ell(\theta) = \sum \ln f(x_i; \theta)$ (log-verosimilitud).
3. Resolver la **ecuación de verosimilitud**: $\frac{d\ell}{d\theta} = 0$.
4. Verificar que es un máximo (segunda derivada negativa o verificar límites).

**Propiedades asintóticas del MLE**:
- **Consistente**: $\hat{\theta}_n \xrightarrow{P} \theta^*$.
- **Asintóticamente Normal**: $\sqrt{n}(\hat{\theta}_n - \theta) \xrightarrow{d} N(0, 1/\mathcal{I}(\theta))$.
- **Asintóticamente eficiente**: alcanza la cota de Cramér–Rao en el límite.
- **Invarianza**: Si $\hat{\theta}$ es MLE de $\theta$, entonces $g(\hat{\theta})$ es MLE de $g(\theta)$.

**Ejemplos canónicos**:

| Distribución | MLE |
|---|---|
| Bernoulli($p$) | $\hat{p} = \bar{X}$ |
| Normal($\mu, \sigma^2$) | $\hat{\mu} = \bar{X}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(X_i-\bar{X})^2$ (sesgado) |
| Exponencial($\lambda$) | $\hat{\lambda} = 1/\bar{X}$ |
| Poisson($\lambda$) | $\hat{\lambda} = \bar{X}$ |

---

## 6.3 Intervalos de Confianza

Un **intervalo de confianza** (IC) al nivel $1-\alpha$ para $\theta$ es un intervalo aleatorio $[\hat{L}, \hat{U}]$ tal que:
$$P(\hat{L} \le \theta \le \hat{U}) = 1 - \alpha$$

**Interpretación correcta**: Si el procedimiento se repitiera muchas veces, el $(1-\alpha)$\% de los intervalos construidos contendrían al verdadero $\theta$. Un intervalo *realizado* no tiene probabilidad —ya sea contiene $\theta$ o no.

### Cantidad Pivotal
Una función $Q = Q(X_1,\ldots,X_n; \theta)$ cuya distribución es **conocida e independiente de $\theta$**.

### Intervalos para la Media $\mu$

**$\sigma$ conocida** — Pivote: $Z = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \sim N(0,1)$
$$\bar{X} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

**$\sigma$ desconocida** — Pivote: $T = \frac{\bar{X}-\mu}{S/\sqrt{n}} \sim t_{n-1}$
$$\bar{X} \pm t_{\alpha/2,\, n-1}\, \frac{S}{\sqrt{n}}$$

**Diferencia de medias** (dos muestras independientes, varianzas iguales):
$$(\bar{X}_1 - \bar{X}_2) \pm t_{\alpha/2,\, n_1+n_2-2}\, S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}$$
donde $S_p^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$ es la varianza combinada (*pooled*).

**Datos pareados**: Calcular $D_i = X_{1i} - X_{2i}$ y aplicar el IC de una muestra con $D_i$.

### Intervalo para $\sigma^2$
Pivote: $\chi^2 = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$
$$\left(\frac{(n-1)S^2}{\chi^2_{\alpha/2,\, n-1}},\; \frac{(n-1)S^2}{\chi^2_{1-\alpha/2,\, n-1}}\right)$$

### Intervalo para una Proporción $p$
Para $n$ grande (usando CLT):
$$\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

**Tamaño de muestra**: Para un margen de error $E$ dado:
$$n \ge \frac{z_{\alpha/2}^2\, \hat{p}(1-\hat{p})}{E^2} \qquad \text{(conservador: } \hat{p}=0.5 \Rightarrow n \ge \frac{z_{\alpha/2}^2}{4E^2}\text{)}$$

---

## 6.4 Pruebas de Hipótesis

### Marco General

- **$H_0$**: hipótesis nula (afirmación de "no efecto" o valor de referencia).
- **$H_a$**: hipótesis alternativa (lo que se quiere detectar).
- **Nivel de significancia** $\alpha$: probabilidad máxima tolerable de cometer Error Tipo I.

| Decisión \ Realidad | $H_0$ verdadera | $H_0$ falsa |
|---|---|---|
| **Rechazar $H_0$** | Error Tipo I ($\alpha$) | Correcto (Potencia $= 1-\beta$) |
| **No rechazar $H_0$** | Correcto | Error Tipo II ($\beta$) |

**$p$-valor**: $p = P(\text{estadístico tan o más extremo que el observado} \mid H_0)$.
Regla de decisión: Rechazar $H_0$ si $p < \alpha$.

### Pruebas Estándar

| Escenario | Hipótesis | Estadístico | Distribución bajo $H_0$ |
|---|---|---|---|
| $\mu$ ($\sigma$ conocida) | $H_0: \mu = \mu_0$ | $Z = \frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}}$ | $N(0,1)$ |
| $\mu$ ($\sigma$ desconocida) | $H_0: \mu = \mu_0$ | $T = \frac{\bar{X}-\mu_0}{S/\sqrt{n}}$ | $t_{n-1}$ |
| Dos medias (igualdad de var.) | $H_0: \mu_1 = \mu_2$ | $T = \frac{\bar{X}_1-\bar{X}_2}{S_p\sqrt{1/n_1+1/n_2}}$ | $t_{n_1+n_2-2}$ |
| Datos pareados | $H_0: \mu_D = 0$ | $T = \frac{\bar{D}}{S_D/\sqrt{n}}$ | $t_{n-1}$ |
| Varianza | $H_0: \sigma^2 = \sigma_0^2$ | $\chi^2 = \frac{(n-1)S^2}{\sigma_0^2}$ | $\chi^2_{n-1}$ |
| Razón de varianzas | $H_0: \sigma_1^2 = \sigma_2^2$ | $F = S_1^2/S_2^2$ | $F_{n_1-1,\, n_2-1}$ |
| Proporción | $H_0: p = p_0$ | $Z = \frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}$ | $N(0,1)$ |

### Regiones de Rechazo según la Alternativa

| $H_a$ | Región de Rechazo | $p$-valor |
|---|---|---|
| $\theta \ne \theta_0$ (bilateral) | $\|T\| > c_{\alpha/2}$ | $2P(T > \|t_{obs}\|)$ |
| $\theta > \theta_0$ (unilateral derecha) | $T > c_\alpha$ | $P(T > t_{obs})$ |
| $\theta < \theta_0$ (unilateral izquierda) | $T < -c_\alpha$ | $P(T < t_{obs})$ |

### Potencia de una Prueba

$$\text{Potencia}(\theta_a) = P(\text{Rechazar } H_0 \mid \theta = \theta_a) = 1 - \beta(\theta_a)$$

Para una prueba $z$ bilateral de $H_0: \mu = \mu_0$ vs $H_a: \mu = \mu_a$ (con $\sigma$ conocida):
$$\text{Potencia} \approx \Phi\!\left(-z_{\alpha/2} + \frac{|\mu_a - \mu_0|}{\sigma/\sqrt{n}}\right) + \Phi\!\left(-z_{\alpha/2} - \frac{|\mu_a - \mu_0|}{\sigma/\sqrt{n}}\right)$$

**Tamaño de muestra**: Para detectar un efecto $\delta = \mu_a - \mu_0$ con potencia $1-\beta$:
$$n \approx \frac{(z_{\alpha/2} + z_\beta)^2 \sigma^2}{\delta^2}$$

### Prueba de Razón de Verosimilitudes (LRT)
Estadístico:
$$\Lambda = -2\ln\frac{\sup_{\theta \in \Theta_0} L(\theta)}{\sup_{\theta \in \Theta} L(\theta)} = -2(\ell(\hat{\theta}_0) - \ell(\hat{\theta})) \xrightarrow{d} \chi^2_r \quad \text{bajo } H_0$$
donde $r = \dim(\Theta) - \dim(\Theta_0)$ es el número de restricciones.

---

## 6.5 Errores Comunes en este Tema

- **Interpretar el $p$-valor como $P(H_0)$**: El $p$-valor es la probabilidad de los datos dado $H_0$, no la probabilidad de que $H_0$ sea cierta.
- **No rechazar $\ne$ aceptar**: "No rechazar $H_0$" significa que los datos son consistentes con $H_0$, no que $H_0$ sea verdadera.
- **Un solo $\alpha$ fijado post-hoc**: $\alpha$ debe especificarse **antes** de recolectar datos.
- **Prueba bilateral vs. unilateral**: Elegir la alternativa según la pregunta científica, nunca mirando los datos primero.
- **$S^2$ sesgado del MLE**: El MLE de $\sigma^2$ usa divisor $n$, no $n-1$; no es insesgado.
- **Varianzas iguales vs. desiguales**: Aplicar la prueba $t$ de Welch si hay dudas sobre la igualdad de varianzas.
- **IC de $\sigma^2$ no es simétrico**: Los cuantiles $\chi^2$ son asimétricos; el IC no se construye como $\hat{\sigma}^2 \pm \text{margen}$.
