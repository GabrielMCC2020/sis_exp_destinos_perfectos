import clips
import tkinter as tk
from tkinter import messagebox

# Definición de las reglas y hechos en CLIPS
def definir_reglas():
    environment = clips.Environment()

    # Definir hechos para las preferencias del cliente
    environment.build("""
    (deftemplate PreferenciasCliente
        (slot tipo)
        (slot presupuesto)
    )
    """)

    # Regla para viajes de Aventura
    environment.build("""
    (defrule aventura-alto
        (PreferenciasCliente (tipo "Aventura") (presupuesto "Alto"))
        =>
        (assert (recomendacion "Un safari de lujo en Kenia"))
    )
    """)

    environment.build("""
    (defrule aventura-medio
        (PreferenciasCliente (tipo "Aventura") (presupuesto "Medio"))
        =>
        (assert (recomendacion "Senderismo en las Montañas Rocosas"))
    )
    """)

    environment.build("""
    (defrule aventura-bajo
        (PreferenciasCliente (tipo "Aventura") (presupuesto "Bajo"))
        =>
        (assert (recomendacion "Camping en el Parque Nacional Yellowstone"))
    )
    """)

    # Regla para viajes de Relax
    environment.build("""
    (defrule relax-alto
        (PreferenciasCliente (tipo "Relax") (presupuesto "Alto"))
        =>
        (assert (recomendacion "Un resort de lujo en las Maldivas"))
    )
    """)

    environment.build("""
    (defrule relax-medio
        (PreferenciasCliente (tipo "Relax") (presupuesto "Medio"))
        =>
        (assert (recomendacion "Una estancia en un resort en Bali"))
    )
    """)

    environment.build("""
    (defrule relax-bajo
        (PreferenciasCliente (tipo "Relax") (presupuesto "Bajo"))
        =>
        (assert (recomendacion "Un fin de semana en una casa rural"))
    )
    """)

    # Regla para viajes Culturales
    environment.build("""
    (defrule cultural-alto
        (PreferenciasCliente (tipo "Cultural") (presupuesto "Alto"))
        =>
        (assert (recomendacion "Un tour privado por los museos de París"))
    )
    """)

    environment.build("""
    (defrule cultural-medio
        (PreferenciasCliente (tipo "Cultural") (presupuesto "Medio"))
        =>
        (assert (recomendacion "Explorar las ciudades históricas de España"))
    )
    """)

    environment.build("""
    (defrule cultural-bajo
        (PreferenciasCliente (tipo "Cultural") (presupuesto "Bajo"))
        =>
        (assert (recomendacion "Un tour histórico en Perú"))
    )
    """)

    # Regla por defecto
    environment.build("""
    (defrule default-recommendation
        =>
        (assert (recomendacion "Un viaje personalizado en Europa"))
    )
    """)

    return environment

# Función para obtener la recomendación
def obtener_recomendacion(environment, tipo_viaje, presupuesto_viaje):
    environment.reset()
    environment.assert_string(f'(PreferenciasCliente (tipo "{tipo_viaje}") (presupuesto "{presupuesto_viaje}"))')
    environment.run()

    for fact in environment.facts():
        if fact.template.name == "recomendacion":
            return fact.__str__().split()[-1].strip('()"')
    return "No se encontró ninguna recomendación."

# Interfaz gráfica
def interfaz_grafica():
    def on_obtener_recomendacion():
        tipo_viaje = tipo.get()
        presupuesto_viaje = presupuesto.get()

        recomendacion = obtener_recomendacion(environment, tipo_viaje, presupuesto_viaje)
        messagebox.showinfo("Recomendación", f"Nuestra recomendación: {recomendacion}")

    environment = definir_reglas()

    root = tk.Tk()
    root.title("Sistema Experto en Turismo")
    root.geometry("500x400")
    root.configure(bg="#E6E6FA")  # Color de fondo suave

    # Estilo de etiquetas y menús desplegables
    label_style = {'font': ('Arial', 12, 'bold'), 'bg': '#E6E6FA'}
    menu_style = {'bg': '#D3D3D3', 'font': ('Arial', 11)}

    # Crear un marco para contener los widgets
    frame = tk.Frame(root, bg="#E6E6FA", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    # Variables para almacenar las selecciones
    tipo = tk.StringVar(value='Aventura')
    presupuesto = tk.StringVar(value='Medio')

    # Crear etiquetas y menús desplegables con mejor estilo
    tk.Label(frame, text="Seleccione el tipo de viaje:", **label_style).grid(row=0, column=0, pady=10, sticky="w")
    opciones_tipo = ["Aventura", "Relax", "Cultural"]
    menu_tipo = tk.OptionMenu(frame, tipo, *opciones_tipo)
    menu_tipo.config(**menu_style)
    menu_tipo.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

    tk.Label(frame, text="Seleccione su presupuesto:", **label_style).grid(row=1, column=0, pady=10, sticky="w")
    opciones_presupuesto = ["Bajo", "Medio", "Alto"]
    menu_presupuesto = tk.OptionMenu(frame, presupuesto, *opciones_presupuesto)
    menu_presupuesto.config(**menu_style)
    menu_presupuesto.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

    # Botón de obtener recomendación
    boton = tk.Button(frame, text="Obtener Recomendación", command=on_obtener_recomendacion,
                      bg="#4682B4", fg="white", font=('Arial', 12, 'bold'), padx=10, pady=5)
    boton.grid(row=2, column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    interfaz_grafica()
