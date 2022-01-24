from tkinter import *
import base64
gui = Tk()
gui.geometry('700x400')
#gui.resizable(0,0)
gui.title("Message Encode and Decode")
Label(gui, text ='🤫ENCODE DECODE🤫', font = 'georgia 20 bold', bg = 'Orange').pack()
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode())


def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')


def Exit():
    gui.destroy()


def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


Label(gui, font='georgia 12 bold', text='MESSAGE').place(x=60, y=60)
Entry(gui, font='georgia 10', textvariable=Text, bg='white').place(x=290, y=60)
Label(gui, font='georgia 12 bold', text='KEY').place(x=60, y=90)
Entry(gui, font='georgia 10', textvariable=private_key, bg='white').place(x=290, y=90)
Label(gui, font='georgia 11 bold', text='MODE(e-encode, d-decode)').place(x=60, y=120)
Entry(gui, font='georgia 10', textvariable=mode, bg='white').place(x=290, y=120)
Label(gui, font='georgia 12 bold', text='RESULT').place(x=60, y=150)
Entry(gui, font='georgia 10 bold', textvariable=Result, bg='white').place(x=290, y=150)
Button(gui, font='georgia 10 bold', text='RESULT', bg='LimeGreen', command=Mode).place(x=80, y=190)
Button(gui, font='georgia 10 bold', text='RESET', width=6, command=Reset, bg='LightGray', padx=2).place(x=180, y=190)
Button(gui, font='georgia 10 bold', text='EXIT', width=6, command=Exit, bg='Red', padx=2, pady=2).place(x=280, y=190)

gui.mainloop()
