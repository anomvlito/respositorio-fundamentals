# Script R para generar gráfico de Valor Presente Neto (Pregunta 42)
# Visualiza los flujos de caja y el cálculo del VPN

# Definir archivo de salida
output_file <- "images/q42_vpn.png"
dir.create(dirname(output_file), showWarnings = FALSE, recursive = TRUE)

# Abrir dispositivo PNG
png(output_file, width = 7, height = 5.5, units = "in", res = 300)

# Configurar márgenes
par(mar = c(4, 5, 3, 2), family = "sans")

# Datos del problema
periodos <- c(0, 1, 2)
flujos_nominales <- c(-10, 11, 12)  # Millones
tasa <- 0.10

# Calcular valores presentes
VP <- flujos_nominales / (1 + tasa)^periodos
VPN_total <- sum(VP)

# Crear gráfico de barras
barplot_result <- barplot(flujos_nominales, 
        names.arg = c("Año 0\n(Hoy)", "Año 1", "Año 2"),
        col = c("#E74C3C", "#27AE60", "#27AE60"),
        border = "white",
        ylim = c(-12, 14),
        ylab = "Flujo de Caja (Millones $)",
        main = "Valor Presente Neto (VPN) - Análisis de Inversión",
        cex.lab = 1.2, cex.main = 1.3, cex.names = 1.1,
        las = 1)

# Agregar grid horizontal
abline(h = seq(-12, 14, by = 2), col = "gray90", lty = 1)

# Redibujar barras sobre el grid
barplot(flujos_nominales, 
        names.arg = c("Año 0\n(Hoy)", "Año 1", "Año 2"),
        col = c("#E74C3C", "#27AE60", "#27AE60"),
        border = "white",
        add = TRUE,
        axes = FALSE)

# Línea de referencia en cero
abline(h = 0, lwd = 2, col = "black")

# Etiquetas de valores nominales
text(barplot_result[1], flujos_nominales[1] - 1, 
     sprintf("$%.0f M\n(Inversión)", abs(flujos_nominales[1])), 
     cex = 1, col = "white", font = 2)
text(barplot_result[2], flujos_nominales[2] + 1, 
     sprintf("$%.0f M", flujos_nominales[2]), 
     cex = 1, col = "#1E8449", font = 2)
text(barplot_result[3], flujos_nominales[3] + 1, 
     sprintf("$%.0f M", flujos_nominales[3]), 
     cex = 1, col = "#1E8449", font = 2)

# Mostrar valores presentes (descontados)
text(barplot_result[2], -3, 
     sprintf("VP = $%.2f M", VP[2]), 
     cex = 0.95, col = "#27AE60", font = 3)
text(barplot_result[3], -5, 
     sprintf("VP = $%.2f M", VP[3]), 
     cex = 0.95, col = "#27AE60", font = 3)

# Fórmulas de descuento
text(barplot_result[2], -7, 
     expression(frac(11, 1.1^1)), 
     cex = 0.9, col = "gray30")
text(barplot_result[3], -9, 
     expression(frac(12, 1.1^2)), 
     cex = 0.9, col = "gray30")

# Resultado VPN
rect(xleft = 0.5, xright = 4.5, ybottom = -11.5, ytop = -10, 
     col = "#3498DB", border = "#2874A6", lwd = 2)
text(2.5, -10.75, 
     sprintf("VPN = $%.2f Millones", VPN_total), 
     cex = 1.2, col = "white", font = 2)

# Interpretación
if (VPN_total > 0) {
  interpretacion <- "✓ ACEPTAR (VPN > 0)"
  color_interp <- "#27AE60"
} else if (VPN_total < 0) {
  interpretacion <- "✗ RECHAZAR (VPN < 0)"
  color_interp <- "#E74C3C"
} else {
  interpretacion <- "INDIFERENTE (VPN = 0)"
  color_interp <- "#F39C12"
}

text(2.5, 13, interpretacion, cex = 1.1, col = color_interp, font = 2)

# Nota sobre tasa de descuento
text(2.5, -12.5, 
     "Tasa de descuento: 10% anual", 
     cex = 0.95, col = "gray30", font = 3)

dev.off()

cat("✓ Gráfico de VPN guardado en:", output_file, "\n")
