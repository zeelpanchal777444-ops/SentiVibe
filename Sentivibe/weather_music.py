# import requests

# API_KEY = "27133e6f4228230521c4f4b1210e7f70"

# def get_weather(city):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#     response = requests.get(url).json()
#     if response.get("main"):
#         return response["weather"][0]["main"]
#     return None

# def recommend_song(city):
#     weather = get_weather(city)
#     if not weather:
#         return "City not found!"
    
#     if weather in ["Rain", "Drizzle"]:
#         return "Rainy Mood - Lo-fi Beats"
#     elif weather in ["Clear"]:
#         return "Sunny Vibes - Happy Pop"
#     elif weather in ["Clouds"]:
#         return "Cloudy Thoughts - Chill Acoustic"
#     else:
#         return "Explore something new 🎧"


# import requests

# def recommend_song(city):
#     api_key = "27133e6f4228230521c4f4b1210e7f70"  # apna OpenWeatherMap API key yahan daalo
#     base_url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {"q": city, "appid": api_key, "units": "metric"}

#     response = requests.get(base_url, params=params)
#     data = response.json()

#     if data.get("cod") != 200:
#         return "<span style='color:red;'>❌ City not found. Please enter a valid city name.</span>"

#     city_name = data["name"]
#     country = data["sys"]["country"]
#     temp = data["main"]["temp"]
#     feels_like = data["main"]["feels_like"]
#     humidity = data["main"]["humidity"]
#     pressure = data["main"]["pressure"]
#     wind = data["wind"]["speed"]
#     description = data["weather"][0]["description"].capitalize()

#     # 🌤️ Weather Info Display
#     weather_details = f"""
#     <div style='background-color:#1e293b; padding:15px; border-radius:10px; color:#f8fafc;'>
#     🌍 <b>{city_name}, {country}</b><br>
#     🌡️ <b>{temp}°C</b><br>
#     {description}<br>
#     Feels like: {feels_like}°C | Humidity: {humidity}%<br>
#     Pressure: {pressure} hPa | Wind: {wind} m/s
#     </div><br>
#     """

#     # 🎵 Song Recommendation
#     if "rain" in description.lower():
#         song = "💧 Mood: Rainy — Try listening to *'Let Her Go - Passenger'*"
#     elif "clear" in description.lower():
#         song = "☀️ Mood: Clear — Try *'Happy - Pharrell Williams'*"
#     elif "cloud" in description.lower():
#         song = "☁️ Mood: Cloudy — Try *'Perfect - Ed Sheeran'*"
#     elif "snow" in description.lower():
#         song = "❄️ Mood: Snowy — Try *'Let It Go - Idina Menzel'*"
#     else:
#         song = "🎶 Mood: Calm — Try *'Viva La Vida - Coldplay'*"

#     return weather_details + f"<b>{song}</b>"

import requests

def recommend_song(city):
    api_key = "27133e6f4228230521c4f4b1210e7f70"  # 🔑 Your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("cod") != 200:
        return "<span style='color:red;'>❌ City not found. Please enter a valid city name.</span>"

    # Weather details
    city_name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    description = data["weather"][0]["description"].capitalize()

    # 🌤️ Weather Info Display
    weather_details = f"""
    <div style='background-color:#0f172a; padding:20px; border-radius:12px; color:#f1f5f9; font-family:Arial;'>
        <h3 style='margin-bottom:10px;'>🌍 {city_name}, {country}</h3>
        <p style='margin:5px 0;'>🌡️ <b>{temp}°C</b> — {description}</p>
        <p style='margin:5px 0;'>Feels like: {feels_like}°C | Humidity: {humidity}%</p>
        <p style='margin:5px 0;'>Pressure: {pressure} hPa | Wind: {wind} m/s</p>
    </div><br>
    """
    

    # 🎵 Spotify Playlist (Based on Weather)
    desc = description.lower()
    playlist = ""  # define upfront to avoid undefined error
    if "rain" in desc:
        mood = "Rainy ☔"
        spotify_embed = """<iframe style="border-radius:0px" src="https://open.spotify.com/embed/playlist/4Z75ud0NOTZdTsXDrncRMs" width="100%" height="500" frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>"""
    elif "clear" in desc:
        mood = "Sunny ☀️"
        spotify_embed = """<iframe style="border-radius:0px" src="https://open.spotify.com/embed/playlist/5wTgcA955Vw5gr2GYVfOiz" width="100%" height="500" frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>"""
    elif "cloud" in desc:
        mood = "Cloudy ☁️"
        spotify_embed = """<iframe style="border-radius:0px" src="https://open.spotify.com/embed/playlist/7A9jHInfzazASpSQJAAc3q" width="100%" height="500" frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>"""
    elif "snow" in desc:
        mood = "Snowy ❄️"
        spotify_embed = """<iframe style="border-radius:0px" src="https://open.spotify.com/embed/playlist/6n2AkbIgFvDOmSRvD6Y1Tf" width="100%" height="500" frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>"""
    elif "old" in desc:
        mood = "Old"
        spotify_embed = """<iframe style="border-radius:0px" src="https://open.spotify.com/embed/playlist/12wqIOTHSGGwuY0aym8SCj" width="100%" height="500" frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>"""
    else:
        mood = "Calm 🌙"
        spotify_embed = """<iframe style="border-radius:0px" src="https://open.spotify.com/embed/playlist/5dmsqv3k1gh6ZO2AGe2H4q" width="100%" height="500" frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>"""


    return f"{weather_details}<h4 style='color:#f8fafc;'>🎶 Mood: {mood}</h4><br>{spotify_embed}"




















