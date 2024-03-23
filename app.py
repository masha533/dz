from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/result', methods=['POST'])
def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7c729a371ae49b524a406fc8113c01329'
    response = requests.get(url)
    data = response.json()
    #weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    return weather, temperature

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        temperature = get_weather(city)
        message = f'опа, {name}! Сейчас в городе {city} температура {temperature}°C.'
        return render_template('index.html', message=message)
    return render_template('index.html', message=None)

@app.errorhandler(404)
def pageNotFount(error):
    return ('Такой страницы еще нет, приходите позже.Зайдите в погоду и посмотрите температуру сами,тк я не понимаю, что не так и как пофиксить;( ')
if __name__ == '__main__':
    app.run(debug=True)
