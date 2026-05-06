registro = {}  # Estructura central del sistema: cada clave es el código del estudiante y su valor un dict con sus datos


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
    nombre = input("Nombre del estudiante: ").strip()  # .strip() elimina espacios accidentales al inicio y al final

    if not nombre:  # Evita registrar estudiantes con nombre vacío o solo espacios en blanco
        print("El nombre no puede estar vacío.")
        return

    curso = input("Curso: ").strip()  # Igual que el nombre, se limpia para evitar entradas con solo espacios

    if not curso:  # Garantiza que el curso tenga contenido real antes de continuar
        print("El curso no puede estar vacío.")
        return

    try:
        codigo = int(input("Código del estudiante: "))  # Se convierte a entero para usarlo como clave numérica del diccionario
    except ValueError:  # Captura el caso en que el usuario ingrese letras u otros caracteres no numéricos
        print("El código solo puede contener números.")
        return

    if codigo not in registro:  # Verifica unicidad: no se permite duplicar códigos ya existentes
        registro[codigo] = {"nombre": nombre, "curso": curso, "notas": []}  # Crea el perfil del estudiante con lista de notas vacía lista para recibir calificaciones
        print("Estudiante registrado con éxito.")
    else:
        print("Ya existe un estudiante con ese código.")  # Informa al usuario que el código ya está en uso por otro estudiante


def subir_nota(codigo):
    """
    Agrega una o varias notas con porcentaje a un estudiante existente.

    Args:
        codigo (int): Código del estudiante.

    Pregunta cuántas notas se desean ingresar y las valida una a una.
    Cada nota debe estar entre 0 y 5, y cada porcentaje entre 1 y 100.
    La suma de todos los porcentajes del estudiante no puede superar 100%.

    Returns:
        None
    """
    if codigo not in registro:  # Frena la ejecución si el código no corresponde a ningún estudiante registrado
        print("Estudiante no encontrado.")
        return

    try:
        cantidad = int(input(f"¿Cuántas notas deseas agregar para {registro[codigo]['nombre']}?: "))  # Muestra el nombre para confirmar que se está modificando al estudiante correcto
    except ValueError:  # Previene errores si el usuario escribe algo que no sea un número entero
        print("Ingresa un número válido.")
        return

    if cantidad <= 0:  # Evita ingresar cero o valores negativos que no tienen sentido como cantidad de notas
        print("La cantidad debe ser mayor a 0.")
        return

    # Calcula el porcentaje ya usado por notas anteriores del estudiante
    porcentaje_usado = sum(n["porcentaje"] for n in registro[codigo]["notas"])
    porcentaje_disponible = 100 - porcentaje_usado  # Lo que queda disponible para nuevas notas

    if porcentaje_disponible <= 0:
        print("Este estudiante ya tiene el 100% de sus notas registradas.")
        return

    print(f"Porcentaje disponible: {porcentaje_disponible}%")

    agregadas = 0  # Contador para reportar al final cuántas notas fueron válidas y realmente guardadas

    for i in range(cantidad):  # Itera exactamente la cantidad de veces que el usuario indicó
        try:
            nota = float(input(f"  Nota {i + 1}: "))  # Se usa float para permitir notas decimales como 3.7 o 4.5
        except ValueError:  # Si el usuario escribe texto en lugar de un número, se omite esa nota y se continúa
            print(f"  Nota {i + 1} inválida, se omite.")
            continue

        if not (0 <= nota <= 5):  # Valida que la nota esté dentro del rango académico permitido (0 a 5)
            print(f"  Nota {i + 1} fuera de rango (0-5), se omite.")
            continue

        try:
            porcentaje = float(input(f"  Porcentaje para nota {i + 1} (disponible: {porcentaje_disponible}%): "))
        except ValueError:
            print(f"  Porcentaje inválido, se omite la nota {i + 1}.")
            continue

        if not (0 < porcentaje <= porcentaje_disponible):  # Verifica que el porcentaje sea positivo y no supere lo disponible
            print(f"  Porcentaje fuera de rango. Debe estar entre 1 y {porcentaje_disponible}%, se omite.")
            continue

        registro[codigo]["notas"].append({"valor": nota, "porcentaje": porcentaje})  # Guarda la nota como dict con valor y porcentaje
        porcentaje_disponible -= porcentaje  # Descuenta el porcentaje usado de lo que queda disponible
        agregadas += 1
        print(f"  ✓ Nota registrada. Porcentaje restante: {porcentaje_disponible}%")

    print(f"{agregadas} nota(s) registrada(s) con éxito.")


