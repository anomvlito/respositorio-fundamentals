#!/bin/bash
set -e

PDF_FILE="/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf"
OUT_DIR="resources/images"

# Extract pages 17-26 (Handbook Pages 11-20)
# PDF Page 17 = Handbook Page 11
# ...
# PDF Page 26 = Handbook Page 20

echo "Extracting pages 17-26 from $PDF_FILE..."
pdftoppm -f 17 -l 26 -png "$PDF_FILE" "$OUT_DIR/extract"

# Renaming
# pdftoppm generates extract-017.png ... extract-026.png

echo "Renaming files..."
mv "$OUT_DIR/extract-017.png" "$OUT_DIR/p11_content.png"
mv "$OUT_DIR/extract-018.png" "$OUT_DIR/p12_content.png"
mv "$OUT_DIR/extract-019.png" "$OUT_DIR/p13_content.png"
mv "$OUT_DIR/extract-020.png" "$OUT_DIR/p14_content.png"
mv "$OUT_DIR/extract-021.png" "$OUT_DIR/p15_content.png"
mv "$OUT_DIR/extract-022.png" "$OUT_DIR/p16_content.png"
mv "$OUT_DIR/extract-023.png" "$OUT_DIR/p17_content.png"
mv "$OUT_DIR/extract-024.png" "$OUT_DIR/p18_content.png"
mv "$OUT_DIR/extract-025.png" "$OUT_DIR/p19_content.png"
mv "$OUT_DIR/extract-026.png" "$OUT_DIR/p20_content.png"

echo "Batch 2 Extraction complete."
ls -l $OUT_DIR/p1*_content.png | head -n 10
