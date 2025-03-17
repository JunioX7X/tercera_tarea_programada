# 🚀 Proyecto de Estructuras de Datos en Python 🐍

¡Bienvenido al repositorio de **Estructuras de Datos en Python**! Este proyecto es una implementación práctica de varias estructuras de datos comunes, como listas enlazadas, listas dobles y colas de prioridad, utilizando el lenguaje de programación Python. Además, se integra con una clase `Persona` para manejar datos de personas de manera eficiente.

## 📂 Estructura del Proyecto

El proyecto está organizado en varios archivos Python, cada uno con una funcionalidad específica:

- **`nodo.py`**: Contiene las clases `NodoSimple` y `NodoDoble`, que son los bloques de construcción para las listas enlazadas y dobles.
- **`persona.py`**: Define la clase `Persona`, que almacena información como nombre, apellidos y edad.
- **`cola_prioridad.py`**: Implementa una cola de prioridad donde las personas mayores de 65 años tienen prioridad.
- **`lista_enlazada_ordenada.py`**: Implementa una lista enlazada ordenada por edad.
- **`lista_doble_ordenada.py`**: Implementa una lista doblemente enlazada ordenada por edad, con búsquedas optimizadas desde el inicio o el final.
- **`programa_cola_prioridad.py`**: Un programa interactivo para probar la cola de prioridad.
- **`programa_lista_simple.py`**: Un programa interactivo para probar la lista enlazada simple.
- **`programa_lista_doble.py`**: Un programa interactivo para probar la lista doblemente enlazada.

## 🛠️ Funcionalidades

### Cola de Prioridad
- **Encolar**: Añade una persona a la cola, dando prioridad a las personas mayores de 65 años.
- **Desencolar**: Elimina y devuelve la persona con mayor prioridad.
- **Imprimir**: Muestra todas las personas en la cola.

### Lista Enlazada Simple
- **Insertar Ordenado**: Añade una persona a la lista, manteniéndola ordenada por edad.
- **Buscar**: Permite buscar personas por edad, nombre o apellido.
- **Borrar**: Elimina una persona de la lista por posición.

### Lista Doble Enlazada
- **Insertar Ordenado**: Añade una persona a la lista, manteniéndola ordenada por edad.
- **Buscar Optimizado**: Busca personas por edad, nombre o apellido, optimizando la búsqueda desde el inicio o el final según la proximidad.
- **Borrar**: Elimina una persona de la lista por posición.

## 🚀 Cómo Usar

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/estructuras-datos-python.git

Ejecuta cualquiera de los programas interactivos:

python programa_cola_prioridad.py
python programa_lista_simple.py
python programa_lista_doble.py
