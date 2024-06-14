import customtkinter as ctk
from tkinter import messagebox
import json
import os
from PIL import Image

def pay_info():
    try:
        if os.path.exists("form.json"):
            with open("form.json", "r") as file:
                return json.load(file)
    except json.JSONDecodeError:
        messagebox.showinfo("Error", "Error reading student data.")
    return []


def save_library(library):
    with open("form.json", "w") as file:
        json.dump(library, file, indent=4)

def save_details():
    library = pay_info()
    try:
        student = {
            "name": entry_name.get(),
            "mail": entry_mail.get(),
            "address": entry_address.get(),
            "city": entry_city.get(),
            "state": entry_state.get(),
            "zip code": entry_zip.get(),
            "card number": entry_card_no.get(),
            "exp month": entry_Exp.get(),
            "exp year": entry_card_no.get(),
            "cvv": entry_cvv.get(),
        }
        library.append(student)
        save_library(library)
        messagebox.showinfo("Success", f"{entry_name.get()} Your Card Details has been saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving details: {e}")

root = ctk.CTk()
root.title("Payment Form")
root.geometry("850x550")

frame_main = ctk.CTkFrame(root)
frame_main.pack(pady=20, padx=20, fill="both", expand=True)

label_pay = ctk.CTkLabel(frame_main, text="Billing Address", font=("Arial Bold", 24), text_color="#0903DA")
label_pay.place(relx=0.18, rely=0.04, anchor="center")

label_title = ctk.CTkLabel(frame_main, text="Payment", font=("Arial Bold", 24), text_color="#5DE2E7")
label_title.place(relx=0.68, rely=0.04, anchor="center")

full_name = ctk.CTkLabel(frame_main, text="Full Name", font=("Arial", 20), text_color="white")
full_name.place(relx=0.1, rely=0.15, anchor="center")
entry_name = ctk.CTkEntry(frame_main, placeholder_text="Enter Your Name")
entry_name.place(relx=0.28, rely=0.15, anchor="center")

email = ctk.CTkLabel(frame_main, text="E-mail", font=("Arial", 20), text_color="white")
email.place(relx=0.1, rely=0.25, anchor="center")
entry_mail = ctk.CTkEntry(frame_main, placeholder_text="ABC@XYZ.com")
entry_mail.place(relx=0.28, rely=0.25, anchor="center")

email = ctk.CTkLabel(frame_main, text="Address", font=("Arial", 20), text_color="white")
email.place(relx=0.1, rely=0.35, anchor="center")
entry_address = ctk.CTkEntry(frame_main, placeholder_text="Enter Your Address")
entry_address.place(relx=0.28, rely=0.35, anchor="center")

city = ctk.CTkLabel(frame_main, text="City", font=("Arial", 20), text_color="white")
city.place(relx=0.1, rely=0.45, anchor="center")
entry_city = ctk.CTkEntry(frame_main, placeholder_text="City Ex:- Delhi") 
entry_city.place(relx=0.28, rely=0.45, anchor="center")


state = ctk.CTkLabel(frame_main, text="State", font=("Arial", 20), text_color="white")
state.place(relx=0.1, rely=0.45, anchor="center")
entry_state = ctk.CTkEntry(frame_main, placeholder_text="State Ex:- Delhi")
entry_state.place(relx=0.28, rely=0.45, anchor="center")

zip_code = ctk.CTkLabel(frame_main, text="Zip Code", font=("Arial", 20), text_color="white")
zip_code.place(relx=0.1, rely=0.55, anchor="center")
entry_zip = ctk.CTkEntry(frame_main, placeholder_text="Zip Code Ex:- 123456")
entry_zip.place(relx=0.28, rely=0.55, anchor="center")

# @@@@@@@@@!###################################

payment_card = ctk.CTkLabel(frame_main, text="Accepted Card:", font=("Arial", 20), text_color="white")
payment_card.place(relx=0.6, rely=0.15, anchor="center")

image_path = os.path.join(os.path.dirname(__file__), "cards.png")

image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(180, 30))
image_label = ctk.CTkLabel(frame_main, image=image)
image_label.place(relx=0.8, rely=0.15, anchor="center")

# @@@@@@@@@!###################################

card_number = ctk.CTkLabel(frame_main, text="Credit Card Number", font=("Arial", 20), text_color="white")
card_number.place(relx=0.58, rely=0.25, anchor="center")
entry_card_no = ctk.CTkEntry(frame_main, placeholder_text="Credit Card Number")
entry_card_no.place(relx=0.8, rely=0.25, anchor="center")

Exp_month = ctk.CTkLabel(frame_main, text="Expiry Month", font=("Arial", 20), text_color="white")
Exp_month.place(relx=0.6, rely=0.35, anchor="center")
entry_Exp = ctk.CTkEntry(frame_main, placeholder_text="EXP Month")
entry_Exp.place(relx=0.8, rely=0.35, anchor="center")

Exp_year = ctk.CTkLabel(frame_main, text="Expiry Year", font=("Arial", 20), text_color="white")
Exp_year.place(relx=0.6, rely=0.45, anchor="center")
entry_year = ctk.CTkEntry(frame_main, placeholder_text="EXP Year")
entry_year.place(relx=0.8, rely=0.45, anchor="center")

cvv = ctk.CTkLabel(frame_main, text="CVV", font=("Arial", 20), text_color="white")
cvv.place(relx=0.6, rely=0.55, anchor="center")
entry_cvv = ctk.CTkEntry(frame_main, placeholder_text="CVV")
entry_cvv.place(relx=0.8, rely=0.55, anchor="center")

# @@@@@@@@@!###################################

ctk.CTkButton(frame_main, text="Pay Now", command=save_details, font=("Arial", 20), border_width=2).place(relx=0.45, rely=0.72, anchor="center")

root.protocol("WM_DELETE_WINDOW")
root.mainloop()
