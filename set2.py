import clips
import tkinter as tk
from tkinter import messagebox

def definir_reglas():
    environment = clips.Environment()

    # Definición de la plantilla de preferencias del cliente
    environment.build("""
    (deftemplate PreferenciasCliente
        (slot tipo)
        (slot presupuesto)
        (slot intereses)
        (slot alojamiento)
        (slot restricciones)
        (slot duracion)
        (slot compania)
        (slot epoca)
        (slot idioma)
    )
    """)

    # Definición de reglas detalladas y personalizadas
    environment.build("""
    ; Aventura con alto presupuesto
    (defrule aventura-alto-acuaticos
        (PreferenciasCliente (tipo "Aventura") (presupuesto "Alto") (intereses "Deportes acuáticos"))
        =>
        (assert (recomendacion "Buceo en la Gran Barrera de Coral, Australia"))
    )
    """)
    environment.build("""
    (defrule aventura-alto-extremos
        (PreferenciasCliente (tipo "Aventura") (presupuesto "Alto") (intereses "Deportes extremos"))
        =>
        (assert (recomendacion "Escalada en el Monte Everest, Nepal"))
    )
    """)
    environment.build("""
    ; Cultural con presupuesto medio
    (defrule cultural-medio-museos
        (PreferenciasCliente (tipo "Cultural") (presupuesto "Medio") (intereses "Museos"))
        =>
        (assert (recomendacion "Explorar el Louvre y otros museos en París, Francia"))
    )
    """)
    environment.build("""
    (defrule cultural-medio-historia
        (PreferenciasCliente (tipo "Cultural") (presupuesto "Medio") (intereses "Historia"))
        =>
        (assert (recomendacion "Visitar el Coliseo y el Foro Romano en Roma, Italia"))
    )
    """)
    environment.build("""
    ; Familiar con presupuesto bajo
    (defrule familiar-bajo-playa
        (PreferenciasCliente (tipo "Familiar") (presupuesto "Bajo") (intereses "Playa"))
        =>
        (assert (recomendacion "Vacaciones en las playas de Cancún, México"))
    )
    """)
    environment.build("""
    (defrule familiar-bajo-naturaleza
        (PreferenciasCliente (tipo "Familiar") (presupuesto "Bajo") (intereses "Naturaleza"))
        =>
        (assert (recomendacion "Explorar los parques nacionales de Costa Rica"))
    )
    """)
    environment.build("""
    ; Relax en pareja con presupuesto alto
    (defrule relax-alto-pareja
        (PreferenciasCliente (tipo "Relax") (presupuesto "Alto") (compania "En pareja"))
        =>
        (assert (recomendacion "Escapada romántica a las Maldivas"))
    )
    """)
    environment.build("""
    (defrule relax-alto-pareja-playa
        (PreferenciasCliente (tipo "Relax") (presupuesto "Alto") (compania "En pareja") (intereses "Playa"))
        =>
        (assert (recomendacion "Vacaciones de lujo en Bora Bora, Polinesia Francesa"))
    )
    """)
    environment.build("""
    ; Solitario con presupuesto medio
    (defrule solitario-medio-aventura
        (PreferenciasCliente (compania "Solo") (presupuesto "Medio") (tipo "Aventura"))
        =>
        (assert (recomendacion "Safari en el Serengeti, Tanzania"))
    )
    """)
    environment.build("""
    (defrule solitario-medio-cultural
        (PreferenciasCliente (compania "Solo") (presupuesto "Medio") (tipo "Cultural"))
        =>
        (assert (recomendacion "Explorar Kioto, Japón, y sus templos"))
    )
    """)
    environment.build("""
    ; Grupo de amigos en primavera
    (defrule grupo-primavera-playa
        (PreferenciasCliente (compania "Grupo de amigos") (epoca "Primavera") (intereses "Playa"))
        =>
        (assert (recomendacion "Fiesta de primavera en Miami, Florida, USA"))
    )
    """)
    environment.build("""
    (defrule grupo-primavera-acuaticos
        (PreferenciasCliente (compania "Grupo de amigos") (epoca "Primavera") (intereses "Deportes acuáticos"))
        =>
        (assert (recomendacion "Surf en Bondi Beach, Sídney, Australia"))
    )
    """)
    environment.build("""
    ; Cultural con presupuesto bajo
    (defrule cultural-bajo-historia
        (PreferenciasCliente (tipo "Cultural") (presupuesto "Bajo") (intereses "Historia"))
        =>
        (assert (recomendacion "Explorar los sitios históricos de Atenas, Grecia"))
    )
    """)
    environment.build("""
    (defrule cultural-bajo-arte
        (PreferenciasCliente (tipo "Cultural") (presupuesto "Bajo") (intereses "Arte"))
        =>
        (assert (recomendacion "Tour artístico en Florencia, Italia"))
    )
    """)
    environment.build("""
    ; Relax en familia en verano
    (defrule relax-verano-familia-playa
        (PreferenciasCliente (tipo "Relax") (epoca "Verano") (compania "Familia") (intereses "Playa"))
        =>
        (assert (recomendacion "Vacaciones familiares en la Riviera Maya, México"))
    )
    """)
    environment.build("""
    (defrule relax-verano-familia-naturaleza
        (PreferenciasCliente (tipo "Relax") (epoca "Verano") (compania "Familia") (intereses "Naturaleza"))
        =>
        (assert (recomendacion "Explorar la belleza de los fiordos noruegos"))
    )
    """)
    environment.build("""
    ; Relax en invierno para pareja
    (defrule relax-invierno-pareja-montana
        (PreferenciasCliente (tipo "Relax") (epoca "Invierno") (compania "En pareja") (intereses "Montaña"))
        =>
        (assert (recomendacion "Escapada romántica en los Alpes Suizos"))
    )
    """)
    environment.build("""
    (defrule relax-invierno-pareja-tranquilo
        (PreferenciasCliente (tipo "Relax") (epoca "Invierno") (compania "En pareja"))
        =>
        (assert (recomendacion "Descanso en una cabaña en los bosques de Noruega"))
    )
    """)
    environment.build("""
    ; Aventura en grupo con bajo presupuesto
    (defrule aventura-bajo-grupo-senderismo
        (PreferenciasCliente (tipo "Aventura") (presupuesto "Bajo") (compania "Grupo de amigos") (intereses "Senderismo"))
        =>
        (assert (recomendacion "Trekking en Machu Picchu, Perú"))
    )
    """)
    environment.build("""
    (defrule aventura-bajo-grupo-exploracion
        (PreferenciasCliente (tipo "Aventura") (presupuesto "Bajo") (compania "Grupo de amigos"))
        =>
        (assert (recomendacion "Explorar el Gran Cañón, USA"))
    )
    """)
    environment.build("""
    ; Viaje corto en pareja con interés cultural
    (defrule corta-pareja-cultural
        (PreferenciasCliente (duracion "Corta") (compania "En pareja") (tipo "Cultural"))
        =>
        (assert (recomendacion "Un fin de semana en Praga, República Checa"))
    )
    """)
    environment.build("""
    (defrule corta-pareja-historia
        (PreferenciasCliente (duracion "Corta") (compania "En pareja") (intereses "Historia"))
        =>
        (assert (recomendacion "Escapada a Berlín, Alemania"))
    )
    """)
    environment.build("""
    ; Viaje largo en solitario con interés por la naturaleza
    (defrule largo-solitario-naturaleza
        (PreferenciasCliente (duracion "Larga") (compania "Solo") (intereses "Naturaleza"))
        =>
        (assert (recomendacion "Recorrido por los parques nacionales de Nueva Zelanda"))
    )
    """)
    environment.build("""
    (defrule largo-solitario-aventura
        (PreferenciasCliente (duracion "Larga") (compania "Solo") (tipo "Aventura"))
        =>
        (assert (recomendacion "Recorrer el Camino Inca en Perú"))
    )
    """)
    environment.build("""
    ; Familiar en otoño con presupuesto medio
    (defrule familiar-otono-medio-naturaleza
        (PreferenciasCliente (tipo "Familiar") (epoca "Otoño") (presupuesto "Medio") (intereses "Naturaleza"))
        =>
        (assert (recomendacion "Visitar el Parque Nacional de Yellowstone, USA"))
    )
    """)
    environment.build("""
    (defrule familiar-otono-medio-historia
        (PreferenciasCliente (tipo "Familiar") (epoca "Otoño") (presupuesto "Medio") (intereses "Historia"))
        =>
        (assert (recomendacion "Tour histórico por Washington, D.C., USA"))
    )
    """)
    environment.build("""
    ; Viaje largo en grupo con interés en la cultura
    (defrule largo-grupo-cultural
        (PreferenciasCliente (duracion "Larga") (compania "Grupo de amigos") (tipo "Cultural"))
        =>
        (assert (recomendacion "Explorar las ciudades de la Ruta de la Seda, Asia Central"))
    )
    """)
    environment.build("""
    (defrule largo-grupo-aventura
        (PreferenciasCliente (duracion "Larga") (compania "Grupo de amigos") (tipo "Aventura"))
        =>
        (assert (recomendacion "Expedición al Polo Norte"))
    )
    """)
    environment.build("""
    ; Regla por defecto
    (defrule default-recommendation
        =>
        (assert (recomendacion "Un viaje personalizado en Europa"))
    )
    """)

    return environment

