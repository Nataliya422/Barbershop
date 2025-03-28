import os
from mistralai import Mistral
# from django.conf import settings  # Правильный способ импорта настроек Django
#from dotenv import load_dotenv
from promt import MISTRAL_REVIEW_PROMPT

import os
 
# load_dotenv()
 
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
MISTRAL_MODEL = os.getenv('MISTRAL_MODEL')
 
REVIEW = "Всё классно! Но кажется от Бородоча немного несло спиртом. Хотя ему можно простить, он же Бро. В целом рекомендую, если вас это не смущает"
 
PROMT = MISTRAL_REVIEW_PROMPT.format(review_text=REVIEW)
 
# Инициализация клиента
def check_review(review_text):
     # Инициализация клиента
     client = Mistral(api_key=MISTRAL_API_KEY)
     prompt = MISTRAL_REVIEW_PROMPT.format(review_text=review_text)
     chat_response = client.chat.complete(
         model=MISTRAL_MODEL,
         messages=[
             {
                 "role": "user",
                 "content": prompt
             }
         ]
     )
     response_text = chat_response.choices[0].message.content.lower()
     # Вывод в консоль ответа
     print(response_text)
     if "true" in response_text.lower():
         return True
     elif "false" in response_text.lower():
         return False
     else:
         return False