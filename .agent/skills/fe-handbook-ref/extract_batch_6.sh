#!/bin/bash
set -e

PDF_FILE="/home/fabian/src/fundamentals/respositorio-fundamentals/fe-handbook-10-1 - ECF.pdf"
OUT_DIR="resources/images"

# Extract pages 57-66 (Handbook Pages 51-60)
# PDF Page 57 = Handbook Page 51
# ...
# PDF Page 66 = Handbook Page 60

echo "Extracting pages 57-66 from $PDF_FILE..."
pdftoppm -f 57 -l 66 -png "$PDF_FILE" "$OUT_DIR/extract"

# Renaming
# pdftoppm generates extract-057.png ... extract-066.png

echo "Renaming files..."
mv "$OUT_DIR/extract-057.png" "$OUT_DIR/p51_content.png"
mv "$OUT_DIR/extract-058.png" "$OUT_DIR/p52_content.png"
mv "$OUT_DIR/extract-059.png" "$OUT_DIR/p53_content.png"
mv "$OUT_DIR/extract-060.png" "$OUT_DIR/p54_content.png"
mv "$OUT_DIR/extract-061.png" "$OUT_DIR/p55_content.png"
mv "$OUT_DIR/extract-062.png" "$OUT_DIR/p56_content.png"
mv "$OUT_DIR/extract-063.png" "$OUT_DIR/p57_content.png"
mv "$OUT_DIR/extract-064.png" "$OUT_DIR/p58_content.png"
mv "$OUT_DIR/extract-065.png" "$OUT_DIR/p59_content.png"
mv "$OUT_DIR/extract-066.png" "$OUT_DIR/p60_content.png"

echo "Batch 6 Extraction complete."
ls -l $OUT_DIR/p5*_content.png | head -n 10
ls -l $OUT_DIR/p6*_content.png | head -n 1
