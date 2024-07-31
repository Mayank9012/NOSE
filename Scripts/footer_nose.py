import streamlit as st



def footer_func():
	# Define the CSS and HTML within a single st.html() call
	st.html("""
	<style>
	.containers1 {
	    display: flex;
	    flex-wrap: wrap;
	    /* Allow items to wrap onto the next line */
	    justify-content: space-between;
	    /* Distribute items evenly */
	    background-color: transparent;
	    padding: 10px;
	    width: 60%;
	    gap: 10px;
	    /* Gap between items */
	    position: relative;
	    left: 12%;
	    margin-bottom: 50px;
	}

	.element1,
	.element2,
	.element3 {
	    flex-basis: calc(33.3% - 10px);
	    /* Each item takes 25% width minus gap */
	    background-color: #f1f1f1;
	    text-align: center;
	    padding: 10px;
	    box-sizing: border-box;
	    /* Include padding in item width calculation */
	    border-radius: 10px;
	    width: fit-content;
	    display: flex;
	    justify-content: center;
	    font-size: 1.2em;
	}

	.containers2 {
	    font-size: 15px;
	    font-weight: bold;
	    background-color: #18382e;
	    color: white;
	    width: fit-content;
	    padding-right: 5px;
	    padding-left: 5px;
	    padding-top: 3px;
	    padding-bottom: 3px;
	    margin-left:15px;
	    border-radius: 10px;

	}
	.foot_links{
		 font-size: 1vw; 
		 display: inline-block;
	}
	.logos{
		width:4vw;
		height:4vw;
		margin-bottom: 5px;
	}
	@media (max-width: 768px) {

	    .element1,
	    .element2,
	    .element3,
	    .element4 {
		flex-basis: calc(50% - 10px);
		/* Two items per row on smaller screens */
	    }
	    .foot_links{
	    	 font-size: 2.5vw;
	    	 display: flex;
	    	} 
	    .logos{
		width:10vw;
		height:10vw;
		margin-bottom: 5px;
	}
	
	}
	</style>
	""")
	st.markdown("""
	<footer class = "footer_nose" style='z-index:78; position: fixed; border-top: 1px solid transparent; bottom:0rem; text-align: justify;  width:150%; padding: 10px; display: inline; max-height:180px; background-color:#e0ece9; grid-row:3; margin-top:200px; '>
		    <img class = "logos" src="https://i.ibb.co/LhXxSRQ/file.png" alt="IITM" style="margin-top: 10px; display: inline; margin-left:13px; margin-right:7px;">
		    <img class = "logos" src="https://i.ibb.co/KmqXmbR/ibse-logo-removebg-preview.png" alt="IBSE"  style="margin-top: 10px; display: inline; margin-left:7px; margin-right:7px;">
		    <img class = "logos" src="https://i.ibb.co/9hyjQpg/WSAI-logo-removebg-preview.png" alt="WSAI"  style="margin-top: 10px; display: inline; margin-left:7px; margin-right:10px;">
	    <p class = "foot_links" style='color: #3d6154; position: relative; transform:translatey(10px);'> © 2024 IIT Madras . <a href="#" class = "foot" >Privacy</a> . <a href= "#" class = "foot"> Terms</a> . <a href = "#" class = "foot"> Documentation</a> </p> 
	</footer>
	""", unsafe_allow_html=True)

