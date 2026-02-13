#!/bin/bash
set -e

PDF_FILE="/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf"
OUT_DIR="resources/images"

# Extract pages 27-36 (Handbook Pages 21-30)
# PDF Page 27 = Handbook Page 21
# ...
# PDF Page 36 = Handbook Page 30

echo "Extracting pages 27-36 from $PDF_FILE..."
pdftoppm -f 27 -l 36 -png "$PDF_FILE" "$OUT_DIR/extract"

# Renaming
# pdftoppm generates extract-027.png ... extract-036.png

echo "Renaming files..."
mv "$OUT_DIR/extract-027.png" "$OUT_DIR/p21_content.png"
mv "$OUT_DIR/extract-028.png" "$OUT_DIR/p22_content.png"
mv "$OUT_DIR/extract-029.png" "$OUT_DIR/p23_content.png"
mv "$OUT_DIR/extract-030.png" "$OUT_DIR/p24_content.png"
mv "$OUT_DIR/extract-031.png" "$OUT_DIR/p25_content.png"
mv "$OUT_DIR/extract-032.png" "$OUT_DIR/p26_content.png"
mv "$OUT_DIR/extract-033.png" "$OUT_DIR/p27_content.png"
mv "$OUT_DIR/extract-034.png" "$OUT_DIR/p28_content.png"
mv "$OUT_DIR/extract-035.png" "$OUT_DIR/p29_content.png"
mv "$OUT_DIR/extract-036.png" "$OUT_DIR/p30_content.png"

echo "Batch 3 Extraction complete."
ls -l $OUT_DIR/p2*_content.png | head -n 10
ls -l $OUT_DIR/p3*_content.png | head -n 1
