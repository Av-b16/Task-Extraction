#  Task Extraction using Flask and NLP

This project extracts tasks, recognizes names, identifies deadlines, and categorizes tasks from user-input text using **Flask**, **Regex**, and **Natural Language Processing (NLP)**. The extracted tasks are displayed dynamically in a web interface with relevant information.

---

##  Features

- ✅ Recognizes and extracts tasks with names and deadlines.
- ✅ Categorizes tasks into relevant categories such as:
    - Shopping
    - Review
    - Submission
    - Meeting
    - General
- ✅ Handles multiple names and deadlines correctly within paragraphs.
- ✅ Provides a clean and interactive UI using Bootstrap.

---

##  Technologies Used

- Python (Flask)
- Regex for pattern matching
- Bootstrap for responsive design
- HTML, CSS, JavaScript for frontend


---

##  How It Works

1. **Input Text**: User enters text describing multiple tasks with deadlines and names.
2. **Task Extraction**: The `task_extractor.py` extracts:
   - Task description
   - Person’s name
   - Task deadline
   - Task category
3. **Display Results**: Tasks are displayed with relevant information on the results page.

---

## 🖥️ Setup and Installation

### 1. Clone the Repository
git clone https://github.com/Av-b16/Task-Extraction.git
cd Task-Extraction

2. Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
# or
venv\Scripts\activate     # For Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the Flask Application
python app.py
Visit http://127.0.0.1:5000 in your browser.

Usage-:
Open the web app.
Enter the text describing tasks with names and deadlines.
Click "Submit" to extract and categorize tasks.
View extracted tasks with details on the result page.