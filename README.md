# NorthStar Voice Assistant

NorthStar is a voice-activated virtual assistant that leverages the power of OpenAI's GPT-3 to provide answers to your questions. It uses the `speech_recognition` library to recognize your voice commands and the `pyttsx3` library for text-to-speech functionality.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)
- [License](#license)

## Installation
```
To get started with the NorthStar Voice Assistant, please follow these steps:

1. Make sure you have Python 3.x installed on your system. 
You can download it from the [official Python website](https://www.python.org/downloads/).
```
```
2. Clone this repository to your local machine:

git clone https://github.com/yourusername/northstar-voice-assistant.git
```
```
3. Change to the project directory:

cd northstar-voice-assistant
```
```
4. Create a virtual environment:

python3 -m venv venv
```
```
5. Activate the virtual environment:

- On Windows:

venv\Scripts\activate
```
```
- On macOS and Linux:

source venv/bin/activate
```

```
6. Install the required dependencies:

pip install -r requirements.txt
```
```
7. Obtain an OpenAI API key by signing up for an account on the [OpenAI website](https://beta.openai.com/signup/).
```
```
8. Set your OpenAI API key as an environment variable:

- On Windows:

set OPENAI_API_KEY=your_api_key
```
```
- On macOS and Linux:

export OPENAI_API_KEY=your_api_key
```


## Usage

To run the NorthStar Voice Assistant:

1. Ensure your microphone is properly connected and configured.

2. Run the `main.py` script:

python main.py

vbnet
Copy code

3. Speak the activation code "hey northstar" to activate the assistant.

4. Ask your question, and NorthStar will provide you with an answer.

5. To ask a new question, say "new question" and the assistant will listen for another activation code.

## Code Explanation

The `main.py` script contains the following functions:

- `listen_for_activation()`: Listens for the activation code "hey northstar" using the `speech_recognition` library. When the code is detected, the assistant speaks a prompt using `pyttsx3`.

- `listen_for_question()`: Listens for a question and returns the text of the question. If the user says "new question," the assistant returns to listening for the activation code.

- `speak_answer(answer)`: Takes an answer as input and uses the `pyttsx3` library to speak the answer.

The script sets up the OpenAI API with the provided API key and continuously listens for questions. Once a question is detected, it sends the question to the OpenAI API, which returns an answer using the GPT-3 model. The assistant then speaks the answer.

## Contributing

We welcome contributions to the NorthStar Voice Assistant! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with clear, concise commit messages.
4. Submit a pull request, describing the changes you've made and the reasoning behind them.

## License

This project is released under the [MIT License](
