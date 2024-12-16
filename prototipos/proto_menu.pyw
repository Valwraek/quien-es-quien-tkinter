from tkinter import *

tk = Tk()

tk.title("¿Quién es Quién?")
tk.geometry("800x600")
tk.resizable(0, 0)
tk.config(bg="lightgray")

caja_padre = Frame(tk, bg="lightblue")
caja_padre.config(width=600, height=400, relief="solid", bd=4)
caja_padre.pack(pady=40, ipady=10)
caja_padre.pack_propagate(False)

encabezado = Label(caja_padre, text="¿Quién es Quién?", font=("Verdana", 20), bg="White")
encabezado.pack(pady=10)

caja_hijos = Frame(caja_padre, bg="lightblue")
caja_hijos.config(width=500, height=300, relief="solid", bd=2)
caja_hijos.pack(pady=20, expand=TRUE)
caja_hijos.pack_propagate(False)

un_jugador = Button(caja_hijos, text="Un jugador")
un_jugador.pack(side=TOP, padx=10, pady=10, anchor="center", expand=TRUE)

dos_jugador = Button(caja_hijos, text="Dos jugadores")
dos_jugador.pack(side=TOP, padx=10, pady=10, anchor="center", expand=TRUE)

reglas = Button(caja_hijos, text="Reglas")
reglas.pack(side=TOP, padx=10, pady=10, anchor="center", expand=TRUE)

tk.mainloop()
