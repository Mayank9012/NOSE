import streamlit as st
import streamlit.components.v1 as components
from footer_nose import footer_func
from navigationbar_nose import navigationbar_nose
from sidebar_nose import sidebar
from dataclasses import dataclass
st.set_page_config(layout="wide", initial_sidebar_state='auto' )

with open('/NOSE/CSS/help.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    
with st.container(border=True):
	st.title("FAQs")
	st.markdown("<hr style='margin:0px; height:2px; margin-bottom:40px;'>", unsafe_allow_html=True)
	with st.expander("Question 1"):
		st.write(" ....................................")
	with st.expander("Question 2"):
		st.write(" ....................................")
	with st.expander("Question 3"):
		st.write(" ....................................")
	with st.expander("Question 4"):
		st.write(" ....................................")
	with st.expander("Question 5"):
		st.write(" ....................................")
	with st.expander("Question 6"):
		st.write(" ....................................")
	with st.expander("Question 7"):
		st.write(" ....................................")
	with st.expander("Question 8"):
		st.write(" ....................................")
st.markdown("<hr style='margin-top:70px; height:3px; width:100%; transform: translateX(0px); margin-bottom:85px;'>", unsafe_allow_html=True)

with st.container(border=True):
	st.title("Contact Us")
	st.markdown("<hr style='margin:0px; height:2px; margin-bottom:40px;'>", unsafe_allow_html=True)

footer_func()
navigationbar_nose()
