import tkinter as tk

# Define app configuration
app_config = {
    "title": "Comptabilité automatisée de l'entreprise",
    "width": 800,
    "height": 600,
    "bg": "white"
}


# Create main window
window = tk.Tk()
window.title(app_config["title"])

# Set window size
window.geometry(f"{app_config['width']}x{app_config['height']}")
window.configure(bg=app_config['bg'])

# Create base frame
frame = tk.Frame(window, bg='blue', width=600, height=50)
frame.place(x=0, y=400)

# # Create 3 buttons for the 3 different functionalities
# salary_button = tk.Button(frame, text="Calculer les salaires mensuels", bg='blue', fg='white')
# salary_button.pack()



if __name__ == "__main__":
    window.mainloop()
