import fitz
import sys

def split_large_pdf(input_pdf, output_pdf):
    # Standard letter size dimensions
    letter_width = 612   # 8.5 inches in points (1 inch = 72 points)
    letter_height = 792  # 11 inches in points
    
    # Open the input PDF
    doc = fitz.open(input_pdf)
    new_doc = fitz.open()
    
    for page in doc:
        # Resize the page to match letter width while maintaining aspect ratio
        current_width = page.rect.width
        current_height = page.rect.height
        
        new_height = int(current_height * (letter_width / current_width))
        
        new_page = new_doc.new_page(width=letter_width, height=new_height)
        
        new_page.show_pdf_page(
            fitz.Rect(0, 0, letter_width, new_height),  # Destination rectangle
            doc, 
            page.number
        )
    
    # Save and close the new document
    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()

def split_large_resized_pdf(input_pdf, output_pdf):
    letter_width = 612
    letter_height = 792
    
    doc = fitz.open(input_pdf)
    new_doc = fitz.open()
    
    for page in doc:
        width, height = page.rect.width, page.rect.height
        
        num_splits = -(-height // letter_height)  # Ceiling division
        
        for i in range(int(num_splits)):
            top = i * letter_height
            bottom = min((i + 1) * letter_height, height)
            
            new_page = new_doc.new_page(width=letter_width, height=letter_height)
            e 
            clip_rect = fitz.Rect(0, top, letter_width, bottom)

            new_page.show_pdf_page(
                fitz.Rect(0, 0, letter_width, letter_height),  # Destination rectangle
                doc, 
                page.number, 
                clip=clip_rect
            )

    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split.py input.pdf output.pdf")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    
    # Resize the PDF to letter width
    resized_pdf = f"{output_pdf}_resized.pdf"
    split_large_pdf(input_pdf, resized_pdf)
    
    # Split the resized PDF
    split_large_resized_pdf(resized_pdf, output_pdf)