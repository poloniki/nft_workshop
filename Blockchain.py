import streamlit as st
from PIL import Image

image = Image.open('Blockhain1.png')
image2 = Image.open('Blockhain2.png')
image3 = Image.open('Blockhain3.png')
image4 = Image.open('Blockhain4.png')
image5 = Image.open('Blockhain5.png')

st.image(image)
st.image(image2)
st.image(image3)
st.image(image4)
st.image(image5)
