from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
import streamlit as st
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model=genai.GenerativeModel("gemini-pro")

def generate_product_description(product_attributes):
    # Construct the prompt as a string
    prompt_text = f"Write a compelling product description for a product with the following attributes: {product_attributes}."
    try:
        # Call the generate_text function with the prompt
        response = model.generate_content(prompt_text)
        
        # Check if the response contains some text
        if response.text:
            # Extract and return the generated text 
            return response.text
        else:
            return "No description generated."
    except Exception as e:
        return f"An error occurred: {e}"
    
import streamlit as st
st.title("Product Description Generator")

# Input fields for product attributes
name = st.text_input("Product Name")
product_type = st.text_input("Product Type")
material = st.text_input("Material")
color = st.text_input("Color")
size = st.text_input("Size")
price = st.number_input("Price", min_value=0.0, format="%.2f")

# Button to generate description
if st.button("Generate Description"):
    product_attributes = {
        "name": name,
        "type": product_type,
        "material": material,
        "color": color,
        "size": size,
        "price": price
    }
    
    description = generate_product_description(product_attributes)
    st.subheader("Generated Product Description")
    st.write(description)
            
        

