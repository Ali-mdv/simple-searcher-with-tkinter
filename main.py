from tkinter import *
import tkinter.filedialog as filedialog
from os import walk ,path
import subprocess
from tkinter import messagebox


# --------------------------------------function-----------------------------------------
def open_file_search(address,list_box):
    list_box.delete(0, END)
    input_path = filedialog.askopenfile()

    if path.splitext(input_path.name)[1] != '.txt':
        return messagebox.showerror(title='File', message='File Not Support')

    entry_search_with_file.delete(0,END)
    entry_search_with_file.insert(0,path.basename(input_path.name))
    files_search = list(input_path)
    global list_not_found
    list_not_found = []
    for i in range(len(files_search)):
        files_search[i] = files_search[i].strip()
        flag = search(address,list_box,files_search[i])

        if not flag:
            list_not_found.append(files_search[i])

    if len(list_box.get(0,END)) == 0:
        messagebox.showerror(title='Search', message='File Not Exist')

    

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
    flag = True
    len_listbox = len(list_box.get(0,END))
    if not sensitive.get():
        if extention.get():
            if all_file.get():
                for path_, folders, files in walk(address):
                    for item in files:
                        if item.lower() == filesearch.lower():
                            list_box.insert(0,path_ + '/' + item)

    elif sensitive.get():
        if not extention.get():
            if all_file.get():
                for path_, folders, files in walk(address):
                    for item in files:
                        if path.splitext(item)[0] == path.splitext(filesearch)[0]:
                            list_box.insert(0,path_ + '/' + item)

    elif sensitive.get():
        if extention.get():
            if not all_file.get():
                for path_, folders, files in walk(address):
                    for item in files:
                        if item.startswith(filesearch):
                            list_box.insert(0,path_ + '/' + item)

    elif not sensitive.get():
        if not extention.get():
            if all_file.get():
                for path_, folders, files in walk(address):
                    for item in files:
                        if path.splitext(item.lower())[0] == path.splitext(filesearch.lower())[0]:
                            list_box.insert(0,path_ + '/' + item)

    elif not sensitive.get():
        if extention.get():
            if not all_file.get():
                for path_, folders, files in walk(address):
                    for item in files:
                        if filesearch.lower() and item.lower().startswith(filesearch.lower()):
                            list_box.insert(0,path_ + '/' + item)

    elif sensitive.get():
        if not extention.get():
            if not all_file.get():
                for path_, folders, files in walk(address):
                    for item in files:
                        if path.splitext(item)[0].startswith(path.splitext(filesearch)[0]):
                            list_box.insert(0,path_ + '/' + item)

    elif not sensitive.get():
        if not extention.get():
            if not all_file.get():
                for path_, folders, files in walk(address):
                    for item in files:
                        if path.splitext(item.lower())[0].startswith(path.splitext(filesearch.lower())[0]):
                            list_box.insert(0,path_ + '/' + item)

    elif sensitive.get():                    
        if extention.get():
            if all_file.get():
                for path_, folders, files in walk(address):
                    for item in files:
                        if item == filesearch:
                            list_box.insert(0,path_ + '/' + item)

    if len(list_box.get(0,END)) == len_listbox:
        flag = False

    return flag


def  show_function():
    messagebox.showinfo('How to Use With App','')


def save(list_,title,message,name):
    if len(list_) == 0:
        messagebox.showerror(title=title,message=message)
    else:
        input_path = filedialog.askdirectory() + f'/{name}.txt'
        try:
            with open(input_path,'a') as file:
                for item in list_:
                    file.write(f'{item}\n')
        except:
            messagebox.showerror(title="Save Address",message='Not Save To File')
        else:
            messagebox.showinfo(title="Save Address",message='Saved To File')
# --------------------------------------function-----------------------------------------


