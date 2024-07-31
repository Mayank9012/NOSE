import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state='auto' )
import subprocess
from footer_nose import footer_func
from navigationbar_nose import navigationbar_nose
from sidebar_nose import sidebar


# = st.query_params["task_id"]

#if query_param is not None:
#    st.write(f"Task ID: {query_param}")
#else:
#    st.write("No task ID found in URL.")

with open('CSS/ogri.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



# Main content
@st.cache_data
def execute_task(script_path):
    result = subprocess.Popen(['bash', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = result.communicate()
    return stdout.decode(), stderr.decode()

def display_output_1():
    with st.container(border=True,height=630):
        step1 = "Average Nucleotide Identity (ANI)"
        step2 = "Average Amino Acid Identity (AAI)" if not st.session_state.get("tab2", False) else "Average Amino Acid Identity "
        step3 = "digital DNA-DNA Hybridization (dDDH)" if not st.session_state.get("tab3", False) else "digital DNA-DNA Hybridization"
        steps = [step1, step2, step3]
        tab1, tab2, tab3 = st.tabs(steps)
        with tab1:
            flag=0
            if "tab1" not in st.session_state:                             
                with st.container(border=True,height=430):
                    task_status_container = st.empty()
                    task_status_container.text("Task is in progress...")
                    stdout, stderr = execute_task('data/runani.sh')
            
                    if stderr:
                        st.text("")
                        flag=1
                        st.success("Task completed successfully!")
                        with st.container(border=True, height=300):
                            output = stderr + "\n Final output: \n" + stdout
                            st.text(output)
                    task_status_container.empty()
                    flag=1
                    if flag==1:
                        st.markdown("""
                        <style>
                            button[data-baseweb="tab"][aria-controls="tabs-bui3-tabpanel-0"] > div[data-testid="stMarkdownContainer"] > p {
                                    
                                }
                                    </style>""", unsafe_allow_html=True)
                file= open("data/task_status.txt","r")
                btn = st.download_button(
                            label="Download Summary",
                            data=file,
                            file_name="ogri_summary.tsv",
                            key = "ani",
                            mime="text/tsv"
                        )            
                st.session_state["tab1"] = True
    
        with tab2:
            if "tab2" not in st.session_state:
                with st.container(border=True,height=430):
                    task_status_container1 = st.empty()
                    task_status_container1.text("Task is in progress...")
                    stdout, stderr = execute_task('data/runaai.sh')
                    if stderr:
                        st.error(stderr)
                    else:
                        st.success("Task completed successfully!")
                        with st.container(border=True, height=300):
                            st.text(stdout)
                    task_status_container1.empty()
                file= open("data/task_status.txt","r")
                btn = st.download_button(
                        label="Download Summary",
                        data=file,
                        file_name="ogri_summary.tsv",
                        key = "aai",
                        mime="text/tsv"
                    )
                st.session_state["tab2"] = True
   
        with tab3:
            if "tab3" not in st.session_state:
                with st.container(border=True, height=430):
                    task_status_container2 = st.empty()
                    task_status_container2.text("Task is in progress...")
                    # add logic for your task
                    task_status_container2.empty()
                    st.success("Task completed successfully!")
                    with st.container(border=True, height=300):
                        st.session_state["tab3"] = True

            file= open("data/task_status.txt","r")
            btn = st.download_button(
                label="Download Summary",
                data=file,
                file_name="ogri_summary.tsv",
                key = "dDDH",
                mime="text/tsv"
            )

header="""
            <div class = "heading">
                <h2  style = "color:black; font-weight:bold; font-size:42px; position:relative; left:22px;">OGRI</h2>
            </div>    
        
        """
st.markdown(header,unsafe_allow_html=True,help="OGRI is used for the analysis of genomic relatedness between bacterial strains. It provides a comprehensive analysis of the genomic relatedness between bacterial strains using three different methods: Average Nucleotide Identity (ANI), Average Amino Acid Identity (AAI), and digital DNA-DNA Hybridization (dDDH).")  
st.markdown("<hr style='margin:0px; height:2px; margin-bottom:0px; width:99.5%; margin-left: 1px;'>", unsafe_allow_html=True)

display_output_1()

navigationbar_nose()
sidebar(0,0,0,1,0,0)
footer_func()   


