# Main
import tkinter as tk

root = tk.Tk()
root.geometry("1300x720")
root.title("Vallecas")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="¿Duele?")
filemenu.add_separator()
filemenu.add_command(label="Zona", command=root.quit)
menubar.add_cascade(label="Vallecas", menu=filemenu)

main_grid = tk.Frame(root, height=480, width=1280)
main_grid.place(anchor="center", rely=0.4, relx=0.5)

frame_left = tk.Frame(main_grid, height=450, width=200)
frame_left.grid(row=0, column=0, padx=5)

list_menuleft = tk.Listbox(frame_left, relief="sunken")
list_menuleft.place(relheight=1.0, relwidth=1.0)

frame_midleft = tk.Frame(main_grid, height=450, width=400, highlightbackground="red", highlightthickness=3)
frame_midleft.grid(row=0, column=1, padx=5)

frame_midright = tk.Frame(main_grid, height=450, width=400, highlightbackground="red", highlightthickness=3)
frame_midright.grid(row=0, column=2, padx=5)

frame_right = tk.Frame(main_grid, height=450, width=200)
frame_right.grid(row=0, column=3, padx=5)

list_menuright = tk.Listbox(frame_right, relief="sunken")
list_menuright.place(relheight=1.0, relwidth=1.0)

root.config(menu=menubar)
root.mainloop()