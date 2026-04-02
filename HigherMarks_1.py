import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="HigherMarks | IITian & NITian Led Coaching", 
    page_icon="📈",
    layout="centered"
)

# --- Configuration: UPDATE THIS EMAIL ---
your_email = "your-email@gmail.com" 

# --- Header Section ---
st.markdown("# 📈 HigherMarks")
st.subheader("Elevating Education with Mentors from IITs and NITs")
st.write("""
Welcome to **HigherMarks**, where we bridge the gap between classroom learning 
and competitive excellence. Our mission is to provide top-tier conceptual 
clarity delivered by India's finest engineering minds.
""")

st.divider()

# --- The Pedigree Section ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎓 The HigherMarks Advantage")
    st.write("- **Premium Faculty:** Taught exclusively by **IITians and NITians**.")
    st.write("- **Small Batch Sizes:** Personalized attention for every student.")
    st.write("- **Result Oriented:** Specialized focus on conceptual depth and board patterns.")

with col2:
    st.markdown("### 💡 Our Expertise")
    st.write("Our educators have cleared the toughest exams in the country. We know the path because we've walked it.")
    st.info("📍 **Location:** \nHiranandani Estate, Thane")

st.divider()

# --- Curriculum Section ---
st.header("📚 Our Programs")

card1, card2, card3 = st.columns(3)

with card1:
    st.markdown("### **ICSE**")
    st.caption("Grades 8th - 10th")
    st.write("**PCM Focus**")
    st.write("Physics, Chemistry, and Math covered with rigorous practice for Board prep.")

with card2:
    st.markdown("### **CBSE**")
    st.caption("Grade 10th")
    st.write("**PCM Focus**")
    st.write("Specialized modules for Class 10 Boards, focusing on NCERT and PYQs.")

with card3:
    st.markdown("### **Mathematics**")
    st.caption("Grade 11th")
    st.write("**All Boards**")
    st.write("Advanced Mathematics for CBSE, ICSE, and State Boards. Building the JEE foundation.")

st.divider()

# --- Lead Generation Form Section ---
st.header("📩 Book a Free Demo Session")
st.write("Submit the form below to connect with our IITian faculty.")

# Optimized HTML Form for FormSubmit
contact_form_html = f"""
<div style="font-family: sans-serif; padding: 5px; background-color: #f9f9f9; border-radius: 10px; border: 1px solid #eee;">
    <form action="https://formsubmit.co/{your_email}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_subject" value="New HigherMarks Demo Request - Thane">
        
        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Student Name</label>
            <input type="text" name="name" placeholder="Full Name" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;" required>
        </div>

        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Parent's Email</label>
            <input type="email" name="email" placeholder="email@example.com" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;" required>
        </div>

        <div style="display: flex; gap: 10px; margin-bottom: 15px;">
            <div style="flex: 1;">
                <label style="font-weight: bold; display: block; margin-bottom: 5px;">Phone Number</label>
                <input type="tel" name="phone" placeholder="10-digit number" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;" required>
            </div>
            <div style="flex: 1;">
                <label style="font-weight: bold; display: block; margin-bottom: 5px;">Course Interest</label>
                <select name="course" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; background-color: white; box-sizing: border-box;">
                    <option value="ICSE 8-10">ICSE PCM (8th-10th)</option>
                    <option value="CBSE 10">CBSE PCM (10th)</option>
                    <option value="Class 11 Maths">Class 11th Maths</option>
                </select>
            </div>
        </div>

        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; display: block; margin-bottom: 5px;">Academic Goals / Notes</label>
            <textarea name="message" placeholder="How can we help the student excel?" style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 5px; height: 80px; box-sizing: border-box;"></textarea>
        </div>

        <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 14px; border-radius: 5px; width: 100%; cursor: pointer; font-size: 16px; font-weight: bold;">
            Request Call Back & Demo
        </button>
    </form>
</div>
"""

# Render the HTML Component
components.html(contact_form_html, height=600)

# --- Footer ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center'>
    <p><strong>HigherMarks Academic Center</strong></p>
    <p>📍 Hiranandani Estate, Thane, Maharashtra</p>
    <p style='font-size: 0.8em;'>© 2026 HigherMarks Education | Taught by IITians & NITians</p>
</div>
""", unsafe_allow_html=True)
