## GROQ Chat Interface - README

This project is a simple chat tool that interacts with the **GROQ** model using an API. The program allows users to make requests to the model either through the command line or via an input interface in the terminal.

### Features

- **Interactive or command-line input**: Users can input a prompt manually or provide it as a command-line argument using the `-p` flag.
- **Typing animation**: The text is displayed with a typing animation for a more engaging user experience.
- **Response saving**: Both questions and responses are saved to a text file.
- **Terminal colors**: Messages are displayed with colors using the `colorama` library for better readability.

---

### Requirements

- **Python 3.x**
- Required libraries:
  - `colorama`
  - `groq`
  
Install the dependencies using the following command:

```bash
pip install colorama groq 
```
### Setup

To run the program, you need to set the GROQ_API_KEY environment variable with your API key:

```bash
export GROQ_API_KEY="your_api_key"
```

### Usage

#### Interactive Mode (manual)

If you run the script without any arguments, it will enter a loop where it will continuously ask for user input:

```bash
python groq.py
Starting GROQ...
>> 
```

Example:
```bash
>> Hi, Groq!    
Waiting for GROQ...
GROQ: 
Hi there! I'm Groq, but feel free to call me Groq or even G (if you're feeling fancy). What brings you here today? Want to chat about AI, chatbot-related stuff, or just have a fun conversation? Let's get this chat started!
>>  
```

Type exit or bye to exit the program.

#### Command-Line Mode

If you prefer to pass the prompt directly when running the program, use the -p flag:
``` bash
python groq.py -p "How are you?"
```

In this mode, the program will execute with the provided prompt and then automatically close.

Generated Files

	• response.txt: All questions and responses are saved to this text file in the same directory as the script.

Code Structure

The script is divided into the following main functions:

	• typing_animation: Displays text with an animation that mimics typing.
	• typing_text: A similar function with a faster delay.
	• save: Saves questions and responses to the response.txt file.
	• groq: Sends a request to the GROQ model and prints the response.
	• main: Manages the core logic of the program, detecting whether the user is using the -p option or entering prompts manually.

#### Example Execution

##### Interactive Mode:
``` bash
python groq.py

Starting GROQ...
>> What is AI?
Waiting for GROQ...
GROQ: Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems.
```

Command-Line Mode:

```bash
python script.py -p "How are you?"

Starting GROQ...
Waiting for GROQ...
GROQ: I'm doing well, thank you for asking.
Exiting...
```
Error Handling

	• If the API key is not set correctly, the program will display an error message and stop.
	• If any error occurs during the GROQ request, the program will catch and display the error without crashing.



Open to Feedback

Feel free to provide any feedback or suggestions for improving the script. I’m open to any comments that could enhance its functionality or usability!
