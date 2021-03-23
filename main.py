from tkinter import *
import tkinter.filedialog as filedialog
from os import walk ,path,startfile
from tkinter import messagebox



# --------------------------------------function-----------------------------------------
def browse():
    input_path = filedialog.askdirectory()
    entry_address.configure(state='normal')
    entry_address.delete(0,END)
    entry_address.insert(0,input_path)
    entry_address.configure(state='disabled')
    entry_address_update.delete(0,END)
    entry_address_update.insert(0,input_path)
    

def show(address,list_box):
    list_box.delete(0, END)
    for path, folders, files in walk(address):
        for item in files:
            list_box.insert(0,path + '/' + item)
        
        for item in folders:
            list_box.insert(0,path + '/' + item)
        break

def back(list_box):
    current_ulr = list_box.get(0)
    list_box.delete(0, END)
    for address, folders, files in walk("/".join(current_ulr.split("/")[:-2])):
        for item in files:
            list_box.insert(0,address + '/' + item)
        
        for item in folders:
            list_box.insert(0,address + '/' + item)
        break

def search(address,list_box,filesearch):
    list_box.delete(0, END)
    if sensitive.get() == 'off':
        if extention.get() == 'on':
            if all_file.get() == 'on':
                list_box.delete(0, END)
                for path_, folders, files in walk(address):
                    for item in files:
                        if item.lower() == filesearch.lower():
                            list_box.insert(0,path_ + '/' + item)

    if sensitive.get() == 'on':
        if extention.get() == 'off':
            if all_file.get() == 'on':
                list_box.delete(0, END)
                for path_, folders, files in walk(address):
                    for item in files:
                        if path.splitext(item)[0] == path.splitext(filesearch)[0]:
                            list_box.insert(0,path_ + '/' + item)

    if sensitive.get() == 'on':
        if extention.get() == 'on':
            if all_file.get() == 'off':
                list_box.delete(0, END)
                for path_, folders, files in walk(address):
                    for item in files:
                        if item.startswith(filesearch):
                            list_box.insert(0,path_ + '/' + item)

    if sensitive.get() == 'off':
        if extention.get() == 'off':
            if all_file.get() == 'on':
                list_box.delete(0, END)
                for path_, folders, files in walk(address):
                    for item in files:
                        if path.splitext(item.lower())[0] == path.splitext(filesearch.lower())[0]:
                            list_box.insert(0,path_ + '/' + item)

    if sensitive.get() == 'off':
        if extention.get() == 'on':
            if all_file.get() == 'off':
                list_box.delete(0, END)
                for path_, folders, files in walk(address):
                    for item in files:
                        if filesearch.lower() and item.lower().startswith(filesearch.lower()):
                            list_box.insert(0,path_ + '/' + item)

    if sensitive.get() == 'on':
        if extention.get() == 'off':
            if all_file.get() == 'off':
                list_box.delete(0, END)
                for path_, folders, files in walk(address):
                    for item in files:
                        if path.splitext(item)[0].startswith(path.splitext(filesearch)[0]):
                            list_box.insert(0,path_ + '/' + item)

    if sensitive.get() == 'off':                    
        if extention.get() == 'off':
            if all_file.get() == 'off':
                list_box.delete(0, END)
                for path_, folders, files in walk(address):
                    for item in files:
                        if path.splitext(item.lower())[0].startswith(path.splitext(filesearch.lower())[0]):
                            list_box.insert(0,path_ + '/' + item)

    if sensitive.get() == 'on':                    
        if extention.get() == 'on':
            if all_file.get() == 'on':
                list_box.delete(0, END)
                for path_, folders, files in walk(address):
                    for item in files:
                        if item == filesearch:
                            list_box.insert(0,path_ + '/' + item)
    if len(list_box.get(0,END)) == 0:
        messagebox.showerror(title='Search', message='File Not Exist')



def show_maker():
    messagebox.showinfo("Maker",'Ali Mahdavi, twenty-six years old, has a bachelor\'s degree in chemistry')


def  show_function():
    messagebox.showinfo('How to Use With App','Ali Mahdavi, twenty-six years old, has a bachelor\'s degree in chemistry')


def save_too_file(list_box):
    if len(list_box) == 0:
        messagebox.showerror(title="Save",message='File Not Exist To Save')

    else:
        input_path = filedialog.askdirectory() + '/adress.txt'
        try:
            link = open(input_path,mode='a')
            for item in list_box:
                link.write(f'{item}\n')
        except:
            messagebox.showerror(title="Save",message='Not Save To File')
        else:
            messagebox.showinfo(title="Save",message='Saved To File')
        finally:
            link.close()
    

# --------------------------------------function-----------------------------------------




