# Script R para generar gráfico de Monopolio vs Competencia Perfecta (Pregunta 40)
# Muestra la diferencia en producción, precio y beneficios

# Definir archivo de salida
output_file <- "images/q40_monopolio.png"
dir.create(dirname(output_file), showWarnings = FALSE, recursive = TRUE)

# Abrir dispositivo PNG
png(output_file, width = 7, height = 5.5, units = "in", res = 300)

# Configurar márgenes
par(mar = c(4, 4.5, 2, 1), family = "sans")

# Definir rango de cantidades
Q <- seq(0, 100, length.out = 500)

# Curva de demanda (P = 100 - Q)
P_demanda <- 100 - Q

# Costo marginal constante (simplificación)
CMg <- rep(40, length(Q))

# Costo medio (U-shaped, pero simplificado como constante para claridad)
CMe <- rep(40, length(Q))

# Ingreso marginal (IMg = 100 - 2Q para demanda lineal)
IMg <- 100 - 2*Q

# Punto de equilibrio en Competencia Perfecta (P = CMg)
Q_cp <- 60  # Donde P_demanda = CMg
P_cp <- 40

# Punto de equilibrio en Monopolio (IMg = CMg)
Q_monopolio <- 30  # Donde IMg = CMg
P_monopolio <- 70  # P correspondiente en curva de demanda

# Crear gráfico base
plot(Q, P_demanda, type = "l", lwd = 3, col = "#2C3E50",
     xlim = c(0, 105), ylim = c(0, 110),
     xlab = "Cantidad (Q)", ylab = "Precio (P) / Costos",
     main = "Monopolio vs Competencia Perfecta",
     cex.lab = 1.2, cex.main = 1.3, las = 1)

grid(col = "gray90", lty = 1)

# Dibujar curvas
lines(Q, CMg, lwd = 2.5, col = "#E67E22", lty = 1)  # Costo Marginal
lines(Q, CMe, lwd = 2.5, col = "#F39C12", lty = 2)  # Costo Medio
lines(Q, IMg, lwd = 2.5, col = "#9B59B6", lty = 1)  # Ingreso Marginal

# Marcar punto de Competencia Perfecta
points(Q_cp, P_cp, pch = 19, cex = 1.8, col = "#27AE60")
segments(Q_cp, 0, Q_cp, P_cp, lty = 2, col = "#27AE60", lwd = 1.5)
segments(0, P_cp, Q_cp, P_cp, lty = 2, col = "#27AE60", lwd = 1.5)

# Marcar punto de Monopolio
points(Q_monopolio, P_monopolio, pch = 19, cex = 1.8, col = "#E74C3C")
segments(Q_monopolio, 0, Q_monopolio, P_monopolio, lty = 2, col = "#E74C3C", lwd = 1.5)
segments(0, P_monopolio, Q_monopolio, P_monopolio, lty = 2, col = "#E74C3C", lwd = 1.5)

# Sombrear beneficio del monopolio (área entre P y CMe)
polygon(c(0, Q_monopolio, Q_monopolio, 0),
        c(CMe[1], CMe[1], P_monopolio, P_monopolio),
        col = rgb(231, 76, 60, alpha = 40, maxColorValue = 255),
        border = NA)

# Sombrear pérdida de eficiencia (deadweight loss)
polygon(c(Q_monopolio, Q_cp, Q_monopolio),
        c(P_monopolio, P_cp, P_cp),
        col = rgb(149, 165, 166, alpha = 60, maxColorValue = 255),
        border = NA)

# Redibujar curvas principales
lines(Q, P_demanda, lwd = 3, col = "#2C3E50")
lines(Q, CMg, lwd = 2.5, col = "#E67E22")
lines(Q, IMg, lwd = 2.5, col = "#9B59B6")

# Etiquetas de curvas
text(90, 100 - 90, "D (Demanda)", cex = 1.1, font = 2, col = "#2C3E50")
text(90, 40, "CMg = CMe", cex = 1.1, font = 2, col = "#E67E22")
text(45, 100 - 2*45 - 5, "IMg", cex = 1.1, font = 2, col = "#9B59B6")

# Etiquetas de puntos
text(Q_cp + 5, P_cp - 5, "Competencia\nPerfecta", cex = 0.95, font = 2, col = "#27AE60")
text(Q_monopolio - 8, P_monopolio + 8, "Monopolio", cex = 0.95, font = 2, col = "#E74C3C")

# Etiquetas de cantidades y precios
text(Q_cp, -4, expression(Q[CP]), cex = 1.1, col = "#27AE60")
text(Q_monopolio, -4, expression(Q[M]), cex = 1.1, col = "#E74C3C")
text(-5, P_cp, expression(P[CP]), cex = 1.1, col = "#27AE60", srt = 0)
text(-5, P_monopolio, expression(P[M]), cex = 1.1, col = "#E74C3C", srt = 0)

# Anotaciones
text(Q_monopolio/2, (P_monopolio + CMe[1])/2, "Beneficio\nMonopolio", 
     cex = 0.85, col = "#C0392B", font = 3)
text((Q_monopolio + Q_cp)/2, (P_monopolio + P_cp)/2 + 5, "Pérdida de\neficiencia", 
     cex = 0.85, col = "#7F8C8D", font = 3)

# Nota sobre regulación
text(50, 95, "Regulación P = CMe → Beneficio = 0", 
     cex = 0.9, col = "#8E44AD", font = 3)
arrows(x0 = 50, y0 = 92, x1 = 30, y1 = 42, 
       length = 0.12, lwd = 2, col = "#8E44AD", code = 2)

dev.off()

cat("✓ Gráfico de monopolio guardado en:", output_file, "\n")
