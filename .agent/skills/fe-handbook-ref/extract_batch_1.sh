#!/bin/bash
set -e

PDF_FILE="/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf"
OUT_DIR="resources/images"

# Extract pages 8-16 (Handbook Pages 2-10)
# PDF Page 8 = Handbook Page 2
# ...
# PDF Page 16 = Handbook Page 10

echo "Extracting pages 8-16 from $PDF_FILE..."
pdftoppm -f 8 -l 16 -png "$PDF_FILE" "$OUT_DIR/extract"

# Renaming
# pdftoppm generates extract-08.png, extract-09.png, extract-10.png ...
# We need to map them:
# extract-08.png -> p2_content.png
# extract-09.png -> p3_content.png
# extract-10.png -> p4_content.png
# ...
# extract-16.png -> p10_content.png

echo "Renaming files..."
mv "$OUT_DIR/extract-008.png" "$OUT_DIR/p2_content.png"
mv "$OUT_DIR/extract-009.png" "$OUT_DIR/p3_content.png"
mv "$OUT_DIR/extract-010.png" "$OUT_DIR/p4_content.png"
mv "$OUT_DIR/extract-011.png" "$OUT_DIR/p5_content.png"
mv "$OUT_DIR/extract-012.png" "$OUT_DIR/p6_content.png"
mv "$OUT_DIR/extract-013.png" "$OUT_DIR/p7_content.png"
mv "$OUT_DIR/extract-014.png" "$OUT_DIR/p8_content.png"
mv "$OUT_DIR/extract-015.png" "$OUT_DIR/p9_content.png"
mv "$OUT_DIR/extract-016.png" "$OUT_DIR/p10_content.png"

echo "Extraction and renaming complete."
ls -l $OUT_DIR/p*_content.png | head -n 15
