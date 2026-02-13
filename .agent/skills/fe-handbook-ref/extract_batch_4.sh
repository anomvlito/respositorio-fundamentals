#!/bin/bash
set -e

PDF_FILE="/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf"
OUT_DIR="resources/images"

# Extract pages 37-46 (Handbook Pages 31-40)
# PDF Page 37 = Handbook Page 31
# ...
# PDF Page 46 = Handbook Page 40

echo "Extracting pages 37-46 from $PDF_FILE..."
pdftoppm -f 37 -l 46 -png "$PDF_FILE" "$OUT_DIR/extract"

# Renaming
# pdftoppm generates extract-037.png ... extract-046.png

echo "Renaming files..."
mv "$OUT_DIR/extract-037.png" "$OUT_DIR/p31_content.png"
mv "$OUT_DIR/extract-038.png" "$OUT_DIR/p32_content.png"
mv "$OUT_DIR/extract-039.png" "$OUT_DIR/p33_content.png"
mv "$OUT_DIR/extract-040.png" "$OUT_DIR/p34_content.png"
mv "$OUT_DIR/extract-041.png" "$OUT_DIR/p35_content.png"
mv "$OUT_DIR/extract-042.png" "$OUT_DIR/p36_content.png"
mv "$OUT_DIR/extract-043.png" "$OUT_DIR/p37_content.png"
mv "$OUT_DIR/extract-044.png" "$OUT_DIR/p38_content.png"
mv "$OUT_DIR/extract-045.png" "$OUT_DIR/p39_content.png"
mv "$OUT_DIR/extract-046.png" "$OUT_DIR/p40_content.png"

echo "Batch 4 Extraction complete."
ls -l $OUT_DIR/p3*_content.png | head -n 10
ls -l $OUT_DIR/p4*_content.png | head -n 1
