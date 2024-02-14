import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Optimize Eyebrow", layout="wide")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
img_1 = Image.open("images/2021-03-12.jpg")
img_2 = Image.open("images/133953700_1063355007518135_1256085435724720813_n.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.header("Optimize Eyebrow")
    st.divider()
    st.subheader("Look Great, Feel Amazing!")
    st.write(
        "Welcome to Optimize Eyebrow, your one-stop-shop for all your beauty needs. Our team of experts has been providing high-quality services to the Maineville, Ohio community for 2 years. Whether you need eyebrow optimization, threading, waxing, facials, haircuts, or beauty products, we have everything you need to keep looking and feeling amazing every single day. Treat yourself to one of our bookable pampering services today."
    )
    # st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT WE DO ----
with st.container():
    st.write("---")
    st.subheader("About Us")
    st.write(
        """
Our journey began in [Year], with a passion for enhancing natural beauty and a commitment to customer satisfaction. Our team of experienced and skilled professionals specializes in a range of services, including eyebrow threading, waxing, facial cleansing, haircuts, and more. We believe in using high-quality products and the latest techniques to ensure you leave our salon feeling and looking your best.

At Optimize Eyebrow, we understand that beauty is not just about appearance; it's about feeling confident and refreshed. That's why we take the time to understand your needs and preferences, ensuring that each service is tailored to suit your individual style and skin type.

Whether you're looking for a quick touch-up or a complete makeover, we are here to provide you with a relaxing and rejuvenating experience. Come visit us and discover the art of beauty, where every detail is crafted with care and every visit leaves you feeling inspired.
        """
    )
    st.write("[Facebook Page >](https://www.facebook.com/Optimize.Eyebrows)")
    st.write("[Instagram Page >](https://www.instagram.com/optimize_eyebrows/)")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Gallery")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_1)
    with text_column:
        st.empty()
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2)
    with text_column:
        st.empty()

# ---- CONTACT ----
with st.sidebar:
    with st.container():
        st.write("---")
        st.subheader("Contact Us!")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/risalsudeep@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        st.write("---")
