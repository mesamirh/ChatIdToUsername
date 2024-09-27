# ChatId To Username

ChatId To Username is script for a Telegram bot that allows users to fetch information about a chat by providing a chat ID or username. The bot can retrieve details such as the chat ID, title, type, and username.

## Features

- Fetch chat information by chat ID or username.
- Send a confirmation message to the bot owner when the bot starts.
- Display a loading animation while fetching chat information.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/mesamirh/ChatIdToUsername.git
   cd ChatIdToUsername
   ```

2. Create a virtual environment and activate it:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your Telegram bot token and owner ID:
   ```env
   BOT_TOKEN=your_bot_token
   OWNER_ID=your_owner_id
   ```

## Usage

1. Run the bot:

   ```sh
   python main.py
   ```

2. Start a conversation with the bot on Telegram and send a chat ID or username to fetch information about that chat.

## Code Overview

### main.py

- **print_header**: Prints a header to the console.
- **send_confirmation_message**: Sends a confirmation message to the bot owner when the bot starts.
- **animate_loading**: Displays a loading animation while fetching chat information.
- **start**: Handles the `/start` command and provides instructions to the user.
- **get_chat_info**: Fetches and displays information about a chat based on the provided chat ID or username.
- **main**: Initializes the bot, sets up command handlers, and starts polling for updates.

## Contact

For any questions or inquiries, please contact [Samir](mailto:samirhossain34250@gmail.com).
