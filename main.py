# import streamlit as st
# import asyncio
# import telegram
# import re

# st.set_page_config(
#     page_title="Increase Stipend",  # This title appears on the tab and when shared
#     page_icon=":rocket:",            # Optional: add an emoji or image as the page icon
#     # layout="wide"                    # Optional: set layout to 'wide' or 'centered'
# )

# hide_streamlit_style = """
#     <style>
#     /* Hide the hamburger menu */
#     #MainMenu {visibility: hidden;}
#     /* Hide the "Manage app" button */
#     footer {visibility: hidden;}
#     </style>
# """

# # Inject CSS with st.markdown
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# API_TOKEN = '7259751187:AAENuR_8zsJ1smrch0AW7mqAkAfmnX-kf40'  # Replace with your bot's API token
# CHANNEL_ID = '-1002369094626'  # Replace with your actual channel ID



# # Now start with your app content below
# st.title("#Increase Stipend 🔥")


# # Create a bot instance
# bot = telegram.Bot(token=API_TOKEN)

# flag = True
# async def send_message(name,institue,email):
#     message = f"Name : {name}\nEmail : {email}\nInstitue : {institue}"
#     await bot.send_message(chat_id=CHANNEL_ID, text=message)
#     global flag
#     flag = False

# # Function to validate email format
# def is_valid_email(email):
#     # Check if there is exactly one "@" symbol
#     if email.count("@") != 1:
#         return False

#     # Split the email into username and domain parts
#     username, domain = email.split("@")

#     # Check basic length requirements
#     if len(username) < 1 or len(domain) < 3:
#         return False

#     # Ensure domain contains at least one "." and it's not the first/last character
#     if "." not in domain or domain.startswith(".") or domain.endswith("."):
#         return False

#     return True

# def func(x):
#     result = ""
#     for i in x:
#         if i == ' ':
#             result += "%20"
#         elif i == '\n':
#             result+="%0A"
#         else:
#             result+=i
#     return result
# def genratedata(n,i,b,e):
#     subject = func("Urgent Appeal for Revision of M.Tech and MS Stipend")
#     body = func(f'''Respected Sir,

#     We, the M.Tech and MS students across NITs and IITs, respectfully request an urgent revision of our stipend, which has remained unchanged since 2015. Over these years, tuition fees and the cost of living have risen significantly, placing a substantial financial burden on us. While the stipend for Ph.D. students has seen adjustments, M.Tech/MS stipends have not, leaving many students struggling to meet basic expenses.

#     In support of this request, with reference the AICTE Act (1987) and UGC Act (1956), which provide for periodic stipend reviews. Guidelines issued by the Ministry of Education (MoE) and Seventh Central Pay Commission (2015), alongside provisions for Cost of Living Adjustment (COLA) and Dearness Allowance (DA), further establish the need for regular updates to stipends based on inflation and cost of living.

#     We kindly urge you to consider a prompt increase in the M.Tech/MS stipend. This support would alleviate financial pressures, enabling us to focus fully on our academic and research commitments and contribute meaningfully to national advancements in science and technology.

#     Thank you for your attention to this pressing matter.

#     Sincerely,  
#     {n}
#     {b}
#     Enrollment : {e}
#     ({i})
#     ''')
#     emails = '''hrm@mhrd.gov.in
# secy.he@mhrd.gov.in
# js.he1@mhrd.gov.in
# js.he2@mhrd.gov.in
# dir.te@mhrd.gov.in
# ds.te@mhrd.gov.in
# chairman@aicte-india.org
# cmoffice@aicte-india.org
# vcm@aicte-india.org
# ea.vcm@aicte-india.org
# ms@aicte-india.org
# director@nitagartala.in
# director@nitp.ac.in
# director@nitandhra.ac.in
# director@manit.ac.in
# director@nitc.ac.in
# director@nitdelhi.ac.in
# director@nitdgp.ac.in
# director@nitgoa.ac.in
# director@nit.hamirpur.gov.in
# director@mnit.ac.in
# director@nitj.ac.in
# director@nitk.ac.in
# director@nitm.ac.in
# director@nitnagaland.ac.in
# director@nitp.net.in
# director@nitrr.ac.in
# director@nitrl.ac.in
# director@nuts.ac.in
# director@nitsikkim.ac.in
# director@nit.srinagar.gov.in
# director@nitt.edu
# director@nitw.ac.in
# director@iitbhilai.ac.in
# director@iitbbs.ac.in
# director@iitb.ac.in
# director@iitd.ac.in
# director@iitdh.ac.in
# director@iitgn.ac.in
# director@iitgoa.ac.in
# director@iitg.ac.in
# director@iith.ac.in
# director@iiti.ac.in
# director@iitjammu.ac.in
# director@iitj.ac.in
# director@iitk.ac.in
# director@iitkgp.ac.in
# director@iitm.ac.in
# director@iitmandi.ac.in
# director@iitpkd.ac.in
# director@iitp.ac.in
# director@iitr.ac.in
# director@iitrpr.ac.in
# director@iiti.ac.in
# director@iitbhu.ac.in
# pmosb@pmo.nic.in
# psecy@pmo.nic.in
# apsecy@pmo.nic.in
# secy@pmo.nic.in'''

