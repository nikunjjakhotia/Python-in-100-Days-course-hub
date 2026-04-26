# Day 92 – Writing a Python Developer Resume

# Exercise 1: Generate a plaintext resume skeleton populated with your own details.

def generate_resume(name, email, github, linkedin, skills, projects, education):
    lines = [
        f"{name}",
        f"{email}  |  github.com/{github}  |  linkedin.com/in/{linkedin}",
        "",
        "SKILLS",
        "-" * 40,
    ]
    for category, items in skills.items():
        lines.append(f"  {category}: {', '.join(items)}")
    lines += ["", "PROJECTS", "-" * 40]
    for p in projects:
        lines.append(f"  {p['title']} — {', '.join(p['tech'])}")
        for bullet in p["bullets"]:
            lines.append(f"    • {bullet}")
        lines.append(f"    github.com/{github}/{p['repo']}")
        lines.append("")
    lines += ["EDUCATION", "-" * 40]
    for e in education:
        lines.append(f"  {e}")
    return "\n".join(lines)


resume = generate_resume(
    name      = "Nikunj Jakhotia",
    email     = "nikunjjakhotia@gmail.com",
    github    = "nikunjjakhotia",
    linkedin  = "nikunjjakhotia",
    skills    = {
        "Languages":  ["Python", "SQL"],
        "Frameworks": ["Flask", "pandas", "requests", "BeautifulSoup"],
        "Tools":      ["Git", "SQLite", "VS Code"],
        "Concepts":   ["REST APIs", "OOP", "Testing (unittest)", "Data Analysis"],
    },
    projects  = [
        {
            "title":   "Expense Tracker",
            "tech":    ["Python", "SQLite", "CLI"],
            "repo":    "expense-tracker",
            "bullets": [
                "Full CRUD CLI with SQLite; validates all inputs and produces monthly summaries.",
            ],
        },
        {
            "title":   "Weather Dashboard",
            "tech":    ["Python", "requests", "Open-Meteo API"],
            "repo":    "weather-dashboard",
            "bullets": [
                "Fetches live forecasts for any city using REST API + Nominatim geocoding.",
            ],
        },
    ],
    education = [
        "Python in 100 Days — Online course (2026)",
    ],
)

print(resume)


# Exercise 2: Rewrite these weak bullet points as strong achievement-based bullets.

weak = [
    "Made a to-do app",
    "Did some web scraping",
    "Wrote scripts for automation",
]

strong = [
    "Built a persistent CLI to-do app with SQLite CRUD, timestamps, and CSV export",
    "Scraped 500+ quotes from 10 pages using requests + BeautifulSoup; exported to JSON",
    "Automated file organisation with pathlib/shutil; reduced manual sorting from 15 min to zero",
]

print("\n--- Bullet Rewrites ---")
for w, s in zip(weak, strong):
    print(f"Weak:   {w}")
    print(f"Strong: {s}")
    print()
