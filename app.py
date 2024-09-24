import gradio as gr
import cv2
import pytesseract

def ocr_function(image):
    # Convert the image to RGB (Gradio uses BGR by default)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    return text

# Define the Gradio interface with updated input syntax
interface = gr.Interface(
    fn=ocr_function,
    inputs=gr.Image(type="numpy"),  # Updated way to specify image input
    outputs="text",
    title="OCR Web Application",
    description="Upload an image to extract text using OCR."
)

# Launch the app
if __name__ == "__main__":
    interface.launch(share=True)  # Set share=True for a public link
