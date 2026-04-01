import streamlit as st

# Page Configuration
st.set_page_config(page_title="HigherMarks | IITian & NITian Led Coaching", page_icon="📈")

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
    st.info("**Our Expertise** \n\n Our educators have cleared the toughest exams in the country. We know the path because we've walked it.")

st.divider()

# --- Curriculum Section ---
st.header("📚 Our Programs")

# Creating three columns for a "Card" look
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

# --- Lead Generation Form ---
st.header("📩 Get Started with HigherMarks")
st.write("Book a free demo session with our IITian faculty.")

with st.form("inquiry_form"):
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
        st.success(f"Success! HigherMarks will reach out to you shortly to discuss the {course} program.")
    else:
        st.error("Please provide a name and contact number.")

# --- Footer ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center'>
    <p><strong>HigherMarks Academic Center</strong></p>
    <p style='font-size: 0.8em;'>© 2026 HigherMarks Education | Taught by IITians & NITians</p>
</div>
""", unsafe_allow_html=True)