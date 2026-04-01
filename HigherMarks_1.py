import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- Page Configuration ---
st.set_page_config(
    page_title="HigherMarks | IITian Led Coaching", 
    page_icon="📈",
    layout="centered"
)

# --- Header & Branding ---
st.markdown("# 📈 HigherMarks")
st.subheader("Elevating Education with Mentors from IITs and NITs")
st.write("""
Master PCM with engineers from India's premier institutes. 
Focused on conceptual depth for ICSE, CBSE, and 11th Grade Mathematics.
""")

st.divider()

# --- Program Overview ---
st.header("📚 Our Programs")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("### **ICSE**\nGrades 8-10")
with c2:
    st.markdown("### **CBSE**\nGrade 10")
with c3:
    st.markdown("### **Maths**\nGrade 11")

st.divider()

# --- Lead Generation Form Section ---
st.header("📩 Book a Free Demo Session")
st.write("Submit the form below and check your email shortly.")

# 1. DOUBLE CHECK THIS EMAIL
# Make sure there are no typos!
your_email = "your-email@gmail.com" 

# 2. Updated HTML Form (Optimized for Streamlit Components)
contact_form_html = f"""
<div style="font-family: sans-serif; padding: 5px;">
    <form action="https://formsubmit.co/{your_email}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        
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
            Submit Request
        </button>
    </form>
</div>
"""

# 3. Render the HTML
components.html(contact_form_html, height=550)

# --- Footer ---
st.divider()
st.markdown("<center>© 2026 HigherMarks | Quality Coaching by IITians & NITians</center>", unsafe_allow_html=True)
