#Like Notepad Project 


import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, messagebox,filedialog
import os

win = tk.Tk()
win.title('TVPF Text Editor')
win.geometry('700x500')
win.iconbitmap('icon.ico')


############################################### Main Menu ####################################################
# ............................................. End Menu ....................................................
main_menu = tk.Menu()
#file icons
new_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\new.png")
open_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\open.png")
save_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\save.png")
save_as_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\save_as.png")
exit_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\exit.png")

file = tk.Menu(main_menu,tearoff=False)

## edit_icons
copy_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\copy.png")
paste_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\paste.png")
cut_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\cut.png")
clear_all_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\clear_all.png")
find_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\find.png")

edit = tk.Menu(main_menu,tearoff=False)

# view_icons
toolbar = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\tool_bar.png")
statusbar = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\status_bar.png")

view = tk.Menu(main_menu,tearoff=False)

# Color_Theme
light_default = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\light_default.png")
light_plus = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\light_plus.png")
night_blue = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\night_blue.png")
monokai = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\monokai.png")
red = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\red.png")
dark = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\dark.png")

color_theme = tk.Menu(main_menu,tearoff=False)

theme_choice = tk.StringVar()
color_icons=(light_default,light_plus,night_blue,monokai,red,dark)

color_dict = {
    'Light Default ':('#000000','#ffffff'),
    'Light Plus ':('#474747','#e0e0e0'),
    'Night Blue ':('#ededed','#6b9dc2'),
    'Monokia ':('#d3b774','#474747'),
    'Red ':('#2d2d2d','#ffe8e8'),
    'Dark ':('#c4c4c4','#2d2d2d')
}


main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color_Theme',menu=color_theme)


############################################### Toolbar ####################################################
tool_bar = tk.Label(win,bg='orange')
tool_bar.pack(side=tk.TOP,fill=tk.X)
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(padx=10)

# font size
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(2,81,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=20)

# bold Button
bold_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\bold.png")
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=2)

# italic Button
italic_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\italic.png")
italic_btn = ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

# underline Button
underline_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\underline.png")
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

# font color buttun
color_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\font_color.png")
color_btn=ttk.Button(tool_bar,image=color_icon)
color_btn.grid(row=0,column=5,padx=5)

# align left
align_left_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\align_left.png")
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

# align center
align_center_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\align_center.png")
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

# aling right
align_right_icon = tk.PhotoImage(file=r"E:\Python Practice\Notepad\icon\align_right.png")
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

# ............................................. End Toolbar ................................................



############################################### Text Editor ####################################################
text_editor=tk.Text(win)
text_editor.config(wrap='word',relief='flat')

scroll_bar = tk.Scrollbar(win)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font faimily and font size functionality
current_font_family = 'Arial'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size= size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_fontsize)




# ####################### Buttons functionality ###################################

# Bold Button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=change_bold)

# Italic Button functionality
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_btn.configure(command=change_italic)

# Underline Button functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_underline)

# font color functionality
def change_color():
    color_var=tk.colorchooser.askcolor() # this give all color box
    text_editor.configure(fg=color_var[1])
color_btn.configure(command=change_color)    


# left,right and center Aling Button

# align_left
def alignleft():
    text_left = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_left,'left')
align_left_btn.configure(command=alignleft)

# center_left
def aligncenter():
    text_center = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_center,'center')
align_center_btn.configure(command=aligncenter)

# align_right
def alignright():
    text_right = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_right,'right')
align_right_btn.configure(command=alignright)


text_editor.configure(font = ('Arial',12))
# ............................................. End Text Editor ................................................


############################################### status bar ######################################################

status_Bars =tk.Label(win,text='Status Bar')
status_Bars.pack(side=tk.BOTTOM)

text_changed = True
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        word = len(text_editor.get(1.0,'end-1c').split())   # count input words
        charactor = len(text_editor.get(1.0,'end-1c'))      # count input charactors
        status_Bars.config(text=f'Charactors : {charactor} words : {word}') # show words & charactors in Status_Bar
    text_editor.edit_modified(False)    # continue to count
text_editor.bind('<<Modified>>',changed)    # check to Modified or not

# .......................................... End status bar .....................................................

############################################### Main Menu Functionality ###########################################

# Variable
url = ''
# new_file Functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

# File command
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='ctrl+N',command=new_file)

# open_file Functionality
def open_file():
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetype=(('Text File','*txt'),
    ('All File','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    win.title(os.path.basename(url))
# Open command
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='ctrl+O',command=open_file)

# save_file Functionality
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All File','*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

# Save command
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='ctrl+S',command=save_file)

# save_as Functionality
def save_as(event=None):
    global url
    try:
        content = str(text_editor.get(1.0,tk.END))
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),('All File','*.*')))
        url.write(content)
        url.close()
    except:
        return

# Save As Command
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='F12',command=save_as)

# Exit Functionality
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        win.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text File','*.txt'),
                    ('All File','*.*')))
                    url.write(content2)
                    url.close()
                    win.destroy()
            elif mbox is False: 
                win.destroy()
        else:
            win.destroy()
    except:
        return
# Exit Command
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Alt+F4',command=exit_func)

############# Find Functionality #########

def find_func(event=None):
    
    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialog = tk.Toplevel()  # it is use to create new window page
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)

# Frame
    find_frame = ttk.LabelFrame(find_dialog,text='Find/Replace')
    find_frame.pack(pady=50)

# Label
    find_label=ttk.Label(find_frame,text='Find :')
    find_label.grid(row=0,column=0,padx=4,pady=4)
    replace_label=ttk.Label(find_frame,text='Replace :')
    replace_label.grid(row=1,column=0,padx=4,pady=4)

# Entry Box
    find_input=ttk.Entry(find_frame,width=40)
    find_input.grid(row=0,column=1,padx=4)
    replace_input=ttk.Entry(find_frame,width=40)
    replace_input.grid(row=1,column=1,padx=4)

# Button
    find_btn = ttk.Button(find_frame,text='Find',command=find)
    find_btn.grid(row=2,column=0,padx=3,pady=0)
    replace_btn = ttk.Button(find_frame,text='Replace',command=replace)
    replace_btn.grid(row=2,column=1,padx=1,pady=0)

    find_dialog.mainloop()

# Edit Command
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear_All',image=clear_all_icon,compound=tk.LEFT,accelerator='ctrl+Alt+X',command = lambda :text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='ctrl+F',command=find_func)

# View Command
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_Bars.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_Bars.pack(side=tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_Bars.pack_forget()
        show_statusbar = False
    else:
        status_Bars.pack(side=tk.BOTTOM)
        show_statusbar = True  


view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=False,variable=show_toolbar,image=toolbar,compound=tk.LEFT,
command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,variable=show_statusbar,image=statusbar,compound=tk.LEFT,
command=hide_statusbar)

# color theme functionality
def change_theme():
    choosen_theme = theme_choice.get()
    color_tuple = color_dict.get(choosen_theme)
    fg_color, bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
# color theme
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1
# ............................................. End Main Menu Functionality .......................................

win.config(menu=main_menu)

win.bind('<Control-n>', new_file)
win.bind('<Control-o>', open_file)
win.bind('<Control-s>', save_file)
win.bind('<F11>', save_as)
win.bind('<Alt-F4>',exit_func)
win.bind('<Control-f>',find_func)
win.bind('<Control-Alt-x>',exit_func)

win.mainloop()
