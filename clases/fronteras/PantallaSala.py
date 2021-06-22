import tkinter as  tk



class PantallaSala():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("800x380") 
        self.window.resizable(0,0)
        self.window.config(background='#1f2f3f')
        self.window.title('') 
        self.current_max_label = tk.Label(text="", font=('ComicSans', 44), fg='#ffffff', bg='#449a66',pady=10,padx=10)
        self.current_max_label.place(x=175, y=160)
        self.current_act_label = tk.Label(text="test", font=('ComicSans', 44), fg='#ffffff', bg='#72a922',pady=10,padx=10)
        self.current_act_label.place(x=175, y=50)
        self.act_cant_visitantes()
        self.window.mainloop()

    def act_cant_visitantes(self):
        cant_maxima_visitantes = "CANT MAX: ", 40
        cant_actual_visitantes = "CANT ACT: ", 23
        self.current_max_label.configure(text= cant_maxima_visitantes)
        self.current_act_label.configure(text= cant_actual_visitantes)
        
       

main = PantallaSala()