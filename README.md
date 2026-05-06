# Sistema de Registro de Estudiantes

Sistema de gestión académica desarrollado en Python que permite registrar estudiantes, administrar sus notas y consultar su rendimiento académico desde la consola.

---

## Funcionalidades

- **Registrar estudiantes** con nombre, curso y código único
- **Agregar notas con porcentaje** (nota entre 0.0 y 5.0, porcentaje entre 1 y 100) a cada estudiante
- **Calcular promedio ponderado** teniendo en cuenta el peso porcentual de cada nota
- **Modificar datos** de un estudiante: nombre, curso o notas específicas
- **Dar de baja** a un estudiante del sistema
- **Ver promedio** individual y estado académico (Aprobado / Reprobado)
- **Ver todos los estudiantes** registrados con su información completa
- **Listar estudiantes reprobados** (promedio ponderado menor a 3.0)
- **Listar estudiantes aprobados** (promedio ponderado mayor o igual a 3.0)
- **Ver cursos registrados** y cantidad de estudiantes por curso
- **Filtrar estudiantes** por curso
- **Buscar estudiantes** por nombre

---

## Requerimientos del sistema

| Componente | Mínimo recomendado |
|---|---|
| Sistema operativo | Windows 10 / macOS 10.15 / Linux Ubuntu 20.04 |
| Python | Versión 3.10 o superior |
| RAM | 512 MB |
| Almacenamiento | 10 MB libres |
| Terminal | CMD, PowerShell, bash o cualquier consola de comandos |

> No requiere librerías externas. Usa únicamente módulos nativos de Python.

---

## Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Estructuras de datos:** Diccionarios y listas
- **Interfaz:** Línea de comandos (consola)

---

## Cómo ejecutar el programa

1. Asegúrate de tener **Python 3** instalado en tu equipo.
2. Clona o descarga este repositorio.
3. Abre una terminal en la carpeta del proyecto.
4. Ejecuta el siguiente comando:

```bash
python Proyecto_fianl_o_si_.py
```

5. Sigue las instrucciones del menú interactivo.

---

## Menú principal

```
--- Menú principal ---
1.  Registrar estudiante
2.  Subir nota(s)
3.  Modificar estudiante (nombre, curso o nota)
4.  Dar de baja a un estudiante
5.  Ver promedio de un estudiante
6.  Ver todos los estudiantes
7.  Ver estudiantes reprobados
8.  Ver estudiantes aprobados
9.  Ver cursos registrados
10. Filtrar estudiantes por curso
11. Buscar estudiante por nombre
12. Salir
```

---

## Consideraciones

- El **código del estudiante** debe ser un número entero único.
- Las **notas** deben estar en el rango de **0.0 a 5.0**.
- Cada nota lleva un **porcentaje** que indica su peso en el promedio final.
- La suma de porcentajes por estudiante **no puede superar el 100%**.
- El promedio se calcula de forma **ponderada** según el porcentaje de cada nota.
- Un estudiante se considera **aprobado** si su promedio ponderado es **≥ 3.0**.
- Los datos se almacenan **en memoria**, por lo que se pierden al cerrar el programa.

---

## 👨‍💻 Autores

- Juan Diego Narvaez
- Juan Pablo Quintana
