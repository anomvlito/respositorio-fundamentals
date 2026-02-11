
# Script to generate contour plots for Question 9 alternatives
# A) z = 1 - 2x^2 + 4y^2
# C) z = (x + y)^2
# D) z = x / y

# Set output directory
output_dir <- "../images"
if (!dir.exists(output_dir)) dir.create(output_dir, recursive = TRUE)

# Data range
x <- seq(-10, 10, length.out = 200)
y <- seq(-10, 10, length.out = 200)

# Colors
colors <- hcl.colors(20, "YlOrRd", rev = TRUE)

# ---- Plot A: z = 1 - 2x^2 + 4y^2 ----
png(filename = file.path(output_dir, "q9_alt_a.png"), width = 6, height = 6, units = "in", res = 300)
z_a <- outer(x, y, function(x, y) 1 - 2*x^2 + 4*y^2)
par(mar = c(4, 4, 3, 2))
filled.contour(x, y, z_a, col = colors,
               plot.title = title(main = "a) z = 1 - 2x^2 + 4y^2"),
               plot.axes = { axis(1); axis(2); grid() },
               xlab = "x", ylab = "y")
dev.off()

# ---- Plot C: z = (x + y)^2 ----
png(filename = file.path(output_dir, "q9_alt_c.png"), width = 6, height = 6, units = "in", res = 300)
z_c <- outer(x, y, function(x, y) (x + y)^2)
par(mar = c(4, 4, 3, 2))
filled.contour(x, y, z_c, col = colors,
               plot.title = title(main = "c) z = (x + y)^2"),
               plot.axes = { axis(1); axis(2); grid() },
               xlab = "x", ylab = "y")
dev.off()

# ---- Plot D: z = x / y ----
png(filename = file.path(output_dir, "q9_alt_d.png"), width = 6, height = 6, units = "in", res = 300)
z_d <- outer(x, y, function(x, y) {
  res <- x / y
  res[abs(res) > 10] <- NA  # Limit z-range for better visualization
  return(res)
})
par(mar = c(4, 4, 3, 2))
filled.contour(x, y, z_d, col = colors,
               plot.title = title(main = "d) z = x / y"),
               plot.axes = { axis(1); axis(2); grid() },
               xlab = "x", ylab = "y")
dev.off()

cat("Generated plots: q9_alt_a.png, q9_alt_c.png, q9_alt_d.png\n")
