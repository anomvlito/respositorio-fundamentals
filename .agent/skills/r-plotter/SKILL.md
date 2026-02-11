---
name: r-plotter
description: Skill for modeling and rendering mathematical functions and data visualizations using R. Generates R scripts to create high-quality, appropriately scaled images for LaTeX documents. Handles directory management for image assets.
---

# R Plotter Skill

## When to use this skill
**ALWAYS** use this skill when the user requests:
- To graph mathematical functions (contours, surfaces, 2D plots).
- To visualize data distributions or statistical models.
- To create high-quality images for LaTeX or other documents.
- To replicate existing graphs from screenshots using R.

## 1. Environment Setup

Ensure R is installed. If not, request installation:
```bash
sudo apt install r-base-core
```
Verify installation with `Rscript --version`.

## 2. Script Generation Protocol

1.  **Create a dedicated R script** for the specific visualization (e.g., `plot_q9.R`).
2.  **Define the Output Path**:
    -   Identify the target directory for images (e.g., `images/` or `figures/` within the LaTeX project).
    -   Ensure the directory exists or create it in the script.
3.  **Configure the Device**:
    -   Use `png()` or `pdf()` devices.
    -   **CRITICAL**: Set appropriate dimensions and resolution for LaTeX inclusion.
    -   Recommended for LaTeX: `width = 6, height = 6, units = "in", res = 300` (for PNG).
4.  **Plotting**:
    -   Use `ggplot2` for complex, layered plots or `base` graphics for simple mathematical functions if dependencies are limited.
    -   For **Contour Plots** (as in Q9): Use `filled.contour()` or `levelplot()` from `lattice`, or `geom_contour_filled()` from `ggplot2`.
5.  **Export**:
    -   Close the device with `dev.off()`.

## 3. Image Placement Strategy

-   **Standard Location**: `/material-recopilado/guia_antigua/images/` (or relative to the `.tex` file).
-   **Naming Convention**: `[question_number]_[description].png` (e.g., `q9_contour_plot.png`).
-   **LaTeX Integration**:
    ```latex
    \begin{center}
    \includegraphics[width=0.6\textwidth]{images/q9_contour_plot.png}
    \end{center}
    ```

## 4. Replicating Specific Graphs (Reverse Engineering)

-   **Analyze the Screenshot**: Identify the function type (hyperbolas, parabolas, etc.), domains, and ranges.
-   **Estimate Parameters**: Guess coefficients to match the visual curves.
-   **Iterate**: Run the script, check the output, adjust parameters until it matches the screenshot.

## 5. Example Script (Template)

```r
# Load necessary libraries (if any)
# library(ggplot2)

# Define output file
output_file <- "images/example_plot.png"
dir.create(dirname(output_file), showWarnings = FALSE, recursive = TRUE)

# Open device
png(output_file, width = 6, height = 5, units = "in", res = 300)

# Define data
x <- seq(-10, 10, length.out = 100)
y <- seq(-10, 10, length.out = 100)
grid <- expand.grid(x = x, y = y)
z <- with(grid, x * y) # Example function z = xy

# Plot
# Use a custom color palette similar to the screenshot (e.g., heat.colors)
filled.contour(x, y, matrix(z, nrow = 100),
               color.palette = function(n) hcl.colors(n, "YlOrRd", rev = TRUE),
               plot.title = title(main = "Question 9: Level Curves"),
               xlab = "x", ylab = "y")

# Close device
dev.off()
print(paste("Image saved to:", output_file))
```
