
import streamlit as st
import pandas as pd

# Sample Data
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math': [88, 76, 90, 70],
    'Science': [92, 65, 85, 75],
    'English': [85, 80, 78, 88]
}
df = pd.DataFrame(data)

# Title
st.title("🎓 Student Performance Tracker")

# Dropdown
student = st.selectbox("Select Student", df['Student'])

# Show Student Marks
student_data = df[df['Student'] == student]
st.write("Marks:", student_data)

# Slider to update marks
math_score = st.slider("Update Math Score", 0, 100, int(student_data['Math']))
science_score = st.slider("Update Science Score", 0, 100, int(student_data['Science']))
english_score = st.slider("Update English Score", 0, 100, int(student_data['English']))

# Button
if st.button("Update Scores"):
    df.loc[df['Student'] == student, ['Math', 'Science', 'English']] = [math_score, science_score, english_score]
    st.success("Scores Updated!")
    st.write(df)

# Show full table
st.dataframe(df)
