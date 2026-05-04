registro = {}  # Diccionario principal que almacena todos los estudiantes


def registrar_estudiante():
    """
    Solicita los datos de un estudiante y lo registra en el sistema.

    Pide por consola:
    - Nombre
    - Curso
    - Código numérico

    Valida que el código sea un número entero y que no exista previamente
    en el diccionario global `registro`.

    Returns:
        None
    """
    nombre = input("Nombre del estudiante: ").strip()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    curso = input("Curso: ").strip()

    if not curso:
        print("El curso no puede estar vacío.")
        return

    try:
        codigo = int(input("Código del estudiante: "))
    except ValueError:
        print("El código solo puede contener números.")
        return

    if codigo not in registro:
        registro[codigo] = {"nombre": nombre, "curso": curso, "notas": []}
        print("Estudiante registrado con éxito.")
    else:
        print("Ya existe un estudiante con ese código.")


def subir_nota(codigo):
    """
    Agrega una o varias notas a un estudiante existente.

    Args:
        codigo (int): Código del estudiante.

    Pregunta cuántas notas se desean ingresar y las valida una a una.
    Cada nota debe estar entre 0 y 5.

    Returns:
        None
    """
    if codigo not in registro:
        print("Estudiante no encontrado.")
        return

    try:
        cantidad = int(input(f"¿Cuántas notas deseas agregar para {registro[codigo]['nombre']}? "))
    except ValueError:
        print("Ingresa un número válido.")
        return

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        return

    agregadas = 0

    for i in range(cantidad):
        try:
            nota = float(input(f"  Nota {i + 1}: "))
        except ValueError:
            print(f"Nota {i + 1} inválida, se omite.")
            continue

        if 0 <= nota <= 5:
            registro[codigo]["notas"].append(nota)
            agregadas += 1
        else:
            print(f"Nota {i + 1} fuera de rango (0-5), se omite.")

    print(f"{agregadas} nota(s) registrada(s) con éxito.")


def modificar_estudiante(codigo):
    """
    Permite modificar el nombre, curso o una nota específica de un estudiante.

    Args:
        codigo (int): Código del estudiante.

    Muestra un submenú con las opciones de modificación disponibles.

    Returns:
        None
    """
    if codigo not in registro:
        print("Estudiante no encontrado.")
        return

    datos = registro[codigo]

    print(f"\n--- Modificar: {datos['nombre']} | Curso: {datos['curso']} | Notas: {datos['notas']} ---")
    print("1. Modificar nombre")
    print("2. Modificar curso")
    print("3. Modificar una nota")

    try:
        opcion = int(input("¿Qué deseas modificar? "))
    except ValueError:
        print("Opción inválida.")
        return

    if opcion == 1:
        nuevo_nombre = input("Nuevo nombre: ").strip()
        if not nuevo_nombre:
            print("El nombre no puede estar vacío.")
            return
        datos["nombre"] = nuevo_nombre
        print("Nombre actualizado con éxito.")

    elif opcion == 2:
        nuevo_curso = input("Nuevo curso: ").strip()
        if not nuevo_curso:
            print("El curso no puede estar vacío.")
            return
        datos["curso"] = nuevo_curso
        print("Curso actualizado con éxito.")

    elif opcion == 3:
        notas = datos["notas"]

        if not notas:
            print("Este estudiante no tiene notas registradas.")
            return

        print(f"Notas actuales: {notas}")

        try:
            indice = int(input("Índice de la nota a modificar (desde 0): "))
            nueva_nota = float(input("Nueva nota: "))
        except ValueError:
            print("Entrada inválida.")
            return

        if 0 <= indice < len(notas) and 0 <= nueva_nota <= 5:
            notas[indice] = nueva_nota
            print("Nota modificada con éxito.")
        else:
            print("Índice o nota fuera de rango.")

    else:
        print("Opción no válida.")


def dar_de_baja(codigo):
    """
    Elimina un estudiante del registro tras confirmación del usuario.

    Args:
        codigo (int): Código del estudiante.

    Returns:
        None
    """
    if codigo not in registro:
        print("Estudiante no encontrado.")
        return

    nombre = registro[codigo]["nombre"]
    confirmacion = input(f"¿Estás seguro de dar de baja a {nombre}? (s/n): ").strip().lower()

    if confirmacion == "s":
        del registro[codigo]
        print(f"Estudiante {nombre} dado de baja con éxito.")
    else:
        print("Operación cancelada.")


def obtener_promedio(codigo):
    """
    Calcula y muestra el promedio de notas de un estudiante.

    Args:
        codigo (int): Código del estudiante.

    Returns:
        None
    """
    if codigo not in registro:
        print("Estudiante no encontrado.")
        return

    notas = registro[codigo]["notas"]

    if not notas:
        print("Este estudiante no tiene notas registradas.")
        return

    promedio = sum(notas) / len(notas)
    estado = "Aprobado ✓" if promedio >= 3.0 else "Reprobado ✗"
    print(f"Promedio de {registro[codigo]['nombre']}: {promedio:.2f} — {estado}")


def ver_estudiantes():
    """
    Muestra todos los estudiantes registrados con sus datos y estado académico.

    Imprime:
    - Código
    - Nombre
    - Curso
    - Lista de notas
    - Promedio y estado (Aprobado/Reprobado/Sin notas)

    Returns:
        None
    """
    if not registro:
        print("No hay estudiantes registrados.")
        return

    print("\n--- Lista de todos los estudiantes ---")

    for codigo, datos in registro.items():
        notas = datos["notas"]

        if notas:
            promedio = sum(notas) / len(notas)
            estado = f"Promedio: {promedio:.2f} — {'Aprobado ✓' if promedio >= 3.0 else 'Reprobado ✗'}"
        else:
            estado = "Sin notas"

        print(
            f"Código: {codigo} | "
            f"Nombre: {datos['nombre']} | "
            f"Curso: {datos['curso']} | "
            f"Notas: {notas} | "
            f"{estado}"
        )


