import os
from mistralai import Mistral
from django.conf import settings
from .promt import MISTRAL_REVIEW_PROMPT

def check_review(review_text):
    """
    Проверяет содержимое отзыва на корректность с помощью Mistral AI.
    
    Args:
        review_text (str): Текст отзыва для проверки
        
    Returns:
        bool: True если отзыв корректный, False если отзыв нарушает правила
    """
    # Получаем ключи из настроек Django
    api_key = settings.MISTRAL_API_KEY
    model = settings.MISTRAL_MODEL
    
    # Проверяем наличие ключа API
    if not api_key:
        print("ОШИБКА: Отсутствует ключ API Mistral. Модерация отзывов недоступна.")
        return False
    
    try:
        # Инициализация клиента
        client = Mistral(api_key=api_key)
        
        # Форматируем промпт с текстом отзыва
        prompt = MISTRAL_REVIEW_PROMPT.format(review_text=review_text)
        
        # Отправляем запрос к API
        chat_response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Получаем ответ и приводим к нижнему регистру
        response_text = chat_response.choices[0].message.content.lower()
        
        # Выводим результат для отладки
        print(f"Результат проверки отзыва: {response_text}")
        
        # Простая проверка наличия слова "true" в ответе
        return "true" in response_text
        
    except Exception as e:
        print(f"Ошибка при модерации отзыва: {str(e)}")
        return False  # В случае ошибки считаем отзыв некорректным