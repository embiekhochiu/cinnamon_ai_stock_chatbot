import os
from flask import Blueprint, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import requests
from . import db
from .models import UserInput

load_dotenv()

main = Blueprint('main', __name__)

api_key = os.getenv("OPENAI_API_KEY")
stock_api_key = os.getenv("STOCK_API_KEY")

client = OpenAI(
    api_key=api_key
)

def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    try:
        time_series = data["Time Series (5min)"]
        formatted_data = "Time Series (5min):\n"
        for time, values in time_series.items():
            formatted_data += (
                f"Time: {time}\n"
                f"Close: {values['4. close']}\n"
                f"Volume: {values['5. volume']}\n\n"
            )
        return formatted_data
    except KeyError:
        return None


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']

    # Check if the user is asking for a stock price
    if user_input.lower().startswith("price of"):
        symbol = user_input.split()[-1].upper()
        price = get_stock_price(symbol)
        if price:
            response_text = f"The current price of {symbol} is {price}."
        else:
            response_text = f"Sorry, I couldn't fetch the price for {symbol}."
    else:
        try:
        # Provide context for stock-related queries
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert knowledgeable in stocks."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150
            )
        
            response_text = response.choices[0].text.strip()
        except Exception as e:
            response_text = "Failed due to rate limit from OpenAI API."


    # Save user input and response to the database
    new_input = UserInput(user_input=user_input, response=response_text)
    db.session.add(new_input)
    db.session.commit()

    return jsonify({'response': response_text})
