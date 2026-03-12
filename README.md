# Django Models & ORM Implementation — Learning Notes

![Django](https://img.shields.io/badge/Framework-Django-092e20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Language-Python-3776ab?style=for-the-badge&logo=python&logoColor=white)
![Database](https://img.shields.io/badge/Database-ORM-blue?style=for-the-badge)

## 📌 Project Overview
This project demonstrates the core concepts of **Django Models** and the **Object Relational Mapper (ORM)**. I designed a database structure for a recruitment system to manage organizations, job postings, and candidates, while integrating modern data handling techniques like `JSONField` for AI-extracted information.

---

## 🏗️ Implemented Architecture

### 1. Database Schema & Models
The system is built on four main models, each serving a specific purpose in the recruitment workflow:

* **Organization:** Stores company details (Name, Website, Timestamp).
* **JobPosting:** Manages job roles linked to specific organizations.
* **Candidate:** Records personal information of applicants.
* **Resume:** Handles file uploads and AI-processed skill data.

### 2. Relationships & Logic
| Relationship | Type | Description |
| :--- | :--- | :--- |
| **Organization → JobPosting** | One-to-Many | One organization can host multiple job listings. |
| **Candidate → Resume** | One-to-Many | A candidate can upload multiple resume versions. |
| **Data Integrity** | `CASCADE` | Deleting a parent record (e.g., Candidate) automatically cleans up related children (e.g., Resumes). |

---

## 🧠 Technical Highlights

### ⚡ Power of Django ORM
Using the ORM allowed me to interact with the database using pure Python, avoiding manual SQL.
- **Creation:** `Candidate.objects.create(...)`
- **Retrieval:** `Candidate.objects.all()`
- **Filtering:** `Candidate.objects.filter(first_name="Bader")`

### 🤖 Flexible AI Data with `JSONField`
I implemented a `JSONField` in the `Resume` model to store skills extracted by AI. This allows for a dynamic data structure without requiring extra tables.
**Example Entry:**
```json
{ 
  "languages": ["Python", "JavaScript"], 
  "frameworks": ["Django", "React"], 
  "tools": ["Git", "Docker"] 
}

🚀 Key Learning Outcomes
[x] Defining database schemas using Pythonic Models.

[x] Establishing relational constraints using Foreign Keys.

[x] Implementing on_delete behaviors to maintain database health.

[x] Utilizing JSONField for semi-structured data storage.

[x] Testing backend logic through Django Admin and Django Shell.

[x] Managing database evolution with Migrations.

🛠️ Local Setup
Clone the repository:

Bash
git clone [https://github.com/Baderaljobery/Learning-Django.git](https://github.com/Baderaljobery/Learning-Django.git)
Apply migrations:

Bash
python manage.py migrate
Create a superuser to access the Admin Panel:

Bash
python manage.py createsuperuser
Run the development server:

Bash
python manage.py runserver
