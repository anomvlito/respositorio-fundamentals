# Script R para generar gráfico de Ingreso Total y Elasticidad (Pregunta 39)
# Muestra la relación entre elasticidad e ingreso total

# Definir archivo de salida
output_file <- "images/q39_ingreso_total.png"
dir.create(dirname(output_file), showWarnings = FALSE, recursive = TRUE)

# Abrir dispositivo PNG
png(output_file, width = 7, height = 6, units = "in", res = 300)

# Configurar para dos gráficos verticales
par(mfrow = c(2, 1), mar = c(4, 4.5, 2, 1), family = "sans")

# ============ GRÁFICO 1: Curva de Demanda ============
Q <- seq(0, 100, length.out = 500)
P <- 100 - Q

plot(Q, P, type = "l", lwd = 3, col = "#2C3E50",
     xlim = c(0, 105), ylim = c(0, 105),
     xlab = "Cantidad (Q)", ylab = "Precio (P)",
     main = "Curva de Demanda Lineal",
     cex.lab = 1.1, cex.main = 1.2, las = 1)

grid(col = "gray90", lty = 1)

# Marcar punto de elasticidad unitaria
Q_unit <- 50
P_unit <- 50
points(Q_unit, P_unit, pch = 19, cex = 1.8, col = "#8E44AD")
segments(Q_unit, 0, Q_unit, P_unit, lty = 2, col = "#8E44AD", lwd = 1.5)
segments(0, P_unit, Q_unit, P_unit, lty = 2, col = "#8E44AD", lwd = 1.5)

# Etiquetas de regiones
text(25, 85, "ELÁSTICA\n|ε| > 1", cex = 1, font = 2, col = "#2980B9")
text(75, 20, "INELÁSTICA\n|ε| < 1", cex = 1, font = 2, col = "#C0392B")
text(Q_unit + 10, P_unit + 8, "ε = -1", cex = 0.95, font = 2, col = "#8E44AD")

# ============ GRÁFICO 2: Ingreso Total ============
# IT = P × Q = (100 - Q) × Q = 100Q - Q²
IT <- (100 - Q) * Q

plot(Q, IT, type = "l", lwd = 3, col = "#27AE60",
     xlim = c(0, 105), ylim = c(0, 2600),
     xlab = "Cantidad (Q)", ylab = "Ingreso Total (IT = P × Q)",
     main = "Ingreso Total y Elasticidad",
     cex.lab = 1.1, cex.main = 1.2, las = 1)

grid(col = "gray90", lty = 1)

# Marcar el máximo (donde ε = -1)
IT_max <- max(IT)
points(Q_unit, IT_max, pch = 19, cex = 1.8, col = "#8E44AD")
segments(Q_unit, 0, Q_unit, IT_max, lty = 2, col = "#8E44AD", lwd = 1.5)
segments(0, IT_max, Q_unit, IT_max, lty = 2, col = "#8E44AD", lwd = 1.5)

# Sombrear regiones
polygon(c(0, 0, Q_unit, Q_unit),
        c(0, 2600, 2600, 0),
        col = rgb(52, 152, 219, alpha = 30, maxColorValue = 255),
        border = NA)

polygon(c(Q_unit, Q_unit, 100, 100),
        c(0, 2600, 2600, 0),
        col = rgb(231, 76, 60, alpha = 30, maxColorValue = 255),
        border = NA)

# Redibujar curva IT
lines(Q, IT, lwd = 3, col = "#27AE60")

# Anotaciones
text(25, 2200, "IT ↑ cuando P ↓\n(Demanda elástica)", 
     cex = 0.9, font = 3, col = "#2980B9")
text(75, 2200, "IT ↓ cuando P ↓\n(Demanda inelástica)", 
     cex = 0.9, font = 3, col = "#C0392B")
text(Q_unit + 12, IT_max - 150, "IT máximo\n(ε = -1)", 
     cex = 0.9, font = 2, col = "#8E44AD")

# Etiquetas de valores
text(Q_unit, -120, sprintf("Q = %.0f", Q_unit), cex = 0.95, col = "#8E44AD")
text(-8, IT_max, sprintf("%.0f", IT_max), cex = 0.95, col = "#8E44AD", srt = 0)

# Cerrar dispositivo
dev.off()

cat("✓ Gráfico de ingreso total guardado en:", output_file, "\n")
