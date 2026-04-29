<!-- nav -->
[← Day 98](../Day98/lesson.md) | [🏠 Home](../../) | [Day 100 →](../Day100/lesson.md)

---
<!-- nav -->

# Day 99 – Deploying Python Projects

## Learning Objectives
- Understand the main Python deployment options
- Deploy a Flask app to a free PaaS platform
- Write environment-safe configuration

---

## Deployment Options

| Option | Best For | Cost |
|--------|---------|------|
| Render | Flask/FastAPI web apps | Free tier |
| Railway | Any web app + DB | Free tier |
| Fly.io | Dockerised apps | Free tier |
| PythonAnywhere | Simple Flask/Django | Free tier |
| Heroku | Classic PaaS | Paid |
| AWS Lambda | Serverless functions | Pay per use |

---

## Preparing a Flask App for Deployment

### 1. Create `requirements.txt`
```bash
pip freeze > requirements.txt
```

### 2. Use environment variables, not hardcoded values
```python
import os
SECRET_KEY = os.environ["SECRET_KEY"]
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///local.db")
```

### 3. Use a production WSGI server
```bash
pip install gunicorn
# requirements.txt should include gunicorn
```

### 4. `Procfile` (for Heroku/Render)
```
web: gunicorn app:app
```

---

## Deploying to Render

1. Push your project to GitHub
2. Create a new **Web Service** on render.com
3. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Add environment variables in the Render dashboard
5. Deploy — Render gives you a `*.onrender.com` URL

---

## Security Before Going Live

- [ ] `debug=False` in production
- [ ] `SECRET_KEY` is a long random string from env var
- [ ] No `.env` or `*.db` in git
- [ ] HTTPS only (Render provides this automatically)

---

## Key Takeaways
- Never run `debug=True` in production — it exposes your source code
- All secrets belong in environment variables, never in code
- Render is the easiest free option for Python web apps right now

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week14/Day99/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 98](../Day98/lesson.md) | [Day 100 →](../Day100/lesson.md)
<!-- nav -->
