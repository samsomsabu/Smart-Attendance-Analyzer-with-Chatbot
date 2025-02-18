import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import calendar

# Load Hugging Face model and tokenizer (cached for performance)
@st.cache_resource
def load_model():
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()

# Summarize key insights from the attendance data
def summarize_attendance_data(df):
    summary = {
        "total_students": len(df["Student_ID"].unique()),
        "total_days": df["Date"].nunique(),
        "most_absent_student": int(df[df["Present"] == 0]["Student_ID"].value_counts().idxmax()),
        "most_absent_days": str(df[df["Present"] == 0]["Date"].value_counts().idxmax().date()),
        "total_absences": len(df[df["Present"] == 0]),
    }
    return summary

# Visualize patterns in attendance data
def analyze_patterns(attendance_df):
    st.subheader("📊 Attendance Pattern Visualizations")

    # Morning hour skipping pattern
    attendance_df["Is_Morning"] = attendance_df["Time_Slot"].str.contains("9:00|10:00").astype(int)
    morning_absences = attendance_df[(attendance_df["Is_Morning"] == 1) & (attendance_df["Present"] == 0)]
    top_morning_skippers = morning_absences["Student_ID"].value_counts().head(10)
    st.write("### Top Morning Skippers (9:00 AM - 10:00 AM)")
    st.bar_chart(top_morning_skippers)

    # Last hour skipping pattern
    attendance_df["Is_Last_Hour"] = attendance_df["Time_Slot"].str.contains("2:00|3:00|4:00").astype(int)
    last_hour_absences = attendance_df[(attendance_df["Is_Last_Hour"] == 1) & (attendance_df["Present"] == 0)]
    top_last_hour_skippers = last_hour_absences["Student_ID"].value_counts().head(10)
    st.write("### Top Last Hour Skippers (2:00 PM - 4:00 PM)")
    st.bar_chart(top_last_hour_skippers)

    # Absences by weekday
    attendance_df["Date"] = pd.to_datetime(attendance_df["Date"])
    attendance_df["Weekday"] = attendance_df["Date"].dt.day_name()
    day_wise_absences = attendance_df[attendance_df["Present"] == 0]["Weekday"].value_counts()
    st.write("### Absences by Weekday")
    st.bar_chart(day_wise_absences)

    # Monthly absence pattern
    attendance_df["Month"] = attendance_df["Date"].dt.month
    monthly_absences = attendance_df[attendance_df["Present"] == 0].groupby("Month").size()
    st.write("### Monthly Absences")
    st.line_chart(monthly_absences)

# Rule-based response for specific queries
def rule_based_response(question, attendance_df):
    question = question.lower()

    if "month" in question and "absence" in question:
        monthly_absences = attendance_df[attendance_df['Present'] == 0].groupby(attendance_df['Date'].dt.month).size()
        top_months = monthly_absences.sort_values(ascending=False).head(3)
        top_month_names = [calendar.month_name[month] for month in top_months.index]
        top_month_absences = top_months.tolist()
        return f"The months with the highest absences are: {', '.join(top_month_names)} with absences: {top_month_absences}."

    elif "monday" in question and "absence" in question:
        monday_absences = attendance_df[attendance_df['Date'].dt.weekday == 0]['Present'].value_counts().get(0, 0)
        return f"There were {monday_absences} absences on Mondays."

    elif "most absent student" in question or "student with most absences" in question:
        most_absent_student = attendance_df[attendance_df['Present'] == 0]["Student_ID"].value_counts().idxmax()
        return f"The student with the most absences is Student ID {most_absent_student}."

    elif "total absences" in question:
        total_absences = len(attendance_df[attendance_df["Present"] == 0])
        return f"The total number of absences is {total_absences}."

    elif "top students skipping morning" in question or "morning hour skippers" in question:
        attendance_df["Is_Morning"] = attendance_df["Time_Slot"].str.contains("9:00|10:00").astype(int)
        morning_absences = attendance_df[(attendance_df["Is_Morning"] == 1) & (attendance_df["Present"] == 0)]
        top_morning_skippers = morning_absences["Student_ID"].value_counts().head(5)
        if not top_morning_skippers.empty:
            return f"The top students skipping morning hours are: {', '.join(str(sid) for sid in top_morning_skippers.index)}."
        else:
            return "There are no significant morning hour skippers."

    elif "top students skipping last hour" in question or "last hour skippers" in question:
        attendance_df["Is_Last_Hour"] = attendance_df["Time_Slot"].str.contains("2:00|3:00|4:00").astype(int)
        last_hour_absences = attendance_df[(attendance_df["Is_Last_Hour"] == 1) & (attendance_df["Present"] == 0)]
        top_last_hour_skippers = last_hour_absences["Student_ID"].value_counts().head(5)
        if not top_last_hour_skippers.empty:
            return f"The top students skipping the last hours are: {', '.join(str(sid) for sid in top_last_hour_skippers.index)}."
        else:
            return "There are no significant last-hour skippers."

    return None

# Chatbot powered by Hugging Face LLM (fallback)
def chatbot_response(summary, user_query):
    prompt = (
        f"The attendance data summary is as follows:\n"
        f"- Total number of students: {summary['total_students']}\n"
        f"- Total number of days: {summary['total_days']}\n"
        f"- Student ID with most absences: {summary['most_absent_student']}\n"
        f"- Date with the most absences: {summary['most_absent_days']}\n"
        f"- Total number of absences: {summary['total_absences']}\n\n"
        f"User's Question: {user_query}\n"
        f"Please analyze the patterns and provide a detailed and easy-to-understand answer."
    )
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs, max_length=150, num_beams=4, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit Web App
st.title("📅 Attendance Insights & Chatbot")
st.write("Upload an attendance CSV file and analyze attendance patterns. You can also chat with the bot for insights.")

# File upload section
uploaded_file = st.file_uploader("📤 Upload CSV File", type=["csv"])

if uploaded_file is not None:
    attendance_df = pd.read_csv(uploaded_file)
    st.write("### Sample of Uploaded Data")
    st.dataframe(attendance_df.head())

    # Pattern analysis and visualization
    analyze_patterns(attendance_df)

    # Summarize attendance data
    summary = summarize_attendance_data(attendance_df)
    st.write("### Attendance Data Summary")
    st.write(summary)

    # Chatbot Section
    st.subheader("🤖 Ask the Attendance Chatbot")
    user_query = st.text_input("What would you like to know about the attendance data?")
    if user_query:
        rule_response = rule_based_response(user_query, attendance_df)
        if rule_response:
            st.write("### Chatbot's Response:")
            st.write(rule_response)
        else:
            response = chatbot_response(summary, user_query)
            st.write("### Chatbot's Response:")
            st.write(response)
