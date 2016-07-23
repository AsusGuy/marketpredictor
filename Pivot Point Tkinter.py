from Tkinter import *

def about():
    about = Toplevel()
    about.wm_title("Market Predictions - About")
    version = Label(about, text="Version: 0.1 Beta")
    version.pack()
    details = Label(about, text="Uses the Pivot Point Theory, Fraction Theory and some")
    details.pack()
    details2 = Label(about, text="basic math to predict a stocks future movements.")
    details2.pack()
    creator = Label(about, text="Created by Nick Clunes - Application can be freely distributed.")
    creator.pack()


def pivotcal():

    r1 = e8.get()
    r = int(r1)

    H2 = e1.get()
    L2 = e2.get()
    C2 = e3.get()

    T1 = e4.get()
    T2 = e5.get()
    T3 = e6.get()
    T4 = e7.get()

    H1 = float(H2)
    L1 = float(L2)
    C1 = float(C2)

    TH = float(T1)
    TL = float(T2)
    TC = float(T3)
    TO = float(T4)

    if TC < TO:
        X = TH + TL + TC + TL
        Y = X / 2
        HI = Y - TL
        LO = Y - TH
    elif TC > TO:
        X = TH + TL + TC + TH
        Y = X / 2
        HI = Y - TL
        LO = Y - TH
    elif TC == TO:
        X = TH + TL + TC + TC
        Y = X / 2
        HI = Y - TL
        LO = Y - TH

    Pold = H1 + L1 + C1
    P = Pold / 3
    R1old = P * 2
    R1 = R1old - L1
    R2old = H1 - L1
    R2 = P + R2old
    S1old = P * 2
    S1 = S1old - H1
    S2old = H1 - L1
    S2 = P - S2old

    hlc = H1+C1+L1
    Y2 = hlc*0.67
    R1F = Y2-L1
    S1F = Y2-H1
    PB = Y2-C1

    R1r = round(R1,r)
    R2r = round(R2,r)
    Pr = round(P,r)
    S1r = round(S1,r)
    S2r = round(S2,r)
    HIr = round(HI,r)
    LOr = round(LO,r)
    R1Fr = round(R1F,r)
    S1Fr = round(S1F,r)
    PBr = round(PB,r)

    toplevel = Toplevel()
    toplevel.wm_title("Predictions")
    pivotpointinfo = Label(toplevel, text="Pivot Point Results:")
    pivotpointinfo.pack()
    label1 = Label(toplevel, text="Resistance 1: " + str(R1r), height=0, width=0)
    label1.pack()
    label2 = Label(toplevel, text="Resistance 2: " + str(R2r), height=0, width=0)
    label2.pack()
    label3 = Label(toplevel, text="Pivot Point: " + str(Pr), height=0, width=0)
    label3.pack()
    label4 = Label(toplevel, text="Support 1: " + str(S1r), height=0, width=0)
    label4.pack()
    label5 = Label(toplevel, text="Support 2: " + str(S2r), height=0, width=0)
    label5.pack()
    blank = Label(toplevel, text="")
    blank.pack()
    predictioninfo = Label(toplevel, text="Tomorrow Predictions:")
    predictioninfo.pack()
    label6 = Label(toplevel, text="Tomorrow's High: " + str(HIr), height=0, width=0)
    label6.pack()
    label7 = Label(toplevel, text="Tomorrow's Low:  " + str(LOr), height=0, width=0)
    label7.pack()
    blank = Label(toplevel, text="")
    blank.pack()
    fractioninfo = Label(toplevel, text="Fraction Theory Results:")
    fractioninfo.pack()
    label8 = Label(toplevel, text="Resistance: " + str(R1Fr), height=0, width=0)
    label8.pack()
    label9 = Label(toplevel, text="Support:  " + str(S1Fr), height=0, width=0)
    label9.pack()
    label10 = Label(toplevel, text="Possible Buy:  " + str(PBr), height=0, width=0)
    label10.pack()



master = Tk()
master.wm_title("Clunes Predictor")
pivotinfo = Label(master, text="Market Calculator").grid(row=0)
Label(master, text="High: ").grid(row=1)
Label(master, text="Low:  ").grid(row=2)
Label(master, text="Close:").grid(row=3)
predinfo = Label(master, text="Tomorrow High/Low Prediction").grid(row=4)
Label(master, text="Today's High: ").grid(row=5)
Label(master, text="Today's Low:  ").grid(row=6)
Label(master, text="Today's Close:").grid(row=7)
Label(master, text="Today's Open: ").grid(row=8)
Label(master, text="").grid(row=9)
Label(master, text="Decimal Rounding: ").grid(row=10)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)

e1.insert(10,"0")
e2.insert(10,"0")
e3.insert(10,"0")
e4.insert(10,"0")
e5.insert(10,"0")
e6.insert(10,"0")
e7.insert(10,"0")
e8.insert(10,"4")

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=5, column=1)
e5.grid(row=6, column=1)
e6.grid(row=7, column=1)
e7.grid(row=8, column=1)
e8.grid(row=10, column=1)

Button(master, text='Calculate', command=pivotcal).grid(row=11, column=0, sticky=W, pady=4)
Button(master, text='About', command=about).grid(row=11, column=1, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=11, column=2, sticky=W, pady=4)

mainloop()