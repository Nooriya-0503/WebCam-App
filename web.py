import streamlit as st
from PIL import Image

with st.expander("Start Camera to convert image To GreyScale."):
    #Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #Creating pillow image instance
    img = Image.open(camera_image)

    #Converting img to greyscale
    grey_img = img.convert("L")

    #Displaying the image using streamlit
    st.image(grey_img)
