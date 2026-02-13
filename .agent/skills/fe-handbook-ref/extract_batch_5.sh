#!/bin/bash
set -e

PDF_FILE="/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf"
OUT_DIR="resources/images"

# Extract pages 47-56 (Handbook Pages 41-50)
# PDF Page 47 = Handbook Page 41
# ...
# PDF Page 56 = Handbook Page 50

echo "Extracting pages 47-56 from $PDF_FILE..."
pdftoppm -f 47 -l 56 -png "$PDF_FILE" "$OUT_DIR/extract"

# Renaming
# pdftoppm generates extract-047.png ... extract-056.png

echo "Renaming files..."
mv "$OUT_DIR/extract-047.png" "$OUT_DIR/p41_content.png"
mv "$OUT_DIR/extract-048.png" "$OUT_DIR/p42_content.png"
mv "$OUT_DIR/extract-049.png" "$OUT_DIR/p43_content.png"
mv "$OUT_DIR/extract-050.png" "$OUT_DIR/p44_content.png"
mv "$OUT_DIR/extract-051.png" "$OUT_DIR/p45_content.png"
mv "$OUT_DIR/extract-052.png" "$OUT_DIR/p46_content.png"
mv "$OUT_DIR/extract-053.png" "$OUT_DIR/p47_content.png"
mv "$OUT_DIR/extract-054.png" "$OUT_DIR/p48_content.png"
mv "$OUT_DIR/extract-055.png" "$OUT_DIR/p49_content.png"
mv "$OUT_DIR/extract-056.png" "$OUT_DIR/p50_content.png"

echo "Batch 5 Extraction complete."
ls -l $OUT_DIR/p4*_content.png | head -n 10
ls -l $OUT_DIR/p5*_content.png | head -n 1
