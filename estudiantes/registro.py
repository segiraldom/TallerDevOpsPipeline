import csv

def cargar_estudiantes(ruta_archivo):
    estudiantes = []

    with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = fila.get("nombre")
            try:
                nota = float(fila.get("nota", 0))
                if 0.0 <= nota <= 5.0:
                    estudiantes.append({"nombre": nombre, "nota": nota})
                else:
                    print(f"[!] Nota inválida para {nombre}: {nota}")
            except ValueError:
                print(f"[!] Nota no numérica para {nombre}: {fila.get('nota')}")

    return estudiantes
