# Script R para generar gráfico de Desastre Natural (Pregunta 38)
# Muestra la contracción de la curva de oferta debido a reducción de capacidad productiva

# Definir archivo de salida
output_file <- "images/q38_desastre_natural.png"
dir.create(dirname(output_file), showWarnings = FALSE, recursive = TRUE)

# Abrir dispositivo PNG con dimensiones apropiadas para LaTeX
png(output_file, width = 6, height = 5, units = "in", res = 300)

# Configurar márgenes y parámetros gráficos
par(mar = c(4, 4, 2, 1), family = "sans")

# Definir rango de cantidades
Q <- seq(0, 100, length.out = 200)

# Definir curva de demanda (permanece constante)
# P = a - bQ, donde a=90, b=0.7
P_demanda <- 90 - 0.7 * Q

# Definir curva de oferta ANTES del desastre (S₀)
# P = c + dQ, donde c=15, d=0.5
P_oferta_antes <- 15 + 0.5 * Q

# Definir curva de oferta DESPUÉS del desastre (S₁)
# Desplazamiento hacia la izquierda: menor capacidad productiva
# Modelamos esto aumentando el intercepto y la pendiente
# P = c' + d'Q, donde c'=30, d'=0.65
P_oferta_despues <- 30 + 0.65 * Q

# Calcular puntos de equilibrio
# Equilibrio ANTES del desastre (S₀ y D)
Q_antes <- (90 - 15) / (0.7 + 0.5)  # Q ≈ 62.5
P_antes <- 15 + 0.5 * Q_antes        # P ≈ 46.25

# Equilibrio DESPUÉS del desastre (S₁ y D)
Q_despues <- (90 - 30) / (0.7 + 0.65)  # Q ≈ 44.44
P_despues <- 30 + 0.65 * Q_despues      # P ≈ 58.89

# Crear gráfico base
plot(Q, P_demanda, type = "l", lwd = 2.5, col = "#2C3E50", 
     xlim = c(0, 100), ylim = c(0, 100),
     xlab = "Cantidad (Q)", ylab = "Precio (P)",
     main = "Impacto de Desastre Natural en la Oferta",
     cex.lab = 1.2, cex.main = 1.3, las = 1)

# Agregar grid sutil
grid(col = "gray90", lty = 1)

# Dibujar curvas de oferta
lines(Q, P_oferta_antes, lwd = 2.5, col = "#27AE60")     # S₀ en verde (antes)
lines(Q, P_oferta_despues, lwd = 2.5, col = "#E67E22")   # S₁ en naranja (después)

# Marcar puntos de equilibrio
points(Q_antes, P_antes, pch = 19, cex = 1.8, col = "#27AE60")
points(Q_despues, P_despues, pch = 19, cex = 1.8, col = "#E67E22")

# Líneas punteadas para mostrar equilibrios
segments(Q_antes, 0, Q_antes, P_antes, lty = 2, col = "gray50", lwd = 1.5)
segments(0, P_antes, Q_antes, P_antes, lty = 2, col = "gray50", lwd = 1.5)
segments(Q_despues, 0, Q_despues, P_despues, lty = 2, col = "gray50", lwd = 1.5)
segments(0, P_despues, Q_despues, P_despues, lty = 2, col = "gray50", lwd = 1.5)

# Etiquetas de curvas
text(85, 90 - 0.7*85, "D", cex = 1.4, font = 2, col = "#2C3E50")
text(85, 15 + 0.5*85, "S₀\n(Antes)", cex = 1.2, font = 2, col = "#27AE60")
text(85, 30 + 0.65*85, "S₁\n(Después)", cex = 1.2, font = 2, col = "#E67E22")

# Etiquetas de equilibrios
text(Q_antes + 5, P_antes - 4, "E₀", cex = 1.2, font = 2, col = "#27AE60")
text(Q_despues - 5, P_despues + 4, "E₁", cex = 1.2, font = 2, col = "#E67E22")

# Etiquetas de ejes
text(Q_antes, -4, "Q₀", cex = 1.1, col = "gray30")
text(Q_despues, -4, "Q₁", cex = 1.1, col = "gray30")
text(-4, P_antes, "P₀", cex = 1.1, col = "gray30", srt = 0)
text(-4, P_despues, "P₁", cex = 1.1, col = "gray30", srt = 0)

# Flecha indicando el desplazamiento (contracción)
arrows(x0 = 50, y0 = 15 + 0.5*50, 
       x1 = 50, y1 = 30 + 0.65*50,
       length = 0.15, lwd = 2.5, col = "#C0392B", code = 2)

# Área sombreada mostrando la pérdida de producción
polygon(c(Q_despues, Q_antes, Q_antes, Q_despues),
        c(0, 0, P_antes, P_despues),
        col = rgb(231, 76, 60, alpha = 40, maxColorValue = 255),
        border = NA)

# Etiqueta de pérdida
text((Q_antes + Q_despues)/2, (P_antes + P_despues)/4, 
     "Pérdida de\nproducción", cex = 0.9, col = "#C0392B", font = 3)

# Cerrar dispositivo
dev.off()

cat("✓ Gráfico guardado en:", output_file, "\n")