# --------------------------------------class event-----------------------------------------
class object_event():
    @staticmethod
    def click(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            address_update.set(data)

    @staticmethod
    def double_click(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            # show(data,list_box_show)
            if path.isfile(data):
                a = path.realpath(data)
                startfile(a)
            else:
                show(data,list_box_show)

    # @staticmethod
    # def key_o(event):
    #     selection = event.widget.curselection()
    #     if selection:
    #         index = selection[0]
    #         data = event.widget.get(index)
    #         a = path.realpath(data)
    #         startfile(a)

    @staticmethod
    def key_n(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            test = "/".join(data.split("/")[0:-1])
            a = path.realpath(test)
            startfile(a)
# --------------------------------------class event-----------------------------------------




# --------------------------------------tkinter-----------------------------------------
# --------------------------------------tkinter-----------------------------------------

window = Tk()
window.title("Search")
window.geometry('380x375')
# window.resizable(width=0,height=0)



# --------------------------------------var-----------------------------------------
address = StringVar()
file_search = StringVar()
address_update = StringVar()

sensitive = StringVar()
extention = StringVar()
all_file = StringVar()
# --------------------------------------var-----------------------------------------



# --------------------------------------label-----------------------------------------
label_adress = Label(window,text='Address:')
label_adress.config(font=("Calibri", 13))
label_adress.grid(column=0,row=0,sticky=W+E,padx=(5,5),pady=(2,2))
label_search = Label(window,text='Search:')
label_search.config(font=("Calibri", 13))
label_search.grid(column=0,row=2,sticky=W+E,padx=(5,5),pady=(2,2))
# --------------------------------------label-----------------------------------------



# --------------------------------------entry-----------------------------------------
entry_address = Entry(window,textvariable=address,state=DISABLED,width=33)
entry_address.grid(column=1,row=0,padx=(5,5),pady=(2,2),sticky=W+E)
entry_search = Entry(window,textvariable=file_search,width=33)
entry_search.grid(column=1,row=2,padx=(5,5),pady=(2,2),sticky=W+E)
entry_address_update = Entry(window,textvariable=address_update,width=33)
entry_address_update.grid(column=0,row=9,padx=(5,5),pady=(2,2),sticky=W+E,columnspan = 3)
# --------------------------------------entry-----------------------------------------



# --------------------------------------botton-----------------------------------------
btn_browse = Button(window,text='Browse',bg='white',fg='black',pady=1,command = lambda : browse())
btn_browse.grid(column=2,row=0,padx=(1,1),pady=(2,1),sticky=W+E)
btn_show = Button(window,text='Show',bg='black',fg='white',pady=2,command=lambda:show(address_update.get(),list_box_show))
btn_show.grid(column=0,row=1,padx=(4,1),pady=(2,1),sticky=W+E,columnspan = 3)
btn_search = Button(window,text='Search',bg='white',fg='black',pady=1,command=lambda:search(address.get(),list_box_show,file_search.get()))
btn_search.grid(column=2,row=2,padx=(1,1),pady=(2,1),sticky=W+E)
btn_back = Button(window,text='Back',bg='black',fg='white',pady=2,command=lambda:back(list_box_show))
btn_back.grid(column=0,row=10,padx=(4,1),pady=(2,1),sticky=W+E,columnspan = 3)
# --------------------------------------botton-----------------------------------------



# --------------------------------------listbox-----------------------------------------
list_box_show = Listbox(window,width=40,height=12)
list_box_show.grid(column=0,row=4,rowspan=4,padx=(5,5),pady=(2,2),sticky=W+E,columnspan = 3)
list_box_show.bind("<<ListboxSelect>>", object_event.click)
list_box_show.bind("<Double-Button-1>", object_event.double_click)
# list_box_show.bind("<Control-o>", object_event.key_o)
list_box_show.bind("<Control-n>", object_event.key_n)
# --------------------------------------listbox-----------------------------------------



# --------------------------------------scroll-----------------------------------------
scroll_y = Scrollbar(window,orient="vertical")
scroll_y.grid(column=2,row=4,rowspan=4,padx=(5,5),pady=(2,2),sticky=E+S+N)
list_box_show.config(yscrollcommand=scroll_y.set)
scroll_y.config(command=list_box_show.yview)

scroll_x = Scrollbar(window,orient='horizontal')
scroll_x.grid(row=7,padx=(5,5),pady=(2,2),sticky=S+W+E,columnspan = 3)
list_box_show.config(xscrollcommand=scroll_x.set)
scroll_x.config(command=list_box_show.xview)
# --------------------------------------scroll-----------------------------------------



# --------------------------------------menu-----------------------------------------
menu_bar = Menu(window)
option = Menu(menu_bar,tearoff = 0)
menu_bar.add_cascade(label ='Option', menu = option)
option.add_command(label = 'Save',command = lambda: save_too_file(list_box_show.get(0,END)))
option.add_separator()
option.add_command(label = 'Exit', command = lambda : window.destroy())


help_ = Menu(menu_bar, tearoff = 0) 
menu_bar.add_cascade(label ='Help', menu = help_)
help_.add_command(label = 'Maker', command = lambda:show_maker())
help_.add_command(label = 'information', command = lambda:show_function())


window.config(menu = menu_bar)
# ------------------------------------menu-------------------------------------------------


# ------------------------------------Checkbutton-------------------------------------------------
checkbtn_case_sensitive = Checkbutton(window,text = 'Case Sensitive',variable =sensitive,offvalue = 'off',onvalue = 'on')
checkbtn_case_sensitive.grid(column=0,row=3)
checkbtn_extensions = Checkbutton(window,text = 'Extensions',variable =extention,offvalue = 'off',onvalue = 'on')
checkbtn_extensions.grid(column=1,row=3)
checkbtn_all_file = Checkbutton(window,text = 'All File',variable =all_file,offvalue = 'off',onvalue = 'on')
checkbtn_all_file.grid(column=2,row=3)


# ------------------------------------Checkbutton-------------------------------------------------


window.mainloop()