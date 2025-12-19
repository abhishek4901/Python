import tkinter as tk
import random
import time

# ----------------- Multi-line Passages -----------------
passages = [
    """Python is a high-level programming language.
It is easy to learn and simple to use.
Python is widely used in AI and data science.""",

    """Typing speed improves with regular practice.
Accuracy is more important than speed.
Consistent practice gives better results.""",

    """Artificial intelligence is transforming the world.
It helps machines think like humans.
AI is used in healthcare, education, and robotics.""",

    """Consistency is the key to success.
Hard work and patience bring good results.
Never stop learning new skills.""",

    """Machine learning is a part of artificial intelligence.
It allows systems to learn from data.
ML is widely used in prediction systems."""
]

start_time = 0
current_passage = ""
previous_passage = ""

# ----------------- Window -----------------
root = tk.Tk()
root.title("Typing Speed Game")
root.geometry("800x520")

# ----------------- Functions -----------------

def get_new_passage():
    global previous_passage
    new_passage = random.choice(passages)
    while new_passage == previous_passage:
        new_passage = random.choice(passages)
    previous_passage = new_passage
    return new_passage

def start_game():
    global start_time, current_passage
    text_entry.delete("1.0", tk.END)
    result_label.config(text="")
    current_passage = get_new_passage()
    passage_label.config(text=current_passage)
    start_time = time.time()

def refresh_game():
    global start_time, current_passage
    text_entry.delete("1.0", tk.END)
    result_label.config(text="Game refreshed. New passage loaded.")
    current_passage = get_new_passage()
    passage_label.config(text=current_passage)
    start_time = time.time()

def submit_game():
    end_time = time.time()
    typed_text = text_entry.get("1.0", tk.END).strip()
    time_taken = end_time - start_time

    if time_taken <= 0 or not current_passage:
        return

    correct_chars = 0
    for i in range(min(len(current_passage), len(typed_text))):
        if current_passage[i] == typed_text[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(current_passage)) * 100
    wpm = (len(typed_text) / 5) / (time_taken / 60)

    result_label.config(
        text=f"Time: {time_taken:.2f}s | WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%"
    )

def exit_game():
    root.destroy()

# ----------------- UI -----------------

title = tk.Label(root, text="Typing Speed Game",
                 font=("Arial", 20, "bold"))
title.pack(pady=10)

passage_label = tk.Label(
    root,
    text="Click Start or Refresh to get a passage",
    font=("Arial", 14),
    wraplength=760,
    justify="left",
    bg="#f2f2f2",
    padx=10,
    pady=10
)
passage_label.pack(pady=10, fill="x")

text_entry = tk.Text(root, height=6, font=("Arial", 14))
text_entry.pack(pady=10, padx=10, fill="x")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(
    btn_frame, text="Start",
    command=start_game, width=14
)
start_btn.grid(row=0, column=0, padx=8)

refresh_btn = tk.Button(
    btn_frame, text="Refresh",
    command=refresh_game, width=14
)
refresh_btn.grid(row=0, column=1, padx=8)

submit_btn = tk.Button(
    btn_frame, text="Submit",
    command=submit_game, width=14
)
submit_btn.grid(row=0, column=2, padx=8)

exit_btn = tk.Button(
    btn_frame, text="Exit",
    command=exit_game, width=14
)
exit_btn.grid(row=0, column=3, padx=8)

result_label = tk.Label(
    root, text="",
    font=("Arial", 14, "bold"),
    fg="blue"
)
result_label.pack(pady=15)

# ----------------- Run -----------------
root.mainloop()
