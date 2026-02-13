# Script R para generar gráfico de Oferta y Demanda (Pregunta 35)
# Muestra el desplazamiento de la curva de oferta S0 a S1

# Definir archivo de salida
output_file <- "images/q35_oferta_demanda.png"
dir.create(dirname(output_file), showWarnings = FALSE, recursive = TRUE)

# Abrir dispositivo PNG con dimensiones apropiadas para LaTeX
png(output_file, width = 6, height = 5, units = "in", res = 300)

# Configurar márgenes y parámetros gráficos
par(mar = c(4, 4, 2, 1), family = "sans")

# Definir rango de cantidades
Q <- seq(0, 100, length.out = 200)

# Definir curva de demanda (pendiente negativa)
# P = a - bQ, donde a=100, b=0.8
P_demanda <- 100 - 0.8 * Q

# Definir curva de oferta inicial S0 (pendiente positiva)
# P = c + dQ, donde c=20, d=0.6
P_oferta_S0 <- 20 + 0.6 * Q

# Definir curva de oferta desplazada S1 (hacia la izquierda/arriba)
# Aumenta el intercepto (mayores costos)
# P = c' + dQ, donde c'=35, d=0.6
P_oferta_S1 <- 35 + 0.6 * Q

# Calcular puntos de equilibrio
# Equilibrio original (S0 y D)
Q0 <- (100 - 20) / (0.8 + 0.6)  # Q0 ≈ 57.14
P0 <- 20 + 0.6 * Q0              # P0 ≈ 54.29

# Nuevo equilibrio (S1 y D)
Q1 <- (100 - 35) / (0.8 + 0.6)  # Q1 ≈ 46.43
P1 <- 35 + 0.6 * Q1              # P1 ≈ 62.86

# Crear gráfico base
plot(Q, P_demanda, type = "l", lwd = 2.5, col = "#2C3E50", 
     xlim = c(0, 100), ylim = c(0, 110),
     xlab = "Cantidad (Q)", ylab = "Precio (P)",
     main = "Desplazamiento de la Curva de Oferta",
     cex.lab = 1.2, cex.main = 1.3, las = 1)

# Agregar grid sutil
grid(col = "gray90", lty = 1)

# Dibujar curvas de oferta
lines(Q, P_oferta_S0, lwd = 2.5, col = "#E74C3C")  # S0 en rojo
lines(Q, P_oferta_S1, lwd = 2.5, col = "#C0392B")  # S1 en rojo oscuro

# Marcar puntos de equilibrio
points(Q0, P0, pch = 19, cex = 1.8, col = "#E74C3C")
points(Q1, P1, pch = 19, cex = 1.8, col = "#C0392B")

# Líneas punteadas para mostrar equilibrios
segments(Q0, 0, Q0, P0, lty = 2, col = "gray50", lwd = 1.5)
segments(0, P0, Q0, P0, lty = 2, col = "gray50", lwd = 1.5)
segments(Q1, 0, Q1, P1, lty = 2, col = "gray50", lwd = 1.5)
segments(0, P1, Q1, P1, lty = 2, col = "gray50", lwd = 1.5)

# Etiquetas de curvas
text(85, 100 - 0.8*85, "D", cex = 1.4, font = 2, col = "#2C3E50")
text(85, 20 + 0.6*85, "S₀", cex = 1.4, font = 2, col = "#E74C3C")
text(85, 35 + 0.6*85, "S₁", cex = 1.4, font = 2, col = "#C0392B")

# Etiquetas de equilibrios
text(Q0 + 5, P0 - 5, "E₀", cex = 1.2, font = 2, col = "#E74C3C")
text(Q1 - 5, P1 + 5, "E₁", cex = 1.2, font = 2, col = "#C0392B")

# Etiquetas de ejes
text(Q0, -5, "Q₀", cex = 1.1, col = "gray30")
text(Q1, -5, "Q₁", cex = 1.1, col = "gray30")
text(-5, P0, "P₀", cex = 1.1, col = "gray30", srt = 0)
text(-5, P1, "P₁", cex = 1.1, col = "gray30", srt = 0)

# Flecha indicando el desplazamiento
arrows(x0 = 60, y0 = 20 + 0.6*60, 
       x1 = 60, y1 = 35 + 0.6*60,
       length = 0.15, lwd = 2.5, col = "#8E44AD", code = 2)
text(65, (20 + 0.6*60 + 35 + 0.6*60)/2, "Desplazamiento\nhacia arriba", 
     cex = 0.9, col = "#8E44AD", font = 3)

# Cerrar dispositivo
dev.off()

cat("✓ Gráfico guardado en:", output_file, "\n")