def calcular_promedio_ponderado(notas):
    """
    Calcula el promedio ponderado de una lista de notas con porcentaje.

    Args:
        notas (list): Lista de dicts con 'valor' y 'porcentaje'.

    Returns:
        float | None: Promedio ponderado o None si no hay notas.
    """
    if not notas:
        return None
    return sum(n["valor"] * (n["porcentaje"] / 100) for n in notas)  # Suma cada nota multiplicada por su peso porcentual


def modificar_estudiante(codigo):
    """
    Permite modificar el nombre, curso o una nota específica de un estudiante.

    Args:
        codigo (int): Código del estudiante.

    Muestra un submenú con las opciones de modificación disponibles.

    Returns:
        None
    """
    if codigo not in registro:  # Verifica existencia antes de mostrar el submenú para no operar sobre datos inexistentes
        print("Estudiante no encontrado.")
        return

    datos = registro[codigo]  # Referencia directa al dict del estudiante para acceder y modificar sus campos fácilmente

    print(f"\n--- Modificar: {datos['nombre']} | Curso: {datos['curso']} ---")
    print("1. Modificar nombre")
    print("2. Modificar curso")
    print("3. Modificar una nota")

    try:
        opcion = int(input("¿Qué deseas modificar?: "))  # Captura la elección del submenú de modificación
    except ValueError:  # Evita que una entrada no numérica rompa el flujo del programa
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

        for i, n in enumerate(notas):  # Muestra cada nota con su índice, valor y porcentaje para que el usuario elija
            print(f"  [{i}] Nota: {n['valor']} | Porcentaje: {n['porcentaje']}%")

        try:
            indice = int(input("Índice de la nota a modificar: "))
            nueva_nota = float(input("Nuevo valor de la nota: "))
            nuevo_porcentaje = float(input("Nuevo porcentaje: "))
        except ValueError:
            print("Entrada inválida.")
            return

        # Calcula el porcentaje disponible excluyendo la nota que se va a reemplazar
        porcentaje_sin_esta = sum(n["porcentaje"] for i2, n in enumerate(notas) if i2 != indice)
        porcentaje_disponible = 100 - porcentaje_sin_esta

        if 0 <= indice < len(notas) and 0 <= nueva_nota <= 5 and 0 < nuevo_porcentaje <= porcentaje_disponible:
            notas[indice] = {"valor": nueva_nota, "porcentaje": nuevo_porcentaje}
            print("Nota modificada con éxito.")
        else:
            print(f"Datos inválidos. La nota debe estar entre 0-5 y el porcentaje entre 1 y {porcentaje_disponible}%.")

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
    Calcula y muestra el promedio ponderado de notas de un estudiante.

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

    promedio = calcular_promedio_ponderado(notas)
    porcentaje_total = sum(n["porcentaje"] for n in notas)  # Muestra qué tanto del 100% se ha evaluado ya
    estado = "Aprobado ✓" if promedio >= 3.0 else "Reprobado ✗"
    print(f"Promedio ponderado de {registro[codigo]['nombre']}: {promedio:.2f} — {estado} (sobre {porcentaje_total}% evaluado)")


