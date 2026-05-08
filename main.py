import numpy as np
import matplotlib.pyplot as plt
from pyscript import display, document

days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
absences = np.array([0, 0, 0, 0, 0])

def show_graph():
    plt.close()
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(days, absences, marker="o", linestyle="-", color="b")

    ax.set_title("Attendance Tracker")
    ax.set_xlabel("Days")
    ax.set_ylabel("Absences")
    ax.grid(True)

    output_div = document.getElementById("output")
    output_div.innerHTML = ""   
    display(fig, target="output") 

def add_data(event):
    day_val = document.getElementById("day").value
    abs_val = document.getElementById("absences").value

    try:
        value = int(abs_val) if abs_val != "" else 0
    except ValueError:
        value = 0

    index = list(days).index(day_val)
    absences[index] = value

    show_graph()

show_graph()

