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

with open('CSS/ogri1.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


header="""
            <div class = "heading">
                <h2  style = "color:black; font-weight:bold; font-size:42px; position:relative; left:22px;">OGRI</h2>
            </div>    
        
        """
st.markdown(header,unsafe_allow_html=True,help="OGRI is used for the analysis of genomic relatedness between bacterial strains. It provides a comprehensive analysis of the genomic relatedness between bacterial strains using three different methods: Average Nucleotide Identity (ANI), Average Amino Acid Identity (AAI), and digital DNA-DNA Hybridization (dDDH).")  
st.markdown("<hr style='margin:0px; height:2px; margin-bottom:0px; width:100%; margin-left: 1px;'>", unsafe_allow_html=True)



@st.cache_resource
def execute_task(script_path):
    result = subprocess.Popen(['bash', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = result.communicate()
    return stdout.decode(), stderr.decode()

def display_output_1():
    with st.container(border=True,height=495):
        with st.container(border=True):
            col1,col2 = st.columns([1,4])
            with col1:
                st.markdown("""<div class = "heading">
                    <h2  style = "color:black; font-weight:bold; font-size:22px; position:relative; justify-content:center; text-align:center; align-items:center;">Average Nucleotide Identity (ANI)</h2>
                </div> """, unsafe_allow_html=True)
            with col2:
                with st.container(border=False,height=185):
                        task_status_container = st.empty()
                        task_status_container.text("Task is in progress...")
                        stdout, stderr = execute_task('data/runani.sh')
                
                        if stderr:
                            st.text("")
                            flag=1
                            st.success("Task completed successfully!")
                            with st.container(border=False,height=35):
                                output = stdout
                                st.text(output)
                        task_status_container.empty()
                        file= open("data/task_status.txt","r")
                        btn = st.download_button(
                                    label="Download Summary",
                                    data=file,
                                    file_name="ogri_summary.tsv",
                                    key = "ani",
                                    mime="text/tsv"
                                )
        with st.container(border=True):
            col3,col4 = st.columns([1,4])
            with col3:
                st.markdown("""<div class = "heading">
                    <h2  style = "color:black; font-weight:bold; font-size:22px; position:relative; justify-content:center; text-align:center; align-items:center;"> Average Amino Acid Identity (AAI) </h2>
                </div> """, unsafe_allow_html=True)
            with col4: 
                with st.container(border=False,height=185):
                        task_status_container1 = st.empty()
                        task_status_container1.text("Task is in progress...")
                        stdout, stderr = execute_task('data/runaai.sh')
                        if stderr:
                            st.error(stderr)
                        else:
                            st.success("Task completed successfully!")
                            with st.container(border=False, height=35):
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
                
                 
display_output_1()
navigationbar_nose()
sidebar(0,0,1,0,0,0)
st.markdown("""<style>
        .stStepCircle {
            background-color: #023b2a;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            border: 4px solid #fff;
            /* Add white border */
            display: flex;
            margin-bottom: 2vh;
            transform: translateX(-40px) translateY(-621.9px);
            justify-content: left;
            align-items: left;
            color: white;
            font-weight: bold;
        }

        .stStepCircle1 {
            background-color: #023b2a;
            width: 4vh;
            height: 4vh;
            border-radius: 50%;
            display: inline-block;
            margin-bottom: 1vh;
            transform: translateX(-45px) translateY(-977px) !important;
            justify-content: left;
            align-items: left;
            color: white;
            font-weight: bold;
        }

        .stStepCircle2 {
            background-color: #023b2a;
            width: 4vh;
            height: 4vh;
            border: 4px solid #fff;
            border-radius: 50%;
            display: flex;
            margin-bottom: 1vh;
            transform: translateX(35.2px) translateY(-271.9px) !important;
            justify-content: center;
            align-items: left;
            color: white;
            text-wrap: wrap;
            font-weight: bold;
            font-size: 0.9rem;
        }
        .image{
                transform: translateY(-9.78px) !important;
        }
        .index{
                transform: translateY(-5px);
        }
        .steps{
               transform: translateY(-1001%) translateX(29%);
        }

        </style> """, unsafe_allow_html=True)


footer_func()   
