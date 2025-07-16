import streamlit as st
from PIL import Image
from ingredient_extractor import extract_ingredients_from_image
from recipe_generator import generate_recipe

st.set_page_config(page_title="Multimodal Recipe Assistant", layout="centered")
st.title("🧠 Multimodal Recipe Assistant")

uploaded_file = st.file_uploader("Upload an image of ingredients or food", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    with st.spinner("Extracting ingredients..."):
        ingredients = extract_ingredients_from_image(image)
        st.success("Ingredients detected!")
        st.write("### 🥬 Ingredients:")
        st.write(ingredients)

    with st.spinner("Generating recipe..."):
        recipe = generate_recipe(ingredients)
        st.write("### 🍳 Generated Recipe:")
        st.markdown(recipe)
