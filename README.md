# OpenAI Model Information

Welcome to OpenAI Model Management! This tool allows you to interact with the OpenAI API to retrieve information about available models and view their details. With this script, you can easily explore the various models offered by OpenAI and learn more about their specifications.

## Prerequisites

Before using this tool, please ensure that you have the following:

1. **Python**: Make sure Python is installed on your computer. If you don't have Python installed, you can download and install it from the official Python website: [python.org](https://www.python.org).

2. **API Key**: You will need an OpenAI API key to access the models. If you don't have an API key, you can sign up for OpenAI and generate one in your account settings.

3. **API Key Configuration**: To configure your API key, create a file named `.env` in the same directory as the script. Open the `.env` file using a text editor and add the following line, replacing `YOUR_API_KEY` with your actual API key:

   ```
   OpenAIKey=YOUR_API_KEY
   ```

   Save the file after adding your API key.

## Getting Started

To use the OpenAI Model Management tool, follow these steps:

1. Download the script: Download the `openai_model_management.py` script from the [OpenAI Model Management GitHub repository](https://github.com/yourusername/openai-model-management). Save it to a location on your computer.

2. Install Dependencies: Open a command prompt or terminal and navigate to the directory where you saved the script. Install the required dependencies by running the following command:

   ```shell
   pip install requests python-dotenv
   ```

3. Configure API Key: Open the `.env` file you created earlier and replace `YOUR_API_KEY` with your actual OpenAI API key. Save the file.

4. Run the Script: In the command prompt or terminal, navigate to the directory where you saved the script and run the following command:

   ```shell
   python openai_model_management.py
   ```

5. Explore Available Models: The script will display a list of available models. Each model will be assigned a number. Enter the corresponding number to select a model.

6. View Model Details: Once you've selected a model, the script will display detailed information about the chosen model, including its creation date, ownership, and permissions.

7. Repeat or Exit: After viewing the model details, you can choose to explore more models or exit the script.

## Note

- This tool is intended for end users who want to explore the available models and view their details without having to write or understand programming code.
- The `.env` file containing your API key is kept separate from the script to ensure the security of your credentials. Make sure to keep the `.env` file confidential and do not share it with others.

## Support

For any questions or assistance regarding the OpenAI Model Management tool, please reach out to the OpenAI support team or refer to the OpenAI documentation for further guidance.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as permitted by the license.

## Acknowledgements

This tool was created using the OpenAI API, which is developed and maintained by OpenAI. Special thanks to the OpenAI team for providing access to their powerful models and supporting the developer community.