# import requests

# def recommend_song(city):
#     api_key = "27133e6f4228230521c4f4b1210e7f70"  # 🔑 Your OpenWeatherMap API Key
#     base_url = "https://api.openweathermap.org/data/2.5/weather"
#     params = {"q": city, "appid": api_key, "units": "metric"}

#     response = requests.get(base_url, params=params)
#     data = response.json()

#     if data.get("cod") != 200:
#         return "<span style='color:red;'>❌ City not found. Please enter a valid city name.</span>"

#     # 🌤️ Weather Info
#     city_name = data["name"]
#     country = data["sys"]["country"]
#     temp = data["main"]["temp"]
#     feels_like = data["main"]["feels_like"]
#     humidity = data["main"]["humidity"]
#     pressure = data["main"]["pressure"]
#     wind = data["wind"]["speed"]
#     description = data["weather"][0]["description"].capitalize()

#     # 🌍 Display Weather Box
#     weather_details = f"""
#     <div style='background-color:#0f172a; padding:20px; border-radius:12px; color:#f1f5f9; font-family:Arial;'>
#         <h3>🌍 {city_name}, {country}</h3>
#         <p>🌡️ <b>{temp}°C</b> — {description}</p>
#         <p>Feels like: {feels_like}°C | Humidity: {humidity}%</p>
#         <p>Pressure: {pressure} hPa | Wind: {wind} m/s</p>
#     </div><br>
#     """

#     # 🎧 Hindi Spotify Playlists Based on Weather
#     desc = description.lower()
#     playlist = ""  # ✅ define upfront to avoid undefined error

#     if "rain" in desc:
#         mood = "Romantic Rainy Vibes ☔💞"
#         playlist = "https://open.spotify.com/embed/playlist/6b2CzxPUQx6XJtskeMisZM"  # Hindi Rain Songs
#     elif "clear" in desc:
#         mood = "Happy Sunshine ☀️🎉"
#         playlist = "https://open.spotify.com/embed/playlist/5Z7rLI5ny52UBbZ0FcN4Gz"  # Happy Hindi Vibes
#     elif "cloud" in desc:
#         mood = "Relaxed Cloudy Mood ☁️😌"
#         playlist = "https://open.spotify.com/embed/playlist/37i9dQZF1DWYcDQ1hSjOpY"  # Chill Bollywood Mix
#     elif "snow" in desc:
#         mood = "Soft Romantic Snow ❄️❤️"
#         playlist = "https://open.spotify.com/embed/playlist/6LrEOf1k1qfYw3Eqx8eT2V"  # Romantic Hindi Olds
#     else:
#         mood = "Night Calm LoFi 🌙🎧"
#         playlist = "https://open.spotify.com/embed/playlist/4gxuPYmVMDK2cE6i7OZTZC"  # Hindi LoFi Vibes

    # # 🎵 Spotify Embed Player
    # spotify_embed = f"""
    # <iframe style="border-radius:12px" src="{playlist}" width="100%" height="380"
    # frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
    # """

    # return f"{weather_details}<h4 style='color:#f8fafc;'>🎶 Mood: {mood}</h4><br>{spotify_embed}"
