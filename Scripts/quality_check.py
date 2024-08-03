import time
import streamlit as st
import subprocess
from footer_nose import footer_func
from navigationbar_nose import navigationbar_nose
from sidebar_nose import sidebar

st.set_page_config(layout="wide", initial_sidebar_state='auto' )

with open('CSS/quality_check.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def display_output_0():
    with st.container(border=True):
        header1 = """
             <div class = "heading1">
             Title
              </div>    
            """
        st.markdown(header1, unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("Task is in progress...")
        file= open("data/task_status.txt","r")
        btn = st.download_button(
                label="Download Summary",
                data=file,
                file_name="16stree_summary.tsv",
                mime="text/tsv"
            )

header="""
        <div class = "heading">
            <h2  style = "color:black; font-weight:bold; ">Quality Check</h2>
        </div>           
        """
st.markdown(header,unsafe_allow_html=True, help="Quality Check")  

# Main content
st.markdown("<hr style='margin:0px; height:2px; margin-bottom:40px;'>", unsafe_allow_html=True)

display_output_0()
navigationbar_nose()
sidebar(0,1,0,0,0,0)
footer_func()
