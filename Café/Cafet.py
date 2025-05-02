import tkinter as tk
from tkinter import ttk, messagebox
import time  # Importamos el módulo time para manejar la hora
from datetime import datetime  # Para formatear la hora

# Menú de LoboCafé (precios en MXN)
menu_lobocafe = {
    "Alimentos": {
        "Croissant": 45.00,
        "Pan de Chocolate": 55.00,
        "Bagel con Queso Crema": 65.00,
        "Tarta de Manzana": 75.00,
        "Sándwich de Jamón y Queso": 85.00,
        "Ensalada César": 95.00,
        "Muffin de Arándanos": 50.00,
        "Brownie": 60.00,
    },
    "Alimentos Veganos/Vegetarianos": {
        "Croissant Vegano": 55.00,
        "Bagel Integral con Hummus": 70.00,
        "Tarta de Manzana Vegana": 80.00,
        "Ensalada de Quinoa": 90.00,
        "Sándwich Vegetariano": 75.00,
    },
    "Bebidas": {
        "Cafés": {
            "Café Americano": 35.00,
            "Café Latte": 65.00,
            "Capuchino": 70.00
        },
        "Tés e Infusiones": {
            "Té Verde": 45.00,
            "Té Negro": 45.00,
            "Chocolate Caliente": 60.00
        },
        "Bebidas Frías": {
            "Jugo de Naranja Natural": 55.00,
            "Agua Mineral": 25.00,
            "Refrescos": {
                "Coca-Cola": 30.00,
                "Sprite": 30.00,
                "Fanta (Naranja)": 30.00,
                "Boing! (Mango)": 35.00,
                "Jarritos (Lima)": 32.00
            }
        }
    }
}

# Variables globales
carrito = {}
total = 0.0
ventana = None  # Variable para la ventana principal

# Función para actualizar el reloj
def actualizar_reloj(label_reloj):
    ahora = datetime.now().strftime("%H:%M:%S")  # Formato HH:MM:SS
    label_reloj.config(text=ahora)
    label_reloj.after(1000, lambda: actualizar_reloj(label_reloj))  # Actualizar cada segundo

def mostrar_ventana_principal():
    global ventana
    
    # Crear la ventana principal si no existe
    if ventana is None or not ventana.winfo_exists():
        ventana = tk.Tk()
        ventana.title("🐺 LoboCafé - Inicio")
        ventana.geometry("450x350")
        ventana.configure(bg="#f5f5f5")

        # Logo y título
        frame_titulo = tk.Frame(ventana, bg="#f5f5f5")
        frame_titulo.pack(pady=30)

        tk.Label(frame_titulo, 
                text="🐺", 
                font=("Arial", 40), 
                bg="#f5f5f5").pack(side="left")

        tk.Label(frame_titulo, 
                text="LoboCafé", 
                font=("Arial", 28, "bold"), 
                bg="#f5f5f5").pack(side="left", padx=10)

        # Mensaje de bienvenida
        tk.Label(ventana, 
                text="Bienvenido a nuestra cafetería", 
                font=("Arial", 12), 
                bg="#f5f5f5").pack(pady=10)

        # Botones principales
        frame_botones = tk.Frame(ventana, bg="#f5f5f5")
        frame_botones.pack(pady=20)

        tk.Button(frame_botones, 
                text="Soy Cliente", 
                command=cliente,
                font=("Arial", 12),
                width=15,
                height=2,
                bg="#4CAF50",
                fg="white").pack(pady=10)

        tk.Button(frame_botones, 
                text="Soy Trabajador", 
                command=trabajador,
                font=("Arial", 12),
                width=15,
                height=2,
                bg="#2196F3",
                fg="white").pack(pady=5)

        # Footer
        tk.Label(ventana, 
                text="© 2023 LoboCafé - Todos los derechos reservados", 
                font=("Arial", 8), 
                bg="#f5f5f5").pack(side="bottom", pady=10)

        ventana.mainloop()
    else:
        # Si la ventana ya existe, simplemente la traemos al frente
        ventana.deiconify()
        ventana.lift()

