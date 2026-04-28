import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Дозволяємо запити з усіх джерел (важливо, якщо фронтенд на іншому хостингу)
CORS(app)

def generate_response(message):
    msg = message.lower()

    # FAQ
    if "доставка" in msg:
        return "Доставка займає 1–3 дні по Україні 🚚"
    
    if "оплата" in msg:
        return "Можлива оплата картою або при отриманні 💳"

    if "повернення" in msg:
        return "Повернення можливе протягом 14 днів за чеком."

    # Поради по техніці
    if "ноутбук" in msg:
        return "Рекомендую ноутбук з мінімум 8–16 ГБ ОЗП та SSD. Для ігор — бажано відеокарта NVIDIA."

    if "пк" in msg or "комп'ютер" in msg:
        return "Для ПК зверни увагу на процесор (i5/Ryzen 5), 16 ГБ ОЗП і SSD."

    if "монітор" in msg:
        return "Для роботи краще IPS-матриця, для ігор — висока герцовка (144 Гц+)."

    # Пояснення термінів
    if "ssd" in msg:
        return "SSD — це швидкий накопичувач. Він значно швидший за HDD."

    if "hdd" in msg:
        return "HDD — це звичайний жорсткий диск. Повільніший, але дешевший."

    if "озп" in msg or "ram" in msg:
        return "ОЗП — це оперативна пам'ять. Впливає на швидкість роботи програм."

    # Порівняння
    if "i5" in msg and "i7" in msg:
        return "i7 потужніший, але дорожчий. Для ігор і роботи часто вистачає i5."

    # Навігація
    if "де знайти" in msg or "категорії" in msg:
        return "Подивись розділи: ноутбуки, ПК, монітори, комплектуючі."

    # fallback
    return "Цікаве питання 🤔 Я ще вчуся, але можу допомогти з вибором техніки або поясненням термінів!"

@app.route('/')
def home():
    return "API чат-бота працює."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400
    
    user_message = data.get('message', '').strip()
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400

    response = generate_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    # Отримання порту від хостингу або використання 5000 за замовчуванням
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)