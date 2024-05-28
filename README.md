# Stock Chatbot Application

Welcome to the Stock Chatbot Application! This project is a web-based chatbot that provides real-time stock market information and insights using OpenAI's GPT-3.5-turbo and Alpha Vantage APIs.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## Introduction
The Stock Chatbot Application allows users to interact with a chatbot to get real-time stock prices and market insights. It uses OpenAI's GPT-3.5-turbo for natural language processing and the Alpha Vantage API for fetching stock data. The application is designed with a user-friendly web interface and is containerized using Docker for easy deployment.

## Features
- **Real-Time Stock Information**: Query real-time stock prices and market data.
- **Natural Language Processing**: Provides intelligent responses to user queries using OpenAI's GPT-3.5-turbo.
- **User-Friendly Interface**: Responsive and intuitive web interface for seamless interaction.
- **Dockerized Deployment**: Containerized using Docker for easy deployment and scalability.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript, jQuery
- **Backend**: Python, Flask
- **APIs**: OpenAI GPT-3.5-turbo, Alpha Vantage
- **Database**: SQLite
- **Containerization**: Docker

## Installation
To run this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/embiekhochiu/cinnamon_ai_stock_chatbot.git
    cd cinnamon_ai_stock_chatbot
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the project root and add your API keys:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
    ```

5. **Run the Flask Application**:
    ```bash
    run.py
    ```

6. **Or instead you can build and Run with Docker**:
    ```bash
    docker build -t cinnamon_ai_stock_chatbot .
    docker run -p 5000:5000 cinnamon_ai_stock_chatbot
    ```

## Usage
1. Open your browser and navigate to `http://localhost:5000` if you use Docker to build your app.
2. Click in the development server link  `http://127.0.0.1:5000` if you run normal pip install and run.py.
3. Interact with the chatbot by asking questions about stock prices and market trends.

## Project Structure
![image](https://github.com/embiekhochiu/cinnamon_ai_stock_chatbot/assets/150108017/a21de0f8-0e66-4839-85cb-b1395c589f3a)


## Future Improvements
- **Add More Stock Data Sources**: Integrate additional APIs to provide more comprehensive stock data.
- **Enhanced NLP Capabilities**: Improve natural language processing for more accurate and diverse responses.
- **User Authentication**: Implement user authentication to personalize user experience and save user preferences.
- **Historical Data Analysis**: Provide insights and analysis based on historical stock data.
- **Web UI**: Enhance the front-end of the application web.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.


