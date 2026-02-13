# Script R para generar gráfico de Elasticidad Precio-Demanda (Pregunta 39)
# Muestra las tres regiones de elasticidad en una curva de demanda lineal

# Definir archivo de salida
output_file <- "images/q39_elasticidad_demanda.png"
dir.create(dirname(output_file), showWarnings = FALSE, recursive = TRUE)

# Abrir dispositivo PNG con dimensiones apropiadas para LaTeX
png(output_file, width = 7, height = 5.5, units = "in", res = 300)

# Configurar márgenes y parámetros gráficos
par(mar = c(4, 4, 2, 1), family = "sans")

# Definir curva de demanda lineal: P = 100 - Q
Q <- seq(0, 100, length.out = 500)
P <- 100 - Q

# Punto de elasticidad unitaria (punto medio)
Q_unitaria <- 50
P_unitaria <- 50

# Punto dado en el problema (Q*, P*)
Q_star <- 50
P_star <- 50

# Crear gráfico base
plot(Q, P, type = "l", lwd = 3, col = "#2C3E50", 
     xlim = c(0, 110), ylim = c(0, 110),
     xlab = "Cantidad (Q)", ylab = "Precio (P)",
     main = "Elasticidad Precio-Demanda en Curva Lineal",
     cex.lab = 1.2, cex.main = 1.3, las = 1)

# Agregar grid sutil
grid(col = "gray90", lty = 1)

# Sombrear las tres regiones de elasticidad
# Región ELÁSTICA (|ε| > 1): Precios altos, cantidades bajas
polygon(c(0, 0, Q_unitaria, Q_unitaria),
        c(100, P_unitaria, P_unitaria, 100),
        col = rgb(52, 152, 219, alpha = 50, maxColorValue = 255),
        border = NA)

# Región INELÁSTICA (|ε| < 1): Precios bajos, cantidades altas
polygon(c(Q_unitaria, Q_unitaria, 100, 100),
        c(0, P_unitaria, P_unitaria, 0),
        col = rgb(231, 76, 60, alpha = 50, maxColorValue = 255),
        border = NA)

# Línea de elasticidad unitaria
segments(Q_unitaria, 0, Q_unitaria, P_unitaria, lty = 2, col = "#8E44AD", lwd = 2)
segments(0, P_unitaria, Q_unitaria, P_unitaria, lty = 2, col = "#8E44AD", lwd = 2)

# Redibujar la curva de demanda sobre las regiones sombreadas
lines(Q, P, lwd = 3, col = "#2C3E50")

# Marcar el punto de elasticidad unitaria
points(Q_unitaria, P_unitaria, pch = 19, cex = 2, col = "#8E44AD")

# Marcar puntos de ejemplo en cada región
# Punto en región elástica (Q < Q*, P > P*)
Q_elastica <- 25
P_elastica <- 75
points(Q_elastica, P_elastica, pch = 19, cex = 1.5, col = "#3498DB")

# Punto en región inelástica (Q > Q*, P < P*)
Q_inelastica <- 75
P_inelastica <- 25
points(Q_inelastica, P_inelastica, pch = 19, cex = 1.5, col = "#E74C3C")

# Etiquetas de regiones
text(25, 90, "REGIÓN ELÁSTICA\n|ε| > 1", cex = 1.1, font = 2, col = "#2980B9")
text(75, 15, "REGIÓN INELÁSTICA\n|ε| < 1", cex = 1.1, font = 2, col = "#C0392B")
text(Q_unitaria + 8, P_unitaria + 8, "ε = -1\n(Unitaria)", cex = 1, font = 2, col = "#8E44AD")

# Etiquetas de puntos
text(Q_star, -5, "Q*", cex = 1.2, col = "#8E44AD", font = 2)
text(-5, P_star, "P*", cex = 1.2, col = "#8E44AD", font = 2)

# Etiquetas de ejes
text(0, -5, "0", cex = 1.1, col = "gray30")
text(100, -5, "100", cex = 1.1, col = "gray30")
text(-5, 100, "100", cex = 1.1, col = "gray30")

# Añadir anotaciones explicativas
text(Q_elastica - 5, P_elastica + 8, "A", cex = 1.2, font = 2, col = "#3498DB")
text(Q_inelastica + 5, P_inelastica - 8, "B", cex = 1.2, font = 2, col = "#E74C3C")

# Flechas indicando dirección de cambio de elasticidad
arrows(x0 = 15, y0 = 50, x1 = 5, y1 = 70, 
       length = 0.12, lwd = 2, col = "#3498DB", code = 2)
text(18, 45, "Más elástica\n(P ↑)", cex = 0.85, col = "#2980B9", font = 3)

arrows(x0 = 85, y0 = 50, x1 = 95, y1 = 30, 
       length = 0.12, lwd = 2, col = "#E74C3C", code = 2)
text(82, 55, "Más inelástica\n(P ↓)", cex = 0.85, col = "#C0392B", font = 3)

# Cerrar dispositivo
dev.off()

cat("✓ Gráfico de elasticidad guardado en:", output_file, "\n")
