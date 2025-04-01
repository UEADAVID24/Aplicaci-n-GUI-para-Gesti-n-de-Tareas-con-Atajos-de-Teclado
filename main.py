import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Gestión de Tareas")
        self.root.geometry("400x400")

        # Lista de tareas
        self.tasks = []

        # Entrada para nueva tarea
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(root, height=10, width=30, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Botones
        self.add_button = tk.Button(root, text="Añadir tarea", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como completada", width=20, command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar tarea", width=20, command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Asignación de atajos de teclado
        self.root.bind("<Return>", self.add_task_from_key)
        self.root.bind("<C>", self.mark_complete_from_key)
        self.root.bind("<Delete>", self.delete_task_from_key)
        self.root.bind("<Escape>", self.quit_application)

    def add_task(self, event=None):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Por favor ingresa una tarea.")

    def add_task_from_key(self, event):
        self.add_task()

    def mark_complete(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            self.tasks[task_index]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showwarning("Error", "Por favor selecciona una tarea para marcar como completada.")

    def mark_complete_from_key(self, event):
        self.mark_complete()

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            del self.tasks[task_index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Error", "Por favor selecciona una tarea para eliminar.")

    def delete_task_from_key(self, event):
        self.delete_task()

    def quit_application(self, event):
        self.root.quit()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_display = task["task"]
            if task["completed"]:
                task_display += " (Completada)"
            self.task_listbox.insert(tk.END, task_display)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