def ver_reprobados():
    """
    Lista todos los estudiantes con promedio inferior a 3.0.

    Solo muestra estudiantes que tienen al menos una nota registrada.

    Returns:
        None
    """
    if not registro:
        print("No hay estudiantes registrados.")
        return

    reprobados = [
        (codigo, datos)
        for codigo, datos in registro.items()
        if datos["notas"] and sum(datos["notas"]) / len(datos["notas"]) < 3.0
    ]

    if not reprobados:
        print("No hay estudiantes reprobados.")
        return

    print(f"\n--- Estudiantes reprobados ({len(reprobados)}) ---")

    for codigo, datos in reprobados:
        promedio = sum(datos["notas"]) / len(datos["notas"])
        print(
            f"Código: {codigo} | "
            f"Nombre: {datos['nombre']} | "
            f"Curso: {datos['curso']} | "
            f"Promedio: {promedio:.2f}"
        )


def ver_cursos():
    """
    Muestra todos los cursos únicos registrados en el sistema
    junto con la cantidad de estudiantes en cada uno.

    Returns:
        None
    """
    if not registro:
        print("No hay estudiantes registrados.")
        return

    cursos = {}

    for datos in registro.values():
        curso = datos["curso"]
        cursos[curso] = cursos.get(curso, 0) + 1

    print(f"\n--- Cursos registrados ({len(cursos)}) ---")

    for curso, cantidad in sorted(cursos.items()):
        print(f"  {curso}: {cantidad} estudiante(s)")


def filtrar_por_curso():
    """
    Muestra todos los estudiantes que pertenecen a un curso específico.

    Solicita el nombre del curso y lista los estudiantes encontrados
    con su código, notas y promedio.

    Returns:
        None
    """
    if not registro:
        print("No hay estudiantes registrados.")
        return

    curso_buscado = input("Nombre del curso a buscar: ").strip()

    encontrados = [
        (codigo, datos)
        for codigo, datos in registro.items()
        if datos["curso"].lower() == curso_buscado.lower()
    ]

    if not encontrados:
        print(f"No se encontraron estudiantes en el curso '{curso_buscado}'.")
        return

    print(f"\n--- Estudiantes del curso '{curso_buscado}' ({len(encontrados)}) ---")

    for codigo, datos in encontrados:
        notas = datos["notas"]

        if notas:
            promedio = sum(notas) / len(notas)
            estado = f"Promedio: {promedio:.2f} — {'Aprobado ✓' if promedio >= 3.0 else 'Reprobado ✗'}"
        else:
            estado = "Sin notas"

        print(f"  Código: {codigo} | Nombre: {datos['nombre']} | Notas: {notas} | {estado}")


def buscar_por_nombre():
    """
    Busca un estudiante por nombre y muestra el curso al que pertenece.

    Si hay varios estudiantes con nombres similares, los muestra todos.

    Returns:
        None
    """
    if not registro:
        print("No hay estudiantes registrados.")
        return

    nombre_buscado = input("Nombre del estudiante a buscar: ").strip().lower()

    encontrados = [
        (codigo, datos)
        for codigo, datos in registro.items()
        if nombre_buscado in datos["nombre"].lower()
    ]

    if not encontrados:
        print("No se encontró ningún estudiante con ese nombre.")
        return

    print(f"\n--- Resultados ({len(encontrados)}) ---")

    for codigo, datos in encontrados:
        notas = datos["notas"]
        promedio = f"{sum(notas) / len(notas):.2f}" if notas else "Sin notas"
        print(
            f"  Código: {codigo} | "
            f"Nombre: {datos['nombre']} | "
            f"Curso: {datos['curso']} | "
            f"Promedio: {promedio}"
        )


def pedir_codigo():
    """
    Solicita al usuario el código de un estudiante.

    Valida que sea un número entero.

    Returns:
        int | None: Código ingresado o None si es inválido.
    """
    try:
        return int(input("Código del estudiante: "))
    except ValueError:
        print("El código solo puede contener números.")
        return None

def main():
    # Bucle principal del menú, se ejecuta indefinidamente hasta que el usuario elija salir
    while True:
        print("\n--- Menú principal ---")
        print("1.  Registrar estudiante")
        print("2.  Subir nota(s)")
        print("3.  Modificar estudiante (nombre, curso o nota)")
        print("4.  Dar de baja a un estudiante")
        print("5.  Ver promedio de un estudiante")
        print("6.  Ver todos los estudiantes")
        print("7.  Ver estudiantes reprobados")
        print("8.  Ver cursos registrados")
        print("9.  Filtrar estudiantes por curso")
        print("10. Buscar estudiante por nombre")
        print("11. Salir")

        try:
            seleccion = int(input("Opción: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if seleccion == 1:
            registrar_estudiante()
        elif seleccion == 2:
            codigo = pedir_codigo()
            if codigo is not None:
                subir_nota(codigo)
        elif seleccion == 3:
            codigo = pedir_codigo()
            if codigo is not None:
                modificar_estudiante(codigo)
        elif seleccion == 4:
            codigo = pedir_codigo()
            if codigo is not None:
                dar_de_baja(codigo)
        elif seleccion == 5:
            codigo = pedir_codigo()
            if codigo is not None:
                obtener_promedio(codigo)
        elif seleccion == 6:
            ver_estudiantes()
        elif seleccion == 7:
            ver_reprobados()
        elif seleccion == 8:
            ver_cursos()
        elif seleccion == 9:
            filtrar_por_curso()
        elif seleccion == 10:
            buscar_por_nombre()
        elif seleccion == 11:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()