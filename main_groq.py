import os
import sys
import time
from colorama import Fore, Style, init  # type: ignore
from groq import Groq

# Inicializa Colorama para compatibilidad con terminales
init(autoreset=True)


def typing_animation(text, color):
    """Función para imprimir texto con animación de escritura."""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.02)  # Retraso para la animación
    print()  # Nueva línea al finalizar


def typing_text(text, color):
    """Función para imprimir texto con animación de escritura."""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.01)  # Retraso para la animación
    print()  # Nueva línea al finalizar


def save(response):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "response.txt")

    try:
        with open(file_path, "a") as f:
            f.write(response + "\n")
    except Exception as e:
        print(f"Failed to save response: {e}")

def groq(question,client):
    try:
                typing_animation("Waiting for GROQ...", Fore.YELLOW)

                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"{question}",
                        }
                    ],
                    model="llama3-8b-8192",
                )

                response = chat_completion.choices[0].message.content
                typing_text("GROQ: ", Fore.LIGHTRED_EX)
                typing_text(response, Fore.LIGHTMAGENTA_EX)
                save(question)
                save(response)

    except Exception as e:
                print(f"An error occurred: {e}")



def main():
    typing_animation("Starting GROQ...", Fore.CYAN)

    # Obtener la clave API de la variable de entorno
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        print("API key not found. Please set your GROQ_API_KEY environment variable.")
        return

    client = Groq(api_key=api_key)

    # Verificar si la flag '-p' está presente en los argumentos
    if '-p' in sys.argv:
        # Si está presente, toma el siguiente argumento como el prompt y termina
        prompt_index = sys.argv.index('-p') + 1
        if prompt_index < len(sys.argv):
            question = sys.argv[prompt_index]
        else:
            print("Error: No prompt provided after '-p'.")
            return

        # Procesar el prompt y terminar
        groq(question,client)
        typing_animation("Exiting...", Fore.RED)



    else:
        # Si no está presente '-p', se ejecuta un loop para obtener el input manual
        loop = True
        while loop:
            try:
                question = input(Fore.GREEN + ">> " + Style.RESET_ALL)

                if question.lower() in ["exit", "bye"]:
                    typing_animation("Exiting...", Fore.RED)
                    loop = False
                    break

                if question:
                    groq(question,client)

            except KeyboardInterrupt:
                typing_animation("Exiting...", Fore.RED)
                loop = False
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