#     x = emails.split("\n")
#     mail = ",".join(x)
#     print(mail.count(','))
#     link = "mailto:"+mail+"?subject="+subject+"&body="+body
#     return link


# # Set the title of the app
# st.subheader("Make your contribution count by reaching out to the government today to support an increase in our stipend!")

# st.success("Thankyou guys for you support , this website is no longer supporting")
# # Create a form
# # with st.form(key='student_info_form'):
# #     # Create text inputs for the form
# #     name = st.text_input("Name")
# #     institute_name = st.text_input("Institute Name")
# #     branch = st.text_input("Branch")
# #     roll_number = st.text_input("Roll Number")
# #     email = st.text_input("Email Address")

# #     # Check if all inputs are filled and if the email is valid
# #     all_filled = all([name, institute_name, email,branch,roll_number])
# #     email_valid = is_valid_email(email)

# #     # Create a submit button that is active only if all fields are filled and email is valid

# #     # If the form is submitted and valid, display the entered information
# #     if st.form_submit_button("Genrate Email"):
# #         if (all_filled and email_valid):
# #             asyncio.run(send_message(name,institute_name,email))
# #             link = genratedata(name,institute_name)
# #             with st.spinner("Generating Email ..."):
# #                 while flag:
# #                     pass
# #             st.success("Email Generated Successfully!")
# #             st.link_button("Click to send Email",link)
# #         else:
# #             st.error("Please Fill all the details Properly")

# st.text("")
# x = st.columns((1,2,1))
# x[1].text("Thankyou for contributing :) 🙏🏻")








import streamlit as st
import json
import telegram
import asyncio
import os
import base64

# Set the layout to wide
st.set_page_config(layout="wide")

API_TOKEN = '7259751187:AAENuR_8zsJ1smrch0AW7mqAkAfmnX-kf40'  # Replace with your bot's API token
CHANNEL_ID = '-1002256449759'  # Replace with your actual channel ID

# Create a bot instance
bot = telegram.Bot(token=API_TOKEN)

# async def send_message_with_file(data, file_path=None):
#     message = json.dumps(data, indent=4)
#     if file_path:
#         with open(file_path, 'rb') as f:
#             await bot.send_document(chat_id=CHANNEL_ID, document=f)
#     else:
#         await bot.send_message(chat_id=CHANNEL_ID, text=message)

# def handle_submission(name, question, constraints, tags, question_type, algorithm, test_cases, file_upload):
#     data = {
#         "name": name,
#         "question": question,
#         "constraints": constraints,
#         "difficulty_level": tags,
#         "question_type": question_type,
#         "algorithm": algorithm,
#         "test_cases": [{"input": inp, "output": out} for inp, out in test_cases],
#         "file_upload": file_upload.name if file_upload else None
#     }
    
#     json_file_path = "submission.json"
#     with open(json_file_path, "w") as f:
#         json.dump(data, f, indent=4)
    
#     if file_upload:
#         file_path = os.path.join("uploads", file_upload.name)
#         with open(file_path, "wb") as f:
#             f.write(file_upload.getbuffer())
#     else:
#         file_path = None

#     asyncio.run(send_message_with_file(data, json_file_path))
    
#     st.success("Form submitted successfully!")
#     st.write("Data saved to submission.json")

