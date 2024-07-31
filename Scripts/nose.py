import streamlit as st
st.set_page_config(initial_sidebar_state='auto', layout="wide")
import re
import os
import uuid
from footer_nose import footer_func
from navigationbar_nose import navigationbar_nose
from sidebar_nose import sidebar   



with open('/NOSE/CSS/nosepy.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Generate task ID
sequence_number = 0
def generate_task_id():
    return str(uuid.uuid4())

#confirmation dialog
@st.experimental_dialog("Confirmation")
def pop(task_id):
    st.success("Your query is submitted successfully")
    st.write(f"Your Job-ID is {task_id}")
    st.link_button("Check Status", f"http://192.168.1.4:8503?task_id={task_id}")

 #validate email               
def validate_email(email):
    pattern = r'^\S+@\S+\.\S+$'
    if re.match(pattern, email):
        return True
    else:
        return False
            


# Main function
with open('/NOSE/data/data.txt', 'r') as file:
    # Read each line and strip whitespace (including newline characters)
    lines = file.readlines()

running_jobs = int(lines[0].strip())
queued_jobs = int(lines[1].strip())
jobs_done = int(lines[2].strip())
st.markdown(f'''<div class="containers1">
                    <div class="element1">
                        <b>Runnning Jobs</b>
                        <div class = "containers2">{running_jobs}</div>
                    </div>
                    <div class="element2">
                        <b>Queued Jobs</b>
                        <div class = "containers2">{queued_jobs}</div>
                    </div>
                    <div class="element3">
                        <b>Jobs Processed</b>
                        <div class = "containers2">{jobs_done}</div> 
                    </div>
            </div>''', unsafe_allow_html=True)         

with st.container(border=True):
       
    heading="""
            <div class = "title">
                <h2 style = "position:relative; right:1px;" >Submit your query</h2>
            </div>    

            """
    col3,col4 = st.columns([1,1])
    with col3:
        st.markdown(heading,unsafe_allow_html=True)
    with col4:  
        with open("/home/mayank/NoSE/Files/Ci.fasta", "rb") as file:
            st.download_button(label="Load sample data", data = file,file_name="sample_query.fasta", type="primary")    
    # Main content
    st.markdown("<hr style='margin-top: 0px; height:2px; margin-bottom:40px; width:58.1vw; margin-right:15px;'>", unsafe_allow_html=True)
    def create_task_folder(task_id):
        # Create folder with task_id
        os.makedirs(task_id)
        
        # Create folder for input files
        os.makedirs(os.path.join(task_id, "input_files"))
        
        # Create file to store chosen checkbox id and emailid
        with open(os.path.join(task_id, "details.txt"), "w") as f:
            f.write(f"\nEmail ID: {email}\n")

    

    with st.form("query"):
        st.markdown("<b style = 'font-size:20px;'>Query file(s)*</b>", unsafe_allow_html=True)
        query_files = st.file_uploader("", type=["fasta","fna","fa"], accept_multiple_files=True)

        st.markdown("<hr style='margin-top:20px; margin-bottom:10px; background-color: transparent;'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<b style = 'font-size:20px; margin-top: 10px;'>Extra Features</b>", unsafe_allow_html=True)
            checkbox1 = st.checkbox("Feature 1",key="Feature 1")
            checkbox2 = st.checkbox("Feature 2",key="Feature 2")
            checkbox3 = st.checkbox("Feature 3",key="Feature 3")

        with col2:
            st.markdown("<b style = 'font-size:20px;margin-top: 10px;'>Email Address*</b>", unsafe_allow_html=True)
            email = st.text_input("", placeholder="abc@gmail.com")
        submit = st.form_submit_button("Submit")
            
        if submit:
            if not query_files or not email:
                st.error("Please fill in all required fields")
            else:
                @st.cache_resource
                def write_to_file(completed):
                    with open(completed, 'w') as f:
                        f.write('1\n')
                write_to_file("completed.txt")
                # Create a unique task ID
                task_id = generate_task_id()
                    
                # Create task folder
                create_task_folder(task_id)
                    
                # Move uploaded query files to the input_files folder
                for idx, file in enumerate(query_files):
                    file_path = os.path.join(task_id, "input_files", f"query_file_{idx}.fasta")
                    with open(file_path, "wb") as f:
                        f.write(file.getvalue())
                    
                pop(task_id)



sidebar(1,0,0,0,0,0)    

navigationbar_nose()
footer_func()
