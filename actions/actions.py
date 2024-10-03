import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionGetExchangeRate(Action):

    def name(self) -> str:
        return "action_get_exchange_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        # Get the base and target currencies from the user's message
        base_currency = tracker.get_slot("base_currency")
        target_currency = tracker.get_slot("target_currency")
        
        # Ensure the currencies are in uppercase
        base_currency = base_currency.upper()
        target_currency = target_currency.upper()
        
        url = f"https://v6.exchangerate-api.com/v6/658908509add4f1771174b54/latest/{base_currency}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            rates = data['conversion_rates']
            
            if target_currency and target_currency in rates:
                rate = rates[target_currency]
                message = f"The current {base_currency} to {target_currency} exchange rate is: {rate}"
            else:
                # Provide all exchange rates if the target currency is not found
                rate_list = "\n".join([f"{currency}: {rate}" for currency, rate in rates.items()])
                message = f"Here are the current exchange rates for {base_currency}:\n{rate_list}"
        else:
            message = "Sorry, I couldn't fetch the exchange rates at the moment."

        dispatcher.utter_message(text=message)
        return []

