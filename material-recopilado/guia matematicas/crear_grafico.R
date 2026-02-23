output_file <- "images/2018_1_q2_grafico.png"
dir.create(dirname(output_file), showWarnings = FALSE, recursive = TRUE)

png(output_file, width = 6, height = 5, units = "in", res = 300)

par(mar = c(4, 4, 3, 2), bg = "white")

# Rango base extendido
x_range <- seq(-2, 10, length.out = 500)
y_range <- seq(-1, 3, length.out = 500)

# Configurar plot vacío
plot(0, 0, type="n", xlim=c(-2, 10), ylim=c(-1, 3), 
     xlab="x", ylab="y", 
     main="Región acotada por y = ln(x), y = 1-x e y = 2")
grid(col = "lightgray")

# Ejes
abline(h=0, col="black", lwd=1.5)
abline(v=0, col="black", lwd=1.5)

# Dibujar Región de Integración (entre y=0 e y=2)
y_pol <- seq(0, 2, length.out = 100)
x_left <- 1 - y_pol
x_right <- exp(y_pol)

# Ensamblamos el polígono
polygon(c(x_left, rev(x_right)), c(y_pol, rev(y_pol)), 
        col=rgb(0.2, 0.5, 0.8, alpha=0.3), border=NA)

# Curva y = ln(x) o x = e^y
x_ln <- seq(0.1, 10, length.out=500)
y_ln <- log(x_ln)
lines(x_ln, y_ln, col="blue", lwd=2)

# Recta y = 1 - x
y_recta <- 1 - x_range
lines(x_range, y_recta, col="red", lwd=2)

# Límite y = 2
abline(h=2, col="darkgreen", lwd=2, lty=2)

# Opcional: punto de intersección
points(1, 0, pch=19, col="black")
text(1, -0.2, "(1,0)", cex=0.9, font=2)

legend("bottomright", legend=c(expression(y == ln(x)), expression(y == 1-x), expression(y == 2)), 
       col=c("blue", "red", "darkgreen"), lty=c(1,1,2), lwd=2, bty="n")

dev.off()
print(paste("Image saved to:", output_file))