def cliente():
    ventana_cliente = tk.Toplevel()
    ventana_cliente.title("🐺 LoboCafé - Cliente")
    ventana_cliente.geometry("400x300")
    ventana_cliente.configure(bg="#f5f5f5")
    # Barra superior con reloj
    frame_superior = tk.Frame(ventana_cliente, bg="#e0e0e0", padx=10, pady=5)
    frame_superior.pack(fill="x")
    
    # Reloj
    label_reloj = tk.Label(frame_superior, font=('Arial', 10), bg="#e0e0e0")
    label_reloj.pack(side="right")
    actualizar_reloj(label_reloj)

    # Función para regresar al inicio
    def regresar_inicio():
        ventana_cliente.destroy()
        mostrar_ventana_principal()
    
    # Botón de inicio
    btn_inicio = tk.Button(ventana_cliente, text="🏠 Inicio", command=regresar_inicio,
                        font=("Arial", 10), bg="#2196F3", fg="white")
    btn_inicio.pack(anchor="nw", padx=10, pady=10)

    # Logo y título
    tk.Label(ventana_cliente, 
            text="🐺 LoboCafé", 
            font=("Arial", 20, "bold"), 
            bg="#f5f5f5").pack(pady=20)
    
    tk.Label(ventana_cliente, 
            text="¡Bienvenido! Por favor ingresa tu nombre:", 
            font=("Arial", 11), 
            bg="#f5f5f5").pack(pady=10)

    # Entrada de nombre
    entrada_nombre = tk.Entry(ventana_cliente, font=("Arial", 12))
    entrada_nombre.pack(pady=10, ipady=5)

    def guardar_nombre():
        nombre = entrada_nombre.get().strip()
        if nombre:
            # Limpiar ventana
            for widget in ventana_cliente.winfo_children():
                widget.destroy()
            
            # Mostrar mensaje de bienvenida
            tk.Label(ventana_cliente, 
                    text=f"¡Hola, {nombre}!", 
                    font=("Arial", 16, "bold"), 
                    bg="#f5f5f5").pack(pady=30)
            
            tk.Label(ventana_cliente, 
                    text="¿Qué deseas ordenar hoy?", 
                    font=("Arial", 12), 
                    bg="#f5f5f5").pack()
            
            # Botón para ver el menú
            tk.Button(ventana_cliente, 
                    text="Ver Menú Completo", 
                    command=lambda: mostrar_menu(ventana_cliente),
                    font=("Arial", 12),
                    bg="#4CAF50",
                    fg="white",
                    width=15).pack(pady=20)
        else:
            messagebox.showerror("Error", "Por favor ingresa tu nombre")

    # Botón de continuar
    tk.Button(ventana_cliente, 
            text="Continuar", 
            command=guardar_nombre,
            font=("Arial", 11),
            bg="#2196F3",
            fg="white").pack(pady=15)

