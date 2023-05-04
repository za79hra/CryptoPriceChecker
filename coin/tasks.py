from celery import shared_task, Celery
from .models import Coin
import requests
# app =Celery('coin', broker='redis://redis:6000/0')

@shared_task
# @app.tasks()
def update_coins():
    # Set up the API request to CoinGecko
    api_url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 5,
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        # If the request was successful, extract the coin data and save it to the database
        data = response.json()
        coins = []
        for coin_data in data:
            coin, _ = Coin.objects.get_or_create(
                name=coin_data['name'],
                symbol=coin_data['symbol'].upper(),
            )
            coin.price = coin_data['current_price']
            coin.save()
            coins.append(coin)
        print(f'Updated {len(coins)} coins.')
    else:
        # If the request failed, log an error message
        print('Failed to retrieve coin data from CoinGecko API.')
