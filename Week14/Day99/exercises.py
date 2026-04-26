# Day 99 – Deploying Python Projects

import os

# Exercise 1: Simulate environment-safe Flask configuration.

def create_app_config():
    """Build app configuration from environment variables with safe defaults."""
    return {
        "SECRET_KEY":   os.environ.get("SECRET_KEY", "dev-only-key-change-in-prod"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", "sqlite:///local.db"),
        "DEBUG":        os.environ.get("FLASK_DEBUG", "0") == "1",
        "PORT":         int(os.environ.get("PORT", 5000)),
    }

config = create_app_config()
print("App config:")
for k, v in config.items():
    # Mask the secret key value
    display = "****" if "SECRET" in k else v
    print(f"  {k:<15} = {display}")


# Exercise 2: Check a production readiness list.

PROD_CHECKLIST = [
    ("SECRET_KEY is not the default",           os.environ.get("SECRET_KEY", "") not in ("", "dev-only-key-change-in-prod")),
    ("FLASK_DEBUG is not 1",                    os.environ.get("FLASK_DEBUG", "0") != "1"),
    ("requirements.txt exists",                 os.path.exists("requirements.txt")),
    (".env is not committed (gitignore check)", True),   # manual check
    ("No hardcoded DB path in source",          True),   # manual check
]

print("\nProduction Readiness Checklist:")
all_pass = True
for item, ok in PROD_CHECKLIST:
    status = "✓" if ok else "✗  ← FIX THIS"
    if not ok:
        all_pass = False
    print(f"  [{status}] {item}")
print("Overall:", "Ready to deploy ✓" if all_pass else "Fix issues before deploying ✗")


# Exercise 3: Generate a Procfile and runtime.txt for Render/Heroku deployment.

PROCFILE  = "web: gunicorn app:app"
RUNTIME   = "python-3.12.0"

print(f"\nProcfile:\n  {PROCFILE}")
print(f"\nruntime.txt:\n  {RUNTIME}")


# Exercise 4: Print the deployment checklist steps.

STEPS = [
    "1. pip freeze > requirements.txt",
    "2. Add gunicorn to requirements.txt",
    "3. Create Procfile: web: gunicorn app:app",
    "4. Push to GitHub",
    "5. Create Render Web Service → connect repo",
    "6. Set environment variables in Render dashboard",
    "7. Deploy — get your .onrender.com URL",
]
print("\nDeploy to Render — steps:")
for step in STEPS:
    print(f"  {step}")
