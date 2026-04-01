import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="HigherMarks | IITian Led Coaching", page_icon="📈")

# --- Google Sheets Connection ---
# This looks for credentials in your .streamlit/secrets.toml file
conn = st.connection("gsheets", type=GSheetsConnection)

# Header Section
st.markdown("# 📈 HigherMarks")
st.subheader("Elevating Education with Mentors from IITs and NITs")
st.divider()

# --- Courses Section (Simplified for this example) ---
st.header("📚 Our Programs")
col1, col2, col3 = st.columns(3)
with col1: st.write("**ICSE 8th-10th PCM**")
with col2: st.write("**CBSE 10th PCM**")
with col3: st.write("**Class 11th Maths**")

st.divider()

# --- Lead Generation Form ---
st.header("📩 Get Started with HigherMarks")
with st.form("inquiry_form", clear_on_submit=True):
    name = st.text_input("Student Name")
    parent_phone = st.text_input("Parent's Contact Number")
    course = st.selectbox("Select Interest", [
        "ICSE PCM (8th-10th)", 
        "CBSE PCM (10th)", 
        "Class 11th Maths (All Boards)"
    ])
    note = st.text_area("Any specific academic goals?")
    
    submitted = st.form_submit_button("Request Call Back")

if submitted:
    if name and parent_phone:
        # Create a dataframe for the new lead
        new_lead = pd.DataFrame([{
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Phone": parent_phone,
            "Course": course,
            "Note": note
        }])

        # 1. Read existing data
        existing_data = conn.read(worksheet="Sheet1", usecols=[0,1,2,3,4])
        
        # 2. Append new lead
        updated_df = pd.concat([existing_data, new_lead], ignore_index=True)
        
        # 3. Update the Google Sheet
        conn.update(worksheet="Sheet1", data=updated_df)
        
        st.success("✅ Inquiry sent! An IITian/NITian mentor will call you shortly.")
    else:
        st.error("Please provide a name and contact number.")