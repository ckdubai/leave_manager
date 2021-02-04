from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from datetime import datetime
from tkinter import messagebox as mb
import tkinter.font as font
import backend

def entry_validate():
    if entry_holiday.index("end") == 0 or entry_days.index("end") == 0 or len(staff_name_text.get()) == 0:
        mb.showerror("Add Off Days", "Please fill all details")
        return False
    else:
        return True

def add_command():

    if entry_validate() == True:
        backend.insert(holiday_text.get(),days_text.get(),staff_name_text.get())
        view_command()

    #save_image()
    #clear_textfield()

def view_command():
    tree.delete(*tree.get_children())
    for row in backend.view():
        tree.insert("",END,values=row,tag='gray')

def get_selected_row(event):

    clear_textfield()
    global selected_tuple
    for selected_tuple in tree.selection():
        global id
        id,holiday,days,staff = tree.item(selected_tuple, 'values')
        #e1.insert(END, id)
        entry_holiday.insert(END, holiday)
        entry_days.insert(END, days)
        staff_combo.set(staff)

def get_selected_row_offtaken(event):

    #clear_textfield_offtaken()
    global selected_tuple
    for selected_tuple in tree2.selection():
        global sid
        sid,staff,off_day = tree2.item(selected_tuple, 'values')
        #e1.insert(END, id)
        staff_combo2.set(staff)
        OBJ=datetime.strptime(off_day,"%Y-%m-%d")
        #print(type(OBJ))
        #off_day.strftime('%x')
        cal.set_date(OBJ)

def clear_textfield():
    entry_days.delete(0,END)
    entry_holiday.delete(0,END)

def delete_command():
    qst = mb.askquestion("Confirm Delete","Are you sure?")
    if qst == 'yes':
        try:
            backend.delete(id)
            view_command()
        except:
            mb.showerror("Delete Off Days", "Please select data to delete")
    else:
        pass



def update_command():
    if entry_validate() == True:
        backend.update(id,entry_holiday.get(),entry_days.get(),staff_name_text.get())
        view_command()
        clear_textfield()

def search_command():
    tree.delete(*tree.get_children())
    for row in backend.search(entry_holiday.get(),entry_days.get(),staff_name_text.get()):
        tree.insert("",END,values=row)


def get_selected_date(event):
    global off_date
    off_date =cal.get_date()
    #off_date = datetime.datetime.now()
    #print(off_date)
    #print(type(off_date))

def add_offtaken():
    if len(staff_name_text2.get()) == 0:
        mb.showerror("Add Off Taken", "Please fill all details")
        return False

    off_date=cal.get_date()
    #print("image path = "+image_path)
    backend.insert_offtaken(staff_name_text2.get(),off_date)
    view_offtaken()
    #save_image()
    #clear_textfield()

def view_offtaken():
    tree2.delete(*tree2.get_children())
    for row in backend.view_offtaken():
        tree2.insert("",END,values=row)

def del_offtaken():

    qst =mb.askquestion("Confirm Delete","Are you sure?")
    if qst == 'yes':
        try:
            backend.delete_offtaken(sid)
            view_offtaken()
        except:
            mb.showerror("delete Off taken", "Please select data to delete")
    else:
        Pass



def update_offtaken():
    if len(staff_name_text2.get()) == 0:
        mb.showerror("Add Off Taken", "Please fill all details")
        return False

    off_date=cal.get_date()
    #print(off_date)
    #print(staff_name_text2)
    try:
        backend.update_offtaken(sid,staff_name_text2.get(),off_date)
    except:
        mb.showerror("update Off taken", "Please select data to update")

    #view_command()
    #clear_textfield()
def staff_name_selected_func(event):
    #print(staff_combo2.get())
    staff_name=staff_combo2.get()
    #print(staff_name)
    tree2.delete(*tree2.get_children())
    for row in backend.viewby_staffname(staff_name):
        tree2.insert("",END,values=row)

    balance = backend.get_off_status(staff_name)
    if balance is not None:
        label_bal.config(text="Remaining Pending OFF: " + str(balance))
    else:
        label_bal.config(text="No Pending Off Remaining!")

def callback(input):
	if input.isdigit():
		return True
	else:
		return False

window=Tk()
#window.geometry("1000x800")
window.wm_title("Pending Leave")

tab_parent = ttk.Notebook(window)

"""  two tabs """
entry_tab = ttk.Frame(tab_parent)
view_tab = ttk.Frame(tab_parent)

tab_parent.add(entry_tab, text='Add Holidays')
tab_parent.add(view_tab, text='Pending Off Register')

tab_parent.grid(row=0,column=0)

""" widget centering"""

# Gets the requested values of the height and widht.
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth()/3 - windowWidth/3)
positionDown = int(window.winfo_screenheight()/3 - windowHeight/3)

# Positions the window in the center of the page.
window.geometry("+{}+{}".format(positionRight, positionDown))


"""  tab entry form """
boldFont = font.Font(size = 10, weight = "bold")
label_event = Label(entry_tab,text="Holiday")
label_event.grid(row=1,column=0,columnspan=2,padx=20,pady=3,sticky=W)
label_days = Label(entry_tab,text="No: of Days")
label_days.grid(row=1,column=2,sticky=W)
label_staff = Label(entry_tab,text="Select Staff Name")
label_staff.grid(row=1,column=3,sticky = W,padx=10)

