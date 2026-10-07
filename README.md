# 🤖 AI Employee Database Agent

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-Function%20Calling-412991?logo=openai&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)

An AI agent that manages an employee database using **plain English**.
Instead of writing SQL, you just type what you want, such as *"Find employees from Kolkata"* or *"Add Rahul as an IT employee with salary 55000"*, and the agent works out which database action to run.

---

## 📌 Table of Contents

- [Demo](#-demo)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Agent Tools](#-agent-tools)
- [Database Schema](#-database-schema)
- [Design Notes](#-design-notes)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🎬 Demo

> Add a screenshot or GIF of the app here.
>
> `![App Screenshot](screenshots/app.png)`

**Example conversation:**

| You type | Agent does |
|---|---|
| `How many employees are there?` | Calls `count_employees()` and replies with the number |
| `Find employees from Kolkata` | Calls `search_by_city("Kolkata")` and lists the matches |
| `Who has the highest salary?` | Calls `highest_salary()` |
| `Find employees earning between 40000 and 60000` | Calls `search_by_salary(40000, 60000)` |
| `Update employee 1 salary to 65000` | Calls `update_employee(...)` |

---

## ✨ Features

- 💬 **Natural-language interface**: no SQL knowledge needed
- 🗂️ **Full CRUD**: create, read, update and delete employee records
- 🔍 **Smart search**: by name, department, city and salary range
- 📊 **Quick analytics**: employee count, highest salary, department-wise salary search
- 🖥️ **Streamlit web app** with 3 tabs: AI Agent, Employee table, About
- ⌨️ **Terminal mode** for quick testing
- 🛡️ **Safe by design**: the AI never runs raw SQL, it can only call predefined Python functions
- 🔁 **Multi-step tool loop**: the agent can call several tools in a row before giving the final answer

---

## 🧠 How It Works

```
┌──────────┐   question   ┌──────────────┐  picks a tool  ┌───────────────┐   SQL    ┌──────────┐
│   User   │ ───────────▶ │ OpenAI model │ ─────────────▶ │ Python tool   │ ───────▶ │  SQLite  │
│          │              │ (agent loop) │                │ (database.py) │          │ database │
└──────────┘              └──────────────┘                └───────────────┘          └──────────┘
      ▲                          ▲                                 │
      │      final answer        │          tool result            │
      └──────────────────────────┴─────────────────────────────────┘
```

1. The user types a request in natural language.
2. The model reads it and decides **which function (tool) to call** and with what arguments. This is **function calling**.
3. `agent.py` runs the chosen Python function, which talks to SQLite.
4. The result is sent back to the model.
5. The model repeats steps 2–4 if it needs more data, then writes a clear, human-friendly answer.

> The model **never writes or executes SQL directly**. It can only use the tools defined in this project.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| AI / LLM | OpenAI API (Responses API + function calling) |
| Database | SQLite (`sqlite3`) |
| Frontend | Streamlit |
| Config | python-dotenv |

---

## 📁 Project Structure

```
.
├── app.py              # Streamlit web interface
├── agent.py            # OpenAI agent: tool definitions + ask_agent() loop
├── database.py         # SQLite connection + CRUD and search functions
├── test_agent.py       # Chat with the agent in the terminal
├── test_database.py    # Quick test of the database functions
├── requirements.txt    # Python dependencies
├── employees.db        # SQLite database (auto-created on first run)
└── .devcontainer/      # GitHub Codespaces / dev container config
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- An [OpenAI API key](https://platform.openai.com/api-keys)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a file named `.env` in the project folder:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`.

---

## ▶️ Usage

### Web app (Streamlit)

```bash
streamlit run app.py
```

Open the local URL shown in the terminal (usually `http://localhost:8501`).

### Terminal mode

```bash
python test_agent.py
```

Type your question and press Enter. Type `exit` to quit.

### Example prompts

```text
Show all employees.
How many employees are there?
Find employees from IT.
Find employees from Kolkata.
Who has the highest salary?
Find employees earning between 40000 and 60000.
Add Riya as a Marketing employee with salary 47000.
Update employee 2 city to Mumbai.
Delete employee 5.
```

---

## 🧰 Agent Tools

These are the functions the AI is allowed to call (defined in `agent.py`, implemented in `database.py`):

| Tool | Purpose |
|---|---|
| `create_employee` | Add a new employee |
| `get_employee` | Get one employee by ID |
| `get_all_employees` | List every employee |
| `update_employee` | Update an employee's details |
| `delete_employee` | Remove an employee by ID |
| `search_by_name` | Partial name search |
| `search_by_department` | Filter by department |
| `search_by_city` | Filter by city |
| `search_by_salary` | Filter by salary range |
| `search_department_salary` | Combine department and salary filters |
| `count_employees` | Total number of employees |
| `highest_salary` | Employee with the highest salary |

---

## 🗄️ Database Schema

Table: **`employees`**

| Column | Type | Constraints |
|---|---|---|
| `id` | INTEGER | Primary key, auto-increment |
| `name` | TEXT | Not null |
| `email` | TEXT | Not null, **unique** |
| `department` | TEXT | Not null |
| `salary` | REAL | Not null |
| `city` | TEXT | Not null |

---

## 📝 Design Notes

- **Parameterized queries**: all SQL uses `?` placeholders, which protects against SQL injection.
- **Duplicate protection**: emails must be unique. The agent returns a friendly message if one already exists.
- **Careful deletes**: the system instructions tell the agent to delete only when the request clearly identifies the employee.
- **No made-up data**: the agent is told to always use database tools and never invent employee information.
- **Structured tool schemas**: tools use strict JSON schemas, so the model must pass correctly typed arguments.

---

## 🔮 Future Improvements

- [ ] Chat-style history in the Streamlit UI
- [ ] Confirmation step before delete/update actions
- [ ] User login and role-based access (HR vs. employee)
- [ ] Charts and dashboards (salary by department, headcount by city)
- [ ] Export results to CSV / Excel
- [ ] Switch to PostgreSQL / MySQL for larger datasets
- [ ] Add unit tests with `pytest`
- [ ] Deploy on Streamlit Community Cloud

---

## 👤 Author

**Tuhin Roy**
Final-year BCA student, JIS University, Kolkata
Interested in Data Analytics, SQL and AI/ML

- GitHub: [@your-username](https://github.com/your-username)
---

⭐ If you found this project useful, consider giving it a star!
