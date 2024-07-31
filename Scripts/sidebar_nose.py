import streamlit as st

def sidebar(step1, step2, step3, step4, step5, step6):
    st.markdown("""
    <style>
        [data-testid=stSidebar] button[title="View fullscreen"] {
            visibility: hidden;
        }

        [data-testid="collapsedControl"] {
            transform: translateY(25px);
        }

        .stProgress {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 50px;
            transform: translateX(-50%) translateY(50%);
        }

        .stProgress>div {
            display: flex;
            justify-content: space-between;
            /* Spread the progress circles evenly */
            align-items: center;
            /* Center vertically */
            width: 450px;
            height: 150px;
            /* Adjust width of the progress bar */
        }

        .stProgress>div>div {
            width: 1450px;
            /* Adjust width of each progress circle */
            transform: translateX(-265px) translateY(205px);
        }

        .stProgress>div>div>div {
            background-color: #cac1c3;
            transform: rotate(90deg);
            justify-content: center;
            width: 620px;
        }

        .stProgress>div>div>div>div {
            background-color: #69ffd2;
        }

        .stStepCircle {
            background-color: #023b2a;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            border: 4px solid #fff;
            /* Add white border */
            display: flex;
            margin-bottom: 30px;
            transform: translateX(-40px) translateY(-121.9px);
            justify-content: left;
            align-items: left;
            color: white;
            font-weight: bold;
        }

        .stStepCircle1 {
            background-color: #023b2a;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: inline-block;
            margin-bottom: 30px;
            transform: translateX(-45px) translateY(-197px);
            justify-content: left;
            align-items: left;
            color: white;
            font-weight: bold;
        }

        .stStepCircle2 {
            background-color: #023b2a;
            width: 39px;
            height: 39px;
            border: 4px solid #fff;
            border-radius: 50%;
            display: flex;
            margin-bottom: 39px;
            transform: translateX(24px) translateY(-197.9px);
            justify-content: center;
            align-items: left;
            color: white;
            text-wrap: wrap;
            font-weight: bold;
            font-size: 1.2em;
        }

        [data-testid=stSidebar] {
            background-color: #016a4f;
            overflow-x: hidden;
            z-index: 200;
            
        }

        [data-testid=stSidebarContent] {
            background-color: #016a4f;
            overflow-x: hidden;
            padding-top: 60px;
            padding-bottom: 0px;
        }

        [data-testid=stSidebar] [data-testid=stImage] {
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-top: 0px;
            transform: translateY(-30%) translateX(0%);
            width: 100%;
        }

        .stContainer {
            background-color: grey;
        }

        [data-testid="stSidebarCollapseButton"] {
            display: none;
        }

        [data-testid="stToolbar"] {
            display: none;
        }

        [data-testid="stHeader"] {
            display: none;
        }

        [data-testid="stSidebarHeader"] {
            display: none;
        }

        section[data-testid="stSidebar"][aria-expanded="true"] {
            height: 100% !important;
            width: 390px !important;
            bottom: 10%;
        }

        section[data-testid="stSidebar"][aria-expanded="false"] {
            height: 100% !important;
            width: 390px !important;
            bottom: 10%;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        def read_from_file(filename):
            with open(filename, 'r') as f:
                lines = f.readlines()
                return [line.strip() for line in lines]

        values = read_from_file('data/completed.txt')
        completed_step1, completed_step2, completed_step3, completed_step4, completed_step5, completed_step6 = values
        st.image("Images/nose1.svg",
                 caption='',
                 width=350,
                 use_column_width=False,
                 clamp=False,
                 channels='RGB')

        steps_link = ["http://localhost:8501", "http://localhost:8502", "http://localhost:8503", "http://localhost:8504", "http://localhost:8505", "http://localhost:8501"]

        progress = st.progress(0)

        # Function to generate step circle HTML
        def generate_step_circle(step_name, step_index, completed_step, step_active):
            # Initialize circle_html with an empty string

            # Remove underscores from step_name
            step_name_display = step_name.replace("_", " ")

            checked_color = "white" if not step_active else "#FFC362"

            if completed_step == '1':
                circle_html = f"""
                <div class="stStepCircle1" style="display: inline;">
                    <p style="transform: translateY(-480%) translateX(29%); font-weight:bold; font-size:1.1rem;">
                    <a href="{steps_link[i]}" style="color:{checked_color}; text-decoration:none;" target="_self">{step_name_display}</a>
                    </p>
                </div>
                <div class="stStepCircle2" style="color:{checked_color};"><p style="position:relative; transform: translateX(-0.5px) translateY(-1.751px);"><img src="https://svgshare.com/i/17pL.svg" width="35" height="35"></p></div>
                """
                return circle_html
            else:
                circle_html = f"""
                <div class="stStepCircle1" style="display: inline;">
                    <p style="transform: translateY(-480%) translateX(29%); font-weight:bold; font-size:1.1rem;">
                    <a href="{step_name}" style="color:{checked_color}; text-decoration:none;" target="_self">{step_name_display}</a>
                    </p>
                </div>
                <div class="stStepCircle2" style="color:{checked_color};">{step_index}</div>
                """
                return circle_html

        # Mapping steps to their respective conditions and progress
        step_conditions = [
            (step1, "Submit_Query", completed_step1),
            (step2, "Quality_Check", completed_step2),
            (step3, "Taxanomic_Classification", completed_step3),
            (step4, "Genome_Relatednss_Index", completed_step4),
            (step5, "Phylogenic_Tree", completed_step5),
            (step6, "Summary", completed_step6)
        ]
        
        # Display steps and progress dynamically
        with st.container():
            for i, (step_condition, step_name, completed_step) in enumerate(step_conditions):
                if step_condition == 1:
                    st.markdown(generate_step_circle(step_name, i + 1, completed_step, True), unsafe_allow_html=True)
                    
                else:
                    st.markdown(generate_step_circle(step_name, i + 1, completed_step, False), unsafe_allow_html=True)
            progress.progress(20*(int(completed_step1) + int(completed_step2) + int(completed_step3) + int(completed_step4) + int(completed_step5) + int(completed_step6)))
