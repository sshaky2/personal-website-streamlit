import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Optimize Eyebrow", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/2021-03-12.jpg")
img_lottie_animation = Image.open("images/133953700_1063355007518135_1256085435724720813_n.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.title("Optimize Eyebrow")
    st.subheader("Look Great, Feel Amazing!")
    st.write(
        "Welcome to Optimize Eyebrow, your one-stop-shop for all your beauty needs. Our team of experts has been providing high-quality services to the Maineville, Ohio community for 2 years. Whether you need eyebrow optimization, threading, waxing, facials, haircuts, or beauty products, we have everything you need to keep looking and feeling amazing every single day. Treat yourself to one of our bookable pampering services today."
    )
    # st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT WE DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Us")
        # st.write("##")
        st.write(
            """
            Eyebrows threading is a process of cleaning and shaping eyebrows with the help of cotton thread. 
            Threading keeps away your skin from coming contact to  chemical like in waxing.
            """
        )
        st.write("[Facebook Page >](https://www.facebook.com/Optimize.Eyebrows)")
        st.write("[Instagram Page >](https://www.instagram.com/optimize_eyebrows/)")
    with right_column:
        st.empty()
        # st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Gallery")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.empty()
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.empty()

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/shobhit.shakya@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# import streamlit as st
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# def send_message(name, email, message):
#     sender_email = "eyebrowoptimize@gmail.com"  # Replace with your email
#     sender_password = "optimize123"  # Replace with your password or app password
#     receiver_email = "eyebrowoptimize@gmail.com"  # Where you want to receive the messages

#     # Email subject and body setup
#     subject = "New Contact Us Message"
#     body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    
#     # Creating a multipart message
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     msg["Subject"] = subject
    
#     # Attach the body to the email
#     msg.attach(MIMEText(body, "plain"))
    
#     try:
#         # Setup the SMTP server
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()  # Secure the connection
#         server.login(sender_email, sender_password)
#         text = msg.as_string()
#         server.sendmail(sender_email, receiver_email, text)
#         st.success("Email sent successfully")
#     except Exception as e:
#         st.error(f"Failed to send email. Error: {e}")
#     finally:
#         server.quit()

#     # left_column, right_column = st.columns(2)
#     # with left_column:
#     #     st.markdown(contact_form, unsafe_allow_html=True)
#     # with right_column:
#     #     st.empty()

# # Streamlit form for "Contact Us"
# st.title('Contact Us')

# with st.container():
#     st.write("We'd love to hear from you! Fill out the form below and we'll get back to you as soon as possible.")
    
#     left_column, right_column = st.columns(2)
#     with left_column:
#         with st.form("contact_form", clear_on_submit=True):
#             name = st.text_input("Name")
#             email = st.text_input("Email")
#             message = st.text_area("Message", height=150)
#             submit_button = st.form_submit_button("Send Message")
        
#             if submit_button:
#                 send_message(name, email, message)

#     with right_column:
#         st.empty()
    
