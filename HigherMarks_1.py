import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="HigherMarks | IITian & NITian Led Coaching", 
    page_icon="📈",
    layout="centered"
)

# --- Header & Branding ---
st.markdown("# 📈 HigherMarks")
st.subheader("Elevating Education with Mentors from IITs and NITs")
st.write("""
Master PCM with engineers from India's premier institutes. 
Specialized coaching for ICSE, CBSE, and 11th Grade Mathematics 
focused on conceptual depth and board excellence.
""")

st.divider()

# --- Program Overview ---
st.header("📚 Our Programs")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### **ICSE**")
    st.caption("Grades 8th - 10th")
    st.write("**PCM Focus**")

with col2:
    st.markdown("### **CBSE**")
    st.caption("Grade 10th")
    st.write("**PCM Focus**")

with col3:
    st.markdown("### **Maths**")
    st.caption("Grade 11th")
    st.write("**All Boards**")

st.divider()

# --- Lead Generation Form Section ---
st.header("📩 Book a Free Demo Session")
st.write("An IITian/NITian mentor will call you back to discuss your academic goals.")

# 1. Update this to your real email
your_email = "vibhuagarwal1998@gmail.com" 

# 2. Define the HTML Form
# Using inline CSS to ensure it looks good inside the iframe
contact_form_html = f"""
<div style="font-family: sans-serif; padding: 10px;">
    <form action="https://formsubmit.co/{your_email}" method="POST" target="_top">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="https://highermarks.streamlit.app/">
        
        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Student Name</label>
            <input type="text" name="name" placeholder="Full Name" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;" required>
        </div>

        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Parent's Phone Number</label>
            <input type="tel" name="phone" placeholder="10-digit mobile number" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;" required>
        </div>

        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Course Interest</label>
            <select name="course" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; background-color: white; box-sizing: border-box;">
                <option value="ICSE 8-10">ICSE PCM (8th-10th)</option>
                <option value="CBSE 10">CBSE PCM (10th)</option>
                <option value="Class 11 Maths">Class 11th Maths (All Boards)</option>
            </select>
        </div>

        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Notes/Goals</label>
            <textarea name="message" placeholder="How can we help?" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; height: 80px; box-sizing: border-box;"></textarea>
        </div>

        <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 14px; border-radius: 5px; width: 100%; cursor: pointer; font-size: 16px; font-weight: bold;">
            Request Call Back
        </button>
    </form>
</div>
"""

# 3. Render the HTML using components.html
# This prevents the code from showing as text
components.html(contact_form_html, height=520)

# --- Footer ---
st.divider()
st.markdown("<center>© 2026 HigherMarks Academic Center | Quality Coaching by IITians & NITians</center>", unsafe_allow_html=True)
