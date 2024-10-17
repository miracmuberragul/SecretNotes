import tkinter
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from tkinter import messagebox


window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(400,500)
window.config(padx=30,pady=30)

img = Image.open('top_secret.jpg')
resized_image = img.resize((50,50))
image = ImageTk.PhotoImage(resized_image)
image_label = tkinter.Label(window, image=image)
image_label.pack()

title = tkinter.Label(text="Enter Your Title")
title.pack()


title_entry = tkinter.Entry()
title_entry.config(width=20)
title_entry.pack()
secret_file = open("secretnotes.txt","a")


secret_label = tkinter.Label(text="Enter Your Secret:")
secret_label.pack()

secret_text = tkinter.Text(width=30, height=20)
secret_text.pack()

key_label = tkinter.Label(text="Enter the Key")
key_label.pack()

key_entry = tkinter.Entry(width=20)
key_entry.pack()

def encrypte_text():

    master_key = key_entry.get()
    if(master_key == "miro"):

        secret_file.write(secret_text.get("1.0", tkinter.END))
        secret_file.close()
        key = Fernet.generate_key()
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)

        # opening the key
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open('secretnotes.txt', 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)
        with open('secretnotes.txt', 'wb') as encrypted_file:

            encrypted_file.write(encrypted)
    else:
        messagebox.showerror('Python Error', 'Error: You Entered the Wrong Key!')



def decrypte_text():
    master_key = key_entry.get()
    if (master_key == "miro"):
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        # using the generated key
        fernet = Fernet(key)
         # opening the encrypted file
        with open('secretnotes.txt', 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)


        # opening the file in write mode and
        # writing the decrypted data
        with open('secretnotes.txt', 'wb') as dec_file:
            dec_file.write(decrypted)
    else:
        messagebox.showerror('Python Error', 'Error: You Entered the Wrong Key!')



save_button = tkinter.Button(text="Save & Encrypt", command=encrypte_text)
save_button.pack()

decrypt_button = tkinter.Button(text="Decrypt", command=decrypte_text)
decrypt_button.pack()

window.mainloop()