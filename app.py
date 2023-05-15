import streamlit as st
from sd_utils import pipe
st.title("Text to Image Generation")

prompt = st.text_area(label="Enter your prompt")
print(f"len of prompt: {len(prompt)}")
if len(prompt) > 0:
    print(f"len of prompt: {len(prompt)}")
    image = pipe(prompt).images[0]
    st.image(image, caption=f'Generated Image: {prompt}', use_column_width=True)

# image = Image.open(uploaded_file)
    # st.image(image, caption='Uploaded Image.', use_column_width=True)