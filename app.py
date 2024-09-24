import gradio as gr
import cv2  # Import necessary libraries for OCR processing
import pytesseract

def ocr_function(image):
    # Convert the image to RGB (Gradio uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    return text

# Define the Gradio interface
interface = gr.Interface(
    fn=ocr_function,
    inputs=gr.inputs.Image(type="numpy"),
    outputs="text",
    title="OCR Web Application",
    description="Upload an image to extract text using OCR."
)

# Launch the app
if __name__ == "__main__":
    interface.launch(share=True)  # Set share=True for public link
