from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coin
from .serializers import CoinSerializer


class TopFiveCoinsView(APIView):

    def get(self, request):

        coins = Coin.objects.all()[:5]

        serializer = CoinSerializer(coins, many=True)
    
        return Response(serializer.data)






















# class TopFiveCoinsView(APIView):
#     def get(self, request):
#         # Set up the API request to CoinGecko
#         api_url = 'https://api.coingecko.com/api/v3/coins/markets'
#         params = {
#             'vs_currency': 'usd',
#             'order': 'market_cap_desc',
#             'per_page': 5,
#         }
#         response = requests.get(api_url, params=params)
#         if response.status_code == 200:
#             # If the request was successful, extract the coin data and save it to the database
#             data = response.json()
#             coins = []
#             for coin_data in data:
#                 coin, _ = Coin.objects.get_or_create(
#                     name=coin_data['name'],
#                     symbol=coin_data['symbol'].upper(),
#                 )
#                 coin.price = coin_data['current_price']
#                 coin.save()
#                 coins.append(coin)
#             # Serialize the coin data and return it in the response
#             # coins = get_coin()
#             serializer = CoinSerializer(coins, many=True)
#             return Response(serializer.data)
#         else:
#             # If the request failed, return an error response
#             return Response({'error': 'Failed to retrieve coin data from CoinGecko API.'}, status=response.status_code)
