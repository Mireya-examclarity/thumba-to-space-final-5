
import streamlit as st
import datetime
import math
import requests
import urllib.parse

# ============================================================
# THUMBA TO SPACE 🚀
# Streamlit Space Experience
# ============================================================

st.set_page_config(
    page_title="Thumba to Space",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CONFIG
# ============================================================

NASA_API_KEY = "DEMO_KEY"

APOD_URL = (
    f"https://api.nasa.gov/planetary/apod"
    f"?api_key={NASA_API_KEY}"
)

ISS_URL = "http://api.open-notify.org/iss-now.json"

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 20% 20%, #171744 0%, transparent 30%),
        radial-gradient(circle at 80% 10%, #101040 0%, transparent 25%),
        linear-gradient(180deg, #000000 0%, #05051a 45%, #10102d 100%);
    color: white;
}

html {
    scroll-behavior: smooth;
}

h1, h2, h3, h4, h5, h6,
p, div, label, span {
    color: white !important;
}

.hero {
    padding: 45px 20px;
    text-align: center;
    border-radius: 25px;
    background:
        linear-gradient(135deg,
        rgba(30,30,80,.95),
        rgba(0,0,0,.95));
    border: 1px solid rgba(255,255,255,.15);
    box-shadow: 0 0 50px rgba(75,80,255,.2);
    margin-bottom: 30px;
}

.hero-title {
    font-size: 60px;
    font-weight: 900;
    letter-spacing: 2px;
}

.hero-subtitle {
    font-size: 22px;
    color: #b9c7ff !important;
}

.space-card {
    background: rgba(255,255,255,.06);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 20px;
    padding: 22px;
    margin: 10px 0;
    box-shadow: 0 10px 30px rgba(0,0,0,.25);
}

.glow {
    text-shadow:
        0 0 5px #fff,
        0 0 10px #7aa2ff,
        0 0 20px #536dfe;
}

.big-number {
    font-size: 45px;
    font-weight: 800;
}

.groot-container {
    text-align: center;
    padding: 25px;
    border-radius: 25px;
    background: linear-gradient(
        180deg,
        rgba(30,60,40,.4),
        rgba(5,20,10,.8)
    );
    border: 1px solid rgba(100,255,150,.2);
}

.timeline {
    padding: 20px;
    border-left: 4px solid #536dfe;
    background: rgba(255,255,255,.04);
    border-radius: 10px;
}

.footer {
    text-align: center;
    color: #8890b5 !important;
    padding: 40px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

@st.cache_data(ttl=3600)
def get_apod():

    try:
        response = requests.get(APOD_URL, timeout=10)

        if response.status_code == 200:
            return response.json()

    except Exception:
        pass

    return None


def get_iss():

    try:
        response = requests.get(ISS_URL, timeout=10)

        if response.status_code == 200:
            return response.json()

    except Exception:
        pass

    return None


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="hero-title glow">
🚀 THUMBA TO SPACE
</div>

<div class="hero-subtitle">
From Thiruvananthapuram to the Stars 🌌
</div>

<p>
A journey through India's space story — from the small coastal
village of Thumba to the Moon, Mars and beyond.
</p>

<div style="font-size:65px;">
🇮🇳 🚀 🌍 🌙 🛰️ ⭐
</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# QUICK NAVIGATION
# ============================================================

st.markdown("""
<div style="text-align:center">

### 🧭 Mission Navigation

</div>
""")

n1, n2, n3, n4, n5 = st.columns(5)

with n1:
    st.markdown("🚀 **Launch**")

with n2:
    st.markdown("🛰️ **ISS**")

with n3:
    st.markdown("🌙 **Moon**")

with n4:
    st.markdown("🔴 **Mars**")

with n5:
    st.markdown("🌱 **Kuttan**")


# ============================================================
# COUNTDOWN
# ============================================================

st.divider()

st.header("⏱️ Next Mission Countdown")

next_launch = datetime.datetime(2026, 9, 15, 10, 30)

now = datetime.datetime.now()

diff = next_launch - now

if diff.total_seconds() > 0:

    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60

else:

    days = 0
    hours = 0
    minutes = 0

c1, c2, c3, c4 = st.columns(4)

c1.metric("Days", days)
c2.metric("Hours", hours)
c3.metric("Minutes", minutes)
c4.metric("Mission", "Gaganyaan")


# ============================================================
# THUMBA HISTORY
# ============================================================

st.divider()

st.header("🇮🇳 The Beginning — Thumba")

st.markdown("""
<div class="space-card">

<h3>21 November 1963</h3>

<p>
India's early sounding-rocket programme began at Thumba,
near Thiruvananthapuram, Kerala.
</p>

<p>
The location was selected because of its proximity to the
magnetic equator, making it scientifically valuable for
atmospheric and geophysical experiments.
</p>

</div>
""", unsafe_allow_html=True)

a, b = st.columns(2)

with a:

    st.subheader("🚲 The Bicycle Story")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/"
        "3/3f/Vikram_Sarabhai.jpg/"
        "800px-Vikram_Sarabhai.jpg",
        caption="Dr. Vikram Sarabhai",
        use_container_width=True
    )

    if st.button("📖 Hear the Story"):

        st.info(
            "India's early rocket programme worked with extremely "
            "limited infrastructure. Equipment and rocket components "
            "were famously transported manually."
        )


with b:

    st.subheader("⛪ Church & Control Room")

    st.markdown("""
    <div style="
        font-size:100px;
        text-align:center;
        padding:40px;
        background:linear-gradient(#101040,#03030b);
        border-radius:25px;">
        ⛪📡🚀
    </div>
    """, unsafe_allow_html=True)

    st.write(
        "The St. Mary Magdalene Church at Thumba became associated "
        "with India's early space programme."
    )


# ============================================================
# ROCKET BUILDER
# ============================================================

st.divider()

st.header("🚀 Kilimanoor Rocket Builder")

name = st.text_input(
    "Enter your name:",
    placeholder="Commander..."
)

power = st.slider(
    "Launch Power",
    0,
    100,
    75
)

st.progress(power)

if st.button("🔥 LAUNCH FROM THUMBA"):

    if name:

        st.balloons()

        st.success(
            f"🚀 Commander {name}, your rocket has launched!"
        )

        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:90px;
                padding:30px;">
                🚀
                <br>
                <span style="font-size:25px;">
                THUMBA → SPACE
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.warning("Enter your name first!")


# ============================================================
# MISSION CONTROL
# ============================================================

st.divider()

st.header("🛰️ Mission Control")

mission = st.slider(
    "Launch System Power",
    0,
    100,
    75
)

st.progress(mission)

if mission >= 90:
    st.success("🔥 ROCKET READY FOR IGNITION!")
elif mission >= 60:
    st.info("⛽ Fuel systems active...")
else:
    st.warning("⚠️ Systems require more power.")


# ============================================================
# CHANDRAYAAN
# ============================================================

st.divider()

st.header("🇮🇳 Chandrayaan-3 🌙")

moon1, moon2 = st.columns(2)

with moon1:

    st.subheader("India's Lunar Achievement")

    st.write("""
    Chandrayaan-3 successfully landed near the lunar south
    polar region on 23 August 2023.
    """)

    st.metric(
        "Mission",
        "SUCCESS",
        "23 Aug 2023"
    )

with moon2:

    st.image(
        "https://www.isro.gov.in/media_isro/image/index/"
        "Chandrayaan3/ch3_lander.jpg.webp",
        caption="Chandrayaan-3",
        use_container_width=True
    )


if st.button("🎉 Celebrate Chandrayaan-3"):

    st.balloons()

    st.success(
        "🇮🇳 INDIA REACHED THE MOON!"
    )


# ============================================================
# QUIZ
# ============================================================

st.divider()

st.header("🧠 ISRO Space Quiz")

score = 0

q1 = st.radio(
    "1. Where did India's early sounding rocket programme begin?",
    ["Thumba", "Delhi", "Bengaluru"],
    key="quiz1"
)

q2 = st.radio(
    "2. When did Chandrayaan-3 land?",
    ["2020", "2023", "2025"],
    key="quiz2"
)

q3 = st.radio(
    "3. Who is regarded as the father of India's space programme?",
    [
        "Dr. Vikram Sarabhai",
        "Homi Bhabha",
        "Rakesh Sharma"
    ],
    key="quiz3"
)

q4 = st.radio(
    "4. What is India's human spaceflight programme?",
    [
        "Gaganyaan",
        "Mangalyaan",
        "Aditya"
    ],
    key="quiz4"
)

q5 = st.radio(
    "5. Which planet did Mangalyaan orbit?",
    [
        "Mars",
        "Venus",
        "Jupiter"
    ],
    key="quiz5"
)

if st.button("✅ CHECK QUIZ"):

    answers = [
        q1 == "Thumba",
        q2 == "2023",
        q3 == "Dr. Vikram Sarabhai",
        q4 == "Gaganyaan",
        q5 == "Mars"
    ]

    score = sum(answers)

    st.progress(score / 5)

    if score == 5:
        st.balloons()
        st.success("🏆 PERFECT SCORE — SPACE EXPERT!")

    elif score >= 3:
        st.success(
            f"🚀 {score}/5 — Great job!"
        )

    else:
        st.warning(
            f"🌱 {score}/5 — Keep exploring!"
        )


# ============================================================
# TIMELINE
# ============================================================

st.divider()

st.header("📅 India's Space Timeline")

year = st.slider(
    "Time Travel",
    1963,
    2026,
    1963,
    key="timeline"
)

events = {

    1963:
        "🚀 1963 — First sounding rocket launched from Thumba.",

    1969:
        "🇮🇳 1969 — ISRO was established.",

    1975:
        "🛰️ 1975 — Aryabhata, India's first satellite, launched.",

    1980:
        "🚀 1980 — Rohini satellite was placed into orbit by SLV-3.",

    2013:
        "🔴 2013 — Mars Orbiter Mission launched.",

    2014:
        "🔴 2014 — Mangalyaan successfully entered Mars orbit.",

    2023:
        "🌙 2023 — Chandrayaan-3 successfully landed on the Moon.",

    2024:
        "👨‍🚀 2024 — Gaganyaan preparations continued.",

    2026:
        "🚀 2026 — India's space programme continues toward human spaceflight."
}

closest_year = min(
    events.keys(),
    key=lambda x: abs(x - year)
)

st.markdown(
    f"""
    <div class="timeline">

    <h2>{closest_year}</h2>

    <p style="font-size:22px;">
    {events[closest_year]}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# NASA APOD
# ============================================================

st.divider()

st.header("🌌 NASA Astronomy Picture of the Day")

apod = get_apod()

if apod:

    st.subheader(apod.get("title", "NASA APOD"))

    media_type = apod.get("media_type")

    if media_type == "image":

        st.image(
            apod.get("url"),
            caption=apod.get("title"),
            use_container_width=True
        )

    elif media_type == "video":

        st.video(apod.get("url"))

    st.write(
        apod.get("explanation", "")
    )

    if apod.get("date"):
        st.caption(
            f"NASA APOD — {apod.get('date')}"
        )

else:

    st.warning(
        "NASA APOD could not be loaded right now."
    )


# ============================================================
# SPACE VIDEO
# ============================================================

st.divider()

st.header("🎬 From Earth to Space")

st.write(
    "Watch a space video directly inside the website."
)

st.video(
    "https://www.youtube.com/watch?v=WeA7edXsU40"
)


# ============================================================
# M83 MUSIC
# ============================================================

st.divider()

st.header("🎵 Space Vibes — M83")

st.markdown("""
<div class="space-card">

<h3>🎧 M83 — Outro</h3>

<p>
Listen to the track through the official video player.
</p>

</div>
""", unsafe_allow_html=True)

# Official YouTube-style embedded player
m83_url = "https://www.youtube.com/watch?v=1H4B7Zp2w1Y"

st.video(m83_url)

st.caption(
    "Music belongs to its respective copyright holder. "
    "The player above streams the video rather than storing the song "
    "inside the GitHub project."
)


# ============================================================
# LIVE ISS TRACKER
# ============================================================

st.divider()

st.header("🛰️ LIVE ISS TRACKER")

st.write(
    "Get the International Space Station's current approximate position."
)

iss = get_iss()

if st.button("🌍 FIND ISS NOW"):

    if iss:

        lat = float(
            iss["iss_position"]["latitude"]
        )

        lon = float(
            iss["iss_position"]["longitude"]
        )

        st.success(
            f"🛰️ ISS Position: {lat:.2f}°, {lon:.2f}°"
        )

        st.map({
            "lat": [lat],
            "lon": [lon]
        })

        st.metric(
            "Latitude",
            f"{lat:.2f}°"
        )

        st.metric(
            "Longitude",
            f"{lon:.2f}°"
        )

    else:

        st.error(
            "ISS service is currently unavailable."
        )


# ============================================================
# MARS
# ============================================================

st.divider()

st.header("🔴 Mars Explorer")

mars_col1, mars_col2 = st.columns(2)

with mars_col1:

    st.image(
        "https://images-assets.nasa.gov/image/"
        "PIA24464/PIA24464~orig.jpg",
        caption="Mars — NASA",
        use_container_width=True
    )

with mars_col2:

    st.markdown("""
    <div class="space-card">

    <h2>🤖 Explore Mars</h2>

    <p>
    Mars is one of the most explored worlds beyond Earth.
    NASA's robotic missions have studied its atmosphere,
    geology and ancient environments.
    </p>

    </div>
    """, unsafe_allow_html=True)

if st.button("📸 Show Mars Mission Mode"):

    st.balloons()

    st.success(
        "🔴 Mars exploration mode activated!"
    )


# ============================================================
# ISRO x NASA
# ============================================================

st.divider()

st.header("🇮🇳🤝🇺🇸 ISRO × NASA")

st.markdown("""
<div class="space-card">

<h2 style="text-align:center;">
🇮🇳 🤝 🇺🇸
</h2>

<h3 style="text-align:center;">
NISAR — NASA + ISRO
</h3>

<p style="text-align:center;">
A joint Earth-observation mission designed to study
changes on our planet using radar.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# ROCKET SIMULATOR
# ============================================================

st.divider()

st.header("🚀 LEVEL 2 — ROCKET SIMULATOR")

thrust = st.slider(
    "Thrust (kN)",
    100,
    2000,
    800,
    key="thrust"
)

fuel_kg = st.slider(
    "Fuel (kg)",
    1000,
    10000,
    5000,
    key="fuel"
)

if st.button("🔥 IGNITE ROCKET"):

    velocity = thrust * 10 / fuel_kg * 100

    altitude = velocity * 5

    st.progress(
        min(int(velocity), 100)
    )

    st.metric(
        "Estimated Altitude",
        f"{int(altitude)} km"
    )

    if altitude > 100:

        st.success(
            f"🌌 SPACE REACHED — {int(altitude)} km!"
        )

        st.balloons()

    else:

        st.warning(
            f"🚀 {int(altitude)} km — Need 100 km!"
        )


# ============================================================
# ORBIT SIMULATOR
# ============================================================

st.subheader("🛰️ Orbit Simulator")

angle = st.slider(
    "Orbit Angle",
    0,
    360,
    0,
    key="orbit"
)

r = 120

x = r * math.cos(
    math.radians(angle)
)

y = r * math.sin(
    math.radians(angle)
)

st.markdown(
    f"""
    <div style="
        width:300px;
        height:300px;
        border:3px solid #6875ff;
        border-radius:50%;
        margin:auto;
        position:relative;
        background:
        radial-gradient(circle,#15154a,#000 70%);
        box-shadow:0 0 40px #303f9f;
    ">

    <div style="
        position:absolute;
        left:50%;
        top:50%;
        width:50px;
        height:50px;
        background:radial-gradient(circle,#fff,#6c63ff);
        border-radius:50%;
        transform:translate(-50%,-50%);
        box-shadow:0 0 30px #6c63ff;
    "></div>

    <div style="
        position:absolute;
        left:{150+x}px;
        top:{150+y}px;
        width:14px;
        height:14px;
        background:#fff;
        border-radius:50%;
        box-shadow:0 0 20px #fff;
        transform:translate(-50%,-50%);
    "></div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# STAR DENSITY
# ============================================================

st.subheader("⭐ Deep Space Generator")

star_density = st.slider(
    "Star Density",
    0,
    100,
    50,
    key="stars"
)

stars = "⭐" * (star_density // 5)

st.markdown(
    f"""
    <div style="
        min-height:100px;
        padding:20px;
        text-align:center;
        font-size:25px;
        background:#000;
        border-radius:20px;
        overflow:hidden;
    ">
    {stars}
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# KILIMANOOR → MOON
# ============================================================

st.divider()

st.header("🌱 Kilimanoor → Moon")

fuel = st.slider(
    "Mission Fuel %",
    0,
    100,
    10,
    key="moonfuel"
)

st.progress(fuel)

distance = int(
    fuel * 3844
)

st.metric(
    "Journey Distance",
    f"{distance:,} km"
)

st.markdown(
    f"""
    <div style="
        text-align:center;
        font-size:28px;
        padding:20px;
        overflow:hidden;
    ">
    🚀
    {"━" * max(1, fuel // 10)}
    🌙
    </div>
    """,
    unsafe_allow_html=True
)

if fuel == 100:

    st.balloons()

    st.success(
        "🌕 MOON REACHED!"
    )


# ============================================================
# MISSION CONTROL
# ============================================================

st.divider()

st.header("🛰️ MISSION CONTROL")

st.caption(
    "Mission Control — by Advika"
)

astronauts = [
    "Advika — Commander",
    "Rakesh Sharma",
    "Ritu Karidhal"
]

selected_astronaut = st.selectbox(
    "Select Astronaut",
    astronauts,
    key="astronaut"
)

st.success(
    f"👩‍🚀 {selected_astronaut} ready!"
)

st.markdown(
    """
    <div style="
        text-align:center;
        font-size:90px;
        padding:20px;">
        👩‍🚀🚀
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEALTH CHECK
# ============================================================

st.subheader("🚨 Rocket Health Check")

fuel_ok = st.checkbox(
    "⛽ Fuel Full?"
)

oxygen_ok = st.checkbox(
    "🫁 Oxygen OK?"
)

computer_ok = st.checkbox(
    "💻 Computer Online?"
)

camera_ok = st.checkbox(
    "📷 Camera Working?"
)

if st.button("🔍 RUN SYSTEM CHECK"):

    score = sum([
        fuel_ok,
        oxygen_ok,
        computer_ok,
        camera_ok
    ])

    percentage = score * 25

    st.progress(
        percentage / 100
    )

    if percentage == 100:

        st.balloons()

        st.success(
            "🟢 ALL SYSTEMS GO!"
        )

    else:

        st.warning(
            f"🟡 SYSTEM STATUS: {percentage}%"
        )


# ============================================================
# MESSAGE TO ISS
# ============================================================

st.subheader("📡 Message to Space")

message = st.text_input(
    "Message:",
    key="space_message"
)

if st.button("📡 SEND MESSAGE"):

    if message:

        st.success(
            f"🛰️ ISS received: '{message}'"
        )

    else:

        st.warning(
            "Write a message first."
        )


# ============================================================
# GROOT / KUTTAN
# ============================================================

st.divider()

st.header("🌱 Meet Kuttan — The Tree-Naut")

st.markdown("""
<div class="groot-container">

<h2>🌱 KUTTAN 🚀</h2>

<p>
Your space-loving tree companion.
</p>

</div>
""", unsafe_allow_html=True)

st.info(
    "For the actual Marvel Groot GIF, place a properly licensed "
    "Groot asset in your project's assets folder and load it with "
    "`st.image()`."
)

# Local asset support:
# Put your licensed GIF here:
# assets/groot.gif

try:

    st.image(
        "assets/groot.gif",
        caption="Groot",
        use_container_width=False
    )

except Exception:

    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:110px;
            padding:40px;">
            🌱
        </div>
        """,
        unsafe_allow_html=True
    )

mood = st.selectbox(
    "Kuttan's mood",
    [
        "Happy 😊",
        "Dancing 💃",
        "Sleepy 😴",
        "Hungry 🍃",
        "Studying 📚"
    ],
    key="mood"
)

if mood == "Happy 😊":

    st.success(
        "Kuttan: I love Kilimanoor! 💚"
    )

elif mood == "Dancing 💃":

    st.success(
        "Kuttan is dancing through space! 💃🌱"
    )

elif mood == "Sleepy 😴":

    st.info(
        "Kuttan is sleeping among the stars. 😴⭐"
    )

elif mood == "Hungry 🍃":

    if st.button("🍃 Feed Kuttan"):

        st.success(
            "Kuttan: YUMMY! 🌱😋"
        )

else:

    st.info(
        "Kuttan is studying rocket science. 📚🚀"
    )


if st.button("✋ HIGH FIVE KUTTAN"):

    st.balloons()

    st.success(
        "🌱 Kuttan gave you a HIGH FIVE!"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    🚀 <b>THUMBA TO SPACE</b> 🚀

    <br><br>

    Made with 💚 by Advika

    <br>

    Thumba → Kilimanoor → Moon → Mars → Beyond

    <br><br>

    🇮🇳 India to the Stars 🌌

    </div>
    """,
    unsafe_allow_html=True)
   