# Day 93 – Optimising Your GitHub Profile

# Exercise 1: Generate a GitHub profile README.md in Markdown format.

def github_profile_readme(username, name, bio, tech_stack, projects):
    lines = [
        f"# Hi, I'm {name} 👋",
        "",
        bio,
        "",
        "## 🛠 Tech Stack",
    ]
    for tech in tech_stack:
        badge = tech.replace(" ", "%20")
        lines.append(f"![{tech}](https://img.shields.io/badge/{badge}-blue?style=flat-square)")
    lines += [
        "",
        "## 🚀 Featured Projects",
        "",
        "| Project | Description | Tech |",
        "|---------|-------------|------|",
    ]
    for p in projects:
        lines.append(f"| [{p['name']}](https://github.com/{username}/{p['repo']}) | {p['desc']} | {p['tech']} |")
    lines += [
        "",
        "## 📊 GitHub Stats",
        f"![Stats](https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=default)",
        "",
        "---",
        f"*Built with Python in 100 Days 🐍*",
    ]
    return "\n".join(lines)


readme = github_profile_readme(
    username   = "nikunjjakhotia",
    name       = "Nikunj Jakhotia",
    bio        = "Python developer | Automation & Data Analysis enthusiast",
    tech_stack = ["Python", "Flask", "SQLite", "pandas"],
    projects   = [
        {"name": "Expense Tracker",    "repo": "expense-tracker",    "desc": "CLI finance tracker",    "tech": "Python, SQLite"},
        {"name": "Weather Dashboard",  "repo": "weather-dashboard",  "desc": "Live weather CLI",       "tech": "Python, requests"},
        {"name": "File Organiser Bot", "repo": "file-organiser-bot", "desc": "Automation file sorter", "tech": "Python, pathlib"},
    ],
)
print(readme)


# Exercise 2: Generate conventional commit messages for common actions.

def commit_msg(type_, scope, description):
    return f"{type_}({scope}): {description}" if scope else f"{type_}: {description}"

commits = [
    commit_msg("feat",     "db",       "add monthly summary query"),
    commit_msg("fix",      "validation","reject negative expense amounts"),
    commit_msg("docs",     "readme",    "add Quick Start installation steps"),
    commit_msg("test",     "db",        "add unit tests for add_expense"),
    commit_msg("refactor", "reports",   "extract format_expense helper"),
    commit_msg("chore",    None,        "add .gitignore for venv and .env"),
]

print("\n--- Conventional Commits ---")
for msg in commits:
    print(f"  git commit -m \"{msg}\"")
