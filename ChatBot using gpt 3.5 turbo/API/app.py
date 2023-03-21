from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# OpenAI API anahtarını burada ayarlayın
openai.api_key = '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'

# OpenAI API'ye gönderilecek varsayılan motor ayarları
engine = 'davinci-codex'

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# API çağrısı işleyicisi
@app.route('/api', methods=['POST'])
def api():
    # İstemci tarafından gönderilen mesajı al
    message = request.json.get('message')

    # OpenAI API'ye gönderilen mesajı hazırla
    prompt = f'User: {message}\nBot:'

    # OpenAI API'ye istek gönder
    response = openai.Completion.create(
        prompt=prompt,
        engine=engine,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Yanıtı geri döndür
    if response.choices[0].text.strip() == '':
        return 'Bot: İşlem tamam!'
    else:
        return 'Bot: ' + response.choices[0].text.strip()

# Flask uygulamasını çalıştır
if __name__ == '__main__':
    app.run()
