import streamlit as st

def footer_func():
    st.html("""
    <style>
    [data-testid="stAppViewBlockContainer"]{
        bottom-padding:10px;
    }
    .footer_nose {
        background-color: #e0ece9; 
        text-align: center;
        padding: 10px;
        width: 100%; 
        margin-top: 20px; /* Adjust as needed for spacing */
    }

    .logos {
        width: 4vw;
        height: 4vw;
        margin-bottom: 5px;
        display: inline-block; 
    }

    .foot_links {
        font-size: 1vw; 
        display: inline-block;
        color: #3d6154;
        margin-top: 10px; 
    }

    /* Responsive adjustments for smaller screens */
    @media (max-width: 768px) {
        .logos {
            width: 10vw;
            height: 10vw;
        }

        .foot_links {
            font-size: 2.5vw;
        }
    }
    </style>
    """)

    # Create a container for the footer
    with st.container():
        st.markdown("""
        <footer class="footer_nose">
            <img class="logos" src="https://i.ibb.co/LhXxSRQ/file.png" alt="IITM">
            <img class="logos" src="https://i.ibb.co/KmqXmbR/ibse-logo-removebg-preview.png" alt="IBSE">
            <img class="logos" src="https://i.ibb.co/9hyjQpg/WSAI-logo-removebg-preview.png" alt="WSAI">
            <p class="foot_links">© 2024 IIT Madras . <a href="#" class="foot">Privacy</a> . <a href="#" class="foot">Terms</a> . <a href="#" class="foot">Documentation</a></p> 
        </footer>
        """, unsafe_allow_html=True)
