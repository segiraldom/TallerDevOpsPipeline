from estudiantes.registro import (
    cargar_estudiantes,
    mostrar_estudiantes_tabla,
    calcular_promedio,
)

def main():
    estudiantes = cargar_estudiantes("estudiantes.csv")
    mostrar_estudiantes_tabla(estudiantes)
    calcular_promedio(estudiantes)

if __name__ == "__main__":
    main()
