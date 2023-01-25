# Lesson 13

- Discussed how to make migration if we use migration previously with custom validators, and now we deleted the validator (--> delete validator from migration file (where init etc) ).
- Created new from UpdateStudentForm with the same model to edit existed student and show only these fields we want (from CreateStudentForm differ only "fields" list) 
- Templates (finally, changed all my last "shitcode" to normal templates)

Homework:

1. Add Teachers App \
1.5. Add fields to the model:
   - name
   - surname 
   - Date of Birth 
   - salary 
   - Field options are up to you.

2. Add templates to display:
   - group list
   - group details 
   - list of teachers 
   - detailed information about teachers

3. Add view functions and routes for:
   - group editing 
   - displaying detailed information about the group 
   - teacher editing 
   - displaying detailed information about the teacher

From lesson_9 Homework is here:
- [homework 13](https://github.com/0xDyno/django-lms/pull/4/commits/bbd5d9e03ae3c8123feaa3a99ec47bbb90835022)
- [Whole project "django-lms"](https://github.com/0xDyno/django-lms)