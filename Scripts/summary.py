import time
import streamlit as st
import subprocess
from footer_nose import footer_func
from navigationbar_nose import navigationbar_nose
from sidebar_nose import sidebar


st.set_page_config(layout="wide", initial_sidebar_state='auto' )

with open('/NOSE//CSS/summary.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)




def display_output_4():
    with st.container(border=True):
        header1 = """
              </style>
             <div class = "heading1">
             ...................
              </div>    
            """
        st.markdown(header1, unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Task is in progress...")
        


navigationbar_nose()

sidebar(0,0,0,0,0,1)

header="""
        <div class = "heading">
            <h2  style = "color:black; font-weight:bold; ">Summary</h2>
        </div>           
        """
st.markdown(header,unsafe_allow_html=True)  

# Main content
st.markdown("<hr style='margin:0px; height:2px; margin-bottom:40px;'>", unsafe_allow_html=True)
footer_func()

display_output_4()
