# Script R para generar gráfico de Excedente del Consumidor (Pregunta 41)
# Compara CP, Monopolio y Monopolio Regulado

# Definir archivo de salida
output_file <- "images/q41_excedente_consumidor.png"
dir.create(dirname(output_file), showWarnings = FALSE, recursive = TRUE)

# Abrir dispositivo PNG
png(output_file, width = 7, height = 6, units = "in", res = 300)

# Configurar para tres gráficos horizontales
par(mfrow = c(1, 3), mar = c(4, 3, 3, 1), family = "sans")

# Parámetros comunes
Q <- seq(0, 100, length.out = 500)
P_demanda <- 100 - Q
CMg <- rep(40, length(Q))
Q_cp <- 60
P_cp <- 40
Q_monopolio <- 30
P_monopolio <- 70

# ============ GRÁFICO 1: Competencia Perfecta ============
plot(Q, P_demanda, type = "l", lwd = 2.5, col = "#2C3E50",
     xlim = c(0, 100), ylim = c(0, 110),
     xlab = "Q", ylab = "P",
     main = "Competencia Perfecta",
     cex.lab = 1.1, cex.main = 1.2, las = 1)
grid(col = "gray90", lty = 1)
lines(Q, CMg, lwd = 2, col = "#E67E22")

# Excedente del consumidor (área bajo demanda, sobre precio)
polygon(c(0, Q_cp, 0),
        c(100, P_cp, P_cp),
        col = rgb(46, 204, 113, alpha = 80, maxColorValue = 255),
        border = NA)

# Redibujar curvas
lines(Q, P_demanda, lwd = 2.5, col = "#2C3E50")
lines(Q, CMg, lwd = 2, col = "#E67E22")
points(Q_cp, P_cp, pch = 19, cex = 1.5, col = "#27AE60")

text(20, 75, "EC\n(máximo)", cex = 1, font = 2, col = "#27AE60")
text(85, 45, "CMg", cex = 0.9, col = "#E67E22")

# ============ GRÁFICO 2: Monopolio ============
plot(Q, P_demanda, type = "l", lwd = 2.5, col = "#2C3E50",
     xlim = c(0, 100), ylim = c(0, 110),
     xlab = "Q", ylab = "",
     main = "Monopolio",
     cex.lab = 1.1, cex.main = 1.2, las = 1)
grid(col = "gray90", lty = 1)
lines(Q, CMg, lwd = 2, col = "#E67E22")

# Excedente del consumidor (reducido)
polygon(c(0, Q_monopolio, 0),
        c(100, P_monopolio, P_monopolio),
        col = rgb(46, 204, 113, alpha = 80, maxColorValue = 255),
        border = NA)

# Pérdida de eficiencia
polygon(c(Q_monopolio, Q_cp, Q_monopolio),
        c(P_monopolio, P_cp, P_cp),
        col = rgb(149, 165, 166, alpha = 60, maxColorValue = 255),
        border = NA)

lines(Q, P_demanda, lwd = 2.5, col = "#2C3E50")
lines(Q, CMg, lwd = 2, col = "#E67E22")
points(Q_monopolio, P_monopolio, pch = 19, cex = 1.5, col = "#E74C3C")

text(10, 88, "EC\n(reducido)", cex = 1, font = 2, col = "#27AE60")
text(45, 60, "DWL", cex = 0.9, font = 2, col = "#7F8C8D")

# ============ GRÁFICO 3: Monopolio Regulado (P = CMg) ============
plot(Q, P_demanda, type = "l", lwd = 2.5, col = "#2C3E50",
     xlim = c(0, 100), ylim = c(0, 110),
     xlab = "Q", ylab = "",
     main = "Monopolio Regulado\n(P = CMg)",
     cex.lab = 1.1, cex.main = 1.2, las = 1)
grid(col = "gray90", lty = 1)
lines(Q, CMg, lwd = 2, col = "#E67E22")

# Excedente del consumidor (igual a CP)
polygon(c(0, Q_cp, 0),
        c(100, P_cp, P_cp),
        col = rgb(46, 204, 113, alpha = 80, maxColorValue = 255),
        border = NA)

lines(Q, P_demanda, lwd = 2.5, col = "#2C3E50")
lines(Q, CMg, lwd = 2, col = "#E67E22")
points(Q_cp, P_cp, pch = 19, cex = 1.5, col = "#8E44AD")

text(20, 75, "EC\n(= CP)", cex = 1, font = 2, col = "#27AE60")
text(50, 25, "Regulación\nóptima", cex = 0.85, font = 3, col = "#8E44AD")

dev.off()

cat("✓ Gráfico de excedente del consumidor guardado en:", output_file, "\n")
