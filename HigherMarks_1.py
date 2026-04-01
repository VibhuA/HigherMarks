import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="HigherMarks | IITian & NITian Led Coaching", 
    page_icon="📈",
    layout="centered"
)

# --- Google Sheets Connection ---
# Make sure your st.secrets contains the [connections.gsheets] section
conn = st.connection("gsheets", type=GSheetsConnection)

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
    st.write("- **Concept First:** We don't just teach formulas; we teach the 'why' behind them.")
    st.write("- **Result Oriented:** Specialized focus on conceptual depth and board patterns.")

with col2:
    st.info("**Our Expertise** \n\n Our educators have cleared the toughest exams in the country. We know the path because we've walked it.")

st.divider()

# --- Curriculum Section ---
st.header("📚 Our Programs")

card1, card2, card3 = st.columns(3)

with card1:
    st.markdown("### **ICSE**")
    st.caption("Grades 8th - 10th")
    st.write("**PCM Focus**")
    st.write("Comprehensive Physics, Chemistry, and Math with rigorous Board prep.")

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

# --- Lead Generation Form ---
st.header("📩 Get Started with HigherMarks")
st.write("Book a free demo session with our expert faculty.")

with st.form("inquiry_form", clear_on_submit=True):
    name = st.text_input("Student Name")
    parent_phone = st.text_input("Parent's Contact Number")
    course = st.selectbox("Select Interest", [
        "ICSE PCM (8th-10th)", 
        "CBSE PCM (10th)", 
        "Class 11th Maths (All Boards)"
    ])
    note = st.text_area("Any specific academic goals or concerns?")
    
    submitted = st.form_submit_button("Request Call Back")

if submitted:
    if name and parent_phone:
        try:
            # 1. Resilient Data Loading
            # This ensures we don't crash if the sheet is empty or being updated
            try:
                existing_data = conn.read(worksheet="Sheet1", ttl=0)
            except Exception:
                existing_data = pd.DataFrame(columns=["Timestamp", "Name", "Phone", "Course", "Note"])

            # 2. Create New Entry
            new_lead = pd.DataFrame([{
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Name": name,
                "Phone": parent_phone,
                "Course": course,
                "Note": note
            }])

            # 3. Append and Update
            # We handle cases where existing_data might be None or empty
            if existing_data is None or existing_data.empty:
                updated_df = new_lead
            else:
                updated_df = pd.concat([existing_data, new_lead], ignore_index=True)
            
            conn.update(worksheet="Sheet1", data=updated_df)
            
            st.success("✅ Inquiry sent! A HigherMarks mentor will call you shortly.")
            st.balloons()
            
        except Exception as e:
            st.error("We are experiencing a high volume of requests. Please try again in a few minutes.")
            # Log the error for you to see in Streamlit Cloud logs
            print(f"Error updating sheet: {e}")
    else:
        st.warning("Please provide both a name and a contact number so we can reach you.")

# --- Footer ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center'>
    <p><strong>HigherMarks Academic Center</strong></p>
    <p style='font-size: 0.8em;'>© 2026 HigherMarks Education | Taught by IITians & NITians</p>
</div>
""", unsafe_allow_html=True)
