# Day 63 – Project: To-Do List Database App

import sqlite3
from datetime import datetime

DB_PATH = "todo.db"


def setup(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            title      TEXT    NOT NULL,
            done       INTEGER NOT NULL DEFAULT 0,
            created_at TEXT    NOT NULL
        )
    """)
    conn.commit()


def add_task(conn, title):
    cur = conn.execute(
        "INSERT INTO tasks (title, created_at) VALUES (?, ?)",
        (title.strip(), datetime.now().strftime("%Y-%m-%d"))
    )
    conn.commit()
    return cur.lastrowid


def list_tasks(conn):
    return [dict(r) for r in conn.execute(
        "SELECT * FROM tasks ORDER BY id"
    ).fetchall()]


def complete_task(conn, task_id):
    conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()


def delete_task(conn, task_id):
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()


def print_tasks(tasks):
    if not tasks:
        print("  No tasks.")
        return
    print(f"\n  {'ID':<4} {'Done':<5} {'Created':<12} Task")
    print("  " + "─" * 50)
    for t in tasks:
        done = "✓" if t["done"] else " "
        print(f"  {t['id']:<4} {done:<5} {t['created_at']:<12} {t['title']}")
    print()


MENU = """
Todo App
─────────────────────────────
1. List all tasks
2. Add task
3. Complete task
4. Delete task
5. Quit
"""


def main():
    import os
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        setup(conn)

        while True:
            print(MENU)
            choice = input("> ").strip()

            if choice == "1":
                print_tasks(list_tasks(conn))
            elif choice == "2":
                title = input("Task: ").strip()
                if title:
                    tid = add_task(conn, title)
                    print(f"Added task #{tid}.")
            elif choice == "3":
                print_tasks(list_tasks(conn))
                try:
                    tid = int(input("Complete task #: "))
                    complete_task(conn, tid)
                    print("Marked done.")
                except ValueError:
                    print("Invalid id.")
            elif choice == "4":
                print_tasks(list_tasks(conn))
                try:
                    tid = int(input("Delete task #: "))
                    delete_task(conn, tid)
                    print("Deleted.")
                except ValueError:
                    print("Invalid id.")
            elif choice == "5":
                print("Bye!")
                break
            else:
                print("Unknown option.")

        # Clean up demo file
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)


if __name__ == "__main__":
    main()