# Función para obtener la recomendación
def obtener_recomendacion(environment, cliente):
    environment.reset()
    environment.assert_string(f'(PreferenciasCliente {cliente})')
    environment.run()

    for fact in environment.facts():
        if fact.template.name == "recomendacion":
            return fact.__str__().split()[-1].strip('()"')
    return "No se encontró ninguna recomendación."

def interfaz_grafica():
    def on_obtener_recomendacion():
        cliente = f'(tipo "{tipo.get()}") (presupuesto "{presupuesto.get()}") (intereses "{intereses.get()}") ' \
                  f'(alojamiento "{alojamiento.get()}") (restricciones "{restricciones.get()}") (duracion "{duracion.get()}") ' \
                  f'(compania "{compania.get()}") (epoca "{epoca.get()}") (idioma "{idioma.get()}")'

        recomendacion = obtener_recomendacion(environment, cliente)
        messagebox.showinfo("Recomendación", f"Nuestra recomendación: {recomendacion}")

    environment = definir_reglas()

    # Crear ventana principal
    root = tk.Tk()
    root.title("Sistema Experto en Turismo")
    root.geometry("600x700")
    root.configure(bg="#F0F8FF")  # Fondo de color suave

    # Estilo de las etiquetas y menús
    label_style = {'font': ('Arial', 12, 'bold'), 'bg': '#F0F8FF'}
    menu_style = {'bg': '#ADD8E6', 'font': ('Arial', 11)}

    # Marco principal
    frame = tk.Frame(root, bg="#F0F8FF", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    # Widgets de la interfaz
    opciones_tipo = ["Aventura", "Relax", "Cultural", "Familiar"]
    opciones_presupuesto = ["Bajo", "Medio", "Alto"]
    opciones_intereses = ["Senderismo", "Museos", "Deportes acuáticos", "Gastronomía", "Historia", "Naturaleza"]
    opciones_alojamiento = ["Hoteles de lujo", "Hostales", "Cabañas", "Alquileres vacacionales"]
    opciones_restricciones = ["Ninguna", "Vegetariano", "Vegano", "Sin gluten"]
    opciones_duracion = ["Corta", "Media", "Larga"]
    opciones_compania = ["Solo", "En pareja", "Familia", "Grupo de amigos"]
    opciones_epoca = ["Verano", "Otoño", "Invierno", "Primavera"]
    opciones_idioma = ["Español", "Inglés", "Francés", "Alemán"]

    # Variables para almacenar las selecciones
    tipo = tk.StringVar(value='Aventura')
    presupuesto = tk.StringVar(value='Medio')
    intereses = tk.StringVar(value='Cultural')
    alojamiento = tk.StringVar(value='Hoteles de lujo')
    restricciones = tk.StringVar(value='Ninguna')
    duracion = tk.StringVar(value='Media')
    compania = tk.StringVar(value='Solo')
    epoca = tk.StringVar(value='Verano')
    idioma = tk.StringVar(value='Español')

    # Crear etiquetas y menús desplegables con mejor estilo
    widgets = [
        ("Tipo de viaje:", opciones_tipo, tipo),
        ("Presupuesto:", opciones_presupuesto, presupuesto),
        ("Intereses específicos:", opciones_intereses, intereses),
        ("Preferencias de alojamiento:", opciones_alojamiento, alojamiento),
        ("Restricciones alimenticias:", opciones_restricciones, restricciones),
        ("Duración del viaje:", opciones_duracion, duracion),
        ("Compañía de viaje:", opciones_compania, compania),
        ("Época del año preferida:", opciones_epoca, epoca),
        ("Idioma preferido:", opciones_idioma, idioma)
    ]

    for i, (label_text, options, variable) in enumerate(widgets):
        label = tk.Label(frame, text=label_text, **label_style)
        label.grid(row=i, column=0, sticky="w", pady=5)
        menu = tk.OptionMenu(frame, variable, *options)
        menu.config(**menu_style)
        menu.grid(row=i, column=1, sticky="ew", pady=5)

    # Botón de obtener recomendación
    boton = tk.Button(frame, text="Obtener Recomendación", command=on_obtener_recomendacion,
                      bg="#4682B4", fg="white", font=('Arial', 12, 'bold'), padx=10, pady=5)
    boton.grid(row=len(widgets), column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    interfaz_grafica()