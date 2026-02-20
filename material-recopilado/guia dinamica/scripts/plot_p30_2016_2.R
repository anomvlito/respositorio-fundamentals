
# Directory for images
img_dir <- "../images"
if (!dir.exists(img_dir)) {
  dir.create(img_dir, recursive = TRUE)
}

# --- Geometry Data ---
# Vertices: A(0,0) [Pivot], B(60,0), C(0,-30)
# Centroid: x_c = 20, y_c = -10

# 1. Geometry & Centroid Plot
png(file.path(img_dir, "2016_2_p30_geom.png"), width = 600, height = 400)

# Set up plot area
par(mar = c(5, 4, 4, 2) + 0.1)
plot(NA, xlim = c(-10, 70), ylim = c(-40, 10), xlab = "x [cm]", ylab = "y [cm]", main = "Geometría Inicial (Referencia Local)", asp = 1)
grid()

# Triangle
polygon(c(0, 60, 0), c(0, 0, -30), col = "lightblue", border = "black")

# Pivot
points(0, 0, col = "blue", pch = 19, cex = 1.5)
text(0, 2, "A (Pivote)", col = "blue", pos = 4)

# Centroid
points(20, -10, col = "red", pch = 19, cex = 1.5)
text(20, -10, " C (20, -10)", col = "red", pos = 4)

# Line Pivot-Centroid
segments(0, 0, 20, -10, col = "red", lty = 2)

# Annotations
text(30, 2, "b = 60 cm", pos = 3)
text(-5, -15, "h = 30 cm", pos = 2)

dev.off()

# 2. Equilibrium Plot
# Rotation angle
theta_rot_rad <- -atan2(-10, 20) - pi/2 # Rotate so vector (20,-10) aligns with (0,-1)
# Angle of (20,-10) is approx -26.56 deg. We want -90 deg. Rotation is -90 - (-26.56) = -63.44 deg.

rotate_pt <- function(x, y, angle_rad) {
  x_new <- x * cos(angle_rad) - y * sin(angle_rad)
  y_new <- x * sin(angle_rad) + y * cos(angle_rad)
  return(list(x = x_new, y = y_new))
}

# Vertices
v1 <- rotate_pt(0, 0, theta_rot_rad)
v2 <- rotate_pt(60, 0, theta_rot_rad)
v3 <- rotate_pt(0, -30, theta_rot_rad)

# Centroid
c_rot <- rotate_pt(20, -10, theta_rot_rad)

# Plot
png(file.path(img_dir, "2016_2_p30_eq.png"), width = 600, height = 600)

par(mar = c(5, 4, 4, 2) + 0.1)
# Calculate limits based on rotated points
xs <- c(v1$x, v2$x, v3$x, c_rot$x, 0)
ys <- c(v1$y, v2$y, v3$y, c_rot$y, -50)
plot(NA, xlim = range(xs) + c(-10, 10), ylim = range(ys) + c(-10, 10), xlab = "x [cm]", ylab = "y [cm]", main = "Equilibrio (Centroide alineado con vertical)", asp = 1)
grid()

# Vertical Line
abline(v = 0, col = "gray", lty = 2)
# Horizontal Line
abline(h = 0, col = "gray", lty = 2)

# Rotated Triangle
polygon(c(v1$x, v2$x, v3$x), c(v1$y, v2$y, v3$y), col = "lightgreen", border = "black")

# Pivot
points(0, 0, col = "blue", pch = 19, cex = 1.5)
text(0, 0, "Pivote", col = "blue", pos = 3)

# Centroid
points(c_rot$x, c_rot$y, col = "red", pch = 19, cex = 1.5)

# Line Pivot-Centroid (Vertical)
segments(0, 0, c_rot$x, c_rot$y, col = "red", lwd = 2)
text(c_rot$x + 2, c_rot$y, "Vertical\n(Gravedad)", col = "red", pos = 4, cex = 0.8)

# Angle alpha (between cathetus b and vertical)
# Cathetus b is from A(0,0) to B_rot(v2).
# Vertical is (0, -1). 
# Angle of AB_rot:
angle_AB <- atan2(v2$y, v2$x) * 180 / pi
# Angle vertical is -90. Diff is | -90 - angle_AB |.
# Wait, previous solution said: "cateto b hace un ángulo de 63.4 con la horizontal".
# Here horizontal is 0. Vertical is -90. 
# Let's verify.

dev.off()
