import tkinter

ventana = tkinter.Tk()

ventana.geometry("600x400")

etiqueta = tkinter.Label(ventana, text = 'Pantalla entrada principal')
etiqueta.pack()

ventana.mainloop()