
import fitz  # PyMuPDF
import os
import re

# Config
PDF_PATH = "Guia de Ejercicios ECF 1_2016.pdf"
OUTPUT_IMG_DIR = "/home/fabian/src/fundamentals/respositorio-fundamentals/material-recopilado/guia dinamica/images"
OUTPUT_TEXT_FILE = "extracted_2016_1.txt"
QUESTION_NUMBERS = [23, 24, 25]  # Based on mapping

os.makedirs(OUTPUT_IMG_DIR, exist_ok=True)

def extract_questions():
    doc = fitz.open(PDF_PATH)
    extracted_data = []

    print(f"Processing {PDF_PATH}...")
    
    for page_num, page in enumerate(doc):
        text = page.get_text("text")
        
        # Simple Logic: Iterate through target questions
        for q_num in QUESTION_NUMBERS:
            # Regex to find "Pregunta N°X" or similar
            pattern = rf"Pregunta N°\s?{q_num}"
            match = re.search(pattern, text)
            
            if match:
                print(f"Found Question {q_num} on page {page_num+1}")
                
                # Metadata
                q_data = {
                    "number": q_num,
                    "page": page_num,
                    "text": text, # Raw text for now, can refine
                    "images": []
                }

                # Extract Images on this page
                image_list = page.get_images(full=True)
                for img_index, img in enumerate(image_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    
                    image_filename = f"p{q_num}_2016_1_{img_index}.{image_ext}"
                    image_path = os.path.join(OUTPUT_IMG_DIR, image_filename)
                    
                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)
                    
                    q_data["images"].append(image_filename)
                    print(f"  Saved image: {image_filename}")

                extracted_data.append(q_data)

    # Dictionary to text format for review
    with open(OUTPUT_TEXT_FILE, "w") as f:
        for item in extracted_data:
            f.write(f"--- Question {item['number']} ---\n")
            f.write(f"Images: {item['images']}\n")
            f.write("Text Content (Raw):\n")
            f.write(item['text'])
            f.write("\n" + "="*50 + "\n")

    print(f"Extraction complete. Text saved to {OUTPUT_TEXT_FILE}")

if __name__ == "__main__":
    extract_questions()