"""  textbox and combo """
holiday_text=StringVar()
entry_holiday=Entry(entry_tab,width=50,textvariable=holiday_text)
entry_holiday.grid(row=2,column=0,padx=20,columnspan=2,ipady=3)

days_text=StringVar()
entry_days=Entry(entry_tab,textvariable=days_text)
entry_days.grid(row=2,column=2,ipady=3)

""" combobox font"""
font_for_combo = ("Times New Roman", 16, "bold")

namelist =["ANISH","ARSHAD","SALI","MUSTHAFA","SHAHEER"]
staff_name_text=StringVar()
staff_combo=ttk.Combobox(entry_tab,width=30,height=20,textvariable=staff_name_text)
staff_combo.grid(row=2,column=3,padx=10,columnspan=2,ipady=3)
staff_combo['values'] = namelist
#staff_combo.focus_set()
window.option_add('*TCombobox*Listbox.font', font_for_combo)

btn_add=Button(entry_tab,text="Add Holiday", width=15,font=boldFont, command=add_command)
btn_add.grid(row=2,column=5,padx=(0,20))

btn_view=Button(entry_tab,text="View All", width=12,font=boldFont,command=view_command)
btn_view.grid(row=4,column=1,pady=20,sticky=NSEW)

btn_search=Button(entry_tab,text="Search Entry", width=15,font=boldFont,command=search_command)
btn_search.grid(row=4,column=2,pady=20,sticky=NSEW)

btn_update=Button(entry_tab,text="Update Selected", width=15,font=boldFont,command=update_command)
btn_update.grid(row=4,column=3,pady=20,sticky=NSEW)

btn_delete=Button(entry_tab,text="Delete Selected", width=15,font=boldFont,command=delete_command)
btn_delete.grid(row=4,column=4,pady=20,sticky=NSEW)


""" Treeview """
tree= ttk.Treeview(entry_tab, column=("ID","Holiday", "No: Of Days", "Staff Name"), show='headings')
tree.heading("#1", text="ID")
tree.heading("#2", text="Holidays")
tree.heading("#3", text="NO: Of Days")
tree.heading("#4", text="Staff Name")
tree.column("#1", minwidth=0, width=30, stretch=NO)
tree.column("#3", anchor=CENTER)
tree.grid(row=6,column=0,columnspan=12,pady=20)

tree.bind("<<TreeviewSelect>>",get_selected_row)


reg = window.register(callback)
entry_days.config(validate ="key",
		validatecommand =(reg, '%S'))

"""  tab pending off deduction """

label_staff = Label(view_tab,text="Select Staff Name",padx=10)
label_staff.grid(row=0,column=0)

label_bal = Label(view_tab,text="Off Balance: ",width=20,fg="#0000FF")
label_bal.grid(row=1,column=2)


label_date = Label(view_tab,text="Select OFF Date")
label_date.grid(row=0,column=3)



namelist =["ANISH","ARSHAD","SALI","MUSTHAFA","SHAHEER"]
staff_name_text2=StringVar()
staff_combo2=ttk.Combobox(view_tab,width=30,height=20,textvariable=staff_name_text2)
staff_combo2.grid(row=0,column=2,ipady=3)
staff_combo2['values'] = namelist
staff_combo2.focus_set()
staff_combo2.bind("<<ComboboxSelected>>", staff_name_selected_func)

cal = DateEntry(view_tab,width=30,bg="darkblue",fg="white",year=2021,date_pattern='dd-mm-y')
cal.grid(row=0,column=4,ipady=3)
cal.bind("<<DateEntrySelected>>", get_selected_date)

boldFont = font.Font(size = 10, weight = "bold")
btn_add_off=Button(view_tab,text="Add Off Day", width=12,font = boldFont,command=add_offtaken)
btn_add_off.grid(row=0,column=5,padx=10,pady=10)

btn_view_off=Button(view_tab,text="View All", width=12,font = boldFont,command=view_offtaken)
btn_view_off.grid(row=2,column=2,padx=10,pady=10,sticky=E)

btn_update_off=Button(view_tab,text="Update Selected", width=15,font = boldFont,command=update_offtaken)
btn_update_off.grid(row=2,column=3,pady=10)

btn_delete_off=Button(view_tab,text="Delete Selected", width=15,font = boldFont,command=del_offtaken)
btn_delete_off.grid(row=2,column=4,sticky=W,pady=10,padx=10)

style = ttk.Style()
style.configure(".", font=('Helvetica', 10),relief = 'flat')
style.configure('TNotebook.Tab', font=('URW Gothic L','11','bold') )

#style.configure("Treeview", foreground='red')
style.configure("Treeview.Heading", font=('Helvetica', 12),foreground='green')

""" Treeview for viewing off taken"""
tree2= ttk.Treeview(view_tab, column=("ID", "Staff Name","OFF taken Date"), show='headings')
tree2.heading("#1", text="ID")
tree2.heading("#2", text="Staff Name")
tree2.heading("#3", text="OFF Taken Date")
tree2.column("#1", minwidth=0, width=30, stretch=NO)
tree2.column("#3", anchor=CENTER)
tree2.grid(row=3,column=0,columnspan=6,padx=10,pady=20)
tree2.bind("<<TreeviewSelect>>",get_selected_row_offtaken)

window.mainloop()
