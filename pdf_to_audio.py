import os
import pyttsx3
from PyPDF2 import PdfReader

# Get the current script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Combine the script directory with the PDF file name
pdf_file_path = os.path.join(script_dir, '5AMClub-RobinSharma.pdf')

pdfreader = PdfReader(pdf_file_path)

# Initialize pyttsx3
speaker = pyttsx3.init()


# Create a variable to store the entire book text
book_text = ""

# iterating through each page in the book and cleaning the text of each page
# append to book text
for page in pdfreader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    book_text += clean_text + " "

# Save the entire book text to a single MP3 file
speaker.save_to_file(book_text, '5AMClub.mp3')
speaker.runAndWait()

speaker.stop()
