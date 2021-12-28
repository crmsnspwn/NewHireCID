from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry('500x500')
root.title('New Hire Email Clock ID Query')

## Functions

def open_file():
    global file_path
    global file_path_label
    file_path = filedialog.askopenfilename(initialdir = 'F:/NewHireEmails', title = 'Select a File')
    file_path_label = Label(root, text = file_path).pack(fill = BOTH, expand = 1)

def IIQ_Query():
    with open(file_path,'r') as f1:
        f1_contents = f1.read()
        list = [CID.split()[0] for CID in f1_contents.split('Clock Number: ')]
        string = ', '.join(f'"{n}"' for n in list[1:])
    with open('F:/NewHireEmails/query.txt', 'w+') as f2:
        f2.write(f'name.in({{{string}}})').pack(fill = BOTH, expand = 1)

## Objects 

# Labels

# Buttons

search = Button(root, text = 'Open File',padx = 50, pady = 20, command=open_file)
execute = Button(root, text = 'Create Query', padx = 50, pady = 20, command=IIQ_Query)

# Object Positions
search.pack(fill = BOTH, expand = True)
execute.pack(fill = BOTH, expand = True)

root.mainloop()

## Original query (keep as backup)

# with open(r'F:\NewHireEmails\New Hire Emails.txt','r') as f:
#         f_contents = f.read()
#         list = [CID.split()[0] for CID in f_contents.split('Clock Number: ')]
#         string = ', '.join(f'"{n}"' for n in list[1:])
#         print(f'name.in({{{string}}})')