## Requirements

- Python (3.10.4)
- Django (5.0)

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/alizadasaleh/menus.git
   ```

2. **Set up a virtual environment:**

   - For Unix/MacOS:

     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

   - For Windows:

     ```
     py -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Set up the database (if applicable):**

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Load the data to the DB:**

   ```
   python manage.py web/seed/seed.json 
   ```
6. **Create a superuser:**

   ```
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```
   python manage.py runserver
   ```

   Now, you can access your application at `http://127.0.0.1:8000/`.


