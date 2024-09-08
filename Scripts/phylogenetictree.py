import time
import os
import streamlit as st
import subprocess
from footer_nose import footer_func
from navigationbar_nose import navigationbar_nose
from sidebar_nose import sidebar
from dataclasses import dataclass
st.set_page_config(layout="wide", initial_sidebar_state='auto' )
import newick
from newick import loads
from streamlit_image_zoom import image_zoom
from PIL import Image
from phytreeviz import TreeViz, load_example_tree_file


def next16s(): st.session_state.counter1 += 1
def prev16s(): st.session_state.counter1 -= 1
if 'counter1' not in st.session_state: st.session_state.counter1 = 0

def nextwgs(): st.session_state.counter2 += 1
def prevwgs(): st.session_state.counter2 -= 1
if 'counter2' not in st.session_state: st.session_state.counter2 = 0

@dataclass
class AnnotatedImage16stree:
    '''
    Dataclass to store an image with an id and an annotation
    '''
    id: int
    annotation: str = ""  # Added type annotation for clarity
    
    def __post_init__(self):
        self.url = f"Trees/16STree/file_{self.id}.newick"  # Assuming images are named like image_1.jpg, image_2.jpg, etc.
        if not os.path.exists(self.url):
            raise ValueError(f"File not found: {self.url}")
@dataclass
class AnnotatedImagewgstree:
    '''
    Dataclass to store an image with an id and an annotation
    '''
    id: int
    annotation: str = ""  # Added type annotation for clarity
    
    def __post_init__(self):
        self.url = f"Trees/WGSTree/image_{self.id}.png"  # Assuming images are named like image_1.jpg, image_2.jpg, etc.
        if not os.path.exists(self.url):
            raise ValueError(f"Image file not found: {self.url}")


with open('CSS/phylogenictree.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def display_output_3():
    with st.container(border=True):
        type1 = "16S Tree"
        type2 = "WGS Tree"
        
        tab1, tab2 = st.tabs([type1, type2])
        
        with tab1:
            with st.container(border=True):
                    def read_file_content(file_path):
                        with open(file_path, 'r') as file:
                            content = file.read()
                        return content

                    if "trees" not in st.session_state:
                        trees = [AnnotatedImage16stree(id=i) for i in range(1,5)]
                        st.session_state.trees = trees

                    else: 
                        trees = st.session_state.trees

                    n_trees = len(trees)

                    # App layout
                    download = trees[st.session_state.counter1%n_trees]
                    download_file = download.url
                    download_data = read_file_content(download_file)
                    name = "file_"+str((st.session_state.counter1%n_trees)+1)+".svg"
                    container = st.empty()
                    cols = st.columns(3)
                    with cols[2]: st.button("Next Species ➡️", on_click=next16s,key="type1", use_container_width=True)
                    with cols[1]:st.download_button(
                            label="Download Tree",
                            data=download_data,
                            file_name=name,
                            key = "16stree",
                            mime="png/img",
                            use_container_width=True
                        )
                    with cols[0]: st.button("⬅️ Previous Species", on_click=prev16s,key ="type12" , use_container_width=True)    
                    
                    # Fill layout
                    with container.container():
                        ## Display image
                        with st.container(border=True,height=470):
                            # Load the tree from the Newick string
                            #tree = newick.loads(download_data)[0]
                            #st.code(f'\u200E{tree.ascii_art()}')
                            #st.image(img.url, use_column_width=True)
                            
                            tree_file = load_example_tree_file(download.url)
                            tv = TreeViz(tree_file)
                            tv.show_branch_length(color="red")
                            tv.show_confidence(color="blue")
                            tv.show_scale_bar()
                            
                            tv.savefig(name, dpi=300)
                            st.image(name,use_column_width=True)

        with tab2:
            with st.container(border=True):
                    
                    def read_file_content(file_path):
                        with open(file_path, 'r') as file:
                            content = file.read()
                        return content
                    
                    if "wgs" not in st.session_state:
                        wgs = [AnnotatedImagewgstree(id=i) for i in range(1,5)]
                        st.session_state.wgs = wgs

                    else: 
                        wgs = st.session_state.wgs

                    n_wgs = len(wgs)

                    downloadwgs = wgs[st.session_state.counter2%n_wgs]
                    download_wgsdata = open(downloadwgs.url,"rb")
                    wgsname = "file_"+str((st.session_state.counter2%n_wgs)+1)+".png"
                    # App layout
                    container = st.empty()
                    cols = st.columns(3)
                    with cols[2]: st.button("Next Species ➡️", on_click=nextwgs, use_container_width=True)
                    with cols[1]:st.download_button(
                            label="Download Tree",
                            data=download_wgsdata,
                            file_name = wgsname,
                            key = "wgstree",
                            mime = "image/png",
                            use_container_width=True
                        )
                    with cols[0]: st.button("⬅️ Previous Species", on_click=prevwgs, use_container_width=True)    
                    
                    # Fill layout
                    with container.container():
                        ## Select image based on the current counter
                        wgstree = wgs[st.session_state.counter2%n_wgs]

                        ## Display image
                        with st.container(border=True,height=470):
                            image = Image.open(wgstree.url)
                            image_zoom(image, mode="dragmove", size = 1270,zoom_factor=4.0, increment=0.2)

        

header="""
        <div class = "heading">
            <h2  style = "color:black; font-weight:bold;">Phylogenic Trees</h2>
        </div>           
        """
st.markdown(header,unsafe_allow_html=True,help="Phylogenic Trees are used to show the evolutionary relationships among various species or organisms. It is a branching diagram or a tree showing the inferred evolutionary relationships among various biological species based upon similarities and differences in their physical or genetic characteristics.")  

# Main content
st.markdown("<hr style='margin:0px; height:2px; margin-bottom:20px;'>", unsafe_allow_html=True)
display_output_3()

footer_func()
navigationbar_nose()


sidebar(0,0,0,0,1,0)
