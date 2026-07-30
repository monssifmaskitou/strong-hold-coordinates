import customtkinter as ctk

app = ctk.CTk()
app.title("Coordinate Tool")
app.geometry("300x250")


entry_x = ctk.CTkEntry(app, placeholder_text="X Coordinate")
entry_x.pack(pady=10)

entry_z = ctk.CTkEntry(app, placeholder_text="Z Coordinate")
entry_z.pack(pady=10)

result_label = ctk.CTkLabel(app, text="Result: --")
result_label.pack(pady=10)

def calculate():
    x = entry_x.get()
    z = entry_z.get()
    result_label.configure(text=f"Target: ({x}, {z})")

btn = ctk.CTkButton(app, text="Calculate", command=calculate)
btn.pack(pady=10)

app.mainloop()