# Day 95 – Contributing to Open Source

# These exercises prepare you for real open-source contribution.
# The code exercises simulate the git workflow.


# Exercise 1: Generate a commit message following Conventional Commits for common PR types.

PR_SCENARIOS = [
    ("Fixing a typo in the Flask docs README",                 "docs",     "flask",    "fix typo in installation guide"),
    ("Adding a missing test for a pandas edge case",           "test",     "pandas",   "add test for empty DataFrame sort"),
    ("Fixing a bug where ValueError wasn't caught",            "fix",      "requests", "catch ValueError in json() method"),
    ("Adding a new utility function to a helper module",       "feat",     "utils",    "add slugify helper to string module"),
]

print("Conventional Commit Messages:")
for desc, type_, scope, summary in PR_SCENARIOS:
    msg = f"{type_}({scope}): {summary}"
    print(f"\n  Scenario: {desc}")
    print(f"  Commit  : {msg}")


# Exercise 2: Write a PR description template.

def pr_description(what, why, testing_notes):
    return f"""## What this PR does
{what}

## Why
{why}

## Testing
{testing_notes}

---
*Generated with Python in 100 Days Day 95 exercise*
"""

print("\nSample PR Description:")
print(pr_description(
    what          = "Fix typo in README installation section ('installaton' → 'installation')",
    why           = "Incorrect spelling may confuse new users following the Quick Start guide.",
    testing_notes = "Documentation only — no code changes, no tests required.",
))


# Exercise 3: Simulate the fork-branch-commit-push workflow as shell commands.

WORKFLOW = [
    "# 1. Fork on GitHub, then clone your fork:",
    "git clone https://github.com/YOU/project.git",
    "cd project",
    "",
    "# 2. Add upstream remote:",
    "git remote add upstream https://github.com/OWNER/project.git",
    "",
    "# 3. Create a feature branch:",
    "git checkout -b fix/typo-in-readme",
    "",
    "# 4. Make changes, then stage and commit:",
    "git add README.md",
    'git commit -m "docs(readme): fix typo in installation section"',
    "",
    "# 5. Push and open a pull request:",
    "git push origin fix/typo-in-readme",
    "# → Then click 'Compare & pull request' on GitHub",
]

print("Open Source Contribution Workflow:")
for line in WORKFLOW:
    print(f"  {line}")
