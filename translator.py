from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
import os

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")

translator = Translator()

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END).strip()
        c2 = combo1.get()
        c3 = combo2.get()
        print(f"Translating from {c2} to {c3}: {text_}")
        if text_:
            detection = translator.detect(text_)
            lan = detection.lang
            print(f"Detected language: {lan}")
            for i, j in language.items():
                if j == c3:
                    lan_ = i
                    break
            print(f"Translating to language code: {lan_}")
            translated = translator.translate(text_, src=lan, dest=lan_)
            print(f"Translated text: {translated.text}")
            text2.delete(1.0, END)
            text2.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Error: {e}")
        print(f"Error: {e}")

def check_image_files():
    missing_files = []
    if not os.path.exists("img/google.jpg"):
        missing_files.append("img/google.jpg")
    if not os.path.exists("img/arrow.png"):
        missing_files.append("img/arrow.png")
    
    if missing_files:
        messagebox.showerror("Image Error", f"Missing image files: {', '.join(missing_files)}")
        return False
    return True

if check_image_files():
    try:
        # Icon
        image_icon = PhotoImage(file="img/google.jpg")
        root.iconphoto(False, image_icon)

        # Arrow
        arrow_image = PhotoImage(file="img/arrow.png")
        image_label = Label(root, image=arrow_image, width=150)
        image_label.place(x=460, y=50)
    except Exception as e:
        messagebox.showerror("Image Error", f"Error loading image: {e}")

language = googletrans.LANGUAGES
languageV = list(language.values())

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segeo 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segeo 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(bg="white")
root.mainloop()
