## GROQ Chat Interface - README

Este proyecto es una herramienta de chat simple que interactúa con el modelo **GROQ** usando una API. El programa permite a los usuarios hacer solicitudes al modelo a través de la línea de comandos o mediante una interfaz de entrada en la terminal.

### Características

- **Entrada interactiva o por línea de comandos**: Los usuarios pueden ingresar un prompt manualmente o proporcionarlo como un argumento de línea de comandos usando la flag `-p`.
- **Animación de escritura**: El texto se muestra con una animación de escritura para una experiencia de usuario más atractiva.
- **Guardado de respuestas**: Tanto las preguntas como las respuestas se guardan en un archivo de texto.
- **Colores en la terminal**: Los mensajes se muestran con colores utilizando la biblioteca `colorama` para una mejor legibilidad.

---

### Requisitos

- **Python 3.x**
- Bibliotecas requeridas:
  - `colorama`
  - `groq`
  
Instala las dependencias usando el siguiente comando:

```bash
pip install colorama groq 
```

### Configuración

Para ejecutar el programa, necesitas establecer la variable de entorno GROQ_API_KEY con tu clave API:
```bash
export GROQ_API_KEY="tu_api_key"
```

### Uso

#### Modo Interactivo (manual)

Si ejecutas el script sin argumentos, entrará en un bucle donde pedirá continuamente la entrada del usuario:
```bash
python groq.py
Starting GROQ...
>> 
```

Ejemplo:
```bash
>> ¡Hola, Groq!    
Waiting for GROQ...
GROQ: 
¡Hola! Soy Groq, pero siéntete libre de llamarme Groq o incluso G (si te sientes elegante). ¿Qué te trae aquí hoy? ¿Quieres hablar sobre IA, cosas relacionadas con chatbots o simplemente tener una conversación divertida? ¡Empecemos esta charla!
>>  
```

Escribe exit o bye para salir del programa.

#### Modo Línea de Comandos

Si prefieres pasar el prompt directamente al ejecutar el programa, usa la flag -p:

```bash
python groq.py -p "¿Cómo estás?"
```

En este modo, el programa se ejecutará con el prompt proporcionado y luego se cerrará automáticamente.

### Archivos Generados

    • response.txt: Todas las preguntas y respuestas se guardan en este archivo de texto en el mismo directorio que el script.

### Estructura del Código

El script se divide en las siguientes funciones principales:

    • typing_animation: Muestra texto con una animación que imita la escritura.
    • typing_text: Una función similar con un retraso más rápido.
    • save: Guarda preguntas y respuestas en el archivo response.txt.
    • groq: Envía una solicitud al modelo GROQ y imprime la respuesta.
    • main: Gestiona la lógica central del programa, detectando si el usuario está usando la opción -p o ingresando prompts manualmente.

### Ejecución de Ejemplo

##### Modo Interactivo:
```bash
python groq.py

Starting GROQ...
>> ¿Qué es la IA?
Waiting for GROQ...
GROQ: La inteligencia artificial es la simulación de procesos de inteligencia humana por parte de máquinas, especialmente sistemas informáticos.
```
##### Modo Línea de Comandos:
```bash
python script.py -p "¿Cómo estás?"

Starting GROQ...
Waiting for GROQ...
GROQ: Estoy bien, gracias por preguntar.
Exiting...
```
### Manejo de Errores

    • Si la clave API no se establece correctamente, el programa mostrará un mensaje de error y se detendrá.
    • Si ocurre algún error durante la solicitud a GROQ, el programa capturará y mostrará el error sin fallar.

### Abierto a Comentarios

Siéntete libre de proporcionar cualquier comentario o sugerencias para mejorar el script. Estoy abierto a cualquier comentario que pueda mejorar su funcionalidad o usabilidad.


