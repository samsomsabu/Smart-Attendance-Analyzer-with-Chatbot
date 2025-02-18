# 📅 **Attendance Insights & Chatbot System**

## 📄 **Project Overview**
The **Attendance Insights & Chatbot System** is a comprehensive data analysis and interactive chatbot tool designed to analyze student attendance patterns, visualize trends, and provide quick insights into student behavior. The chatbot is powered by a combination of **rule-based logic** and **natural language processing (NLP)** using **Hugging Face Transformers**.

This project aims to help educational institutions monitor attendance patterns, identify students with irregular attendance, and gain data-driven insights for better decision-making.

---

## 🛠️ **Key Features**
- **CSV Data Upload:** Upload attendance data in CSV format.
- **Visual Data Analysis:** Graphical representation of key attendance patterns.
  - Morning hour skippers
  - Last-hour skippers
  - Weekday absences
  - Monthly absences
- **Rule-Based Query System:** Quick answers to common attendance-related questions.
- **AI-Powered Chatbot:** Answers complex queries using **Hugging Face's Flan-T5 model**.
- **Summary Statistics:** Instant overview of key attendance insights.

---

## 🧑‍💻 **Tech Stack**
| Component              | Technology                                                                 |
|------------------------|----------------------------------------------------------------------------|
| Programming Language    | Python                                                                    |
| Data Analysis           | Pandas, NumPy                                                             |
| Data Visualization      | Matplotlib, Streamlit                                                     |
| Machine Learning (NLP)  | Hugging Face Transformers (Flan-T5 Model)                                 |
| Web Application         | Streamlit                                                                 |

---

## 📊 **Data Requirements**
The uploaded **CSV file** should have the following columns:
| Column Name | Description                                           | Example                          |
|-------------|-------------------------------------------------------|-----------------------------------|
| `Student_ID`| Unique identifier for each student                    | `1001`, `1002`                   |
| `Date`      | Date of attendance (in `YYYY-MM-DD` format)           | `2025-01-15`                     |
| `Time_Slot` | Time slot representing the class timing               | `9:00 - 10:00 AM`                |
| `Present`   | Attendance status (1 for Present, 0 for Absent)       | `1` or `0`                       |

Ensure the CSV file is clean and formatted correctly before uploading.

---

## 🚀 **How to Run the Project**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/attendance-insights-chatbot.git
cd attendance-insights-chatbot
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Streamlit App**
```bash
streamlit run app.py
```

### 4️⃣ **Upload CSV File & Explore Insights**
- Upload your attendance CSV file.
- View visual insights and summary statistics.
- Ask the chatbot specific questions about the data.

---

## 📥 **Example Questions for Chatbot**
Here are some sample queries to ask the chatbot:
- **Which months had the highest absences?**
- **Who are the top students skipping morning hours?**
- **Who are the top students skipping the last hour?**
- **What is the total number of absences?**
- **Who is the most absent student?**
- **On which day of the week are absences the highest?**

---

## 📸 Screenshots

### Visualizations
| Attendance Patterns | Morning Skippers | Last Hour Skippers | Monthly Absences |
|---------------------|------------------|--------------------|------------------|
| ![Visualization 1](https://github.com/samsomsabu/Smart-Attendance-Analyzer-with-Chatbot/blob/main/Screenshot%202025-02-18%20120020.png) | ![Visualization 2](https://github.com/samsomsabu/Smart-Attendance-Analyzer-with-Chatbot/blob/main/Screenshot%202025-02-18%20120034.png) | ![Visualization 3](https://github.com/samsomsabu/Smart-Attendance-Analyzer-with-Chatbot/blob/main/Screenshot%202025-02-18%20120042.png) | ![Visualization 4](https://github.com/samsomsabu/Smart-Attendance-Analyzer-with-Chatbot/blob/main/Screenshot%202025-02-18%20120051.png) |

### Chatbot Query Example
![Chatbot Query](https://github.com/samsomsabu/Smart-Attendance-Analyzer-with-Chatbot/blob/main/Screenshot%202025-02-18%20120113.png)


---

## 🧑‍💻 **Project Structure**
```
📁 attendance-insights-chatbot
│
├── 📄 app.py             # Main Streamlit application
├── 📄 requirements.txt   # Required libraries
└── 📄 README.md          # Project documentation
```

---

## 📦 **Dependencies**
```bash
streamlit==1.32.0
pandas==2.2.0
matplotlib==3.8.2
transformers==4.39.0
torch==2.2.0
```

---

## 🧑‍💼 **Future Enhancements**
- 📈 **Detailed Student Reports**: Individual student attendance trends.
- 📊 **Customizable Time Slots**: Flexibility to adapt to different institutional schedules.
- 🤖 **Advanced NLP Chatbot**: Integration of more advanced models for better responses.
- 📥 **Export Insights**: Download attendance reports as PDF/Excel.

---

## 📝 **License**
This project is licensed under the **MIT License**.

---

## 📧 **Contact**
For any questions, feel free to reach out via email:
- 📧 sabusamson40@gmail.com
- 🔗 [LinkedIn](www.linkedin.com/in/samson-sabu-8aab0a22b)
