import math
from pathlib import Path
from tkinter import PhotoImage, messagebox

import customtkinter as ctk


BASE_DIR = Path(__file__).resolve().parent
ICON_PATH = BASE_DIR / "icon.png"


def get_stronghold_coords(x1, z1, yaw1, x2, z2, yaw2):
    rad1 = math.radians(-yaw1 - 90)
    rad2 = math.radians(-yaw2 - 90)

    m1 = math.tan(rad1)
    m2 = math.tan(rad2)

    if math.isclose(m1, m2, abs_tol=1e-5):
        return None

    x_target = (m1 * x1 - m2 * x2 + z2 - z1) / (m1 - m2)
    z_target = m1 * (x_target - x1) + z1

    return round(x_target), round(z_target)


def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Stronghold Finder")
    app.geometry("860x560")
    app.minsize(760, 500)

    if ICON_PATH.exists():
        app.iconphoto(True, PhotoImage(file=str(ICON_PATH)))

    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)

    main_frame = ctk.CTkFrame(app, corner_radius=18)
    main_frame.grid(row=0, column=0, padx=24, pady=24, sticky="nsew")
    main_frame.grid_columnconfigure((0, 1), weight=1)
    main_frame.grid_rowconfigure(2, weight=1)

    title_label = ctk.CTkLabel(
        main_frame,
        text="Stronghold Finder",
        font=ctk.CTkFont(size=28, weight="bold"),
    )
    title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 6), sticky="w")

    subtitle_label = ctk.CTkLabel(
        main_frame,
        text="Enter two throws, then calculate the intersection point.",
        text_color="#A1A1AA",
    )
    subtitle_label.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 18), sticky="w")

    def build_throw_frame(parent, title, column):
        frame = ctk.CTkScrollableFrame(parent, corner_radius=16, height=250)
        frame.grid(row=2, column=column, padx=16, pady=8, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)

        header = ctk.CTkLabel(frame, text=title, font=ctk.CTkFont(size=18, weight="bold"))
        header.grid(row=0, column=0, padx=18, pady=(6, 10), sticky="w")

        labels = ["X Coordinate", "Z Coordinate", "Yaw"]
        entries = {}

        for row_index, field_name in enumerate(labels, start=1):
            label = ctk.CTkLabel(frame, text=field_name)
            label.grid(row=row_index * 2 - 1, column=0, padx=18, pady=(4, 0), sticky="w")

            entry = ctk.CTkEntry(frame, placeholder_text=f"Enter {field_name.lower()}")
            entry.grid(row=row_index * 2, column=0, padx=18, pady=(0, 10), sticky="ew")
            entries[field_name] = entry

        return frame, entries

    _, throw_one = build_throw_frame(main_frame, "Throw 1", 0)
    _, throw_two = build_throw_frame(main_frame, "Throw 2", 1)

    result_frame = ctk.CTkFrame(main_frame, corner_radius=16)
    result_frame.grid(row=3, column=0, columnspan=2, padx=16, pady=(14, 6), sticky="ew")
    result_frame.grid_columnconfigure(0, weight=1)

    result_label = ctk.CTkLabel(
        result_frame,
        text="Result will appear here.",
        font=ctk.CTkFont(size=16, weight="bold"),
    )
    result_label.grid(row=0, column=0, padx=18, pady=18, sticky="w")

    def read_float(entry, field_name):
        raw_value = entry.get().strip()
        if not raw_value:
            raise ValueError(f"{field_name} is required.")
        return float(raw_value)

    def calculate():
        try:
            x1 = read_float(throw_one["X Coordinate"], "Throw 1 X Coordinate")
            z1 = read_float(throw_one["Z Coordinate"], "Throw 1 Z Coordinate")
            yaw1 = read_float(throw_one["Yaw"], "Throw 1 Yaw")
            x2 = read_float(throw_two["X Coordinate"], "Throw 2 X Coordinate")
            z2 = read_float(throw_two["Z Coordinate"], "Throw 2 Z Coordinate")
            yaw2 = read_float(throw_two["Yaw"], "Throw 2 Yaw")
        except ValueError as exc:
            messagebox.showerror("Invalid input", str(exc))
            result_label.configure(text="Please enter valid numbers in every field.", text_color="#F97316")
            return

        coords = get_stronghold_coords(x1, z1, yaw1, x2, z2, yaw2)
        if coords is None:
            messagebox.showwarning(
                "Parallel lines",
                "Lines are parallel. Change location and try again.",
            )
            result_label.configure(
                text="Lines are parallel. Change location and try again.",
                text_color="#F97316",
            )
            return

        result_label.configure(
            text=f"Stronghold is near X: {coords[0]}, Z: {coords[1]}",
            text_color="#22C55E",
        )

    button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    button_frame.grid(row=4, column=0, columnspan=2, padx=16, pady=(10, 20), sticky="ew")
    button_frame.grid_columnconfigure(0, weight=1)

    calculate_button = ctk.CTkButton(button_frame, text="Calculate", command=calculate, height=42)
    calculate_button.grid(row=0, column=0, padx=4, pady=4)

    app.mainloop()


if __name__ == "__main__":
    main()