import streamlit as st

def navigationbar_nose():
    st.markdown("""
        <style>
            .navigation {
                overflow: hidden;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 10px 10px;
                top: 0rem;
                right: 0rem;
                z-index: 100;
                margin-bottom: 150px;
                border-bottom: 80px;
                width: 100vw;
                position: fixed;
                background-color: #e0ece9;
            }
            .nav-list {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                width: 100%;
                display: flex;
                justify-content: right;
                top: 0rem;
            }
            .nav-item {
                display: block;
                float: left;
                margin-right: 10px;
            }
            .nav-link {
                display: block;
                text-align: center;
                text-decoration: none;
                text-align: right;
                justify-content: right;
                -webkit-text-stroke: 0.3px #fff;
                margin-right: 1vh;
                top: 0rem;
                font-size: 1.1rem;
            }
            .nav-link:hover {
                border-radius: 5px;
                padding: 4px;
                text-decoration: none;
                font-size: 1.1em;
            }
            .nav-link:active {
                color: black;
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
            @media (max-width: 1000px) {
                .nav-link {
                    font-size: 0.8rem;            
                }
            }
            .modal {
                display: none; /* Hidden by default */
                position: fixed;
                z-index: 1111111; /* Sit on top */
                left: 0;
                top: 0;
                width: 100%; /* Full width */
                height: 100%; /* Full height */
                overflow: auto; /* Enable scroll if needed */
                background-color: rgb(0,0,0); /* Fallback color */
                background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
                padding-top: 6px;
                
            }
            /* Modal content box */
            .modal-content {
                background-color: #fefefe;
                margin: 5% auto; /* 5% from the top and centered */
                padding: 20px;
                top: 0rem;
                border: 1px solid #888;
                width: 100%; /* Could be more or less, depending on screen size */
                max-width: 500px; /* Limiting width for smaller screens */
                border-radius: 15px 15px 15px 15px;
            }
            /* Close button */
            .close {
                color: #aaa;
                float: right;
                font-size: 28px;
                font-weight: bold;
            }
            .close:hover,
            .close:focus {
                color: black;
                text-decoration: none;
                cursor: pointer;
            }
            #submitBtn {
                background-color: #1c3b29;
                border: #3d6154;
                color: white;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 12px;
                margin-left: 0px;
            }
            [data-testid="stHeaderActionElements"] {
                display: none;
            }
        </style>
        <nav class="navigation">
            <ul class="nav-list">
                <li class="nav-item"><a href="http://localhost:8501" class="nav-link" style='color: #1c3b29; font-weight:bold;'>Home </a></li><li class="nav-item" style="color:#1c3b29; font-weight:bold; margin-right: 0.3vw;">|</li>
                <li class="nav-item"><a href="#" class="nav-link" style='color:#1c3b29; font-weight:bold;'>About</a></li><li class="nav-item" style="color:#1c3b29; font-weight:bold; margin-right: 0.3vw;">|</li>
                <li class="nav-item"><a href="#" class="nav-link" style='color: #1c3b29; font-weight:bold;'>Help</a></li><li class="nav-item" style="color:#1c3b29; font-weight:bold; margin-right: 0.3vw;">|</li>
                <li class="nav-item"><a href="#" id="openModal" class="nav-link" style='color:#1c3b29; font-weight:bold; margin-right: 10px;'>Check Status</a></li>
            </ul>
        </nav>
        <div id="myModal" class="modal">
            <div class="modal-content">
                <span class="close">&times;</span>
                <h3 style='margin: 0px; margin-bottom: 10px; font-family: "Source Sans Pro", sans-serif; font-size: 1.5rem; font-weight: 600; line-height: 1.5; text-transform: none; display: flex; align-items: center; flex-direction: row;'>Check Status</h3>
                <label for="task_id" style="font-size: 14px; font-family: 'Source Sans Pro', sans-serif; position:relative; left: 3.3px;">Enter the Task ID:</label><br>
                <input type="text" id="task_id" name="task_id" style="width: 100%; margin-top: 7px; margin-bottom: 15px; border-radius: 7px; background-color: rgb(240, 242, 246); border: 1px solid transparent; height: 40px;"><br>
                <button id="submitBtn" class="btn">Check Status</button>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    script = '''
        <script>
        // Get the modal
        var modal = parent.document.getElementById("myModal");

        // Get the button that opens the modal
        var btn = parent.document.getElementById("openModal");

        // Get the <span> element that closes the modal
        var span = parent.document.getElementsByClassName("close")[0];

        // When the user clicks the button, open the modal
        btn.onclick = function() {
          modal.style.display = "block";
        }

        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
          modal.style.display = "none";
        }

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
          if (event.target == modal) {
            modal.style.display = "none";
          }
        }

        // Function to handle form submission
        parent.document.getElementById("submitBtn").onclick = function() {
          var taskId = parent.document.getElementById("task_id").value;
          // Construct the URL with task ID as parameter
          var url = "http://localhost:8503?taskId=" + encodeURIComponent(taskId);
          // Open the URL in a new tab
          window.open(url, "_blank");
          // Optionally, you can keep the modal open or close it here
          // modal.style.display = "none";
        }
        </script>
    '''

    st.components.v1.html(script,height=0)