# --------------------------------------event-----------------------------------------
def get_data(event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            return data

def click(event):
    data = get_data(event)
    address_update.set(data)

def double_click(event):
    data = get_data(event)
    if path.isfile(data):
        a = path.realpath(data)
        subprocess.call(['xdg-open',a])
    else:
        show(data,list_box_show)

# def key_o(event):
#     data = get_data(event)
#     a = path.realpath(data)
#     startfile(a)

def key_n(event):
    data = get_data(event)
    test = "/".join(data.split("/")[0:-1])
    a = path.realpath(test)
    subprocess.call(['xdg-open',a])
# --------------------------------------event-----------------------------------------



# --------------------------------------tkinter-----------------------------------------
# --------------------------------------tkinter-----------------------------------------

window = Tk()
window.title("Search")
window.geometry('565x430')
window.resizable(width=0,height=0)

# --------------------------------------var-----------------------------------------
address = StringVar()
file_search = StringVar()
search_file_name = StringVar()
address_update = StringVar()

sensitive = BooleanVar()
extention = BooleanVar()
all_file = BooleanVar()
# --------------------------------------var-----------------------------------------



# --------------------------------------label-----------------------------------------
label_adress = Label(window,text='Address:')
label_adress.config(font=("Calibri", 13))
label_adress.grid(column=0,row=0,sticky=W+E,padx=(5,5),pady=(2,2))
label_search = Label(window,text='Search:')
label_search.config(font=("Calibri", 13))
label_search.grid(column=0,row=2,sticky=W+E,padx=(5,5),pady=(2,2))
label_search_with_file = Label(window,text='Search With File:')
label_search_with_file.config(font=("Calibri", 13))
label_search_with_file.grid(column=0,row=3,sticky=W+E,padx=(5,5),pady=(2,2))
# --------------------------------------label-----------------------------------------



# --------------------------------------entry-----------------------------------------
entry_address = Entry(window,textvariable=address,state='readonly',width=33)
entry_address.grid(column=1,row=0,padx=(5,5),pady=(2,2),sticky=W+E)

entry_search = Entry(window,textvariable=file_search,width=33)
entry_search.grid(column=1,row=2,padx=(5,5),pady=(2,2),sticky=W+E)

entry_search_with_file = Entry(window,textvariable=search_file_name,width=33)
entry_search_with_file.grid(column=1,row=3,padx=(5,5),pady=(2,2),sticky=W+E)

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
btn_back.grid(column=0,row=12,padx=(4,1),pady=(2,1),sticky=W+E,columnspan = 3)

btn_search_by_file = Button(window,text='search by file',bg='white',fg='black',pady=1,command=lambda:open_file_search(address.get(),list_box_show))
btn_search_by_file.grid(column=2,row=3,padx=(1,1),pady=(2,1),sticky=W+E)
# --------------------------------------botton-----------------------------------------



# --------------------------------------listbox-----------------------------------------
list_box_show = Listbox(window,width=40,height=12)
list_box_show.grid(column=0,row=5,rowspan=4,padx=(5,5),pady=(2,2),sticky=W+E,columnspan = 3)
list_box_show.bind("<<ListboxSelect>>", click)
list_box_show.bind("<Double-Button-1>", double_click)
# list_box_show.bind("<Control-o>", key_o)
list_box_show.bind("<Control-n>", key_n)
# --------------------------------------listbox-----------------------------------------



# --------------------------------------scroll-----------------------------------------
scroll_y = Scrollbar(window,orient="vertical")
scroll_y.grid(column=2,row=5,rowspan=4,padx=(5,5),pady=(2,2),sticky=E+S+N)
list_box_show.config(yscrollcommand=scroll_y.set)
scroll_y.config(command=list_box_show.yview)

scroll_x = Scrollbar(window,orient='horizontal')
scroll_x.grid(row=8,padx=(5,5),pady=(2,2),sticky=S+W+E,columnspan = 3)
list_box_show.config(xscrollcommand=scroll_x.set)
scroll_x.config(command=list_box_show.xview)
# --------------------------------------scroll-----------------------------------------



# --------------------------------------menu-----------------------------------------
menu_bar = Menu(window)
option = Menu(menu_bar,tearoff = 0)
menu_bar.add_cascade(label ='Option', menu = option)
option.add_command(label = 'Save Address',command = lambda: save(list_box_show.get(0,END),"Save Address",'There is no Address to Save','adress'))
option.add_separator()
option.add_command(label = 'Save Not Found',command = lambda: save(list_not_found,"Save Not Found",'All files are available','not_found'))
option.add_separator()
option.add_command(label = 'Exit', command = lambda : window.destroy())

help_ = Menu(menu_bar, tearoff = 0) 
menu_bar.add_cascade(label ='Help', menu = help_)
help_.add_command(label = 'information', command = lambda:show_function())

window.config(menu = menu_bar)
# ------------------------------------menu-------------------------------------------------


# ------------------------------------Checkbutton-------------------------------------------------
checkbtn_case_sensitive = Checkbutton(window,text = 'Case Sensitive',variable =sensitive)
checkbtn_case_sensitive.grid(column=0,row=4)
checkbtn_extensions = Checkbutton(window,text = 'Extensions',variable =extention)
checkbtn_extensions.grid(column=1,row=4)
checkbtn_all_file = Checkbutton(window,text = 'All File',variable =all_file)
checkbtn_all_file.grid(column=2,row=4)
# ------------------------------------Checkbutton-------------------------------------------------


window.mainloop()
