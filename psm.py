import re
import streamlit as st

#page styling

st.set_page_config(page_title="Pasword Strength Checker by M_Tahir", page_icon="🌘", layout="centered")
#custom css
st.markdown("""
<style>
    .main{text-align:center;}
    .stTextInput {widtb:60% ! important; margin:auto;}
    .stButton button {width:50%; background-color #5CAF60; color:white; font_size:180px;}
    .stButton button:hover {background-color:#45a058}
    </style>
""",unsafe_allow_html=True)

#page Title and Description

st.title("🔐 Password strength generator")
st.write("Enter your password below to check its security level. 🔍")
 
 #fuction to check password strength
def Check_password_strength(password):
     score=0
     feedback=[]

     if len(password)>= 8: 
        score+=1 #increased
     else:
        feedback.append(" ❌passwird should be ***atleast 8 character long.***")
     if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
         score+=1
     else:
         feedback.append("❌ password should include ** both uppercase (A-Z) and lowercase(a-z) leeter")
     if re.search(r"\d", password):
         score+=1
     else:
         feedback.append("❌ password should **at least one number (0-9)**")

         #special character
     if re.search(r"[!@#$%&*]",password):
        score+=1
     else:
         feedback.append("❌Include **atleast one special charcter (!@#$%&*)**.")

         #Display password strength results

         if score==4:
             st.success("✔️ **strong password** your password is secure." )
         elif score==3:
             st.info("⚠️**Moderate password** consider improving by adding more feature")         
         else:
             st.error("❌**weak password** -follow the suggestion below to strength it.")

             #feedback
         if feedback:
                with st.expander("🔍**improved your password**"):
                    for item in feedback:
                        st.write(item)
         password=st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

         #Button
         if st.button("Check Strength"):
             if password:
                 Check_password_strength(password)
             else:
                 st.warning("⚠️ Please enter a password first") #show warning if password empty