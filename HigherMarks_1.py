import streamlit as st
import pandas as pd
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="HigherMarks | IITian & NITian Led Coaching", 
    page_icon="📈",
    layout="centered"
)

# --- Custom CSS for a Premium Branding ---
st.markdown("""
    <style>
    .main {
        background-color: #f9fbfd;
    }
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        border-radius: 8px;
        border: none;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    .course-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #eef2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.markdown("# 📈 HigherMarks")
st.subheader("Elevating Education with Mentors from IITs and NITs")
st.write("""
At **HigherMarks**, we bridge the gap between classroom learning and competitive excellence. 
Taught by engineers who have navigated the toughest entrance exams, we focus on 
conceptual depth for students in the Thane and Mumbai regions.
""")

st.divider()

# --- The Pedigree Section ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎓 The HigherMarks Advantage")
    st.write("- **Premium Faculty:** Taught exclusively by **IITians and NITians**.")
    st.write("- **Personalized Attention:** Limited batch sizes to ensure conceptual clarity.")
    st.write("- **Concept First:** Moving beyond rote learning to logical problem solving.")

with col2:
    st.info("**Our Expertise** \n\n We bring the rigour of IIT Bombay and NIT standards to school-level PCM coaching.")

st.divider()

# --- Curriculum Section (Using Pandas for organized display) ---
st.header("📚 Our Programs")

# Quick DataFrame to show structured course details if needed
courses_data = {
    "Program": ["ICSE (8th-10th)", "CBSE (10th)", "Class 11th Maths"],
    "Subjects": ["Physics, Chemistry, Maths", "Physics, Chemistry, Maths", "Advanced Mathematics"],
    "Focus": ["Board Excellence", "Board Mastery & PYQs", "JEE Foundation"]
}
df_courses = pd.DataFrame(courses_data)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### **ICSE**")
    st.caption("Grades 8th - 10th")
    st.write("**PCM Focus**")
    st.write("Rigorous preparation for ICSE boards with in-depth theory.")

with c2:
    st.markdown("### **CBSE**")
    st.caption("Grade 10th")
    st.write("**PCM Focus**")
    st.write("Specialized NCERT deep-dives and previous year paper analysis.")

with c3:
    st.markdown("### **Maths**")
    st.caption("Grade 11th")
    st.write("**All Boards**")
    st.write("Transitioning to higher-order thinking for 11th and JEE entrance.")

st.divider()

# --- Lead Generation via FormSubmit ---
st.header("📩 Book a Free Demo Session")
st.write("Submit your details below. An IITian/NITian mentor will call you back within 24 hours.")

# IMPORTANT: Change this to your actual email address
your_email = "vibhuagarwal1998@gmail.com" 

contact_form = f"""
<form action="https://formsubmit.co/{your_email}" method="POST">
     <input type="text" name="_honey" style="display:none">
     
     <input type="hidden" name="_captcha" value="false">
     
     <input type="hidden" name="_next" value="https://highermarks.streamlit.app/">

     <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #31333F;">Student Name</label>
        <input type="text" name="name" placeholder="Enter student name" style="width: 100%; padding: 12px; border: 1px solid #dcdfe6; border-radius: 5px;" required>
     </div>

     <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #31333F;">Parent's Phone Number</label>
        <input type="tel" name="phone" placeholder="10-digit mobile number" style="width: 100%; padding: 12px; border: 1px solid #dcdfe6; border-radius: 5px;" required>
     </div>

     <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #31333F;">Course Interest</label>
        <select name="course" style="width: 100%; padding: 12px; border: 1px solid #dcdfe6; border-radius: 5px; background-color: white;">
            <option value="ICSE 8-10">ICSE PCM (8th-10th)</option>
            <option value="CBSE 10">CBSE PCM (10th)</option>
            <option value="Class 11 Maths">Class 11th Maths (All Boards)</option>
        </select>
     </div>

     <div style="margin-bottom: 15px;">
        <label style="font-weight: bold; color: #31333F;">Notes/Goals</label>
        <textarea name="message" placeholder="e.g. Preparing for JEE, need help in Physics..." style="width: 100%; padding: 12px; border: 1px solid #dcdfe6; border-radius: 5px; height: 80px;"></textarea>
     </div>

     <button type="submit" style="background-color: #ff4b4b; color: white; border: none; padding: 14px; border-radius: 5px; width: 100%; cursor: pointer; font-size: 16px; font-weight: bold;">
        Request Call Back
     </button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# --- Footer ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center'>
    <p><strong>HigherMarks Academic Center</strong></p>
    <p style='font-size: 0.85em; color: #666;'>Quality Education by IITians & NITians | Serving Thane & Mumbai</p>
</div>
""", unsafe_allow_html=True)
