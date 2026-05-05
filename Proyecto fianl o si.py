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
    Agrega una o varias notas a un estudiante existente.

    Args:
        codigo (int): Código del estudiante.

    Pregunta cuántas notas se desean ingresar y las valida una a una.
    Cada nota debe estar entre 0 y 5.

    Returns:
        None
    """
    if codigo not in registro:  # Frena la ejecución si el código no corresponde a ningún estudiante registrado
        print("Estudiante no encontrado.")
        return

    try:
        cantidad = int(input(f"¿Cuántas notas deseas agregar para {registro[codigo]['nombre']}? "))  # Muestra el nombre para confirmar que se está modificando al estudiante correcto
    except ValueError:  # Previene errores si el usuario escribe algo que no sea un número entero
        print("Ingresa un número válido.")
        return

    if cantidad <= 0:  # Evita ingresar cero o valores negativos que no tienen sentido como cantidad de notas
        print("La cantidad debe ser mayor a 0.")
        return

    agregadas = 0  # Contador para reportar al final cuántas notas fueron válidas y realmente guardadas

    for i in range(cantidad):  # Itera exactamente la cantidad de veces que el usuario indicó
        try:
            nota = float(input(f"  Nota {i + 1}: "))  # Se usa float para permitir notas decimales como 3.7 o 4.5
        except ValueError:  # Si el usuario escribe texto en lugar de un número, se omite esa nota y se continúa
            print(f"Nota {i + 1} inválida, se omite.")
            continue  # Salta al siguiente ciclo sin interrumpir el proceso completo

        if 0 <= nota <= 5:  # Valida que la nota esté dentro del rango académico permitido (0 a 5)
            registro[codigo]["notas"].append(nota)  # Añade la nota al historial de calificaciones del estudiante
            agregadas += 1  # Solo cuenta notas que pasaron la validación de rango
        else:
            print(f"Nota {i + 1} fuera de rango (0-5), se omite.")  # Informa que esa nota específica fue descartada por ser inválida

    print(f"{agregadas} nota(s) registrada(s) con éxito.")  # Resume cuántas notas fueron efectivamente guardadas de las que se intentaron ingresar


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

    print(f"\n--- Modificar: {datos['nombre']} | Curso: {datos['curso']} | Notas: {datos['notas']} ---")  # Muestra el estado actual para que el usuario sepa qué está por cambiar
    print("1. Modificar nombre")
    print("2. Modificar curso")
    print("3. Modificar una nota")

    try:
        opcion = int(input("¿Qué deseas modificar? "))  # Captura la elección del submenú de modificación
    except ValueError:  # Evita que una entrada no numérica rompa el flujo del programa
        print("Opción inválida.")
        return

    if opcion == 1:
        nuevo_nombre = input("Nuevo nombre: ").strip()  # Se limpia el texto para evitar guardar espacios innecesarios
        if not nuevo_nombre:  # Impide reemplazar el nombre actual por un valor vacío
            print("El nombre no puede estar vacío.")
            return
        datos["nombre"] = nuevo_nombre  # Sobreescribe el nombre anterior con el nuevo valor validado
        print("Nombre actualizado con éxito.")

    elif opcion == 2:
        nuevo_curso = input("Nuevo curso: ").strip()  # Se limpia igual que el nombre para mantener consistencia en los datos
        if not nuevo_curso:  # Impide reemplazar el curso actual por un valor vacío
            print("El curso no puede estar vacío.")
            return
        datos["curso"] = nuevo_curso  # Actualiza el campo curso dentro del perfil del estudiante
        print("Curso actualizado con éxito.")

    elif opcion == 3:
        notas = datos["notas"]  # Alias a la lista de notas para acceder a ella con mayor claridad

        if not notas:  # No tiene sentido modificar una nota si la lista está vacía
            print("Este estudiante no tiene notas registradas.")
            return

        print(f"Notas actuales: {notas}")  # Muestra las notas con sus índices implícitos para que el usuario pueda elegir cuál modificar

        try:
            indice = int(input("Índice de la nota a modificar (desde 0): "))  # El índice determina la posición dentro de la lista de notas
            nueva_nota = float(input("Nueva nota: "))  # Float para admitir valores decimales en la calificación
        except ValueError:  # Captura cualquier entrada no convertible a número en alguno de los dos campos
            print("Entrada inválida.")
            return

        if 0 <= indice < len(notas) and 0 <= nueva_nota <= 5:  # Valida simultáneamente que el índice exista en la lista y que la nota sea válida
            notas[indice] = nueva_nota  # Reemplaza la nota en la posición indicada por el nuevo valor
            print("Nota modificada con éxito.")
        else:
            print("Índice o nota fuera de rango.")  # Cubre dos casos de error: índice inexistente o nota fuera del rango 0-5

    else:
        print("Opción no válida.")  # El usuario ingresó un número que no corresponde a ninguna de las tres opciones del submenú


def dar_de_baja(codigo):
    """
    Elimina un estudiante del registro tras confirmación del usuario.

    Args:
        codigo (int): Código del estudiante.

    Returns:
        None
    """
    if codigo not in registro:  # Verifica que el código corresponda a un estudiante antes de intentar eliminarlo
        print("Estudiante no encontrado.")
        return

    nombre = registro[codigo]["nombre"]  # Guarda el nombre antes de eliminar para poder mostrarlo en el mensaje de confirmación
    confirmacion = input(f"¿Estás seguro de dar de baja a {nombre}? (s/n): ").strip().lower()  # Solicita confirmación explícita para evitar eliminaciones accidentales

    if confirmacion == "s":  # Solo procede si el usuario escribe exactamente "s" para confirmar
        del registro[codigo]  # Elimina completamente la entrada del diccionario usando el código como clave
        print(f"Estudiante {nombre} dado de baja con éxito.")
    else:
        print("Operación cancelada.")  # Cualquier respuesta distinta de "s" cancela la eliminación de forma segura


def obtener_promedio(codigo):
    """
    Calcula y muestra el promedio de notas de un estudiante.

    Args:
        codigo (int): Código del estudiante.

    Returns:
        None
    """
    if codigo not in registro:  # Previene el cálculo sobre un estudiante que no existe en el sistema
        print("Estudiante no encontrado.")
        return

    notas = registro[codigo]["notas"]  # Extrae únicamente la lista de calificaciones del estudiante

    if not notas:  # Evita división por cero al intentar calcular el promedio de una lista vacía
        print("Este estudiante no tiene notas registradas.")
        return

    promedio = sum(notas) / len(notas)  # Calcula la media aritmética dividiendo la suma total entre la cantidad de notas
    estado = "Aprobado ✓" if promedio >= 3.0 else "Reprobado ✗"  # Determina el estado académico usando 3.0 como umbral mínimo de aprobación
    print(f"Promedio de {registro[codigo]['nombre']}: {promedio:.2f} — {estado}")  # :.2f limita la presentación del promedio a dos decimales


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
    if not registro:  # Evita recorrer un diccionario vacío e informa al usuario que aún no hay datos
        print("No hay estudiantes registrados.")
        return

    print("\n--- Lista de todos los estudiantes ---")

    for codigo, datos in registro.items():  # Itera sobre cada par clave-valor del diccionario para listar a todos los estudiantes
        notas = datos["notas"]  # Accede directamente a la lista de notas del estudiante actual en la iteración

        if notas:  # Solo calcula promedio si el estudiante tiene al menos una nota registrada
            promedio = sum(notas) / len(notas)  # Media aritmética de las calificaciones del estudiante
            estado = f"Promedio: {promedio:.2f} — {'Aprobado ✓' if promedio >= 3.0 else 'Reprobado ✗'}"  # Construye el texto de estado con el promedio formateado y la etiqueta de aprobación
        else:
            estado = "Sin notas"  # Texto alternativo para estudiantes que todavía no tienen calificaciones

        print(
            f"Código: {codigo} | "
            f"Nombre: {datos['nombre']} | "
            f"Curso: {datos['curso']} | "
            f"Notas: {notas} | "
            f"{estado}"  # Imprime toda la información del estudiante en una sola línea separada por pipes para facilitar la lectura
        )


def ver_reprobados():
    """
    Lista todos los estudiantes con promedio inferior a 3.0.

    Solo muestra estudiantes que tienen al menos una nota registrada.

    Returns:
        None
    """
    if not registro:  # Verifica que haya datos antes de filtrar para evitar operar sobre un sistema vacío
        print("No hay estudiantes registrados.")
        return

    reprobados = [
        (codigo, datos)
        for codigo, datos in registro.items()  # Recorre todos los estudiantes del registro para evaluarlos
        if datos["notas"] and sum(datos["notas"]) / len(datos["notas"]) < 3.0  # Excluye a quienes no tienen notas y filtra los que no alcanzan el umbral de aprobación
    ]

    if not reprobados:  # Si la lista queda vacía, todos los estudiantes con notas están aprobados
        print("No hay estudiantes reprobados.")
        return

    print(f"\n--- Estudiantes reprobados ({len(reprobados)}) ---")  # Encabezado con el total de reprobados para una lectura rápida

    for codigo, datos in reprobados:  # Itera exclusivamente sobre los estudiantes que no alcanzaron el promedio mínimo
        promedio = sum(datos["notas"]) / len(datos["notas"])  # Recalcula el promedio aquí para mostrarlo en el reporte
        print(
            f"Código: {codigo} | "
            f"Nombre: {datos['nombre']} | "
            f"Curso: {datos['curso']} | "
            f"Promedio: {promedio:.2f}"  # Muestra el promedio con dos decimales para identificar qué tan lejos está del mínimo
        )


def ver_cursos():
    """
    Muestra todos los cursos únicos registrados en el sistema
    junto con la cantidad de estudiantes en cada uno.

    Returns:
        None
    """
    if not registro:  # Impide ejecutar la función si aún no hay estudiantes que proporcionen datos de cursos
        print("No hay estudiantes registrados.")
        return

    cursos = {}  # Diccionario auxiliar donde cada clave es el nombre del curso y su valor es el conteo de estudiantes

    for datos in registro.values():  # Solo se necesitan los valores del registro, no las claves (códigos)
        curso = datos["curso"]  # Extrae el nombre del curso del estudiante actual
        cursos[curso] = cursos.get(curso, 0) + 1  # Incrementa el contador del curso si ya existe, o lo inicializa en 1 si es nuevo

    print(f"\n--- Cursos registrados ({len(cursos)}) ---")  # Muestra cuántos cursos distintos hay en el sistema

    for curso, cantidad in sorted(cursos.items()):  # sorted() ordena los cursos alfabéticamente para facilitar la lectura
        print(f"  {curso}: {cantidad} estudiante(s)")  # Muestra el nombre del curso y cuántos estudiantes están inscritos en él


def filtrar_por_curso():
    """
    Muestra todos los estudiantes que pertenecen a un curso específico.

    Solicita el nombre del curso y lista los estudiantes encontrados
    con su código, notas y promedio.

    Returns:
        None
    """
    if not registro:  # Verifica que haya estudiantes registrados antes de intentar cualquier filtrado
        print("No hay estudiantes registrados.")
        return

    curso_buscado = input("Nombre del curso a buscar: ").strip()  # Se limpia la entrada para evitar falsos negativos por espacios

    encontrados = [
        (codigo, datos)
        for codigo, datos in registro.items()  # Recorre todos los estudiantes para comparar su curso
        if datos["curso"].lower() == curso_buscado.lower()  # Comparación insensible a mayúsculas para mayor tolerancia en la búsqueda
    ]

    if not encontrados:  # Si ningún estudiante coincide con el curso ingresado, se informa y se sale
        print(f"No se encontraron estudiantes en el curso '{curso_buscado}'.")
        return

    print(f"\n--- Estudiantes del curso '{curso_buscado}' ({len(encontrados)}) ---")  # Encabezado con el nombre del curso y la cantidad de coincidencias

    for codigo, datos in encontrados:  # Itera solo sobre los estudiantes del curso filtrado
        notas = datos["notas"]  # Accede a las calificaciones del estudiante para calcular su estado

        if notas:  # Calcula promedio solo si el estudiante tiene notas, evitando división por cero
            promedio = sum(notas) / len(notas)  # Media aritmética de las calificaciones
            estado = f"Promedio: {promedio:.2f} — {'Aprobado ✓' if promedio >= 3.0 else 'Reprobado ✗'}"  # Determina el estado académico con base en el umbral de 3.0
        else:
            estado = "Sin notas"  # Etiqueta para estudiantes del curso que aún no tienen calificaciones registradas

        print(f"  Código: {codigo} | Nombre: {datos['nombre']} | Notas: {notas} | {estado}")  # Presenta la información del estudiante en formato compacto de una línea


def buscar_por_nombre():
    """
    Busca un estudiante por nombre y muestra el curso al que pertenece.

    Si hay varios estudiantes con nombres similares, los muestra todos.

    Returns:
        None
    """
    if not registro:  # Evita realizar una búsqueda sobre un sistema sin estudiantes registrados
        print("No hay estudiantes registrados.")
        return

    nombre_buscado = input("Nombre del estudiante a buscar: ").strip().lower()  # Se normaliza a minúsculas para hacer la búsqueda insensible a mayúsculas

    encontrados = [
        (codigo, datos)
        for codigo, datos in registro.items()  # Evalúa cada estudiante del sistema
        if nombre_buscado in datos["nombre"].lower()  # Búsqueda parcial: encuentra coincidencias aunque el usuario ingrese solo parte del nombre
    ]

    if not encontrados:  # Informa si la búsqueda no produjo ningún resultado
        print("No se encontró ningún estudiante con ese nombre.")
        return

    print(f"\n--- Resultados ({len(encontrados)}) ---")  # Encabezado con la cantidad de coincidencias encontradas

    for codigo, datos in encontrados:  # Recorre los resultados para mostrar la información de cada estudiante encontrado
        notas = datos["notas"]  # Extrae las notas para calcular el promedio o mostrar que no hay
        promedio = f"{sum(notas) / len(notas):.2f}" if notas else "Sin notas"  # Expresión condicional: formatea el promedio si hay notas, o indica ausencia de ellas
        print(
            f"  Código: {codigo} | "
            f"Nombre: {datos['nombre']} | "
            f"Curso: {datos['curso']} | "
            f"Promedio: {promedio}"  # Muestra los datos clave del estudiante encontrado en una sola línea
        )


def pedir_codigo():
    """
    Solicita al usuario el código de un estudiante.

    Valida que sea un número entero.

    Returns:
        int | None: Código ingresado o None si es inválido.
    """
    try:
        return int(input("Código del estudiante: "))  # Convierte directamente la entrada a entero para que sea compatible con las claves del diccionario
    except ValueError:  # Si el usuario escribe algo no numérico, retorna None para que la función llamante pueda manejarlo
        print("El código solo puede contener números.")
        return None  # None actúa como señal de error para que el menú principal evite ejecutar la operación solicitada

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
            seleccion = int(input("Opción: "))  # Convierte la entrada del usuario en entero para compararlo con las opciones del menú
        except ValueError:  # Captura entradas no numéricas para evitar que el programa se interrumpa con un error no controlado
            print("Por favor ingresa un número válido.")
            continue  # Vuelve al inicio del bucle sin ejecutar ninguna operación

        match seleccion:  # Evalúa el valor de seleccion y ejecuta el bloque del caso que coincida
            case 1:
                registrar_estudiante()  # Inicia el flujo de captura y validación de datos para un nuevo estudiante
            case 2:
                codigo = pedir_codigo()  # Solicita el código antes de llamar a la función para reutilizar la lógica de validación
                if codigo is not None:  # Solo procede si pedir_codigo() devolvió un entero válido
                    subir_nota(codigo)
            case 3:
                codigo = pedir_codigo()  # Reutiliza pedir_codigo() para mantener consistencia en la forma de obtener el identificador
                if codigo is not None:  # Previene llamar a modificar_estudiante() con un código inválido
                    modificar_estudiante(codigo)
            case 4:
                codigo = pedir_codigo()  # El código es necesario para localizar al estudiante que se desea eliminar
                if codigo is not None:  # Solo invoca la baja si se obtuvo un código numérico válido
                    dar_de_baja(codigo)
            case 5:
                codigo = pedir_codigo()  # Requiere identificar al estudiante antes de calcular su promedio
                if codigo is not None:  # Evita pasar None a obtener_promedio(), lo que causaría un comportamiento inesperado
                    obtener_promedio(codigo)
            case 6:
                ver_estudiantes()  # No requiere código porque opera sobre todos los estudiantes del registro
            case 7:
                ver_reprobados()  # Filtra internamente sin necesitar input del usuario
            case 8:
                ver_cursos()  # Genera el resumen de cursos a partir de los datos actuales del registro
            case 9:
                filtrar_por_curso()  # Solicita internamente el nombre del curso a filtrar
            case 10:
                buscar_por_nombre()  # Solicita internamente el nombre a buscar y permite coincidencias parciales
            case 11:
                print("¡Hasta luego!")
                break  # Termina el bucle while y finaliza la ejecución del programa
            case _:
                print("Opción no válida, intenta de nuevo.")  # El guion bajo actúa como comodín que captura cualquier valor no contemplado en los casos anteriores

if __name__ == "__main__":
    main()  # Punto de entrada: garantiza que main() solo se ejecute cuando el archivo se corre directamente, no al importarlo