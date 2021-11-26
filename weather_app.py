from flask import Flask, request, render_template
from weather import local_request
from datetime import datetime
print('Xoce')

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    weather_pic = ['cloud_and_snow', 'cloud_rain', 'sun_and_cloud', 'sun', 'wind']
    r_city = request.form.get('r_city')
    weather_file = local_request(r_city)
    try:
        city = weather_file['name']
        temp = weather_file['main']['temp']
        description = weather_file['weather'][0]['description']
    except KeyError:
        city = 'None'
        temp = 0
        description = 'None'
    timestamp = datetime.today().strftime('%h %d %H:%M')
    pic_for_weather = weather_pic[0]
    if temp <= 0:
        pic_for_weather = weather_pic[0]
    elif temp > 0 and temp <= 5:
        pic_for_weather = weather_pic[1]
    elif temp >= 5 and temp <= 10:
        pic_for_weather = weather_pic[4]
    elif temp >= 15 and temp <= 25:
        pic_for_weather = weather_pic[2]
    elif temp > 25:
        pic_for_weather = weather_pic[3]

    return render_template(
    'index.html', 
    city=city, 
    temp=temp, 
    weather_pic=pic_for_weather, 
    timestamp=timestamp,
    description=description.upper()
    )




app.run(debug=True)