def ver_estudiantes():
    """
    Muestra todos los estudiantes registrados con sus datos y estado académico.

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
            promedio = calcular_promedio_ponderado(notas)
            porcentaje_total = sum(n["porcentaje"] for n in notas)
            estado = f"Promedio: {promedio:.2f} — {'Aprobado ✓' if promedio >= 3.0 else 'Reprobado ✗'} (sobre {porcentaje_total}% evaluado)"
        else:
            estado = "Sin notas"

        print(
            f"Código: {codigo} | "
            f"Nombre: {datos['nombre']} | "
            f"Curso: {datos['curso']} | "
            f"{estado}"
        )


def ver_reprobados():
    """
    Lista todos los estudiantes con promedio ponderado inferior a 3.0.

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
        if datos["notas"] and calcular_promedio_ponderado(datos["notas"]) < 3.0
    ]

    if not reprobados:
        print("No hay estudiantes reprobados.")
        return

    print(f"\n--- Estudiantes reprobados ({len(reprobados)}) ---")

    for codigo, datos in reprobados:
        promedio = calcular_promedio_ponderado(datos["notas"])
        print(
            f"Código: {codigo} | "
            f"Nombre: {datos['nombre']} | "
            f"Curso: {datos['curso']} | "
            f"Promedio: {promedio:.2f}"
        )


def ver_aprobados():
    """
    Lista todos los estudiantes con promedio ponderado igual o superior a 3.0.

    Solo muestra estudiantes que tienen al menos una nota registrada.

    Returns:
        None
    """
    if not registro:  # Verifica que haya datos antes de filtrar
        print("No hay estudiantes registrados.")
        return

    aprobados = [
        (codigo, datos)
        for codigo, datos in registro.items()
        if datos["notas"] and calcular_promedio_ponderado(datos["notas"]) >= 3.0  # Filtra solo los que superan el umbral mínimo
    ]

    if not aprobados:  # Si la lista queda vacía, ningún estudiante con notas ha aprobado
        print("No hay estudiantes aprobados.")
        return

    print(f"\n--- Estudiantes aprobados ({len(aprobados)}) ---")

    for codigo, datos in aprobados:
        promedio = calcular_promedio_ponderado(datos["notas"])
        porcentaje_total = sum(n["porcentaje"] for n in datos["notas"])
        print(
            f"Código: {codigo} | "
            f"Nombre: {datos['nombre']} | "
            f"Curso: {datos['curso']} | "
            f"Promedio: {promedio:.2f} | "
            f"Evaluado: {porcentaje_total}%"
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

    cursos = {}  # Diccionario auxiliar donde cada clave es el nombre del curso y su valor es el conteo de estudiantes

    for datos in registro.values():
        curso = datos["curso"]
        cursos[curso] = cursos.get(curso, 0) + 1

    print(f"\n--- Cursos registrados ({len(cursos)}) ---")

    for curso, cantidad in sorted(cursos.items()):
        print(f"  {curso}: {cantidad} estudiante(s)")


def filtrar_por_curso():
    """
    Muestra todos los estudiantes que pertenecen a un curso específico.

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
            promedio = calcular_promedio_ponderado(notas)
            estado = f"Promedio: {promedio:.2f} — {'Aprobado ✓' if promedio >= 3.0 else 'Reprobado ✗'}"
        else:
            estado = "Sin notas"

        print(f"  Código: {codigo} | Nombre: {datos['nombre']} | {estado}")


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
        promedio = f"{calcular_promedio_ponderado(notas):.2f}" if notas else "Sin notas"
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
        print("8.  Ver estudiantes aprobados")
        print("9.  Ver cursos registrados")
        print("10. Filtrar estudiantes por curso")
        print("11. Buscar estudiante por nombre")
        print("12. Salir")

        try:
            seleccion = int(input("Opción: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        match seleccion:
            case 1:
                registrar_estudiante()
            case 2:
                codigo = pedir_codigo()
                if codigo is not None:
                    subir_nota(codigo)
            case 3:
                codigo = pedir_codigo()
                if codigo is not None:
                    modificar_estudiante(codigo)
            case 4:
                codigo = pedir_codigo()
                if codigo is not None:
                    dar_de_baja(codigo)
            case 5:
                codigo = pedir_codigo()
                if codigo is not None:
                    obtener_promedio(codigo)
            case 6:
                ver_estudiantes()
            case 7:
                ver_reprobados()
            case 8:
                ver_aprobados()
            case 9:
                ver_cursos()
            case 10:
                filtrar_por_curso()
            case 11:
                buscar_por_nombre()
            case 12:
                print("¡Hasta luego!")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
