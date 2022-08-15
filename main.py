from tkinter import Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END



class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='#4779b2')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='#4779b2')
        self.frame4.grid(column=0, row=2)

        self.codigo = StringVar()
        self.nombre = StringVar()
        self.modelo = StringVar()
        self.precio = StringVar()
        self.cantidad = StringVar()
        self.buscar = StringVar()

        #self.base_datos = Registro_datos()
        self.create_ventana()

    def create_ventana(self):
        Label(self.frame1, text = 'R E G I S T R O   D E   D A T O S',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame2, text = 'Agregar Nuevos Datos',fg='gray90', bg ='#4779b2', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text = 'Nombre',fg='white', bg ='#4779b2', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'Apellido',fg='white', bg ='#4779b2', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame2, text = 'Cedula',fg='white', bg ='#4779b2', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame2, text = 'Direccion', fg='white',bg ='#4779b2', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame2, text = 'Edad',fg='white', bg ='#4779b2', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)

        Entry(self.frame2,textvariable=self.codigo , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame2,textvariable=self.nombre , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.modelo , font=('Arial',12)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.precio , font=('Arial',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.cantidad , font=('Arial',12)).grid(column=1,row=5)
       
        Label(self.frame4, text = 'Control',fg='white', bg ='#4779b2', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame4,command= self.agregar_datos, text='REGISTRAR', font=('Arial',10,'bold'), bg='#8da9c9').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame4,command = self.limpiar_datos, text='LIMPIAR', font=('Arial',10,'bold'), bg='#8da9c9').grid(column=1,row=1, padx=10)        
        Button(self.frame4,command = self.eliminar_fila, text='ELIMINAR', font=('Arial',10,'bold'), bg='#8da9c9').grid(column=2,row=1, padx=4)
        Button(self.frame4,command = self.buscar_nombre, text='BUSCAR POR NOMBRE', font=('Arial',8,'bold'), bg='#8da9c9').grid(columnspan=2,column = 1, row=2)
        Entry(self.frame4,textvariable=self.buscar , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame4,command = self.mostrar_todo, text='MOSTRAR DATOS DE DB', font=('Arial',10,'bold'), bg='#8da9c9').grid(columnspan=3,column=0,row=3, pady=8)


        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.tabla['columns'] = ('Nombre','Apellido', 'Cedula', 'Direccion', 'Edad')

        self.tabla.column('Nombre', minwidth=80, width=80, anchor='center')
        self.tabla.column('Apellido', minwidth=80, width=80 , anchor='center')
        self.tabla.column('Cedula', minwidth=80, width=80, anchor='center' )
        self.tabla.column('Direccion', minwidth=80, width=80 , anchor='center')
        self.tabla.column('Edad', minwidth=80, width=80, anchor='center')

        self.tabla.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla.heading('Apellido', text='Apellido', anchor ='center')
        self.tabla.heading('Cedula', text='Cedula', anchor ='center')
        self.tabla.heading('Direccion', text='Direccion', anchor ='center')
        self.tabla.heading('Edad', text='Edad', anchor ='center')


        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila
        

    def agregar_datos(self):
        self.tabla.get_children()
        codigo = self.codigo.get()
        nombre = self.nombre.get()
        modelo = self.modelo.get()
        precio = self.precio.get()
        cantidad = self.cantidad.get()
        datos = (nombre, modelo, precio, cantidad)
        if codigo and nombre and modelo and precio and cantidad !='':        
            self.tabla.insert('',0, text = codigo, values=datos)
            self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)


    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.codigo.set('')
        self.nombre.set('')
        self.modelo.set('')
        self.precio.set('')
        self.cantidad.set('')

    def buscar_nombre(self):
        nombre_producto = self.buscar.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.base_datos.busca_producto(nombre_producto)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])


    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_productos()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][1:2], values=registro[i][2:6])


    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) !=0:        
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.nombre_borar) + "'")       
            self.base_datos.elimina_productos(nombre)


    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]
   

def main():
    ventana = Tk()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('900x500')
    ventana.resizable(0,0)
    app = Registro(ventana)
    app.mainloop()

if __name__=="__main__":
    main()