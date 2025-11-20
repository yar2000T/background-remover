import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove
import io

# Globals
original_image = None
processed_image = None

# ----------------- Functions -----------------
def load_image():
    global original_image
    path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp *.bmp")]
    )
    if not path:
        return

    original_image = Image.open(path)
    display_image(original_image, input_label)


def remove_background():
    global processed_image, original_image
    if original_image is None:
        messagebox.showerror("Error", "Please load an image first!")
        return

    data = io.BytesIO()
    original_image.save(data, format="PNG")
    result = remove(data.getvalue())
    processed_image = Image.open(io.BytesIO(result))

    display_image(processed_image, output_label)


def save_image():
    global processed_image
    if processed_image is None:
        messagebox.showerror("Error", "No processed image to save!")
        return

    path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )
    if not path:
        return

    processed_image.save(path)
    messagebox.showinfo("Saved", "Image saved successfully!")


def display_image(img, label):
    # Auto-scale image to fit label size while keeping aspect ratio
    label_width = label.winfo_width() or 300
    label_height = label.winfo_height() or 300

    img_copy = img.copy()
    img_copy.thumbnail((label_width, label_height))
    tk_img = ImageTk.PhotoImage(img_copy)

    label.config(image=tk_img)
    label.image = tk_img

# ----------------- UI Setup -----------------
root = tk.Tk()
root.title("AI Background Remover")
root.geometry("800x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

TITLE_FONT = ("Segoe UI", 24, "bold")
BTN_FONT = ("Segoe UI", 12, "bold")
LABEL_FONT = ("Segoe UI", 10)

# Title
title = tk.Label(root, text="AI Background Remover", font=TITLE_FONT, bg="#1e1e1e", fg="#f0f0f0")
title.pack(pady=10)

# Image frame
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10, fill="both", expand=True)

input_label = tk.Label(frame, text="Input Image", bg="#2e2e2e", fg="#aaaaaa", font=LABEL_FONT, relief="ridge")
input_label.pack(side="left", padx=20, pady=10, expand=True, fill="both")

output_label = tk.Label(frame, text="Output Image", bg="#2e2e2e", fg="#aaaaaa", font=LABEL_FONT, relief="ridge")
output_label.pack(side="right", padx=20, pady=10, expand=True, fill="both")

# Buttons frame
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=20)

# Modern buttons
def create_button(parent, text, command):
    btn = tk.Button(parent, text=text, command=command, font=BTN_FONT, bg="#3a3a3a", fg="#ffffff",
                    activebackground="#5a5a5a", activeforeground="#ffffff", bd=0, relief="flat", padx=20, pady=10)
    btn.bind("<Enter>", lambda e: btn.config(bg="#5a5a5a"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#3a3a3a"))
    btn.pack(side="left", padx=15)
    return btn

create_button(btn_frame, "Load Image", load_image)
create_button(btn_frame, "Remove Background", remove_background)
create_button(btn_frame, "Save Result", save_image)

root.mainloop()
