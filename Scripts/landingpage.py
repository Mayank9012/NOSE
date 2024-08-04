import time
import streamlit as st
import streamlit.components.v1 as components
import webbrowser
st.set_page_config(initial_sidebar_state='auto' )
st.write("#")

with open('CSS/landingpage.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Confirmation dialog
@st.experimental_dialog("Check Status")
def pop():
    task_id = st.text_input("Enter the Task ID: ")
    st.markdown("""
        <style>

        </style>

        <a href="#?task_id={task_id}" class="btn1">
            <button type="button" class="btn">Check Status</button>
        </a>
    """, unsafe_allow_html=True)

navbar1 = """
<nav class="navigation">
    <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link" style="color: #1c3b29; font-weight: bold; font-size: 1em;">Home </a></li>
        <li class="nav-item" style="color: #034620; font-weight: bold; font-size: 1em; justify-content: center;">|</li>
        <li class="nav-item"><a href="#" class="nav-link" style="color: #1c3b29; font-weight: bold; font-size: 1em;">About</a></li>
        <li class="nav-item" style="color: #034620; font-weight: bold; font-size: 1em; justify-content: center;">|</li>
        <li class="nav-item dropdown">
            <a href="#" class="nav-link dropbtn" style="color: #1c3b29; font-weight: bold; font-size: 1em;">Help</a>
        </li>
    </ul>
</nav>
"""

with st.container():
    st.markdown(navbar1, unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("""
    <div id="section1" class="section"></div>
    <p id="welcomeText" style="color: #1c3b29;">Welcome to NoSE</p>
    <img class="logo" src="https://svgshare.com/i/17BS.svg">
    <p class="nose">Lorem ipsum dolo. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    """, unsafe_allow_html=True)

    components.html("""
    <style>
    @import url("https://fonts.googleapis.com/css?family=Raleway:900&display=swap");

    #container456 {
        position: fixed;
        width: 300px;
        height: 200px;
      
        filter: url(#threshold) blur(0px);
        top: 30px;
        left: 0;
    }

    #text1,
    #text2 {
        position: fixed;
        width: 100%;
        display: inline-block;
        font-family: "Raleway", sans-serif;
        font-size: 1.3rem;
        text-align: center;
        color: #1c3b29;
        user-select: none;
    }
    </style>
    <div id="container456">
        <span id="text1"></span>
        <span id="text2"></span>
    </div>

    <svg id="filters">
        <defs>
            <filter id="threshold">
                <feColorMatrix in="SourceGraphic" type="matrix" values="1 0 0 0 0
                                        0 1 0 0 0
                                        0 0 1 0 0
                                        0 0 0 255 -140" />
            </filter>
        </defs>
    </svg>
    <script>
    const elts = {
        text1: document.getElementById("text1"),
        text2: document.getElementById("text2")
    };

    const texts = [
        "NoSE",
        "Novel Species"
    ];

    const morphTime = 10;
    const cooldownTime = 5;

    let textIndex = texts.length - 1;
    let time = new Date();
    let morph = 10;
    let cooldown = cooldownTime;

    elts.text1.textContent = texts[textIndex % texts.length];
    elts.text2.textContent = texts[(textIndex + 1) % texts.length];

    function doMorph() {
        morph -= cooldown;
        cooldown = 0;

        let fraction = morph / morphTime;

        if (fraction > 1) {
            cooldown = cooldownTime;
            fraction = 1;
        }

        setMorph(fraction);
    }

    function setMorph(fraction) {
        elts.text2.style.filter = `blur(${Math.min(8 / fraction - 8, 100)}px)`;
        elts.text2.style.opacity = `${Math.pow(fraction, 0.4) * 100}%`;

        fraction = 1 - fraction;
        elts.text1.style.filter = `blur(${Math.min(8 / fraction - 8, 100)}px)`;
        elts.text1.style.opacity = `${Math.pow(fraction, 0.4) * 100}%`;

        elts.text1.textContent = texts[textIndex % texts.length];
        elts.text2.textContent = texts[(textIndex + 1) % texts.length];
    }

    function doCooldown() {
        morph = 0;

        elts.text2.style.filter = "";
        elts.text2.style.opacity = "100%";

        elts.text1.style.filter = "";
        elts.text1.style.opacity = "0%";
    }

    function animate() {
        requestAnimationFrame(animate);

        let newTime = new Date();
        let shouldIncrementIndex = cooldown > 0;
        let dt = (newTime - time) / 1000;
        time = newTime;

        cooldown -= dt;

        if (cooldown <= 0) {
            if (shouldIncrementIndex) {
                textIndex++;
            }

            doMorph();
        } else {
            doCooldown();
        }
    }

    animate();

    </script>
    """, height=400)

    col1, col2, col3,col4,col5 = st.columns([1, 1, 1,1,1])

    with col1:
        butn1 = st.button("Submit Query")
        if butn1:
            url = f'http://localhost:8501/'
            webbrowser.open_new_tab(url)

    with col2:
        butn = st.button("Check Status")
        if butn:
            pop()

    st.markdown("""
    <div class="scroll-down">
        <a class = "sec2" href="#section2"><div class="scroll-down1"></div></a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div id="section2" class="section"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="containercards">
    <ul id="cards">
        <li class="card" id="card1">
            <div class="card-body">
                <p style="font-size: 1.2rem; font-weight: bold; top:0;">Quality Check</p><br>
                <div class="card-content">
                    <p>NoSE is a tool to predict the novel species from the given gene sequences.</p>
                </div>
            </div>
        </li>
        <li class="card" id="card2">
            <div class="card-body">
                <p style="font-size: 1.2rem; font-weight: bold; top:0;">Genome Relatedness Index </p><br>
                <div class="card-content">
                    <p>NoSE is a tool to predict the novel species from the given gene sequences.</p>
                </div>
            </div>
        </li>
        <li class="card" id="card3">
            <div class="card-body">
                <p style="font-size: 1.2rem; font-weight: bold; top:0;">Taxanomic Classification</p><br>
                <div class="card-content">
                    <p>NoSE is a tool to predict the novel species from the given gene sequences.</p>
                </div>
            </div>
        </li>
        <li class="card" id="card4">
            <div class="card-body">
                <p style="font-size: 1.2rem; font-weight: bold; top:0;">Phylogenetic Tree</p><br>
                <div class="card-content">
                    <p>NoSE is a tool to predict the novel species from the given gene sequences.</p>
                </div>
            </div>
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)



st.markdown("<hr style='background-color: #3d6154; margin: 0; height: 4px; width: 100%; margin-top: 100px;'>", unsafe_allow_html=True)


st.markdown("""
<footer style='border-top: 5px solid darkgrey; text-align: center; margin-top: 20px;transform: translateX(0px) translateY(600px); width:100%;'>
    <p style='color: #3d6154; font-size: 15px; '>© .................</p> 
</footer>
""", unsafe_allow_html=True)


scroll_script = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var scrollDownButton = document.querySelector('.scroll-down1 a');
    var scrollSection = document.getElementById('section2');
    var loaded = false;

    function toggleScrollButton() {
        if (loaded && window.scrollY > scrollSection.offsetTop) {
            scrollDownButton.style.display = 'block';
        } else {
            scrollDownButton.style.display = 'none';
        }
    }

    window.addEventListener('scroll', toggleScrollButton);

    scrollDownButton.addEventListener('click', function(event) {
        event.preventDefault();
        var scrollAmount = scrollSection.offsetTop - (window.innerHeight * 0);
        window.scrollTo({
            top: scrollAmount,
            behavior: 'smooth'
        });
        scrollDownButton.style.display = 'none';
    });

    setTimeout(function() {
        loaded = true;
        toggleScrollButton();
    }, 1000);
});
</script>
<script>
// Script to handle adding 'in-view' class based on scroll position
document.addEventListener('scroll', function() {
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    const top = card.getBoundingClientRect().top;
    if (top <= 250) {
      card.classList.add('in-view');
    } else {
      card.classList.remove('in-view');
    }
  });
});
</script>
"""

st.markdown(scroll_script, unsafe_allow_html=True)

