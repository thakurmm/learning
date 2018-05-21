from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox

window = Tk()
window.geometry('750x300')

some_flag="Zero"

# Callback functions should be defined before they are called out later
# Callback functions can use any variable declared prior to being executed at runtime
def clicked01():
    global some_flag
    global window
    global lbl2
    lbl.configure(text="Button 01 was clicked!! - " + some_flag)
    if (some_flag == "Zero"):
        lbl2 = Label(window, text="Label from clicked01")
        lbl2.grid(column=1, row=1)

    if (some_flag == "Two"):
        scroll_txt.delete(1.0,END)

    ival = progress['value']
    progress.configure(value=ival+40)

    progress.start()

    some_flag="One"

def clicked02():
    global some_flag
    global lbl2
    txtstr = "Button 02 was clicked!! - " + some_flag
    lbl.configure(text=txtstr)
    if (some_flag == "One"):
        txtstr = "Welcome - " + txt.get() + " - " + combo.get()
        if chk_state.get():
            txtstr = "True - " + txtstr
        else:
            txtstr = "False - " + txtstr

        txtstr = txtstr + "- Radio " + str(rb_selected.get())

        txtstr = txtstr + " ... Spin1=" + str(spinvar.get())


        progress.stop()
        progress.step(10)

        lbl2.configure(text=txtstr)

        scroll_txt.insert(INSERT,txtstr + "\n")
        scroll_txt.insert(END,"...Text added...\n")



    some_flag="Two"

def clicked03():
    if (rb_selected.get() == 1):
        # Needs import messagebox above
        messagebox.showinfo('Message Box Title','Message Box Content - Info')
    elif (rb_selected.get() == 2):
        # Needs import messagebox above
        messagebox.showwarning('Message Box Title','Message Box Content - Warning')
    elif (rb_selected.get() == 3):
        # Needs import messagebox above
        messagebox.showerror('Message Box Title','Message Box Content - Error')

    YesNoTrueFalse = messagebox.askquestion('Message Box Title','Message Box Content - askquestion')
    YesNoTrueFalse = messagebox.askyesno('Message Box Title','Message Box Content - askyesno')
    OkCancelTrueFalse = messagebox.askokcancel('Message Box Title','Message Box Content - askokcancel')
    RetryCancelTrueFalse = messagebox.askretrycancel('Message Box Title','Message Box Content - askretrycancel')

    YesNoCancelTrueFalseNone = messagebox.askyesnocancel('Message Box Title','Message Box Content - askyesnocancel')


window.title("Hello Tk")

btn = Button(window, text="Click Me", command=clicked01)
btn.grid(column=1, row=0)

btn = Button(window, text="Click Me too", command=clicked02)
btn.grid(column=0, row=1)

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=0, row=2)
txt.focus()

# Needs import tkinter.ttk
combo = Combobox(window)
combo['values'] = ("One","Two","Three")
combo.current(0)
combo.grid(column=1, row=2)

chk_state = BooleanVar()
chk_state.set(True)
checkbutton = Checkbutton(window,text="Choose",var=chk_state)
checkbutton.grid(column=0, row=3)

rb_selected = IntVar()
rb_selected.set(1)
radio1 = Radiobutton(window, text="First", value=1, variable=rb_selected)
radio2 = Radiobutton(window, text="Second", value=2, variable=rb_selected)
radio3 = Radiobutton(window, text="Third", value=3, variable=rb_selected)
radio1.grid(column=0,row=4)
radio2.grid(column=1,row=4)
radio3.grid(column=2,row=4)

# Needs import scrolledtext above
scroll_txt = scrolledtext.ScrolledText(window,width=40,height=4)
scroll_txt.grid(column=0, row=5)

btn = Button(window, text="Test messagebox", command=clicked03)
btn.grid(column=1, row=5)

spinvar = IntVar()
spinvar.set(4)
spinner1 = Spinbox(window,from_=0, to=10, width=5, textvariable=spinvar)
spinner1.grid(column=0,row=6)


spinner2 = Spinbox(window, values=(3,5,8,10), width=5)
spinner2.grid(column=1,row=6)

progress = Progressbar(window, length=250)
progress['value'] = 40
progress.grid(column=0, row=10)


window.mainloop()