#     if file_path:
#         os.remove(file_path)
#     os.remove(json_file_path)

async def send_message_with_file(json_file_path):
    with open(json_file_path, 'rb') as f:
        await bot.send_document(chat_id=CHANNEL_ID, document=f)

# Function to handle form submission
def handle_submission(name, question, constraints, tags, question_type, algorithm, test_cases, file_upload):
    data = {
        "name": name,
        "question": question,
        "constraints": constraints,
        "difficulty_level": tags,
        "question_type": question_type,
        "algorithm": algorithm,
        "test_cases": [{"input": inp, "output": out} for inp, out in test_cases],
        "file_upload": None  # Placeholder for file data
    }

    # Process the uploaded file (if any)
    if file_upload:
        file_content = file_upload.getbuffer()
        encoded_file = base64.b64encode(file_content).decode("utf-8")
        data["file_upload"] = {
            "filename": file_upload.name,
            "content": encoded_file
        }

    # Save JSON file
    json_file_path = "submission.json"
    with open(json_file_path, "w") as f:
        json.dump(data, f, indent=4)

    # Send the JSON file via Telegram bot
    asyncio.run(send_message_with_file(json_file_path))

    st.success("Form submitted successfully!")
    st.write("data shared to the telegram please reload the website :) ")

    # Remove the temporary JSON file
    os.remove(json_file_path)


# Create three columns
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.title("DSA Question")
    # Input fields
    name = st.selectbox("Your Name ", ["Default","Dipanshu", "Gauri", "Yogesh","Sanjay"], key="name")
    question = st.text_area("Enter the Question", height=150, key="question")
    constraints = st.text_area("Enter the Constraints", height=100, key="constraints")
    tags = st.selectbox("Select the Difficulty Level", ["default","Easy", "Medium", "Hard"], key="tags")
    question_type = st.text_input("Enter the Type of Question", help="E.g., Array, String, Dynamic Programming", key="question_type")
    algorithm = st.text_area("Enter the Algorithm", height=200, key="algorithm")
    file_upload = st.file_uploader("Upload a file (optional) any image related to the Question ", type=["jpeg","pdf","png","jpg"], key="file_upload")
    
    # Test cases section
    st.subheader("Test Cases (Input/Output)")
    if "test_cases" not in st.session_state:
        st.session_state.test_cases = []  # Start with an empty list

    test_cases = st.session_state.test_cases

    updated_test_cases = []
    indices_to_remove = []
    for i, (input_case, output_case) in enumerate(test_cases):
        input_col, output_col, remove_col = st.columns([3, 3, 1])
        with input_col:
            input_case = st.text_area(f"Input {i+1}", input_case, height=70, key=f"input_{i}")
        with output_col:
            output_case = st.text_area(f"Output {i+1}", output_case, height=70, key=f"output_{i}")
        with remove_col:
            if st.button("❌", key=f"remove_{i}"):
                indices_to_remove.append(i)
        updated_test_cases.append((input_case, output_case))
    
    # Remove test cases marked for deletion
    st.session_state.test_cases = [tc for idx, tc in enumerate(updated_test_cases) if idx not in indices_to_remove]
    
    # Add new test case button
    if st.button("➕ Add Test Case"):
        st.session_state.test_cases.append(("", ""))
        st.rerun()
    
    # Submit and Clear buttons
    submit_col = list(st.columns(3))
    with submit_col[1]:
        if st.button("Submit",type="primary",use_container_width=True):
            if not question.strip():
                st.error("Question field cannot be empty.")
            elif not constraints.strip():
                st.error("Constraints field cannot be empty.")
            elif not st.session_state.test_cases or any(not inp.strip() or not out.strip() for inp, out in st.session_state.test_cases):
                st.error("All test cases must have both input and output filled. and there should be atleast one test case")
            elif not tags.strip():
                st.error("Please select a difficulty level.")
            elif not question_type.strip():
                st.error("Please enter the type of question.")
            elif not algorithm.strip():
                st.error("Algorithm field cannot be empty.")
            elif tags == "default":
                st.error("Please select a valid difficulty level.")
            elif name == "Default":
                st.error("Please select your name.")
            else:
                handle_submission(name, question, constraints, tags, question_type, algorithm, st.session_state.test_cases, file_upload)
    
  
if __name__ == "__main__":
    pass











