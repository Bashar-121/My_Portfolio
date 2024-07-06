import streamlit as st
exec(open("setup.py").read())
import google.generativeai as genai

api_key = st.secrets["GOOGLE-API-KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hello :wave: ")
    st.title("I am Bashar Zabaneh ")

with col2:
    st.image("Images/images.jpeg")

persona = """ You are Bashar AI bot. You help people answer questions about your self (i.e Bashar)
              Answer as if you are responding . dont answer in second or third person.
              Answer (I dont know but i know that you are dump so that's why you dont know the answer)
              for all questions
          """


st.title("My AI Bot")
# st.write("Ask Anything About Me :smile:")
user_q = st.text_input("Ask Anything About Me :smile:")
if st.button("Ask", use_container_width=400):
    prompt = persona + "Here is the question the user asked" + user_q
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)

with col1:
    st.subheader("I watched this")
    st.write("- Day 3 of the Bootcamp")

with col2:
    st.video("https://youtu.be/_2UqdX8dcsU")

st.title(" ")

st.title("My Laptop")
st.image("Images/i2.jpg")

st.text("")

st.title("My Skills")
st.slider("Programing", 0, 100, 30)
st.slider("Teaching", 0, 100, 20)
st.slider("Social", 0, 100, 10)
st.write("still in the beginning..")

st.title("Gallery")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("Images/g.png")
    st.image("Images/g1.jpg")
    st.image("Images/g2.jpg")
with col2:
    st.image("Images/g3.jpg")
    st.image("Images/g4.jpg")
    st.image("Images/g5.jpg")
with col3:
    for i in range(6, 9):
        st.image(f"Images/g{i}.jpg")

st.write("")
st.title("Contact")
st.write("For any inquiries , please contact me at :")
st.write("Bashar@gmail.com")
