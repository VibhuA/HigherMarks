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
