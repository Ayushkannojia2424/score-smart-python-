import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt


def calculate():
    try:
        marks = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get())
        ]
        
        if any(m < 0 or m > 100 for m in marks):
            messagebox.showerror("Input Error", "Marks must be between 0 and 100!")
            return

        marks_array = np.array(marks)
        total = np.sum(marks_array)
        average = np.mean(marks_array)


        if average >= 90:
            grade = 'A+'
        elif average >= 80:
            grade = 'A'
        elif average >= 70:
            grade = 'B'
        elif average >= 60:
            grade = 'C'
        elif average >= 50:
            grade = 'D'
        else:
            grade = 'F'

        # Display result with improved styling
        result_label.config(
            text=f"Total Marks: {total:.2f} | Average: {average:.2f} | Grade: {grade}",
            fg="#2ecc71" if average >= 50 else "#e74c3c" # Green for passing, Red for failing
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric marks!")

def show_chart():
    try:
        subjects = ["Python", "ADBMS", "Artificial Intelligence", "DAA", "Computing-aptitude"]
        marks = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get())
        ]
        
        # Check for valid marks (0-100)
        if any(m < 0 or m > 100 for m in marks):
            messagebox.showerror("Input Error", "Marks must be between 0 and 100!")
            return

        plt.figure(figsize=(10, 7))
        
        # Define colors for the chart
        colors = ['#3498db', '#f1c40f', '#e74c3c', '#2ecc71', '#9b59b6']
        
        plt.bar(subjects, marks, color=colors)
        plt.title("ScoreSmart", fontsize=18, fontweight='bold')
        plt.xlabel("Subjects", fontsize=14)
        plt.ylabel("Marks (Out of 100)", fontsize=14)
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle=':', alpha=0.6)
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric marks!")

# --- GUI Setup with Full-Screen & Modern Styling (Dark Theme) ---

# Define a dark color palette
BG_DARK = "#2c3e50" # Dark Blue/Charcoal
FG_LIGHT = "#ecf0f1" # Light Gray/Off-White
ACCENT_BLUE = "#3498db" 
ACCENT_GREEN = "#2ecc71"
ACCENT_RED = "#e74c3c"

window = tk.Tk()
window.title("📊ScoreSmart")

# Set window to start full screen / maximized
window.state('zoomed') 
window.config(bg=BG_DARK)

# Configure the main window rows/columns to expand dynamically
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(2, weight=1) # Row containing input_frame

# --- Title Header ---
header_frame = tk.Frame(window, bg="#1a242f") # Slightly darker header
header_frame.grid(row=0, column=0, sticky='ew', padx=0, pady=0)

title = tk.Label(
    header_frame, 
    text="ScoreSmart", 
    font=("Segoe UI", 32, "bold"), 
    bg="#1a242f", 
    fg=ACCENT_BLUE, 
    pady=20
)
title.pack()

# --- Main Content Frame (Centered) ---
content_frame = tk.Frame(window, bg=BG_DARK, padx=50, pady=30)
content_frame.grid(row=2, column=0, sticky='nsew')
content_frame.grid_columnconfigure(0, weight=1)

# --- Input Frame (Inner frame for marks entry, centered) ---
input_frame = tk.Frame(content_frame, bg=BG_DARK)
input_frame.grid(row=0, column=0, pady=20)

# Configure input_frame columns to center elements
input_frame.grid_columnconfigure(0, weight=1) 
input_frame.grid_columnconfigure(1, weight=1)

# List of subjects
subjects = ["Python", "ADBMS", "Artificial Intelligence", "DAA", "Computing-aptitude"]
entry_widgets = []

for i, subject in enumerate(subjects):
    # Subject Label
    tk.Label(
        input_frame, 
        text=f"{subject}:", 
        font=("Segoe UI", 16), 
        bg=BG_DARK, 
        fg=FG_LIGHT,
        anchor='e' # Align text to the east (right)
    ).grid(row=i, column=0, padx=(10, 50), pady=12, sticky='e')
    
    # Entry Box
    entry = tk.Entry(
        input_frame, 
        width=15, 
        font=("Segoe UI", 16), 
        bd=0, # No border
        relief=tk.FLAT, 
        bg="#3b5266", # Slightly lighter input box
        fg=FG_LIGHT,
        insertbackground=FG_LIGHT, # Cursor color
        justify='center'
    )
    entry.grid(row=i, column=1, padx=(10, 50), pady=12, sticky='w')
    entry_widgets.append(entry)

# Assign entry widgets to variables for the functions
entry1, entry2, entry3, entry4, entry5 = entry_widgets

# --- Result Label ---
result_label = tk.Label(
    content_frame, 
    text="Enter marks (0-100) and click Calculate", 
    font=("Segoe UI", 18, "italic"), 
    bg=BG_DARK, 
    fg="#95a5a6", # Subtle initial color
    pady=25
)
result_label.grid(row=1, column=0, sticky='n')

# --- Button Frame ---
button_frame = tk.Frame(content_frame, bg=BG_DARK)
button_frame.grid(row=2, column=0, pady=20)

# Calculate Button - Primary action
calc_btn = tk.Button(
    button_frame, 
    text="✅ Calculate Result", 
    command=calculate, 
    bg=ACCENT_BLUE, 
    fg="white", 
    font=("Segoe UI", 16, "bold"), 
    width=20, 
    height=2,
    relief=tk.FLAT,
    activebackground="#2980b9" 
)
calc_btn.grid(row=0, column=0, padx=20, pady=10)

# Show Chart Button - Secondary action
chart_btn = tk.Button(
    button_frame, 
    text="📊 Show Chart", 
    command=show_chart, 
    bg=ACCENT_GREEN, 
    fg="white", 
    font=("Segoe UI", 16, "bold"), 
    width=20, 
    height=2,
    relief=tk.FLAT,
    activebackground="#27ae60"
)
chart_btn.grid(row=0, column=1, padx=20, pady=10)

# Exit button 
exit_btn = tk.Button(
    content_frame, 
    text="❌ Exit Application", 
    command=window.destroy, 
    bg=ACCENT_RED, 
    fg="white", 
    font=("Segoe UI", 14), 
    width=25,
    height=1,
    relief=tk.FLAT,
    activebackground="#c0392b"
)
exit_btn.grid(row=3, column=0, pady=40)

# Run the GUI
window.mainloop()