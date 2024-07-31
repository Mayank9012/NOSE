import streamlit as st

def footer_func():
    st.html("""
    <style>
    .footer_nose {
        position: fixed; /* Fix the footer to the bottom */
        bottom: 0; /* Stick to the bottom of the viewport */
        left: 0; /* Align to the left */
        width: 100%; /* Full width */
        background-color: #e0ece9; /* Footer background color */
        text-align: center; /* Center align text */
        padding: 10px; /* Padding for the footer */
        z-index: 78; /* Ensure the footer stays above other elements */
    }

    .logos {
        width: 4vw;
        height: 4vw;
        margin-bottom: 5px;
        display: inline-block; /* Allow logos to be side-by-side */
    }

    .foot_links {
        font-size: 1vw; 
        display: inline-block;
        color: #3d6154;
        margin-top: 10px; /* Adjust vertical spacing */
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
    st.markdown("""
    <footer class="footer_nose">
        <img class="logos" src="https://i.ibb.co/LhXxSRQ/file.png" alt="IITM">
        <img class="logos" src="https://i.ibb.co/KmqXmbR/ibse-logo-removebg-preview.png" alt="IBSE">
        <img class="logos" src="https://i.ibb.co/9hyjQpg/WSAI-logo-removebg-preview.png" alt="WSAI">
        <p class="foot_links">© 2024 IIT Madras . <a href="#" class="foot">Privacy</a> . <a href="#" class="foot">Terms</a> . <a href="#" class="foot">Documentation</a></p> 
    </footer>
    """, unsafe_allow_html=True)
