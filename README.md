# Finance Assistant Chatbot 💬

This is a simple **Finance Assistant Chatbot** that interacts with users through a conversational interface. It can answer basic finance-related queries and assist users in managing their finances.

The chatbot is built using **Rasa** for the backend and **Streamlit** for the UI. The backend handles the conversation logic, while the UI is implemented with Streamlit to provide an easy-to-use interface.

## Features
- User-friendly interface with **Streamlit**.
- Chatbot powered by **Rasa** for handling finance-related conversations.
- Customizable starting message.
- Ability to clear chat history.
- Sidebar for configuration and settings.
- OpenAI integration (optional) for fallback conversations (if configured).

## Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **Rasa** (installation details below)
- **Streamlit**
- **Requests** library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/chatbot_project.git
    cd chatbot_project
    ```

2. **Create a virtual environment** and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Train the Rasa model** (if not already trained):
    ```bash
    rasa train
    ```

## How to Run

1. **Start the Rasa Server**:
    Open a terminal, navigate to your project directory, and run:
    ```bash
    rasa run --enable-api
    ```

2. **Run the Streamlit UI**:
    In a separate terminal, navigate to your project directory and run:
    ```bash
    streamlit run app.py
    ```

3. **Access the Chatbot**:
    Open your browser and go to:
    ```bash
    http://localhost:8501
    ```

## Project Structure

- `app.py`: Streamlit app for the chatbot UI.
- `domain.yml`: Rasa domain file defining intents, responses, and actions.
- `data/`: Directory containing Rasa training data (NLU, stories).
- `models/`: Pre-trained Rasa models.
- `config.yml`: Rasa configuration file.

## Customizing the Bot

- **Starting Message**: You can modify the starting message in `app.py` by changing the default assistant message in the following section:
    ```python
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Your custom starting message"}]
    ```

- **Backend Logic**: Modify the conversation logic in the `data/` folder and update your Rasa intents and actions accordingly.

## Troubleshooting

If you encounter connection errors (e.g., "Connection refused"), ensure that:
- Rasa is running on the correct port (`5005` by default).
- The backend server is properly set up.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

Created with ❤️ by [Your Name](https://github.com/username)
