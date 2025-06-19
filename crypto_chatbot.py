# crypto_chatbot.py

crypto_conversations = {
    "bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": "3/10"
    },
    "ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": "6/10"
    },
    "solana": {
        "price_trend": "volatile",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": "8/10"
    }
}

def give_investment_advice(crypto_name):
    crypto_name = crypto_name.lower()
    if crypto_name not in crypto_conversations:
        return "Sorry, I don't have information about that cryptocurrency."

    data = crypto_conversations[crypto_name]

    # Evaluate profitability
    if data["price_trend"] in ["rising", "stable"]:
        profitable = True
    else:
        profitable = False

    # Evaluate sustainability
    sustainable = data["energy_use"] == "low" or float(data["sustainability_score"].split("/")[0]) >= 6

    advice = f"{crypto_name.capitalize()} Info:\n"
    advice += f"• Price Trend: {data['price_trend']}\n"
    advice += f"• Market Cap: {data['market_cap']}\n"
    advice += f"• Energy Use: {data['energy_use']}\n"
    advice += f"• Sustainability Score: {data['sustainability_score']}\n\n"

    if profitable and sustainable:
        advice += "✅ Recommendation: Strong Buy – Profitable and Sustainable.\n"
    elif profitable:
        advice += "⚠️ Recommendation: Consider – Profitable but not very sustainable.\n"
    elif sustainable:
        advice += "⚠️ Recommendation: Consider – Sustainable but currently not very profitable.\n"
    else:
        advice += "❌ Recommendation: Avoid – Neither profitable nor sustainable.\n"

    return advice

# Chat loop
if __name__ == "__main__":
    while True:
        user_input = input("Ask about a crypto (or type 'exit' to quit): ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        print(give_investment_advice(user_input))
