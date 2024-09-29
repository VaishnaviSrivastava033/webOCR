import cv2
import pytesseract
import numpy as np

# Define the path to the Tesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Dell\Tesseract-OCR\tesseract.exe'  

def preprocess_image(image):
    """Convert image to grayscale and apply thresholding for better OCR results."""
    # Convert to grascale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to get a binary image
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    return thresh

def ocr_image(image):
    """
    Perform OCR on the provided image.
    - Accepts: Image in numpy array format.
    - Returns: Extracted text as a string.
    """
    try:
        # Preprocess the image 
        preprocessed_image = preprocess_image(image)
        
        # Extract text from the image using pytesseract
        text = pytesseract.image_to_string(preprocessed_image)
        
        return text
    except Exception as e:
        return f"Error occurred during OCR: {str(e)}"

def search_keyword(text, keyword):
    """
    Search for a keyword in the extracted text.
    - Accepts: Extracted text and a keyword to search for.
    - Returns: Message indicating if the keyword was found or not.
    """
    if keyword.lower() in text.lower():
        return f"Keyword '{keyword}' found in the extracted text!"
    else:
        return f"Keyword '{keyword}' not found."

# Test functions 
if __name__ == "__main__":
    # Example: Load an image from file 
    image_path = 'sample_image.jpg'  # Change to an actual image path for testing
    image = cv2.imread(image_path)
    
    # Performing OCR
    extracted_text = ocr_image(image)
    print("Extracted Text:", extracted_text)
    
    # Keyword search example
    keyword = "example"  # Replace with the actual keyword to search for
    search_result = search_keyword(extracted_text, keyword)
    print(search_result)
