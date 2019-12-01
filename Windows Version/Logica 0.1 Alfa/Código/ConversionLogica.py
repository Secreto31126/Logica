from tkinter import *

def Magia():

    AEIO = BAEIO.get()
    VF = VoF.get()

    print("Magia")

    if AEIO == "":
        AEIO = "A"

    if sujeto.get() == "":
        suj = "A"
    else:
        suj = sujeto.get()

    if predicado.get() == "":
        pre = "B"
    else:
        pre = predicado.get()

    Aa['text'] = "Todo/a " + suj + " es " + pre
    Ea['text'] = "Ningún/a " + suj + " es " + pre
    Ia['text'] = "Algún/a " + suj + " es " + pre
    Oa['text'] = "Algún/a " + suj + " no es " + pre

    if VF == 0:

        print(VF)
        print(AEIO)

        if AEIO == "A":
            Avf['text'] = "V"
            Evf['text'] = "F, Contrariedad"
            Ivf['text'] = "V, Subalternación"
            Ovf['text'] = "F, Contradictoria"

        elif AEIO == "E":
            Avf['text'] = "F, Contrariedad"
            Evf['text'] = "V"
            Ivf['text'] = "F, Contradictoria"
            Ovf['text'] = "V, Subalternación"

        elif AEIO == "I":
            Avf['text'] = "?, Subalternación"
            Evf['text'] = "F, Contradictoria"
            Ivf['text'] = "V"
            Ovf['text'] = "?, Subcontrariedad"

        elif AEIO == "O":
            Avf['text'] = "F, Contradictoria"
            Evf['text'] = "?, Subalternación"
            Ivf['text'] = "?, Subcontrariedad"
            Ovf['text'] = "V"

    else:

        if AEIO == "A":
            Avf['text'] = "F"
            Evf['text'] = "?, Contrariedad"
            Ivf['text'] = "?, Subalternación"
            Ovf['text'] = "V, Contradictoria"

        elif AEIO == "E":
            Avf['text'] = "?, Contrariedad"
            Evf['text'] = "F"
            Ivf['text'] = "V, Contradictoria"
            Ovf['text'] = "?, Subalternación"

        elif AEIO == "I":
            Avf['text'] = "F, Subalternación"
            Evf['text'] = "V, Contradictoria"
            Ivf['text'] = "F"
            Ovf['text'] = "V, Subcontrariedad"

        elif AEIO == "O":
            Avf['text'] = "V, Contradictoria"
            Evf['text'] = "F, Subalternación"
            Ivf['text'] = "V, Subcontrariedad"
            Ovf['text'] = "F"

root = Tk()
root.geometry("280x270+0+0")
root.title("Lógica")
#

s = Label(root, text = "Sujeto: ")
s.grid()
sujeto = Entry(root)
sujeto.grid (column=1, row=0)
#

p = Label(root, text = "Predicado: ")
p.grid(column=0, row=1)
predicado = Entry(root)
predicado.grid (column=1, row=1)
#

frame1 = Frame(root)
frame1.grid(column = 0, row = 3)
VoF = IntVar()
V = Radiobutton(frame1, text="Verdadero", variable=VoF, value=0, command = Magia)
V.grid(column=0, row=0, stick = SW)
F = Radiobutton(frame1, text="Falso", variable=VoF, value=1, command = Magia)
F.grid(column=0, row=1, stick = NW)
#


BAEIO = StringVar()
Ab = Radiobutton(root, text = "A", value = "A", variable = BAEIO, command = Magia)
Ab.grid(column=1, row=3, stick = NE)#(column = 1, row = 3) Eliminar grid
Ib = Radiobutton(root, text = "I", value = "I", variable = BAEIO, command = Magia)
Ib.grid(column=2, row=3, stick = NW)
Eb = Radiobutton(root, text = "E ", value = "E", variable = BAEIO, command = Magia)
Eb.grid(column=1, row=3, stick = SE)
Ob = Radiobutton(root, text = "O", value = "O", variable = BAEIO, command = Magia)
Ob.grid(column=2, row=3, stick = SW)
#

Al = Label(text = "A: ")
Al.grid(column = 0, row = 5)
Aa = Label(text = "")
Aa.place(x = 53, y = 92)
Avf = Label (text = "")
Avf.grid(column = 1, row = 6, stick = W)
El = Label(text = "E: ")
El.grid(column = 0, row = 7)
Ea = Label(text = "")
Ea.place(x = 53, y = 134)
Evf = Label (text = "")
Evf.grid(column = 1, row = 8, stick = W)
Il = Label(text = "I: ")
Il.grid(column = 0, row = 9)
Ia = Label(text = "")
Ia.place(x = 53, y = 177)
Ivf = Label (text = "")
Ivf.grid(column = 1, row = 10, stick = W)
Ol = Label(text = "O: ")
Ol.grid(column = 0, row = 11)
Oa = Label(text = "")
Oa.place(x = 53, y = 218)
Ovf = Label (text = "")
Ovf.grid(column = 1, row = 12, stick = W)
#

mainloop()
