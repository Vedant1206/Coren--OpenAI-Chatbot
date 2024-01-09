# Coren--OpenAI-Chatbot

## Overview
Provide a brief description of what your project is about. Explain its purpose and any important features or functionality.

## Prerequisites
- Rasa Version: 3.6.15
- Compatible Python Version: 3.7, 3.8, or 3.9

## Installation
To set up the project on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. **Install Rasa**:
   It's important to use the same Rasa version as specified in the prerequisites.
   ```bash
   pip install rasa==3.6.15
   ```

3. **Install Rasa SDK**:
   ```bash
   pip install rasa-sdk==3.6.2
   ```

## Configuration
Describe any necessary configuration steps, such as setting up environment variables or external services.

## Training the Model
To train the Rasa model, use the following command:
```bash
rasa train
```

## Running the Bot
To run the Rasa bot, execute:
```bash
rasa shell
```

## Testing
Provide instructions on how to run any tests you've written for your project.

## Deployment
Detail the steps required to deploy the project, if applicable.

## Contributing
Outline the process for contributing to the project, including any coding standards or guidelines.

## License
Specify the license under which your project is released, if any.

## Using rasa shell
- If you update the code, before running code, run the following command to train the bot( If you make changes to it)
```bash
rasa train
```
- followed by
```bash
rasa shell
```