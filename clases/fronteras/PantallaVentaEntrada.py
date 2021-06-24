from tkinter import *
from tkinter import ttk


def send_data():
    pass


def obtener_tarifa(args):
    pass


class PantallaVentaEntrada:
    def __init__(self):
        window = Tk()
        window.geometry("990x550")
        window.resizable(False, False)
        window.config(background='#1f2f3f')
        window.title('Pantalla Venta de Entradas')
        main_tittle = Label(text="Venta de Entradas")
        main_tittle.pack()

        cant_entradas_label = Label(text="Cantidad de entradas: ")
        cant_entradas_label.place(x=22, y=70)
        tarifa_seleccionada_label = Label(text="Tarifa: ")
        tarifa_seleccionada_label.place(x=22, y=130)
        combo_tarifa = ttk.Combobox(window, width=17, state='readonly')
        combo_tarifa.place(x=22, y=150)
        opciones = ["opcion 1", "opcion 2", "opcion 3"]
        combo_tarifa['values'] = opciones
        combo_tarifa.set("opcion 1")
        Button(window, text="Obtener", command=obtener_tarifa).place(x=22, y=160)
        entradas_label = Label(text="Entradas: ")
        entradas_label.place(x=22, y=190)

        cant_entradas = StringVar()
        tarifa_seleccionada = StringVar()
        entradas = StringVar()

        cant_entradas_entry = Entry(textvariable=cant_entradas, width="40")
        tarifa_seleccionada_entry = Entry(textvariable=cant_entradas, width="40")
        entradas_entry = Entry(textvariable=cant_entradas, width="40")

        cant_entradas_entry.place(x=22, y=100)
        tarifa_seleccionada_entry.place(x=22, y=160)
        entradas_entry.place(x=22, y=220)

        submit_btn = Button(window, text="Confirmar Venta", command=send_data, width="40", height="2")
        submit_btn.place(x=22, y=500)

        window.mainloop()


def habilitar_ventana(self):
    ventana = PantallaVentaEntrada()
    return 0


if __name__ == '__habilitar_ventana__':
    habilitar_ventana()

    def __init__(self, cant_entradas, combo_tarifas, entradas, tarifa_seleccionada):
        self.cant_entradas=cant_entradas
        self.combo_tarifas=combo_tarifas
        self.entradas=entradas
        self.tarifa_seleccionada=tarifa_seleccionada
