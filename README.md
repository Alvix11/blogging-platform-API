# 📝 Blogging Platform API

### 🧾 Description

* REST API to manage posts (create, read, update, delete) built with Django and Django REST Framework. Ideal for learning or as a base for a blog or content microservice.

---

### **Main Features**

* ✅ CRUD operations for posts
* ✅ DRF-based serializers and views
* ✅ Environment variable configuration (.env)
* ✅ PostgreSQL support
* ✅ Basic tests included

---

### **Installation**

1. **Clone the repository:**

```bash
git clone <https://github.com/Alvix11/blogging-platform-API.git>
cd blogging-platform-API
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Set up environment variables:**

* Copy the example file and edit the real values:

```bash
cp core/.env.example core/.env
# then edit core/.env and place your actual values
```

4. **Create the database and user in PostgreSQL (example):**

```bash
sudo -u postgres createuser --pwprompt Juansito
sudo -u postgres createdb blog_api -O Juansito
# or inside psql:
# CREATE USER alvix WITH PASSWORD 'your_password';
# CREATE DATABASE blog_api OWNER Juansito;
```

5. **Run migrations and create a superuser:**

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

### **Usage**

* Start the development server:

```bash
python manage.py runserver
```

* Common entry points:

  * Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  * API Root: Located at / (default) and configured in core/urls.py. Provides the main navigation point for all API endpoints.

---

### **Optional Configuration (Environment Variables)**

* `core/.env` (do not upload to the repository)

  * DB_NAME=your_db_name
  * DB_USER=your_db_user
  * DB_PASSWORD=your_db_password
  * DB_HOST=localhost
  * DB_PORT=5432
  * SECRET_KEY=your_secret_key
  * DEBUG=False

**Note:** Values like `DB_HOST=localhost` and `DB_PORT=5432` are not sensitive.
Sensitive values include `DB_PASSWORD` and `SECRET_KEY`.

---

### **Technologies Used**

* Python
* Django 5.x
* Django REST Framework
* PostgreSQL
* python-dotenv
* psycopg2-binary

---

### **Project Structure (Summary)**

* `core/` — Django configuration, .env, settings, urls, wsgi/asgi
* `posts/` — main app (models, views, serializers, tests)
* `requirements.txt` — dependencies
* `.gitignore` — excluded files
* `core/.env.example` — sample environment variables

---

### **License**

* MIT License — see [LICENSE](LICENSE)

---

### **Author**

* **Alvin Angulo**

  * GitHub: [https://github.com/alvix11](https://github.com/alvix11)
  * LinkedIn: [https://www.linkedin.com/in/alvin-angulo](https://www.linkedin.com/in/alvin-angulo)

---

### **Final Notes**

* Make sure `core/.env` is included in `.gitignore` to avoid uploading sensitive credentials.
* Adjust any DRF settings in `core/settings.py` according to your environment if needed.
* This project is based on the learning and practice projects suggested by [roadmap.sh](https://roadmap.sh/projects/blogging-platform-api), a popular resource for developers.

---