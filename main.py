from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter
from tkinter.font import BOLD, ITALIC
import random

ventanain = Tk()
ventanain.title("CAJERO EAN")
ventanain.geometry('600x500')
ventanain.config(bd=40, bg="#8A8A8A")

etiquetabienvenidos = Label(ventanain, text="Bienvenido al Cajero EAN", font=(
    "ARIAL", 30), bg="#60A420", fg="#223499", width="60", height=6, bd=4, relief=RAISED)
etiquetabienvenidos.pack()
#######
usuarios = [["gabriel", "1234", "restaurante", "10_000_000"], ["ivan", "1213",
                                                               "banco", "1000"], ["admin", "clave", "parqueadero", "19999"], [" ", " ", " ", " "]]


def login():

  ventanain.withdraw()
  ventana = tk.Tk()
  ventana.title("log in")
  ventana.geometry("700x600")
  ventana.config(bd=40, bg="#8A8A8A")
  loginto = Label(ventana, text="ingrese usuario y contraseña", font=("Bahnschrift SemiBold Condensed",
                  25, ITALIC, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
  loginto.pack(pady=20)

  #
  usuarioc = tk.Label(ventana, text="Usuario:", bg="#60A420", fg="black")
  usuarioc.pack(pady=3, side=tk.TOP)
  entrada1 = tk.Entry(ventana)
  entrada1.pack(pady=7)
  clavec = tk.Label(ventana, text="Clave:", bg="#60A420", fg="black")
  clavec.pack(pady=3, side=tk.TOP)
  entrada2 = tk.Entry(ventana)
  entrada2.pack(pady=7)

  #
  def validar():
      for a in range(0, 4):
          if (usuarios[a][0] == entrada1.get() and usuarios[a][1] == entrada2.get()):
            entidades()
            break
          else:
              messagebox.showwarning(
                  "intente de nuevo", "usuario o contraseña no validos")

  boton3 = tk.Button(ventana, text="validar clave", command=validar)
  boton3.pack(pady=20)

  loginto3 = Label(ventana, text="En caso de no tener un usuario comuniquese con el administrador (018000 admin)", font=(
      "arial", 11,  BOLD), bg="#E36421", fg="black", width="90", height=2, bd=8, relief=RAISED)
  loginto3.pack(pady=80)

  def entidades():
    ventana.withdraw()
    entidades = tk.Toplevel()
    entidades.geometry("600x500")
    entidades.title("Entidades")
    entidades.config(bd=40, bg="#8A8A8A")
    loginto2 = Label(entidades, text="Seleccione su entidad", font=("Bahnschrift SemiBold Condensed",
                     25, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
    loginto2.pack(pady=20)
    #

    def banco():
      entidades.withdraw()
      banco = tk.Toplevel()
      banco.geometry("600x500")
      banco.title("Banco EAN")
      banco.configure(bd=40, bg="#1586BF")
      for i in usuarios:
        for x in range(0, 4):
          dinero = i[3]

      def saldo():
        messagebox.showinfo("Saldo", "Tu saldo es de " + str(dinero))

      botoncon = tk.Button(banco, text="Consultar su saldo", font=("Bahnschrift SemiBold Condensed", 25, BOLD),
                           bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED, command=saldo)
      botoncon.pack(pady=10)

      Retirar = Label(banco, text="Retiro", font=("Bahnschrift SemiBold Condensed", 25, BOLD),
                      bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      Retirar.pack(pady=25)
      messagebox.askokcancel("Retirar", "Retirando monto")

      Transferir = Label(banco, text="Transferir dinero", font=("Bahnschrift SemiBold Condensed",
                         25, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)

      botoncon = tk.Button(banco, text="Retiro", font=("Bahnschrift SemiBold Condensed", 25, BOLD),
                           bg="yellow", fg="#271F26", width="40", height=2, bd=8, relief=RAISED, command=banco2)
      botoncon.pack(pady=10)

      Transferir = Label(banco, text="Transferir dinero", font=("Bahnschrift SemiBold Condensed",
                                                                25, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)

      Transferir.pack(pady=25)

      messagebox.askquestion("Transferir", "¿Esta seguro de tranferirlo?")
      messagebox.askokcancel("Tranferiendo", "Enviendo el dinero")

    def Parqueadero():
      entidades.withdraw()
      Parqueadero = tk.Toplevel()
      Parqueadero.geometry("600x500")
      Parqueadero.title("Parqueadero EAN")
      Parqueadero.configure(bd=40, bg="#765048")

      opciones = Label(Parqueadero, text="Digite el la cantidad que hay en la caja", font=(
          "Bahnschrift SemiBold Condensed", 25, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      opciones.pack(pady=25)

      entrada3 = tk.Entry(Parqueadero)
      entrada3.pack()

      def opcionespar():
        Parqueadero.withdraw()
        Parqueaderoop = tk.Toplevel()
        Parqueaderoop.geometry("600x500")
        Parqueaderoop.title("Parqueadero EAN")
        Parqueaderoop.configure(bd=40, bg="#765048")

        def sextosentido():
          cantidad=tk.Toplevel()
          cantidad.geometry("300x300")
          cantidad.title("cantidad")
          cantidad.configure(bd=40, bg="#765048")
          dinerocaja = Label(cantidad, text="el dinero en caja es de", font=("Bahnschrift SemiBold Condensed", 15, BOLD), bg="purple", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
          dinerocaja.pack(pady=25)
          dineroc = Label(cantidad,text=str(entrada3.get())) 
          dineroc.pack(pady=25)
          
        

        

        def cambiospues():
          Parqueaderoop.withdraw()
          vueltas = tk.Toplevel()
          vueltas.geometry("600x500")
          vueltas.title("Vueltas")
          vueltas.configure(bd=40, bg="#765048")
          retiro = int(input("¿Cuanto desea retirar?: "))
          
       

        dinerocaja = Button(Parqueaderoop, text='Dinero Caja', font=(
            "ARIAL", 15), fg="black", command=sextosentido)
        dinerocaja.pack(padx=20, pady=30)
        dasda = tk.Label(Parqueaderoop, text="Digite el dinero para dar las vueltas", font=(
            "ARIAL", 13), bg="#60A420", fg="black")
        dasda.pack(pady=3, side=tk.TOP)
        entrada4 = tk.Entry(Parqueaderoop)
        entrada4.pack(pady=20)
        devueltascaja = Button(Parqueaderoop, text="Siguiente ", font=(
            "Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=cambiospues)
        devueltascaja.pack(padx=20, pady=30)

      botonpar = Button(Parqueadero, text='Siguiente', font=(
          "ARIAL", 15), fg="black", command=opcionespar)
      botonpar.pack(padx=20, pady=30)
      retiro = int(input("¿Cuanto desea retirar?: "))


###

    def restaurante():
      entidades.withdraw()
      restaurante = tk.Toplevel()
      restaurante.geometry("600x500")
      restaurante.title("Restaurante EAN")
      restaurante.configure(bd=40, bg="#CD3618")

      bien = Label(restaurante, text="bienvenidos", font=("Bahnschrift SemiBold Condensed",
                   25, BOLD), bg="#60A420", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      bien.pack()
      Transferir = Label(restaurante, text="cuanto dinero", font=("Bahnschrift SemiBold Condensed",
                         25, BOLD), bg="orange", fg="#271F26", width="40", height=2, bd=8, relief=RAISED)
      Transferir.pack(pady=25)
      entrada3 = tk.Entry(restaurante)
      entrada3.pack()

      #
    botonbanco = tk.Button(entidades, text="Banco EAN", font=(
        "Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=banco)
    botonbanco.pack(pady=10)
    botonparque = tk.Button(entidades, text="Parqueadero EAN", font=(
        "Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=Parqueadero)
    botonparque.pack(pady=10)
    botonres = tk.Button(entidades, text="Restaurante EAN", font=(
        "Bahnschrift SemiBold Condensed", 25, ITALIC, BOLD), command=restaurante)
    botonres.pack(pady=10)
    #


botonsig = Button(ventanain, text='Siguiente', font=(
    "ARIAL", 15), fg="black", command=login)
botonsig.pack(padx=20, pady=30)


ventanain.mainloop()
