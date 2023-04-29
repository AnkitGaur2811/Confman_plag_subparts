# ====================================== Imports ================================================
import os
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# ====================================== Functions ==============================================

def folder_traverser (folder_path):
    i=0
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            text = pdf_to_string(file_path)
            text = remove_stop_words(text)
            vector = string_to_vector(text)
            # print(vector)
            i+=1
            print(i)


def pdf_to_string(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader =  PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def remove_stop_words(text):
    
    stop_words = set(stopwords.words('english'))  # Set the desired language for stop words
    
    # Tokenize the text into individual words
    words = word_tokenize(text)
    
    # Remove stop words from the text
    filtered_words = [word for word in words if word.casefold() not in stop_words]
    
    # Reconstruct the text without stop words
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text

def string_to_vector(input_string):
    # Create an instance of the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit the vectorizer on the input string
    vectorizer.fit([input_string])
    
    # Transform the input string to a vector representation
    vector = vectorizer.transform([input_string])
    
    # Return the vector representation
    return vector

def prerequsit():
    nltk.download('stopwords')
    nltk.download('punkt')
# ======================================= Main ==================================================

folder_path = "Data saver folder"
prerequsit()
folder_traverser(folder_path)
