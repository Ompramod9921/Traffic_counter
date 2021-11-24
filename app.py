import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import numpy as np
from PIL import Image
import streamlit as st

st.set_page_config(page_title='Deepface',page_icon='👽')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Traffic counter")
st.write("Made with ❤️ by om pramod")
st.markdown("*****")

image_file = st.file_uploader("upload photo",type=["png","jpg","jpeg"])

try :
    if image_file  is not None:
        st.image(image_file,use_column_width=True)
        image_loaded = Image.open(image_file)
        new_image = np.array(image_loaded.convert('RGB')) #converting image into array
        img = cv2.cvtColor(new_image,1) #converting the image from 3 channel image (RGB) into 1 channel image.if you don't convert the image into one channel, open-cv does it automatically.
        bbox, label, conf = cv.detect_common_objects(img)
        output_image = draw_bbox (img, bbox, label, conf) 
        if st.button("Count number of cars") :
            st.markdown("****")
            st.image(output_image,use_column_width=True)
            st.success('Number of cars in the image is '+ str(label.count('car')))
except:
    st.error("some error occured")