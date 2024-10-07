import os
import tweepy
from datetime import datetime

# Cargar Bearer Token desde el archivo .env
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Autenticación e instanciación de Tweepy
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Fechas importantes de las elecciones en Uruguay
first_round_date = datetime(2024, 10, 27)  # Primera vuelta
second_round_date = datetime(2024, 11, 24)  # Segunda vuelta
departmental_election_date = datetime(2025, 5, 11)  # Elecciones departamentales

# Obtener fecha actual
today = datetime.now()

# Función para calcular los días restantes
def days_until(date):
    delta = date - today
    return delta.days

# Definir el tweet en función de la fecha actual
if today < first_round_date:
    days_left = days_until(first_round_date)
    tweet_text = f"Buen día! Faltan {days_left} días para la primera vuelta electoral en Uruguay 🇺🇾."
elif today < second_round_date:
    days_left = days_until(second_round_date)
    tweet_text = f"Buen día! Faltan {days_left} días para la segunda vuelta electoral en Uruguay 🇺🇾."
elif today < departmental_election_date:
    days_left = days_until(departmental_election_date)
    tweet_text = f"Buen día! Faltan {days_left} días para las elecciones departamentales en Uruguay 🇺🇾."
else:
    tweet_text = "No hay más elecciones programadas por ahora en Uruguay 🇺🇾."

# Función para enviar el tweet
def send_tweet(tweet_text):
    client.create_tweet(text=tweet_text)
    print("Tweet enviado correctamente.")

# Enviar el tweet
send_tweet(tweet_text)
