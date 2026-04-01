import streamlit as st
import pandas as pd
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="HigherMarks | IITian & NITian Led Coaching", 
    page_icon="📈",
    layout="centered"
)

# --- Header Section ---
st.markdown("# 📈 HigherMarks")
st.subheader("Elevating Education with Mentors from IITs and NITs")
st.write("""
Taught by engineers from India's premier institutes, we focus on 
conceptual depth for ICSE, CBSE, and 11th Grade Mathematics.
""")

st.divider()

# --- Course Offerings (Using Pandas for structure) ---
st.header("📚 Our Programs")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### **ICSE**")
    st.caption("Grades 8th - 10th")
    st.write("**PCM Focus**")

with c2:
    st.markdown("### **CBSE**")
    st.caption("Grade 10th")
    st.write("**PCM Focus**")

with c3:
    st.markdown("### **Maths**")
    st.caption("Grade 11th")
    st.write("**All Boards**")

st.divider()

# --- THE FORM SECTION ---
# This is the part that fixes the "showing as text" issue
st.header("📩 Book a Free Demo Session")

# 1. Update this to your real email
your_email = "your-email@gmail.com" 

# 2. Define the HTML string
contact_form_html = f"""
<form action="https://formsubmit.co/{your_email}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="hidden" name="_next" value="https://highermarks.streamlit.app/">

     <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #31333F; display: block; margin-bottom: 5px;">Student Name</label>
        <input type="text" name="name" placeholder="Enter student name" style="width: 100%; padding: 12px; border: 1px solid #dcdfe6; border-radius: 5px;" required>
     </div>

     <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #31333F; display: block; margin-bottom: 5px;">Parent's Phone Number</label>
        <input type="tel" name="phone" placeholder="10-digit mobile number" style="width: 100%; padding: 12px; border: 1px solid #dcdfe6; border-radius: 5px;" required>
     </div>

     <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #31333F; display: block; margin-bottom: 5px;">Course Interest</label>
        <select name="course" style="width: 100%; padding: 12px; border: 1px solid #dcdfe6; border-radius: 5px; background-color: white;">
            <option value="ICSE 8-10">ICSE PCM (8th-10th)</option>
            <option value="CBSE 10">CBSE PCM (10th)</option>
            <option value="Class 11 Maths">Class 11th Maths (All Boards)</option>
        </select>
     </div>

     <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #31333F; display: block; margin-bottom: 5px;">Notes/Goals</label>
        <textarea name="message" placeholder="e.g. Preparing for JEE, need help in Physics..." style="width: 100%; padding: 12px; border: 1px solid #dcdfe6; border-radius: 5px; height: 80px;"></textarea>
     </div>

     <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 14px; border-radius: 5px; width: 100%; cursor: pointer; font-size: 16px; font-weight: bold;">
        Request Call Back
     </button>
</form>
"""

# 3. USE THIS SPECIFIC LINE TO RENDER THE HTML
st.markdown(contact_form_html, unsafe_allow_html=True)

# --- Footer ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<center>© 2026 HigherMarks | Taught by IITians & NITians</center>", unsafe_allow_html=True)
