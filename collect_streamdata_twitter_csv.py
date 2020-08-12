
import tweepy as tw        
import json
import csv
from datetime import date
from datetime import datetime
import time
import pandas as pd

"""#Criandos classe para manipular o Stream"""

class MyStreamListener(tw.StreamListener):
      
    def on_status(self, status):
    	with open('OutputTeste.txt', 'a', encoding='utf-8') as f:
    		writer = csv.writer(f)
            if not tweet['retweeted']:
                if 'extended_tweet' in status._json:
                    print ("extended")
                    print(status.created_at, status.user.screen_name, status.extended_tweet['full_text'], status.coordinates, status.geo, status.user.location)
                    writer.writerow([status.created_at, status.user.screen_name, status.extended_tweet['full_text'], status.coordinates, status.geo, status.user.location])
                else:
                    print(status.text)
                    writer.writerow([status.created_at, status.user.screen_name, status.text, status.coordinates, status.geo, status.user.location])
        	
    
    def on_error(self, status):
    	print("erro")

"""#Conectando na API do Twitter"""

#Ler as chaves de um json
secrets = json.loads(open('./chaves.json').read())
api_key = secrets['api_key']
api_secret_key = secrets['api_secret_key']
access_token = secrets['access_token']
access_token_secret = secrets['access_token_secret']
# Conectar no Twitter
auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

myStreamListener = MyStreamListener()

myStream = tw.Stream(auth=api.auth, listener=myStreamListener, tweet_mode='extended')
myStream.filter(track=['aborto', 'educação sexual', 'ideologia de genero', 'casamento gay', 'homossexuais', 'mudança de sexo', 'prostituição', 'cotas', 'cotas raciais', 'sistemas de cotas'], languages=["pt"], is_async=True)

