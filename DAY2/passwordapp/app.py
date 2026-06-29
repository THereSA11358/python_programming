import streamlit as st
st.title("PASSWORD ANALYZER")
password=st.text_input("ENTER THE PASSWORD",type="password")
#st.button("Validate")
if st.button("Validate"):
    upper=lower=digit=special=False
    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower=True
        elif ch.isdigit():
            digits=True
        else:
            special=True
    if len(password)>=8 and upper and lower and special==True:
        st.success("Strong Password...Thank you")

    else:
        st.error("INVALID")
    if not upper:
        st.write("Must contain Upper Case character")
    if not lower:
        st.write("Must contain Lower Case character")
    if not digit:
        st.write("Must contain Digit")
    if not special:
        st.write("Must contain Special character")
        
