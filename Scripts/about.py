import streamlit as st
import streamlit.components.v1 as components
from footer_nose import footer_func
from navigationbar_nose import navigationbar_nose
from sidebar_nose import sidebar
from dataclasses import dataclass
st.set_page_config(layout="wide", initial_sidebar_state='auto' )

with open('/NOSE/CSS/about.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
header="""
         <div class = "heading">
             <h2  style="color:black; font-size:50px; font-family:"Source Sans Pro", sans-serif; font-weight:bold;">NoSE</h2>
        </div>    

        """
st.markdown(header,unsafe_allow_html=True) 

st.markdown("<hr style='margin:0px; height:2px; margin-bottom:40px;'>", unsafe_allow_html=True)
with st.container(border=True):
	st.write("............................About............................")

footer_func()
navigationbar_nose()
