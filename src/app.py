import tkinter as tk
from encryption import Encryptor
from decryption import Decryptor

"""
GUI for the program
"""

BACKGROUND_COLOR = "#101010"
FONT_COLOR = "#e4e4e4"
FONT = 'Ubuntu Mono'


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA")
        self.root.geometry("1000x800")
        self.root.configure(bg=BACKGROUND_COLOR)

        self.title = tk.Label(
            root,
            text="Write your message (max 190 bytes):",
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=(FONT, 15),
        )
        self.subtitle = tk.Label(
            root,
            text="",
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=(FONT, 15),
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
            font=(FONT, 14),
        )

        self.message_input.place(relx=0.5, rely=0.4, anchor="center")

        self.ok_button = tk.Button(
            root,
            text="OK",
            command=self.show_message,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=(FONT, 14),
        )
        self.ok_button.place(relx=0.5, rely=0.85, anchor="center")

    def show_message(self):
        self.message = self.message_input.get("1.0", "end-1c")
        """
        error handling for the message
        """
        
        if len(self.message.encode('utf-8')) > 190 or len(self.message) < 1:
            self.title.place_forget()
            self.title.config(
                text=f"Message should be between maximum of 190 bytes. \n Your message is {len(self.message.encode('utf-8'))} bytes.", fg="red")
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
                font=(FONT, 14),
            )
            self.output.insert("1.0", self.message)
            self.output.config(state=tk.DISABLED)
            self.output.place(relx=0.5, rely=0.43, anchor="center")

            self.generate_keys_button = tk.Button(
                self.root,
                text="GENERATE KEYS",
                command=self.generate_keys,
                bg=BACKGROUND_COLOR,
                fg=FONT_COLOR,
                font=(FONT, 14),
            )
            self.generate_keys_button.place(
                relx=0.5, rely=0.85, anchor="center")

    def generate_keys(self):
        self.generate_keys_button.place_forget()
        self.output.place_forget()
        self.encrypted_message, self.public_key, self.private_key = encrypt_message(
            self.message)

        with open('src/keys.txt', mode='w') as file:
            file.write(f'{self.public_key[0]}, {self.public_key[1]} \n \n {self.private_key[0]}, {self.private_key[1]}')

        self.title.config(text="Public Key (n, e):", fg=FONT_COLOR)
        self.title.place(relx=0.5, rely=0.125, anchor="center")

        self.subtitle.config(text="Private Key (n, d):", fg=FONT_COLOR)
        self.subtitle.place(relx=0.5, rely=0.4, anchor="center")
        self.output.place(relx=0.5, rely=0.25, anchor="center")
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", f"{self.public_key[0]}, {self.public_key[1]}")
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
            font=(FONT, 14),
        )
        self.show_key.insert("1.0", f'{self.private_key[0]}, {self.private_key[1]}')
        self.show_key.config(state=tk.DISABLED)
        self.show_key.place(relx=0.5, rely=0.61, anchor="center")

        self.encrypt_button = tk.Button(
            self.root,
            text="ENCRYPT MESSAGE",
            command=self.public_key_insertion,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=(FONT, 14),
        )

        self.encrypt_button.place(relx=0.5, rely=0.85, anchor="center")

    def public_key_insertion(self):
        self.title.config(text="Your message: ", fg=FONT_COLOR)
        self.title.place(relx=0.5, rely=0.125, anchor="center")
        self.subtitle.config(
            text="Insert public key in form of n, e:", fg=FONT_COLOR)
        self.subtitle.place(relx=0.5, rely=0.4, anchor="center")
        self.encrypt_button.place_forget()
        self.output.place_forget()

        self.output.place(relx=0.5, rely=0.25, anchor="center")

        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", self.message)
        self.output.config(state=tk.DISABLED)

        self.show_key.place_forget()

        self.public_key_input = tk.Text(
            root,
            width=85,
            height=13,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            insertbackground=FONT_COLOR,
            bd=2,
            highlightthickness=2,
            font=(FONT, 14),
        )

        self.public_key_input.place(relx=0.5, rely=0.6, anchor="center")

        self.encryption_button = tk.Button(
            self.root,
            text="ENCRYPT MESSAGE",
            command=self.show_encrypted,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=(FONT, 14),
        )

        self.encryption_button.place(relx=0.5, rely=0.85, anchor="center")

    def show_encrypted(self):
        publickey_user_input = self.public_key_input.get("1.0", "end-1c")

        if publickey_user_input == '':
            correct_input = True

        else:
            parts = [part.strip() for part in publickey_user_input.split(',')]
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                if int(parts[0]) == self.public_key[0] and int(parts[1]) == self.public_key[1]:
                    correct_input = True
                else:
                    correct_input = False
            else:
                correct_input = False

        if not correct_input:
            self.subtitle.place_forget()
            self.subtitle.config(
                text=f"The public key is invalid! Use the generated public key in form n, e",
                fg="red",
            )
            self.subtitle.place(relx=0.5, rely=0.4, anchor="center")

        else:
            self.encryption_button.place_forget()
            self.public_key_input.place_forget()
            self.output.place_forget()
            self.subtitle.place_forget()

            self.title.config(text="Encrypted Message:", fg=FONT_COLOR)
            self.title.place(relx=0.5, rely=0.29, anchor="center")

            self.output.place(relx=0.5, rely=0.43, anchor="center")

            self.output.config(state=tk.NORMAL)
            self.output.delete("1.0", tk.END)
            self.output.insert("1.0", self.encrypted_message)
            self.output.config(state=tk.DISABLED)

            self.decryption_button = tk.Button(
                self.root,
                text="DECRYPT MESSAGE",
                command=self.private_key_insertion,
                bg=BACKGROUND_COLOR,
                fg=FONT_COLOR,
                font=(FONT, 14),
            )
            self.decryption_button.place(relx=0.5, rely=0.85, anchor="center")

    def private_key_insertion(self):
        self.decryption_button.place_forget()
        self.output.place_forget()

        self.title.config(text="Encrypted message: ", fg=FONT_COLOR)
        self.title.place(relx=0.5, rely=0.125, anchor="center")

        self.subtitle.config(
            text="Insert private key in form of n, d:", fg=FONT_COLOR)
        self.subtitle.place(relx=0.5, rely=0.4, anchor="center")

        self.output.place(relx=0.5, rely=0.25, anchor="center")

        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", self.encrypted_message)
        self.output.config(state=tk.DISABLED)

        self.private_key_input = tk.Text(
            root,
            width=85,
            height=13,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            insertbackground=FONT_COLOR,
            bd=2,
            highlightthickness=2,
            font=(FONT, 14),
        )

        self.private_key_input.place(relx=0.5, rely=0.6, anchor="center")

        self.decrypt_button = tk.Button(
            self.root,
            text="DECRYPT MESSAGE",
            command=self.show_decrypted,
            bg=BACKGROUND_COLOR,
            fg=FONT_COLOR,
            font=(FONT, 14),
        )

        self.decrypt_button.place(relx=0.5, rely=0.85, anchor="center")

    def show_decrypted(self):
        privatekey_user_input = self.private_key_input.get("1.0", "end-1c")

        if privatekey_user_input == '':
            correct_input = True

        else:
            parts = [part.strip() for part in privatekey_user_input.split(',')]
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                if int(parts[0]) == self.private_key[0] and int(parts[1]) == self.private_key[1]:
                    correct_input = True
                else:
                    correct_input = False
            else:
                correct_input = False

        if not correct_input:
            self.subtitle.place_forget()
            self.subtitle.config(
                text=f"The private key is invalid! Use the generated public key in form n, e",
                fg="red",
            )
            self.subtitle.place(relx=0.5, rely=0.4, anchor="center")

        else:
            self.decrypt_button.place_forget()
            self.private_key_input.place_forget()
            self.subtitle.place_forget()
            self.output.place_forget()

            self.decrypted_message = decrypt_message(
                self.encrypted_message, self.private_key)

            self.title.config(text="Decrypted Message:")
            self.title.place(relx=0.5, rely=0.29, anchor="center")

            self.output.place(relx=0.5, rely=0.43, anchor="center")
            self.output.config(state=tk.NORMAL)
            self.output.delete("1.0", tk.END)
            self.output.insert("1.0", self.decrypted_message)
            self.output.config(state=tk.DISABLED)

            self.reset_button = tk.Button(
                self.root,
                text="Write a new message",
                command=self.reset,
                bg=BACKGROUND_COLOR,
                fg=FONT_COLOR,
                font=(FONT, 14),
            )
            self.reset_button.place(relx=0.5, rely=0.85, anchor="center")

    def reset(self):
        self.output.place_forget()
        self.show_key.place_forget()
        self.reset_button.place_forget()
        self.subtitle.place_forget()
        self.title.config(text="Write your message (max 190 bytes):")
        self.message_input.delete("1.0", tk.END)

        self.title.place(relx=0.5, rely=0.29, anchor="center")
        self.message_input.place(relx=0.5, rely=0.4, anchor="center")
        self.ok_button.place(relx=0.5, rely=0.85, anchor="center")


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
