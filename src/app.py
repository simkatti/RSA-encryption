import tkinter as tk
from encryption import Encryptor
from decryption import Decryptor

"""
GUI for the program
"""

BACKGROUND_COLOR = "#101010"
FONT_COLOR = "#e4e4e4"


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA")
        self.root.geometry("1000x800")
        self.root.configure(bg=BACKGROUND_COLOR)

        self.title = tk.Label(
            root,
            text="Write your message (max 256 characters):",
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=("Monospace", 12),
        )
        self.subtitle = tk.Label(
            root,
            text="",
            bg = BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=("Monospace", 12),
        )
        
        self.title.place(relx=0.5, rely=0.29, anchor="center")
        self.message_input = tk.Text(
            root,
            width=85,
            height=6,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            insertbackground=FONT_COLOR,
            bd=2,
            highlightthickness=2,
            font=("Monospace", 12),
        )

        self.message_input.place(relx=0.5, rely=0.4, anchor="center")

        self.ok_button = tk.Button(
            root,
            text="OK",
            command=self.show_message,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=("Monospace", 12),
        )
        self.ok_button.place(relx=0.5, rely=0.85, anchor="center")

    def show_message(self):
        self.message = self.message_input.get("1.0", "end-1c")
        """
        error handling for the message
        """
        if len(self.message) > 256 or len(self.message) < 1:
            self.title.place_forget()
            self.title.config(
                text=f"Message should be between 1 - 256 characters. \n Your message is {len(self.message)} characters.",
                fg="red",
            )
            self.title.place(relx=0.5, rely=0.29, anchor="center")
        else:
            self.title.place_forget()
            self.message_input.place_forget()
            self.ok_button.place_forget()

            self.output = tk.Text(
                root,
                width=85,
                height=8,
                bg=BACKGROUND_COLOR,
                fg=FONT_COLOR,
                insertbackground=FONT_COLOR,
                bd=0,
                highlightthickness=0,
                font=("Monospace", 12),
            )
            self.output.insert("1.0", self.message)
            self.output.config(state=tk.DISABLED)
            self.output.place(relx=0.5, rely=0.43, anchor="center")

            self.encrypt_button = tk.Button(
                self.root,
                text="ENCRYPT",
                command=self.encrypt,
                bg=BACKGROUND_COLOR,
                fg=FONT_COLOR,
                font=("Monospace", 12),
            )
            self.encrypt_button.place(relx=0.5, rely=0.85, anchor="center")

    def encrypt(self):
        self.encrypt_button.place_forget()
        self.output.place_forget()
        self.encrypted_message, self.public_key, self.private_key = encrypt_message(self.message)
        self.root.after(0, self.show_encrypted)

    def show_encrypted(self):
        self.title.config(text="Encrypted Message:", fg=FONT_COLOR)
        self.title.place(relx=0.5, rely=0.1, anchor="center")

        self.subtitle.config(text="Public Key (n, e):", fg=FONT_COLOR)
        self.subtitle.place(relx=0.5,rely=0.4, anchor="center")
        
        self.output.place(relx=0.5, rely=0.25, anchor="center")
        
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", self.encrypted_message)
        self.output.config(state=tk.DISABLED)
        
        self.show_key = tk.Text(
            root,
            width=85,
            height=15,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            insertbackground=FONT_COLOR,
            bd=0,
            highlightthickness=0,
            font=("Monospace", 12),
        )
        self.show_key.insert("1.0", f"({self.public_key[0]}, {self.public_key[1]})")
        self.show_key.config(state=tk.DISABLED)
        self.show_key.place(relx=0.5, rely=0.62, anchor="center")

        self.decrypt_button = tk.Button(
            self.root,
            text="DECRYPT",
            command=self.decrypt,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=("Monospace", 12),
        )
        self.decrypt_button.place(relx=0.5, rely=0.85, anchor="center")

    def decrypt(self):
        self.decrypt_button.place_forget()
        self.decrypted_message = decrypt_message(self.encrypted_message, self.private_key)
        self.root.after(0, self.show_decrypted)

    def show_decrypted(self):
        self.title.config(text="Decrypted Message:")
        self.title.place(relx=0.5, rely=0.1, anchor="center")    
        
        self.subtitle.config(text="Private Key (n, d):", fg=FONT_COLOR)
        self.subtitle.place(relx=0.5,rely=0.4, anchor="center")           
        
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", self.decrypted_message)
        self.output.config(state=tk.DISABLED)
        self.show_key.config(state=tk.NORMAL)
        self.show_key.delete("1.0", tk.END)
        self.show_key.insert("1.0", f"({self.private_key[0]}, {self.private_key[1]})")
        self.show_key.config(state=tk.DISABLED)


        self.reset_button = tk.Button(
            self.root,
            text="Write a new message",
            command=self.reset,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=("Monospace", 12),
        )
        self.reset_button.place(relx=0.5, rely=0.85, anchor="center")

    def reset(self):
        self.output.place_forget()
        self.show_key.place_forget()
        self.reset_button.place_forget()
        self.subtitle.place_forget()
        self.title.config(text="Write your message:")
        self.message_input.delete("1.0", tk.END)

        self.title.place(relx=0.5, rely=0.3, anchor="center")
        self.message_input.place(relx=0.5, rely=0.4, anchor="center")
        self.ok_button.place(relx=0.5, rely=0.85, anchor="center")


"""
dummy functions as placeholders
"""
e = Encryptor()
d = Decryptor()


def encrypt_message(message):
    encrypted_message, public_key, private_key = e.perform_encryption(message)
    return encrypted_message, public_key, private_key


def decrypt_message(encrypted, private_key):
    decrypted_message = d.perform_decryption(encrypted, private_key)
    return decrypted_message


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

# 256 char message for error testing:
# Lorem ipsum dolor sit amet, consectetur adipiscing elit,
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
# Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in
