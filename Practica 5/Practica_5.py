
import re
import tkinter as tk 
from tkinter import messagebox

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Datos de registro")
var_genero = tk.IntVar()

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar():
    limpiar_campos()
    
def TelefonoValido(valor):
    return valor.isdigit() and len(valor)==10 

def TextoValido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))

def EnteroValido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
    
def DecimalValido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


    
def guardar():
    nombre = tbNombre.get()
    apellido = tbApellido.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono=tbTelefono.get()
    
    genero=""
    if var_genero.get()==1:
        genero="Hombre"
    elif var_genero.get()==2:
        genero="Mujer"

    if (EnteroValido(edad) and DecimalValido(estatura) and TelefonoValido(telefono) and TextoValido(nombre)):
    
        datos = "Nombres: " + nombre + "\n" + "Apellido: " + apellido + "\n"  + "Edad: " + edad + "\n" + "Telefono:  " + telefono + "\n" + "Estatura: " + estatura + "\n" + "Genero: " + genero + "\n" 
        with open ("C:\\Users\\Ruben Clemente\\Documents\\Practica 04\\Practica 04.txt", "a") as archivo:
            archivo.write(datos + "\n\n")
            
        messagebox.showinfo("Informacion", "Datos guardados correctamente: \n\n" + datos)
        borrar()
   
    else:
        messagebox.showerror("Error", "Algunos campos son incorrectos")

        

lbNombre = tk.Label(ventana, text="Nombre")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellido = tk.Label(ventana, text="Apellido")
lbApellido.pack()
tbApellido = tk.Entry(ventana)
tbApellido.pack()

lbEdad = tk.Label(ventana, text="Edad")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbTelefono = tk.Label(ventana, text="Telefono")
lbTelefono.pack()
tbTelefono =tk.Entry(ventana)
tbTelefono.pack()

lbEstatura = tk.Label(ventana, text="Estatura")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

rbGenero = tk.Label(ventana, text="Genero")
rbGenero.pack()
rbGenero1 = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbGenero1.pack()
rbGenero2 = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbGenero2.pack()

bnBorrar = tk.Button(ventana, text="Borrar campos", command=borrar)
bnBorrar.pack()

bnGuardar = tk.Button(ventana, text="Guardar", command=guardar)
bnGuardar.pack()

ventana.mainloop()