import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE-API-KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


col1, col2 = st.columns(2)
with col1:
    st.subheader("Hello :wave: ")
    st.title("I am Bashar  ")

with col2:
    st.image("Images/5.jpg")

persona = """ 
              You are Bashar AI bot. You help people answer questions about your self (i.e Bashar)
              Answer as if you are responding . dont answer in second or third person.
              If you don't know they answer you simply say "I'd rather keep that to myself".
              say " your" instead of " the user's "
              
              Bashar is a second-year Artificial Intelligence major at the University of Jordan. Bashar is 19 years 
              old I am still at the beginning of my academic career . Bashar is interested in many field such as: AI,computer vision , 
              Robotics , Brain Computer Interface and Web development and Cyber security. Bashar likes to explor many technological fields. 
              I tried to do some projects (Gesture Volume Control,Object Size Measurement,AI Virtual Mouse ,Login registration page with ReactJS , arduino projects)
              because i liked to know how i can do such things.
              
              
              Note: if the question is to explain a project(Gesture Volume Control,Object Size Measurement,AI Virtual Mouse ,Login registration page with ReactJS , arduino projects)
              or  field(AI,computer vision , Robotics , Brain Computer Interface and Web development and Cyber security)  just explain it by yourself 
              Note: if the question is about anything else just say "I dont know" and try to add some explanation with the fields and projects.
              
              
              Bashar email : contact@basharzabaneh.com
              Bashar github account : https://github.com/Bashar-121 
                   
          """

st.title("My AI Bot")
user_q = st.text_input("Ask Anything About Me ")
col1, col2 = st.columns([0.75,4])
with col1:
    Ask_button = st.button("Ask")
if Ask_button:
    prompt = persona + "Here is the question that the user asked: " + user_q
    response = model.generate_content(prompt)
    with col2:
        st.write(response.text)



st.title(" ")
st.subheader("Things I tried to do:")
colum1, colum2, colum3 = st.columns(3)

with colum1:
    st.write("- Gesture Volume Control")
    st.video("https://youtu.be/9iEPzbG-xLE")
with colum2:
    st.write("- Object Size Measurement")
    st.video("https://youtu.be/tk9war7_y0Q")

with colum3:
    st.write("- AI Virtual Mouse")
    st.video("https://youtu.be/8gPONnGIPgw")

cl1, cl2 = st.columns(2)

with cl1:
    st.write("- Login registration page with ReactJS")
    st.write("https://bashar-121.github.io/Project/")

with cl2:
    st.write("- Some arduino projects on wokwi simulator")
    st.write("https://wokwi.com/makers/bashar")


st.title(" ")

st.title("My Laptop")
st.image("Images/i2.jpg")

st.text("")

st.title("My Skills")

st.slider("Programing", 0, 100, 30)
st.slider("Mathematics", 0, 100, 20)
st.slider("Social", 0, 100, 10)
st.write("")

st.title("Gallary")

co1, co2, co3=st.columns(3)

with co1:
    st.image("Images/4.png")
    st.image("Images/6.png")
    st.image("Images/1.png")

with co2:
    st.image("Images/8.png")
    st.image("Images/2.png")
    st.image("Images/10.png")
with co3:
    st.image("Images/3.png")
    st.image("Images/9.png")
    st.image("Images/7.png")

st.write("")
st.title("Contact")
st.write("For any inquiries , please contact me at :")

st.write('''<style>
                .social-icons{
                  margin: 20px 0;
                  }
                .social-icons a{
                   border: 1px solid #ccc;
                   border-radius: 20%;
                   display: inline-flex;
                   justify-content: center;
                   align-items: center;
                   margin: 0 3px;
                   width: 40px;
                   height: 40px;
                }
           </style>'''
         
         '<link rel="stylesheet" ''href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"/>'
          '<div class="social-icons">'
             '<a herf= https://github.com/Bashar-121 > '
         '   <i class="fa-brands fa-github"> </i>'
         '   </a> '
            '<a herf= mailto: contact@basharzabaneh.com > '
            ' <i class="fa fa-envelope" aria-hidden="true"> </i>'
            '</a>'
         '</div>', unsafe_allow_html=True)

