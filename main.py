import streamlit as st
import asyncio
import telegram
import re

st.set_page_config(
    page_title="Increase Stipend",  # This title appears on the tab and when shared
    page_icon=":rocket:",            # Optional: add an emoji or image as the page icon
    # layout="wide"                    # Optional: set layout to 'wide' or 'centered'
)

hide_streamlit_style = """
    <style>
    /* Hide the hamburger menu */
    #MainMenu {visibility: hidden;}
    /* Hide the "Manage app" button */
    footer {visibility: hidden;}
    </style>
"""

# Inject CSS with st.markdown
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

API_TOKEN = '7259751187:AAENuR_8zsJ1smrch0AW7mqAkAfmnX-kf40'  # Replace with your bot's API token
CHANNEL_ID = '-1002369094626'  # Replace with your actual channel ID



# Now start with your app content below
st.title("#Increase Stipend 🔥")


# Create a bot instance
bot = telegram.Bot(token=API_TOKEN)

flag = True
async def send_message(name,institue,email):
    message = f"Name : {name}\nEmail : {email}\nInstitue : {institue}"
    await bot.send_message(chat_id=CHANNEL_ID, text=message)
    global flag
    flag = False

# Function to validate email format
def is_valid_email(email):
    # Check if there is exactly one "@" symbol
    if email.count("@") != 1:
        return False

    # Split the email into username and domain parts
    username, domain = email.split("@")

    # Check basic length requirements
    if len(username) < 1 or len(domain) < 3:
        return False

    # Ensure domain contains at least one "." and it's not the first/last character
    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    return True

def func(x):
    result = ""
    for i in x:
        if i == ' ':
            result += "%20"
        elif i == '\n':
            result+="%0A"
        else:
            result+=i
    return result
def genratedata(n,i,b,e):
    subject = func("Urgent Appeal for Revision of M.Tech and MS Stipend")
    body = func(f'''Respected Sir,

    We, the M.Tech and MS students across NITs and IITs, respectfully request an urgent revision of our stipend, which has remained unchanged since 2015. Over these years, tuition fees and the cost of living have risen significantly, placing a substantial financial burden on us. While the stipend for Ph.D. students has seen adjustments, M.Tech/MS stipends have not, leaving many students struggling to meet basic expenses.

    In support of this request, with reference the AICTE Act (1987) and UGC Act (1956), which provide for periodic stipend reviews. Guidelines issued by the Ministry of Education (MoE) and Seventh Central Pay Commission (2015), alongside provisions for Cost of Living Adjustment (COLA) and Dearness Allowance (DA), further establish the need for regular updates to stipends based on inflation and cost of living.

    We kindly urge you to consider a prompt increase in the M.Tech/MS stipend. This support would alleviate financial pressures, enabling us to focus fully on our academic and research commitments and contribute meaningfully to national advancements in science and technology.

    Thank you for your attention to this pressing matter.

    Sincerely,  
    {n}
    {b}
    Enrollment : {e}
    ({i})
    ''')
    emails = '''hrm@mhrd.gov.in
secy.he@mhrd.gov.in
js.he1@mhrd.gov.in
js.he2@mhrd.gov.in
dir.te@mhrd.gov.in
ds.te@mhrd.gov.in
chairman@aicte-india.org
cmoffice@aicte-india.org
vcm@aicte-india.org
ea.vcm@aicte-india.org
ms@aicte-india.org
director@nitagartala.in
director@nitp.ac.in
director@nitandhra.ac.in
director@manit.ac.in
director@nitc.ac.in
director@nitdelhi.ac.in
director@nitdgp.ac.in
director@nitgoa.ac.in
director@nit.hamirpur.gov.in
director@mnit.ac.in
director@nitj.ac.in
director@nitk.ac.in
director@nitm.ac.in
director@nitnagaland.ac.in
director@nitp.net.in
director@nitrr.ac.in
director@nitrl.ac.in
director@nuts.ac.in
director@nitsikkim.ac.in
director@nit.srinagar.gov.in
director@nitt.edu
director@nitw.ac.in
director@iitbhilai.ac.in
director@iitbbs.ac.in
director@iitb.ac.in
director@iitd.ac.in
director@iitdh.ac.in
director@iitgn.ac.in
director@iitgoa.ac.in
director@iitg.ac.in
director@iith.ac.in
director@iiti.ac.in
director@iitjammu.ac.in
director@iitj.ac.in
director@iitk.ac.in
director@iitkgp.ac.in
director@iitm.ac.in
director@iitmandi.ac.in
director@iitpkd.ac.in
director@iitp.ac.in
director@iitr.ac.in
director@iitrpr.ac.in
director@iiti.ac.in
director@iitbhu.ac.in
pmosb@pmo.nic.in
psecy@pmo.nic.in
apsecy@pmo.nic.in
secy@pmo.nic.in'''

    x = emails.split("\n")
    mail = ",".join(x)
    print(mail.count(','))
    link = "mailto:"+mail+"?subject="+subject+"&body="+body
    return link


# Set the title of the app
st.subheader("Make your contribution count by reaching out to the government today to support an increase in our stipend!")

st.success("Thankyou guys for you support , this website is no longer supporting")
# Create a form
# with st.form(key='student_info_form'):
#     # Create text inputs for the form
#     name = st.text_input("Name")
#     institute_name = st.text_input("Institute Name")
#     branch = st.text_input("Branch")
#     roll_number = st.text_input("Roll Number")
#     email = st.text_input("Email Address")

#     # Check if all inputs are filled and if the email is valid
#     all_filled = all([name, institute_name, email,branch,roll_number])
#     email_valid = is_valid_email(email)

#     # Create a submit button that is active only if all fields are filled and email is valid

#     # If the form is submitted and valid, display the entered information
#     if st.form_submit_button("Genrate Email"):
#         if (all_filled and email_valid):
#             asyncio.run(send_message(name,institute_name,email))
#             link = genratedata(name,institute_name)
#             with st.spinner("Generating Email ..."):
#                 while flag:
#                     pass
#             st.success("Email Generated Successfully!")
#             st.link_button("Click to send Email",link)
#         else:
#             st.error("Please Fill all the details Properly")

st.text("")
x = st.columns((1,2,1))
x[1].text("Thankyou for contributing :) 🙏🏻")
