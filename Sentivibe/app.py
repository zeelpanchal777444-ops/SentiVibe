# ---------------------------------------------------------------------------------------------


import streamlit as st
from mood_detection import detect_mood
from weather_music import recommend_song
from cyberbullying import check_cyberbullying
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import datetime
import geocoder
import itertools


st.set_page_config(page_title="Live mood-weather...", page_icon="🌦️", layout="centered")

# Auto detect location
g = geocoder.ip('me')
city = g.city

# Weather API
API_KEY = "27133e6f4228230521c4f4b1210e7f70"   # ← yaha apni openweather API key daal do
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url).json()

temperature = response["main"]["temp"]
condition = response["weather"][0]["description"].title()
humidity = response["main"]["humidity"]
wind = response["wind"]["speed"]

# Real-time date & time
now = datetime.datetime.now()
date_today = now.strftime("%A, %d %B %Y")
time_now = now.strftime("%I:%M %p")



# Load environment variables

load_dotenv()

print("Client ID:", os.getenv("e46091b40ee843f99ac1dcedda1f4248"))
print("Client Secret:", os.getenv("3f57eef5c98e4d4e907366d7629fe5d2"))
print("Redirect URI:", os.getenv("https://localhost:8888/callback"))

# ------------html-----------
def local_html(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            html_content = f.read()
            st.markdown(html_content, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("HTML file not found.")

    local_html("sentivibe.html")



# --- Load custom CSS --

def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

local_css("style.css")

#------weather---------------------------

def get_weather(lat, lon):
    api_key = "27133e6f4228230521c4f4b1210e7f70"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    return requests.get(url).json()


# --- App Title ---

st.markdown("<h1 style='text-align:center; margin-top: 2rem;'>🎧 Sentivibe - AI Emotion Assistant</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)




# ------------------------------------------------
import streamlit.components.v1 as components


# --- Sidebar Menu ---

menu = ["🏠 Home", "😊 Mood Detection", "🎵 Weather Detection", "🚨 Cyberbullying","Spotify Mood Player"]
choice = st.sidebar.selectbox("Navigation", menu)

# --- HOME ---

if choice == "🏠 Home":
    st.header("Welcome to Sentivibe 💜")
    st.write("An AI-powered app that detects your mood, recommends songs, and ensures cyber safety.")
    
    st.markdown("""
    <style>
        .wave {
            animation-name: wave-animation;
            animation-duration: 2.5s;
            animation-iteration-count: infinite;
            transform-origin: 70% 70%;
            display: inline-block;
            font-size: 60px;
        }

        @keyframes wave-animation {
            0% { transform: rotate(0deg); }
            10% { transform: rotate(14deg); }
            20% { transform: rotate(-8deg); }
            30% { transform: rotate(14deg); }
            40% { transform: rotate(-4deg); }
            50% { transform: rotate(10deg); }
            60% { transform: rotate(0deg); }
            100% { transform: rotate(0deg); }
        }
    </style>

    <h2 style="text-align:center;">
        <span class="wave">👋</span> Welcome Khushi!
    </h2>
""", unsafe_allow_html=True)
    
    #----------------------------------------------------------
    
    # Weather Widget HTML
    st.markdown(
    f"""
    <style>
        .weather-card {{
            padding:25px;
            background:#1e293b;
            border-radius:2px;
            border:solid #00ffe7;
            width:470px;
            margin:auto;
            color:white;
            text-align:center;
            box-shadow:0px 0px 20px rgba(0,0,0,0.5);
            font-family: Arial;
            margin-bottom:3rem;
        }}
    </style>

    <div class="weather-card">
        <h2>📍 {city}</h2>
        <p style="opacity:0.7; margin-top:-10px;">{date_today}</p>
        <p style="margin-top:-15px; opacity:0.7;">⏰ {time_now}</p>
        <h2 style="font-size:60px;">{int(temperature)}°C -- {condition}</h2>
        <div style="display:flex; justify-content:space-between; margin-top:25px;">
            <div>
                <h2 style="margin:0;">💧 Humidity</h2>
                <p>{humidity}%</p>
            </div>
            <div>
                <h2 style="margin:0;">💨 Wind</h2>
                <p>{wind} m/s</p>
            </div>
        </div>
        
    </div>
    
    """,
    unsafe_allow_html=True
)

#------------------------------------------

#     mood_emojis = {
#     "happy": "<span class='bounce'>😁</span>",
#     "sad": "<span class='shake'>😢</span>",
#     "romantic": "<span class='heart'>💗</span>",
#     "angry": "<span class='shake-hard'>😡</span>",
#     "calm": "<span class='slow'>😌</span>",
#     "energetic": "<span class='glow'>⚡</span>",
#     "fear": "<span class='shake'>😨</span>",
#     "neutral": "<span class='slow'>🙂</span>",
#     "unknown": "<span class='slow'>🙂</span>"
# }

#---------------------------------------------
#     st.markdown("""
# <style>

# .bounce { display:inline-block; animation:bounce 1s infinite; }
# @keyframes bounce {
#   0%{transform:translateY(0);}
#   50%{transform:translateY(-12px);}
#   100%{transform:translateY(0);}
# }

# .shake { display:inline-block; animation:shake 0.5s infinite; }
# @keyframes shake {
#   0%{transform:translateX(0);}
#   50%{transform:translateX(-4px);}
#   100%{transform:translateX(0);}
# }

# .shake-hard { display:inline-block; animation:shakehard 0.3s infinite; }
# @keyframes shakehard {
#   0%{transform:translateX(0);}
#   50%{transform:translateX(-8px);}
#   100%{transform:translateX(0);}
# }

# .slow { display:inline-block; animation:slowblink 2s infinite; }
# @keyframes slowblink {
#   0%{opacity:1;}
#   50%{opacity:0.4;}
#   100%{opacity:1;}
# }

# .glow { display:inline-block; animation:glow 1.5s infinite; }
# @keyframes glow {
#   0%{filter:brightness(100%);}
#   50%{filter:brightness(150%);}
#   100%{filter:brightness(100%);}
# }

# .heart { display:inline-block; animation:beat 1s infinite; }
# @keyframes beat {
#   0%{transform:scale(1);}
#   50%{transform:scale(1.3);}
#   100%{transform:scale(1);}
# }

# </style>
# """, unsafe_allow_html=True)

#-----------------------------------------------------
#     st.markdown("<h2 style='text-align:center;'>🎵 Featured Playlists</h2>", unsafe_allow_html=True)
    
# # Playlist Data
#     playlists = {
#     "Bollywood": {
#         "img": "data:image/jpeg;base64,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",
#         "link":"https://open.spotify.com/embed/playlist/2Kj5NUtVetggUDHPIGC9U7"
#     },
#     "Romantic": {
#         "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMFDbulrkSnuzZ1nREkVY4yR1d3cG6IxwEGw&s",
#         "link":"https://open.spotify.com/embed/playlist/0zc6Hq9OIAengtGG6a3lfs"
#     },
#     "Sad": {
#         "img": "data:image/jpeg;base64,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",
#         "link":"https://open.spotify.com/embed/playlist/37i9dQZF1DXdFesNN9TzXT"
#     },
#     "Old": {
#         "img": "data:image/jpeg;base64,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",
#         "link": "https://open.spotify.com/embed/playlist/32xf01Q2px9Xr8FxBtKtaz"
#     },
   
# }

# # Default state
# if "open_card" not in st.session_state:
#     st.session_state["open_card"] = None

# # 4 columns
# cols = st.columns(4, gap="small")


# # Display cards
# for i, (title, data) in enumerate(playlists.items()):
#     with cols[i]:
#         # Card container with clickable effect
#         if st.button(
#             f"{title}",
#             key=title,
#             help="Click to open playlist",
#             use_container_width=True
#         ):
#             # Toggle logic
#             if st.session_state["open_card"] == title:
#                st.session_state["open_card"] = title
#             else:
#                 st.session_state["open_card"] = title

#         # Card image
#         st.markdown(
#             f"""
#             <div style='text-align:center; margin-top:5px;'>
#                 <img src='{data["img"]}' style='width:80px; height:80px; border-radius:1px;'>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
        

#         # Playlist inside the card
# if st.session_state["open_card"] == title:
#             st.markdown(
#                 f"""
#                 <iframe src="{data['link']}"
#                 width="100%" height="170" frameborder="0"
#                 allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture">
#                 </iframe>
#                 """,
#                 unsafe_allow_html=True
#             )

            
        
           
# --- MOOD DETECTION ---
elif choice == "😊 Mood Detection":
    st.header("🎭 Mood Detection")
    text = st.text_area("Write something to detect your mood:")
    if st.button("Analyze Mood"):
        mood = detect_mood(text)
        st.success(f"Detected Mood: {mood}")


# --- WEATHER + SONGS ---

elif choice == "🎵 Weather Detection":
    st.header("🌤️ Weather Detection")
    city = st.text_input("Enter your city name:")
    if st.button("Song Suggestion"):
        result = recommend_song(city)
        st.markdown(result, unsafe_allow_html=True)


# --- CYBERBULLYING DETECTION ---

elif choice == "🚨 Cyberbullying":
    st.header("🚫 Cyberbullying Detector")
    comment = st.text_area("Enter a message or comment:")
    if st.button("Check Bullying"):
        result = check_cyberbullying(comment)
        st.warning(result)


# --- Spotify Mood Player ---

elif choice == "Spotify Mood Player":
    st.header("🎵 Spotify Mood Based Songs")

    # Spotify Authentication
    scope = "user-read-playback-state,user-modify-playback-state,user-read-currently-playing,user-read-private"
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("e46091b40ee843f99ac1dcedda1f4248"),
    client_secret=os.getenv("3f57eef5c98e4d4e907366d7629fe5d2"),
    redirect_uri=os.getenv("https://localhost:8888/callback"),
    scope=scope
))
    # Mood Selection
    mood = st.selectbox("Select your mood:", ["Happy 😊","Happy 2 😄", "Sad 😢", "Sad 2 😔", "Romantic 💞","Romantic 2 ❤️", "Relaxed 😌", "Relaxed 2 🌿", "Energetic 💃","Energetic 2 🕺","Retro 🎙️"])

    # Playlist Mapping
    mood_playlists = {

    "Happy 😊": "https://open.spotify.com/playlist/37i9dQZF1DWTwbZHrJRIgD",  # Happy Vibes
    "Happy 2 😄": "https://open.spotify.com/playlist/6YAW8Q4YPBL1obegSiARTU",  # Happy Songs Everyone Knows

    "Sad 😢": "https://open.spotify.com/playlist/37i9dQZF1DXdFesNN9TzXT",    # Sad Hindi
    "Sad 2 😔": "https://open.spotify.com/playlist/37i9dQZF1DXdpQPPZq3F7n",    # Melancholic Hindi

    "Romantic 💞": "https://open.spotify.com/playlist/5H7rJxaxGIVot0dhZccwHz", # Romantic Hindi
    "Romantic 2 ❤️": "https://open.spotify.com/playlist/37i9dQZF1DWX76Z8XDsZzF", # Bollywood Love Songs

    "Energetic 💃": "https://open.spotify.com/playlist/37i9dQZF1DX6XE7HRLM75P",  # Dance Bollywood Beats
    "Energetic 2 🕺": "https://open.spotify.com/playlist/3mSm688yR6UeaAJNf93Ydr",  # Hindi Soothing Songs

    "Relaxed 😌": "https://open.spotify.com/playlist/37i9dQZF1DWYRTlrhMB12D",  # Old is Gold
    "Relaxed 2 🌿": "https://open.spotify.com/playlist/37i9dQZF1DX14CbVHtvHRB",  # Hindi Soothing Songs
    
    "Retro 🎙️": "https://open.spotify.com/playlist/13nDKYo4AcyODMGNARWNzZ",  # Lofi + Old Songs
    }

  
    if st.button("Play Songs 🎶"):
     playlist_url = mood_playlists[mood]
     st.success(f"Now playing songs for your mood: **{mood}**")

     st.markdown(f"""
     <iframe src="https://open.spotify.com/embed/playlist/{playlist_url.split('/')[-1]}"
     width="100%" height="400" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
     <br>
     <a href="{playlist_url}" target="_blank" style="color:white; text-decoration:none; font-weight:bold;">
     🎧 Open Full Playlist on Spotify
     </a>
     """, unsafe_allow_html=True)
