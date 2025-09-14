import tkinter as tk
import json
import os

FILE = "tasks.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def refresh():
    listbox.delete(0, tk.END)
    for task in tasks:
        mark = "✓" if task["done"] else "✗"
        listbox.insert(tk.END, f"{mark} {task['task']}")

def add():
    text = entry.get().strip()
    if text:
        tasks.append({"task": text, "done": False})
        save(tasks)
        entry.delete(0, tk.END)
        refresh()

def mark_done():
    index = listbox.curselection()
    if index:
        tasks[index[0]]["done"] = True
        save(tasks)
        refresh()

def delete():
    index = listbox.curselection()
    if index:
        tasks.pop(index[0])
        save(tasks)
        refresh()

tasks = load()

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add)
add_btn.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

done_btn = tk.Button(root, text="Mark as Done", command=mark_done)
done_btn.pack()

del_btn = tk.Button(root, text="Delete Task", command=delete)
del_btn.pack()

refresh()
root.mainloop()