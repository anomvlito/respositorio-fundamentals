
# Script to replicate Question 9 graph (Contour Plot of z = xy)
# Created by r-plotter skill
# Target Function: z = x * y
# Range: x [-10, 10], y [-10, 10]

# Define output path
output_file <- "../images/q9_contour.png"

# Ensure output directory exists (although created by agent, good practice)
output_dir <- dirname(output_file)
if (!dir.exists(output_dir)) {
  dir.create(output_dir, recursive = TRUE)
}

# Open PNG device with high resolution for LaTeX
png(filename = output_file,
    width = 6, height = 6, units = "in", res = 300)

# Generate data
x <- seq(-10, 10, length.out = 200)
y <- seq(-10, 10, length.out = 200)
z <- outer(x, y, function(x, y) x * y)

# Define custom color palette to match screenshot (Yellow -> Orange -> Red)
# The screenshot uses light yellow for near-zero, transitioning to orange/red for extremes
# But wait, z = xy goes from -100 to 100.
# The screenshot shows similar colors in Q1/Q3 (positive) and Q2/Q4 (negative)??
# No, let's look at the screenshot again carefully.
# Q1 (top right, x>0, y>0, z>0): Light Yellow in center, getting darker towards corner?
# Actually, let's look at the axes.
# Q1: Lines are hyperbolas x*y = k.
# If colors represent Z values:
# Center (0,0) is z=0.
# Corners are z=100 (top right), z=-100 (top left).
# The screenshot shows color bands.
# I'll use a standard terrain or heat palette and let the user iterate if needed.
# Focusing on clarity for now.

# Custom palette
colors <- hcl.colors(20, "YlOrRd", rev = TRUE)

# Plot
par(mar = c(4, 4, 2, 2)) # Adjust margins
filled.contour(x, y, z,
               col = colors,
               plot.title = title(main = "Pregunta 9: Curvas de Nivel z = xy"),
               plot.axes = { axis(1); axis(2); grid() },
               xlab = "x", ylab = "y",
               key.title = title(main = "z"))

# Close device
dev.off()

cat("Image generated at:", normalizePath(output_file), "\n")