def trabajador():
    # Ventana de autenticación
    ventana_login = tk.Toplevel()
    ventana_login.title("🐺 LoboCafé - Acceso Trabajadores")
    ventana_login.geometry("400x300")
    ventana_login.configure(bg="#f5f5f5")
    ventana_login.resizable(False, False)
    # Barra superior con reloj
    frame_superior = tk.Frame(ventana_login, bg="#e0e0e0", padx=10, pady=5)
    frame_superior.pack(fill="x")
    
    # Reloj
    label_reloj = tk.Label(frame_superior, font=('Arial', 10), bg="#e0e0e0")
    label_reloj.pack(side="right")
    actualizar_reloj(label_reloj)
    
    # Función para regresar al inicio
    def regresar_inicio():
        ventana_login.destroy()
        mostrar_ventana_principal()
    
    # Botón de inicio
    btn_inicio = tk.Button(ventana_login, text="🏠 Inicio", command=regresar_inicio,
                        font=("Arial", 10), bg="#2196F3", fg="white")
    btn_inicio.pack(anchor="nw", padx=10, pady=10)
    
    # Logo y título
    tk.Label(ventana_login, 
            text="🐺 LoboCafé", 
            font=("Arial", 20, "bold"), 
            bg="#f5f5f5").pack(pady=20)
    
    tk.Label(ventana_login, 
            text="Acceso para trabajadores", 
            font=("Arial", 12), 
            bg="#f5f5f5").pack(pady=5)
    
    # Frame para campos de login
    frame_login = tk.Frame(ventana_login, bg="#f5f5f5")
    frame_login.pack(pady=20)
    
    # Usuario
    tk.Label(frame_login, 
            text="Usuario:", 
            font=("Arial", 10), 
            bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    
    entry_usuario = tk.Entry(frame_login, font=("Arial", 10))
    entry_usuario.grid(row=0, column=1, padx=5, pady=5)
    
    # Contraseña
    tk.Label(frame_login, 
            text="Contraseña:", 
            font=("Arial", 10), 
            bg="#f5f5f5").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    
    entry_contrasena = tk.Entry(frame_login, font=("Arial", 10), show="*")
    entry_contrasena.grid(row=1, column=1, padx=5, pady=5)
    
    # Función para verificar credenciales
    def verificar_login():
        usuario = entry_usuario.get().strip()
        contrasena = entry_contrasena.get().strip()
        
        if usuario == "admin" and contrasena == "12345":
            ventana_login.destroy()
            mostrar_panel_trabajador()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            entry_usuario.delete(0, tk.END)
            entry_contrasena.delete(0, tk.END)
            entry_usuario.focus()
    
    # Frame para botones
    frame_botones = tk.Frame(ventana_login, bg="#f5f5f5")
    frame_botones.pack(pady=10)
    
    # Botón de Iniciar Sesión
    btn_login = tk.Button(frame_botones, 
            text="🔓 Iniciar Sesión", 
            command=verificar_login,
            font=("Arial", 11),
            bg="#4CAF50",
            fg="white",
            width=15)
    btn_login.pack(side="left", padx=10)
    
    # Botón de Cancelar
    btn_cancelar = tk.Button(frame_botones, 
            text="❌ Cancelar", 
            command=regresar_inicio,
            font=("Arial", 11),
            bg="#f44336",
            fg="white",
            width=15)
    btn_cancelar.pack(side="right", padx=10)
    
    # Configurar tecla Enter para iniciar sesión
    ventana_login.bind('<Return>', lambda event: verificar_login())
    
    # Enfocar el campo de usuario al inicio
    entry_usuario.focus()

def mostrar_panel_trabajador():
    ventana_trabajador = tk.Toplevel()
    ventana_trabajador.title("🐺 LoboCafé - Panel de Trabajador")
    ventana_trabajador.geometry("900x700")
    ventana_trabajador.configure(bg="#f5f5f5")
    # Barra superior con reloj
    frame_superior = tk.Frame(ventana_trabajador, bg="#e0e0e0", padx=10, pady=5)
    frame_superior.pack(fill="x")
    
    # Reloj
    label_reloj = tk.Label(frame_superior, font=('Arial', 10), bg="#e0e0e0")
    label_reloj.pack(side="right")
    actualizar_reloj(label_reloj)
    
    # Función para regresar al inicio
    def regresar_inicio():
        ventana_trabajador.destroy()
        mostrar_ventana_principal()
    
    # Botón de inicio
    btn_inicio = tk.Button(ventana_trabajador, text="🏠 Inicio", command=regresar_inicio,
                        font=("Arial", 10), bg="#2196F3", fg="white")
    btn_inicio.pack(anchor="nw", padx=10, pady=10)
    
    # Notebook (pestañas)
    notebook = ttk.Notebook(ventana_trabajador)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)
    
    # Pestaña para agregar productos
    frame_agregar = ttk.Frame(notebook)
    notebook.add(frame_agregar, text="➕ Agregar Productos")
    
    # Variables para el formulario
    categorias = list(menu_lobocafe.keys())
    subcategoria_var = tk.StringVar()
    subcategorias_bebidas = list(menu_lobocafe["Bebidas"].keys())
    
    # Función para actualizar subcategorías
    def actualizar_subcategorias(event=None):
        categoria_seleccionada = combo_categoria.get()
        
        if categoria_seleccionada == "Bebidas":
            combo_subcategoria["values"] = subcategorias_bebidas
            combo_subcategoria.set("")
            combo_subcategoria["state"] = "readonly"
        else:
            combo_subcategoria["values"] = []
            combo_subcategoria.set("")
            combo_subcategoria["state"] = "disabled"
    
    # Formulario para agregar productos
    tk.Label(frame_agregar, 
            text="Agregar Nuevo Producto", 
            font=("Arial", 14, "bold"), 
            background="#f5f5f5").pack(pady=10)
    
    # Frame para el formulario
    frame_formulario = tk.Frame(frame_agregar, bg="#f5f5f5")
    frame_formulario.pack(pady=10)
    
    # Categoría
    tk.Label(frame_formulario, 
            text="Categoría:", 
            font=("Arial", 10), 
            bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    
    combo_categoria = ttk.Combobox(frame_formulario, values=categorias, state="readonly")
    combo_categoria.grid(row=0, column=1, padx=5, pady=5)
    combo_categoria.bind("<<ComboboxSelected>>", actualizar_subcategorias)
    
    # Subcategoría (solo para bebidas)
    tk.Label(frame_formulario, 
            text="Subcategoría:", 
            font=("Arial", 10), 
            bg="#f5f5f5").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    
    combo_subcategoria = ttk.Combobox(frame_formulario, textvariable=subcategoria_var, state="disabled")
    combo_subcategoria.grid(row=1, column=1, padx=5, pady=5)
    
    # Nombre del producto
    tk.Label(frame_formulario, 
            text="Nombre:", 
            font=("Arial", 10), 
            bg="#f5f5f5").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    
    entry_nombre = tk.Entry(frame_formulario, font=("Arial", 10))
    entry_nombre.grid(row=2, column=1, padx=5, pady=5)
    
    # Precio
    tk.Label(frame_formulario, 
            text="Precio ($):", 
            font=("Arial", 10), 
            bg="#f5f5f5").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    
    entry_precio = tk.Entry(frame_formulario, font=("Arial", 10))
    entry_precio.grid(row=3, column=1, padx=5, pady=5)
    
    # Función para agregar el producto al menú
    def agregar_producto():
        categoria = combo_categoria.get()
        subcategoria = combo_subcategoria.get()
        nombre = entry_nombre.get().strip()
        precio = entry_precio.get().strip()
        
        # Validaciones
        if not categoria:
            messagebox.showerror("Error", "Selecciona una categoría")
            return
            
        if categoria == "Bebidas" and not subcategoria:
            messagebox.showerror("Error", "Selecciona una subcategoría para bebidas")
            return
            
        if not nombre:
            messagebox.showerror("Error", "Ingresa el nombre del producto")
            return
            
        try:
            precio_float = float(precio)
            if precio_float <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingresa un precio válido (número mayor a 0)")
            return
        
        # Agregar el producto a la estructura del menú
        if categoria == "Bebidas":
            if subcategoria not in menu_lobocafe[categoria]:
                menu_lobocafe[categoria][subcategoria] = {}
            menu_lobocafe[categoria][subcategoria][nombre] = precio_float
        else:
            menu_lobocafe[categoria][nombre] = precio_float
        
        messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado al menú con precio ${precio_float:.2f}")
        
        # Limpiar el formulario
        combo_categoria.set("")
        combo_subcategoria.set("")
        combo_subcategoria["state"] = "disabled"
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
    
    # Botón para agregar producto
    tk.Button(frame_agregar, 
            text="➕ Agregar Producto", 
            command=agregar_producto,
            font=("Arial", 11),
            bg="#4CAF50",
            fg="white").pack(pady=20)
    
    # Pestaña para modificar precios
    frame_modificar = ttk.Frame(notebook)
    notebook.add(frame_modificar, text="✏️ Modificar Precios")
    
    # Función para cargar productos según categoría seleccionada
    def cargar_productos(event=None):
        categoria_seleccionada = combo_categoria_mod.get()
        combo_producto_mod["values"] = []
        entry_nuevo_precio.delete(0, tk.END)
        
        if categoria_seleccionada:
            productos = []
            if categoria_seleccionada == "Bebidas":
                for subcat, items in menu_lobocafe[categoria_seleccionada].items():
                    for producto in items.keys():
                        productos.append(f"{subcat} > {producto}")
            else:
                productos = list(menu_lobocafe[categoria_seleccionada].keys())
            
            combo_producto_mod["values"] = productos
            combo_producto_mod["state"] = "readonly" if productos else "disabled"
    
    # Función para cargar precio actual
    def cargar_precio_actual(event=None):
        producto_seleccionado = combo_producto_mod.get()
        categoria_seleccionada = combo_categoria_mod.get()
        
        if producto_seleccionado and categoria_seleccionada:
            if categoria_seleccionada == "Bebidas":
                subcat, prod = producto_seleccionado.split(" > ")
                precio_actual = menu_lobocafe[categoria_seleccionada][subcat][prod]
            else:
                precio_actual = menu_lobocafe[categoria_seleccionada][producto_seleccionado]
            
            entry_nuevo_precio.delete(0, tk.END)
            entry_nuevo_precio.insert(0, str(precio_actual))
    
    # Formulario para modificar precios
    tk.Label(frame_modificar, 
            text="Modificar Precio Existente", 
            font=("Arial", 14, "bold"), 
            background="#f5f5f5").pack(pady=10)
    
    # Frame para el formulario
    frame_form_mod = tk.Frame(frame_modificar, bg="#f5f5f5")
    frame_form_mod.pack(pady=10)
    
    # Categoría
    tk.Label(frame_form_mod, 
            text="Categoría:", 
            font=("Arial", 10), 
            bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    
    combo_categoria_mod = ttk.Combobox(frame_form_mod, values=categorias, state="readonly")
    combo_categoria_mod.grid(row=0, column=1, padx=5, pady=5)
    combo_categoria_mod.bind("<<ComboboxSelected>>", cargar_productos)
    
    # Producto
    tk.Label(frame_form_mod, 
            text="Producto:", 
            font=("Arial", 10), 
            bg="#f5f5f5").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    
    combo_producto_mod = ttk.Combobox(frame_form_mod, state="disabled")
    combo_producto_mod.grid(row=1, column=1, padx=5, pady=5)
    combo_producto_mod.bind("<<ComboboxSelected>>", cargar_precio_actual)
    
    # Nuevo precio
    tk.Label(frame_form_mod, 
            text="Nuevo precio ($):", 
            font=("Arial", 10), 
            bg="#f5f5f5").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    
    entry_nuevo_precio = tk.Entry(frame_form_mod, font=("Arial", 10))
    entry_nuevo_precio.grid(row=2, column=1, padx=5, pady=5)
    
    # Función para actualizar el precio
    def actualizar_precio():
        categoria = combo_categoria_mod.get()
        producto = combo_producto_mod.get()
        nuevo_precio = entry_nuevo_precio.get().strip()
        
        if not categoria or not producto:
            messagebox.showerror("Error", "Selecciona una categoría y un producto")
            return
            
        try:
            precio_float = float(nuevo_precio)
            if precio_float <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingresa un precio válido (número mayor a 0)")
            return
        
        # Actualizar el precio en la estructura del menú
        if categoria == "Bebidas":
            subcat, prod = producto.split(" > ")
            menu_lobocafe[categoria][subcat][prod] = precio_float
            producto_nombre = prod
        else:
            menu_lobocafe[categoria][producto] = precio_float
            producto_nombre = producto
        
        messagebox.showinfo("Éxito", f"Precio de '{producto_nombre}' actualizado a ${precio_float:.2f}")
        
        # Limpiar el formulario
        combo_categoria_mod.set("")
        combo_producto_mod.set("")
        combo_producto_mod["state"] = "disabled"
        entry_nuevo_precio.delete(0, tk.END)
    
    # Botón para actualizar precio
    tk.Button(frame_modificar, 
            text="💾 Guardar Cambios", 
            command=actualizar_precio,
            font=("Arial", 11),
            bg="#2196F3",
            fg="white").pack(pady=20)
    
    # Pestaña para ver el menú actual
    frame_ver_menu = ttk.Frame(notebook)
    notebook.add(frame_ver_menu, text="📋 Ver Menú Actual")
    
    # Crear un canvas con scrollbar para el menú
    canvas = tk.Canvas(frame_ver_menu, bg="#f5f5f5")
    scrollbar = ttk.Scrollbar(frame_ver_menu, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Mostrar el menú completo
    tk.Label(scrollable_frame, 
            text="Menú Actual de LoboCafé", 
            font=("Arial", 14, "bold"), 
            bg="#f5f5f5").pack(pady=10)
    
    for categoria, productos in menu_lobocafe.items():
        tk.Label(scrollable_frame, 
                text=f"\n{categoria}", 
                font=("Arial", 12, "bold", "underline"), 
                bg="#f5f5f5").pack(anchor="w", padx=20)
        
        if isinstance(productos, dict):
            for producto, precio in productos.items():
                if isinstance(precio, dict):  # Para subcategorías como en Bebidas
                    tk.Label(scrollable_frame, 
                            text=f"\n  {producto}", 
                            font=("Arial", 11, "bold"), 
                            bg="#f5f5f5").pack(anchor="w", padx=40)
                    
                    for subproducto, subprecio in precio.items():
                        tk.Label(scrollable_frame, 
                                text=f"    - {subproducto}: ${subprecio:.2f}", 
                                font=("Arial", 10), 
                                bg="#f5f5f5").pack(anchor="w", padx=60)
                else:
                    tk.Label(scrollable_frame, 
                            text=f"- {producto}: ${precio:.2f}", 
                            font=("Arial", 10), 
                            bg="#f5f5f5").pack(anchor="w", padx=40)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Botón de salir
    tk.Button(ventana_trabajador, 
            text="🚪 Salir", 
            command=ventana_trabajador.destroy,
            font=("Arial", 11),
            bg="#f44336",
            fg="white").pack(side="bottom", pady=10)

# Funciones para el cliente (menú, carrito, etc.)
def mostrar_menu(ventana_padre):
    ventana_menu = tk.Toplevel(ventana_padre)
    ventana_menu.title("🐺 Menú - LoboCafé")
    ventana_menu.geometry("900x700")
    ventana_menu.configure(bg="#f5f5f5")
    # Barra superior con reloj
    frame_superior = tk.Frame(ventana_menu, bg="#e0e0e0", padx=10, pady=5)
    frame_superior.pack(fill="x")
    
    # Reloj
    label_reloj = tk.Label(frame_superior, font=('Arial', 10), bg="#e0e0e0")
    label_reloj.pack(side="right")
    actualizar_reloj(label_reloj)


    # Función para regresar al inicio
    def regresar_inicio():
        ventana_menu.destroy()
        mostrar_ventana_principal()
    
    # Botón de inicio
    btn_inicio = tk.Button(ventana_menu, text="🏠 Inicio", command=regresar_inicio,
                        font=("Arial", 10), bg="#2196F3", fg="white")
    btn_inicio.pack(anchor="nw", padx=10, pady=10)

    # Configurar estilo
    style = ttk.Style()
    style.configure("TNotebook", background="#f5f5f5")
    style.configure("TNotebook.Tab", 
                font=("Arial", 10, "bold"), 
                padding=[15, 5])

    # Notebook principal
    notebook = ttk.Notebook(ventana_menu)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # ========== PESTAÑA DE ALIMENTOS ==========
    frame_alimentos = ttk.Frame(notebook)
    notebook.add(frame_alimentos, text="🍽️ Alimentos")

    tk.Label(frame_alimentos, 
            text="Alimentos", 
            font=("Arial", 14, "bold"), 
            background="#f5f5f5").pack(pady=10)

    for producto, precio in menu_lobocafe["Alimentos"].items():
        frame_producto = tk.Frame(frame_alimentos, bg="#ffffff", bd=1, relief="solid")
        frame_producto.pack(fill="x", padx=20, pady=5, ipady=5)
        
        tk.Label(frame_producto, 
                text=f"{producto}: ${precio:.2f}", 
                font=("Arial", 11), 
                bg="#ffffff").pack(side="left", padx=10)
        
        tk.Button(frame_producto, 
                text="➕ Agregar", 
                command=lambda p=producto, pr=precio: agregar_al_carrito(p, pr, ventana_menu),
                bg="#4CAF50", 
                fg="white",
                font=("Arial", 9)).pack(side="right", padx=10)

    # ========== PESTAÑA VEGANA/VEGETARIANA ==========
    frame_veganos = ttk.Frame(notebook)
    notebook.add(frame_veganos, text="🌱 Vegano/Vegetariano")

    tk.Label(frame_veganos, 
            text="Opciones Veganas/Vegetarianas", 
            font=("Arial", 14, "bold"), 
            foreground="#2E7D32",
            background="#f5f5f5").pack(pady=10)

    for producto, precio in menu_lobocafe["Alimentos Veganos/Vegetarianos"].items():
        frame_producto = tk.Frame(frame_veganos, bg="#ffffff", bd=1, relief="solid")
        frame_producto.pack(fill="x", padx=20, pady=5, ipady=5)
        
        tk.Label(frame_producto, 
                text=f"{producto}: ${precio:.2f}", 
                font=("Arial", 11), 
                bg="#ffffff").pack(side="left", padx=10)
        
        tk.Button(frame_producto, 
                text="➕ Agregar", 
                command=lambda p=producto, pr=precio: agregar_al_carrito(p, pr, ventana_menu),
                bg="#4CAF50", 
                fg="white",
                font=("Arial", 9)).pack(side="right", padx=10)

    # ========== PESTAÑA DE BEBIDAS ==========
    frame_bebidas = ttk.Frame(notebook)
    notebook.add(frame_bebidas, text="☕ Bebidas")

    # Sub-notebook para categorías de bebidas
    sub_notebook = ttk.Notebook(frame_bebidas)
    sub_notebook.pack(fill="both", expand=True)

    # ---- Cafés ----
    frame_cafes = ttk.Frame(sub_notebook)
    sub_notebook.add(frame_cafes, text="🥛 Cafés")

    tk.Label(frame_cafes, 
            text="Bebidas con café", 
            font=("Arial", 12), 
            background="#f5f5f5").pack(pady=10)

    for producto, precio in menu_lobocafe["Bebidas"]["Cafés"].items():
        frame_producto = tk.Frame(frame_cafes, bg="#ffffff", bd=1, relief="solid")
        frame_producto.pack(fill="x", padx=20, pady=5, ipady=5)
        
        tk.Label(frame_producto, 
                text=f"{producto}: ${precio:.2f}", 
                font=("Arial", 11), 
                bg="#ffffff").pack(side="left", padx=10)
        
        frame_botones = tk.Frame(frame_producto, bg="#ffffff")
        frame_botones.pack(side="right", padx=10)
        
        tk.Button(frame_botones, 
                text="⚙️ Personalizar", 
                command=lambda p=producto, pr=precio: personalizar_bebida(p, pr, ventana_menu),
                bg="#FF9800", 
                fg="white",
                font=("Arial", 9)).pack(side="left", padx=2)
        
        tk.Button(frame_botones, 
                text="➕ Agregar", 
                command=lambda p=producto, pr=precio: agregar_al_carrito(p, pr, ventana_menu),
                bg="#4CAF50", 
                fg="white",
                font=("Arial", 9)).pack(side="left", padx=2)

    # ---- Tés e Infusiones ----
    frame_tes = ttk.Frame(sub_notebook)
    sub_notebook.add(frame_tes, text="🍵 Tés e Infusiones")

    tk.Label(frame_tes, 
            text="Bebidas calientes sin café", 
            font=("Arial", 12), 
            background="#f5f5f5").pack(pady=10)

    for producto, precio in menu_lobocafe["Bebidas"]["Tés e Infusiones"].items():
        frame_producto = tk.Frame(frame_tes, bg="#ffffff", bd=1, relief="solid")
        frame_producto.pack(fill="x", padx=20, pady=5, ipady=5)
        
        tk.Label(frame_producto, 
                text=f"{producto}: ${precio:.2f}", 
                font=("Arial", 11), 
                bg="#ffffff").pack(side="left", padx=10)
        
        tk.Button(frame_producto, 
                text="➕ Agregar", 
                command=lambda p=producto, pr=precio: agregar_al_carrito(p, pr, ventana_menu),
                bg="#4CAF50", 
                fg="white",
                font=("Arial", 9)).pack(side="right", padx=10)

    # ---- Bebidas Frías ----
    frame_frias = ttk.Frame(sub_notebook)
    sub_notebook.add(frame_frias, text="🧊 Bebidas Frías")

    tk.Label(frame_frias, 
            text="Bebidas refrescantes", 
            font=("Arial", 12), 
            background="#f5f5f5").pack(pady=10)

    # Jugos y aguas
    for producto, precio in {k: v for k, v in menu_lobocafe["Bebidas"]["Bebidas Frías"].items() if k != "Refrescos"}.items():
        frame_producto = tk.Frame(frame_frias, bg="#ffffff", bd=1, relief="solid")
        frame_producto.pack(fill="x", padx=20, pady=5, ipady=5)
        
        tk.Label(frame_producto, 
                text=f"{producto}: ${precio:.2f}", 
                font=("Arial", 11), 
                bg="#ffffff").pack(side="left", padx=10)
        
        tk.Button(frame_producto, 
                text="➕ Agregar", 
                command=lambda p=producto, pr=precio: agregar_al_carrito(p, pr, ventana_menu),
                bg="#4CAF50", 
                fg="white",
                font=("Arial", 9)).pack(side="right", padx=10)

    # Refrescos (5 opciones)
    tk.Label(frame_frias, 
            text="\nRefrescos", 
            font=("Arial", 11, "underline"), 
            background="#f5f5f5").pack()

    for producto, precio in menu_lobocafe["Bebidas"]["Bebidas Frías"]["Refrescos"].items():
        frame_producto = tk.Frame(frame_frias, bg="#ffffff", bd=1, relief="solid")
        frame_producto.pack(fill="x", padx=20, pady=5, ipady=5)
        
        tk.Label(frame_producto, 
                text=f"{producto}: ${precio:.2f}", 
                font=("Arial", 11), 
                bg="#ffffff").pack(side="left", padx=10)
        
        tk.Button(frame_producto, 
                text="➕ Agregar", 
                command=lambda p=producto, pr=precio: agregar_al_carrito(p, pr, ventana_menu),
                bg="#4CAF50", 
                fg="white",
                font=("Arial", 9)).pack(side="right", padx=10)

    # Botón del carrito
    tk.Button(ventana_menu, 
            text="🛒 Ver Carrito", 
            command=lambda: ver_carrito(ventana_menu),
            font=("Arial", 12),
            bg="#FFC107",
            fg="black").pack(pady=15)

# Función para personalizar bebidas (solo cafés)
def personalizar_bebida(producto, precio_base, ventana_menu):
    ventana_personalizar = tk.Toplevel()
    ventana_personalizar.title(f"Personalizar {producto}")
    ventana_personalizar.geometry("350x400")
    ventana_personalizar.configure(bg="#f5f5f5")

    tk.Label(ventana_personalizar, 
            text=f"Personalizar {producto}", 
            font=("Arial", 12, "bold"), 
            bg="#f5f5f5").pack(pady=10)

    # Opciones de azúcar
    tk.Label(ventana_personalizar, 
            text="Nivel de azúcar:", 
            font=("Arial", 10), 
            bg="#f5f5f5").pack(anchor="w", padx=20)
    
    azucar_seleccionada = tk.StringVar(value="Normal")
    opciones_azucar = [
        ("Sin azúcar", "Sin azúcar"),
        ("Poca", "Poca"),
        ("Normal", "Normal"),
        ("Extra", "Extra")
    ]
    
    for texto, valor in opciones_azucar:
        tk.Radiobutton(ventana_personalizar, 
                    text=texto, 
                    variable=azucar_seleccionada, 
                    value=valor,
                    bg="#f5f5f5").pack(anchor="w", padx=30)

    # Tipo de leche
    tk.Label(ventana_personalizar, 
            text="\nTipo de leche:", 
            font=("Arial", 10), 
            bg="#f5f5f5").pack(anchor="w", padx=20)
    
    leche_seleccionada = tk.StringVar(value="Entera")
    opciones_leche = [
        ("Entera", "Entera"),
        ("Deslactosada", "Deslactosada"),
        ("Almendra", "Almendra"),
        ("Soya", "Soya"),
        ("Ninguna", "Ninguna")
    ]
    
    for texto, valor in opciones_leche:
        tk.Radiobutton(ventana_personalizar, 
                    text=texto, 
                    variable=leche_seleccionada, 
                    value=valor,
                    bg="#f5f5f5").pack(anchor="w", padx=30)

    # Tamaño
    tk.Label(ventana_personalizar, 
            text="\nTamaño:", 
            font=("Arial", 10), 
            bg="#f5f5f5").pack(anchor="w", padx=20)
    
    tamano_seleccionado = tk.StringVar(value="Mediano (M)")
    opciones_tamano = {
        "Chico (CH)": 0,
        "Mediano (M)": 10,
        "Grande (G)": 20
    }
    
    for opcion, recargo in opciones_tamano.items():
        texto_opcion = f"{opcion} (+${recargo}.00)" if recargo > 0 else opcion
        tk.Radiobutton(ventana_personalizar, 
                    text=texto_opcion, 
                    variable=tamano_seleccionado, 
                    value=opcion,
                    bg="#f5f5f5").pack(anchor="w", padx=30)

    def agregar_personalizado():
        global total
        recargo = opciones_tamano[tamano_seleccionado.get()]
        precio_final = precio_base + recargo
        detalles = f"{producto} ({azucar_seleccionada.get()}, {leche_seleccionada.get()}, {tamano_seleccionado.get()})"
        
        if detalles in carrito:
            carrito[detalles] += 1
        else:
            carrito[detalles] = 1
        
        total += precio_final
        messagebox.showinfo("¡Agregado!", f"{detalles}\nTotal parcial: ${total:.2f} MXN")
        ventana_personalizar.destroy()

    tk.Button(ventana_personalizar, 
            text="✅ Confirmar", 
            command=agregar_personalizado,
            bg="#4CAF50", 
            fg="white",
            font=("Arial", 11)).pack(pady=20)

# Función para agregar al carrito
def agregar_al_carrito(producto, precio, ventana_menu):
    global total
    if producto in carrito:
        carrito[producto] += 1
    else:
        carrito[producto] = 1
    total += precio
    messagebox.showinfo("¡Agregado!", f"{producto}\nTotal parcial: ${total:.2f} MXN")
    ventana_menu.lift()

# Función para ver el carrito
def ver_carrito(ventana_padre):
    ventana_carrito = tk.Toplevel(ventana_padre)
    ventana_carrito.title("🐺 Carrito - LoboCafé")
    ventana_carrito.geometry("600x550")
    ventana_carrito.configure(bg="#f5f5f5")
        # Barra superior con reloj
    frame_superior = tk.Frame(ventana_carrito, bg="#e0e0e0", padx=10, pady=5)
    frame_superior.pack(fill="x")
    
    # Reloj
    label_reloj = tk.Label(frame_superior, font=('Arial', 10), bg="#e0e0e0")
    label_reloj.pack(side="right")
    actualizar_reloj(label_reloj)

    # Función para regresar al inicio
    def regresar_inicio():
        ventana_carrito.destroy()
        mostrar_ventana_principal()
    
    # Botón de inicio
    btn_inicio = tk.Button(ventana_carrito, text="🏠 Inicio", command=regresar_inicio,
                        font=("Arial", 10), bg="#2196F3", fg="white")
    btn_inicio.pack(anchor="nw", padx=10, pady=10)

    # Encabezado
    tk.Label(ventana_carrito, 
            text="🐺 LoboCafé 🐺", 
            font=("Arial", 16, "bold"), 
            bg="#f5f5f5").pack(pady=10)
    tk.Label(ventana_carrito, 
            text="Tu pedido:", 
            font=("Arial", 14), 
            bg="#f5f5f5").pack()

    # Contenido del carrito
    frame_productos = tk.Frame(ventana_carrito, bg="#f5f5f5")
    frame_productos.pack(fill="both", expand=True, padx=20, pady=10)

    if not carrito:
        tk.Label(frame_productos, 
                text="El carrito está vacío", 
                font=("Arial", 12), 
                bg="#f5f5f5").pack()
    else:
        # Crear un canvas con scrollbar
        canvas = tk.Canvas(frame_productos, bg="#f5f5f5")
        scrollbar = ttk.Scrollbar(frame_productos, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for i, (producto, cantidad) in enumerate(carrito.items()):
            # Buscar precio base
            precio_base = 0
            for categoria in menu_lobocafe.values():
                if isinstance(categoria, dict):
                    for prod, precio in categoria.items():
                        if isinstance(precio, dict):  # Para subcategorías como "Cafés"
                            for subprod, subprecio in precio.items():
                                if producto.startswith(subprod):
                                    precio_base = subprecio
                                    break
                        elif producto.startswith(prod):
                            precio_base = precio
                            break
            
            # Calcular recargo por tamaño (si aplica)
            recargo = 0
            if "(Grande (G)" in producto:
                recargo = 20
            elif "(Mediano (M)" in producto:
                recargo = 10
            
            subtotal = (precio_base + recargo) * cantidad
            
            # Frame para cada producto
            frame_item = tk.Frame(scrollable_frame, bg="#ffffff", bd=1, relief="solid")
            frame_item.pack(fill="x", pady=3, padx=5)
            
            # Frame para la información del producto
            frame_info = tk.Frame(frame_item, bg="#ffffff")
            frame_info.pack(side="left", fill="x", expand=True, padx=10)

            tk.Label(frame_info, 
                    text=f"×{cantidad} {producto}", 
                    font=("Arial", 11), 
                    bg="#ffffff").pack(anchor="w")
            
            tk.Label(frame_info, 
                    text=f"${subtotal:.2f}", 
                    font=("Arial", 11), 
                    bg="#ffffff").pack(anchor="w")
            
        # Botón para eliminar
        btn_eliminar = tk.Button(frame_item,
                                    text="❌", 
                                    command=lambda p=producto: eliminar_del_carrito(p, ventana_carrito),
                                    font=("Arial", 9),
                                    bg="#f44336", 
                                    fg="white",
                                    width=3)
        btn_eliminar.pack(side="right", padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # Total y botones
    tk.Label(ventana_carrito, 
            text=f"Total: ${total:.2f} MXN", 
            font=("Arial", 14, "bold"), 
            bg="#f5f5f5").pack(pady=10)

    frame_botones = tk.Frame(ventana_carrito, bg="#f5f5f5")
    frame_botones.pack(pady=10)

    tk.Button(frame_botones, 
            text="← Seguir comprando", 
            command=ventana_carrito.destroy,
            font=("Arial", 10),
            bg="#2196F3", 
            fg="white").pack(side="left", padx=5)

    tk.Button(frame_botones, 
            text="🗑️ Vaciar carrito", 
            command=lambda: vaciar_carrito(ventana_carrito),
            font=("Arial", 10),
            bg="#f44336", 
            fg="white").pack(side="left", padx=5)

    tk.Button(frame_botones, 
            text="✅ Finalizar compra", 
            command=lambda: finalizar_compra(ventana_carrito),
            font=("Arial", 10),
            bg="#4CAF50", 
            fg="white").pack(side="left", padx=5)

# Función para finalizar compra
def finalizar_compra(ventana):
    global total, carrito
    if not carrito:
        messagebox.showwarning("Carrito vacío", "No hay productos en el carrito")
        return
    
    resumen = "\n".join([f"• {prod} x{cant}" for prod, cant in carrito.items()])
    respuesta = messagebox.askyesno(
        "Confirmar compra",
        f"¿Confirmar pedido?\n\n{resumen}\n\nTotal: ${total:.2f} MXN"
    )
    
    if respuesta:
        messagebox.showinfo(
            "¡Gracias!", 
            f"Pedido realizado con éxito\n\nTotal: ${total:.2f} MXN\n\nGracias por elegir LoboCafé 🐺☕"
        )
        carrito.clear()
        total = 0.0
        ventana.destroy()

# Función para eliminar un artículo del carrito
def eliminar_del_carrito(producto, ventana_carrito):
    global total, carrito
    
    # Buscar el precio del producto a eliminar
    precio_eliminar = 0
    
    # Buscar en el menú principal
    for categoria in menu_lobocafe.values():
        if isinstance(categoria, dict):
            for prod, precio in categoria.items():
                if isinstance(precio, dict):  # Para subcategorías como "Cafés"
                    for subprod, subprecio in precio.items():
                        if producto.startswith(subprod):
                            precio_base = subprecio
                            break
                elif producto.startswith(prod):
                    precio_base = precio
                    break
# Calcular recargo por tamaño si es una bebida personalizada
    recargo = 0
    if "(Grande (G)" in producto:
        recargo = 20
    elif "(Mediano (M)" in producto:
        recargo = 10
    
    precio_unitario = precio_base + recargo
    cantidad = carrito[producto]
    
    # Eliminar el producto o reducir la cantidad
    if cantidad > 1:
        carrito[producto] -= 1
        total -= precio_unitario
    else:
        del carrito[producto]
        total -= precio_unitario
    
    # Actualizar la ventana del carrito
    ventana_carrito.destroy()
    ver_carrito(ventana_carrito.master)  # Recargar el carrito      

# Función para vaciar carrito
def vaciar_carrito(ventana):
    global total, carrito
    if not carrito:
        messagebox.showinfo("Carrito vacío", "El carrito ya está vacío")
        return
    
    if messagebox.askyesno("Vaciar carrito", "¿Estás seguro de vaciar el carrito?"):
        carrito.clear()
        total = 0.0
        messagebox.showinfo("Listo", "Carrito vaciado")
        ventana.destroy()

if __name__ == "__main__":
    mostrar_ventana_principal()