# Tema 1 — Combinatoria y Axiomas de Probabilidad

**Referencias**: Ross, *A First Course in Probability* (10th ed.), Ch. 1–3; DeGroot & Schervish, *Probability and Statistics* (4th ed.), Ch. 1.

---

## 1.1 Principios de Conteo

### Regla del Producto
Si un experimento consta de $k$ etapas con $n_1, n_2, \ldots, n_k$ resultados posibles en cada una, el número total de resultados es $n_1 \cdot n_2 \cdots n_k$.

### Permutaciones
Ordenamientos de $k$ objetos tomados de $n$ distintos (el orden importa):
$$P(n,k) = \frac{n!}{(n-k)!}$$
Permutaciones de $n$ objetos con repetición: si el grupo $i$ tiene $n_i$ objetos iguales, $\frac{n!}{n_1!\, n_2!\, \cdots n_r!}$.

### Combinaciones
Subconjuntos de $k$ objetos tomados de $n$ (el orden no importa):
$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

**Identidades clave**:
- $\binom{n}{k} = \binom{n}{n-k}$ (simetría)
- $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ (Triángulo de Pascal)
- $\sum_{k=0}^{n} \binom{n}{k} = 2^n$ (Teorema Binomial con $x=y=1$)

### Coeficiente Multinomial
Número de formas de dividir $n$ objetos en grupos de tamaños $n_1, \ldots, n_r$ (con $\sum n_i = n$):
$$\binom{n}{n_1, n_2, \ldots, n_r} = \frac{n!}{n_1!\, n_2!\, \cdots n_r!}$$

---

## 1.2 Espacios Muestrales y Eventos

- **Espacio muestral** $\Omega$: conjunto de todos los resultados posibles de un experimento.
- **Evento** $A$: subconjunto de $\Omega$.
- **Álgebra $\sigma$**: colección $\mathcal{F}$ de subconjuntos de $\Omega$ cerrada bajo complementos y uniones numerables. Necesaria para definir $P$ rigurosamente.

### Operaciones con Eventos
| Notación | Significado |
|---|---|
| $A^c$ o $A'$ | Complemento de $A$ |
| $A \cup B$ | Unión: $A$ o $B$ (o ambos) |
| $A \cap B$ | Intersección: $A$ y $B$ |
| $A \setminus B$ | Diferencia: $A$ pero no $B$ |
| $A \triangle B$ | Diferencia simétrica |

**Leyes de De Morgan**:
$$(A \cup B)^c = A^c \cap B^c, \qquad (A \cap B)^c = A^c \cup B^c$$

---

## 1.3 Axiomas de Kolmogorov

Sea $(\Omega, \mathcal{F}, P)$ un espacio de probabilidad. $P: \mathcal{F} \to \mathbb{R}$ es una **medida de probabilidad** si:

1. **No-negatividad**: $P(A) \ge 0$ para todo $A \in \mathcal{F}$.
2. **Normalización**: $P(\Omega) = 1$.
3. **Aditividad Contable**: Si $A_1, A_2, \ldots$ son **mutuamente excluyentes** ($A_i \cap A_j = \emptyset$ para $i \ne j$):
$$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

### Consecuencias de los Axiomas (Teoremas)
- $P(A^c) = 1 - P(A)$
- $P(\emptyset) = 0$
- $P(A) \le 1$
- Si $A \subseteq B$, entonces $P(A) \le P(B)$

### Principio de Inclusión-Exclusión
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

---

## 1.4 Probabilidad Condicional

**Definición**: Dado $P(B) > 0$,
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

**Regla de la Multiplicación**:
$$P(A \cap B) = P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)$$

**Regla de la Cadena** (extensión a $n$ eventos):
$$P(A_1 \cap A_2 \cap \cdots \cap A_n) = P(A_1)\,P(A_2 \mid A_1)\,P(A_3 \mid A_1 \cap A_2) \cdots$$

### Regla de la Probabilidad Total
Si $\{B_1, B_2, \ldots, B_k\}$ es una **partición** de $\Omega$ (mutuamente excluyentes y exhaustivos, $P(B_i) > 0$):
$$P(A) = \sum_{i=1}^{k} P(A \mid B_i)\, P(B_i)$$

### Teorema de Bayes
$$P(B_i \mid A) = \frac{P(A \mid B_i)\, P(B_i)}{\sum_{j=1}^{k} P(A \mid B_j)\, P(B_j)}$$

- $P(B_i)$: probabilidad **a priori** de $B_i$.
- $P(B_i \mid A)$: probabilidad **a posteriori** (posterior) dado que $A$ ocurrió.

**Trampa frecuente**: confundir $P(A \mid B)$ con $P(B \mid A)$ — la "falacia del fiscal" (*prosecutor's fallacy*).

---

## 1.5 Independencia

**Definición**: $A$ y $B$ son **independientes** si:
$$P(A \cap B) = P(A) \cdot P(B)$$

Equivalentemente: $P(A \mid B) = P(A)$ (siempre que $P(B) > 0$).

**Independencia mutua** de $n$ eventos $A_1, \ldots, A_n$: la factorización debe cumplirse para **toda** subcolección, no solo en pares.
$$P(A_{i_1} \cap \cdots \cap A_{i_k}) = \prod_{j=1}^k P(A_{i_j}), \quad \text{para todo subconjunto } \{i_1,\ldots,i_k\}$$

> **Distinción crítica**: Independencia por pares **no** implica independencia mutua (hay ejemplos de contraejemplos de Bernstein).

---

## 1.6 Errores Comunes en este Tema

- **Permutación vs. Combinación**: Si el orden importa → permutación; si no → combinación.
- **Sumar probabilidades no excluyentes** sin restar la intersección (olvidar Inclusión-Exclusión).
- **Bayes invertido**: escribir $P(B \mid A)$ cuando se pide $P(A \mid B)$.
- **Independencia vs. Mutua Exclusión**: si $P(A), P(B) > 0$, dos eventos mutuamente excluyentes **no** pueden ser independientes.
- **Conteo con repetición vs. sin repetición**: especificar claramente si los objetos son distinguibles.
