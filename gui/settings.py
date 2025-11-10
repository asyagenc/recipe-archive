import tkinter as tk
from tkinter import ttk, messagebox
from texts import texts  

lang = "en"
language_var = None
language_label = None
save_button = None

def show_settings(parent_frame, language):
    global language_var, language_label, save_button, lang

    lang = language  # Başlangıç dili

    language_label = tk.Label(parent_frame, text=texts[lang]["language_label"])
    language_label.pack(pady=10)

    language_var = tk.StringVar()
    language_combo = ttk.Combobox(parent_frame, textvariable=language_var, state="readonly")
    language_combo['values'] = list(texts.keys())
    language_combo.set(lang)
    language_combo.pack(pady=5)
    language_combo.bind("<<ComboboxSelected>>", change_language)

    save_button = tk.Button(parent_frame, text=texts[lang]["save_btn"], command=save_settings)
    save_button.pack(pady=10)


def change_language(event=None):
    global lang
    lang = language_var.get()
    update_texts()

def update_texts():
    language_label.config(text=texts[lang]["language_label"])
    save_button.config(text=texts[lang]["save_btn"])

def save_settings():
    messagebox.showinfo("Info", f"Language set to {lang}")

def get_lang():
    return lang
