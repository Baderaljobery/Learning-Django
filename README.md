Django Models & ORM Implementation — Learning Notes
Introduction

In this task, I learned how to work with Django models and the Object Relational Mapper (ORM) to design and manage database structures in a Django application. The goal of the task was to understand how Django models represent database tables, how relationships between models are defined, and how to store flexible AI-generated data using JSONField.

Understanding Django Models

A Django Model is a Python class that represents a table in the database. Each attribute of the model corresponds to a database column, and each instance of the model represents a row in the table.

Using Django models allows developers to define the database schema using Python code instead of writing SQL directly.

Example concept:

Model → Database Table

Model Field → Table Column

Model Instance → Table Row

This abstraction simplifies database interaction and ensures a clean and maintainable project structure.

Implemented Models

In this project, I implemented the following models to simulate a simple recruitment system.

Organization

The Organization model represents companies that post job opportunities.

Fields included:

name

website

created_at

This model stores information about organizations that create job postings.

JobPosting

The JobPosting model represents job opportunities created by organizations.

Fields included:

organization (ForeignKey)

title

description

location

created_at

Relationship

A ForeignKey relationship was used between JobPosting and Organization.

This creates a One-to-Many relationship, meaning:

One organization can create multiple job postings

Each job posting belongs to only one organization

Candidate

The Candidate model represents individuals applying for jobs.

Fields included:

first_name

last_name

email

phone

created_at

This model stores the candidate's personal information.

Resume

The Resume model represents uploaded resumes for candidates.

Fields included:

candidate (ForeignKey)

file

ai_extracted_skills

created_at

Relationship

A ForeignKey relationship connects Resume to Candidate, meaning:

One candidate can have multiple resumes

Each resume belongs to one candidate

The on_delete=models.CASCADE option ensures that when a candidate is deleted, all related resumes are also deleted automatically.

Using JSONField for AI Generated Data

The Resume model includes a JSONField named ai_extracted_skills.

This field allows storing structured JSON data inside the database. It is especially useful when dealing with flexible or dynamic data structures that may vary between records.

In this project, the JSONField is used to store skills extracted automatically from resumes using AI.

Example structure:

{
 "languages": ["Python", "JavaScript"],
 "frameworks": ["Django", "React"],
 "tools": ["Git", "Docker"]
}

Using JSONField allows the system to store complex skill information without creating multiple additional database tables.

Django ORM (Object Relational Mapper)

Django provides an ORM that allows developers to interact with the database using Python code instead of raw SQL queries.

For example:

Creating a record:

Candidate.objects.create(...)

Retrieving records:

Candidate.objects.all()

Filtering data:

Candidate.objects.filter(first_name="Bader")

The ORM simplifies database operations and improves code readability and maintainability.

Testing the Implementation

To test the models and database interactions, I used:

Django Admin Panel

Django Shell

ORM queries

Through the Django admin interface, I was able to:

Create organizations

Add job postings

Register candidates

Upload resumes

Store AI-extracted skills in JSON format

This confirmed that the relationships between models and the JSONField functionality were working correctly.

Key Concepts Learned

During this task, I learned several important Django backend development concepts:

How Django models represent database tables

How to define relationships using ForeignKey

How on_delete=models.CASCADE works

How to use JSONField to store flexible structured data

How to use Django ORM to create and query database records

How to manage database schema using migrations

How to test models using Django Admin and Django Shell

Conclusion

This task helped me understand the core concepts of Django database modeling and ORM usage. By implementing a small recruitment system, I gained practical experience in defining models, creating relationships, storing structured JSON data, and interacting with the database using Django ORM.

These concepts form the foundation of backend development with Django and are essential for building scalable web applications.
