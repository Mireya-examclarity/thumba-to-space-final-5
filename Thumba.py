import streamlit as st
import datetime
import math

st.set_page_config(page_title="Thumba to Space", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(180deg, #000000 0%, #0a0a23 50%, #1a1a3e 100%); color: white; }
    h1, h2, h3, p, div, label, span { color: white !important; }
    @keyframes sway { 0%{transform:rotate(-2deg)} 50%{transform:rotate(2deg)} 100%{transform:rotate(-2deg)} }
    @keyframes blink { 0%,90%,100%{height:50px} 95%{height:5px} }
    .groot-box { animation: sway 2s infinite ease-in-out; }
    .eye { animation: blink 3s infinite; }
</style>
""", unsafe_allow_html=True)

st.title("Thumba to Space 🚀")
st.subheader("From Thiruvananthapuram to the Stars")
st.markdown("<div style='text-align:center;font-size:80px;'>🌌🚀🌙</div>", unsafe_allow_html=True)
st.write("India's space journey started in Thumba! Built from Kilimanoor!")

# Countdown
next_launch = datetime.datetime(2026, 9, 15, 10, 30)
diff = next_launch - datetime.datetime.now()
c1,c2,c3 = st.columns(3)
c1.metric("Days", diff.days)
c2.metric("Hours", diff.seconds//3600)
c3.metric("Next", "Gaganyaan")

st.divider()
st.header("🚀 Kilimanoor Rocket Builder")
name = st.text_input("Your Name from Kilimanoor:")
if st.button("Launch from Thumba!"):
    if name:
        st.snow()
        st.success(f"{name} launched from Thumba! Jai Hind!")
        st.markdown("<div style='text-align:center;font-size:100px;'>🚀💨</div>", unsafe_allow_html=True)
    else:
        st.warning("Enter your name da!")

st.divider()
st.header("📰 1963 - THUMBA TIMES")
st.write("**21st Nov 1963 | Thumba, Trivandrum**")
st.write("> 'A small fishing village launched India to the stars. Rocket on BICYCLE!'")
a,b = st.columns(2)
with a:
    st.subheader("🚲 Bicycle Rocket!")
    st.markdown("<div style='text-align:center;font-size:60px;'>🚲🚀⛪</div>", unsafe_allow_html=True)
    if st.button("Hear Old Story"): st.info("Kalam: We pushed rocket on bicycle from church!")
with b:
    st.subheader("⛪ Church = Control Room!")
    st.markdown("<div style='text-align:center;font-size:60px;'>⛪📡🔭</div>", unsafe_allow_html=True)
    if st.button("View Old Photo"):
        st.snow()
        st.success("Church bells + rocket countdown!")

st.divider()
st.subheader("🛰️ Mission Control")
mission = st.slider("Select Launch Power %", 0, 100, 75)
st.progress(mission)
st.write("🔥 ROCKET READY!" if mission>90 else "⛽ Fueling...")

st.divider()
st.header("🇮🇳 Chandrayaan-3 🌙")
col1,col2 = st.columns(2)
with col1:
    st.write("India 1st on Moon South Pole!")
    st.metric("Mission", "Success", "100%")
with col2:
    st.markdown("<div style='text-align:center;font-size:80px;'>🇮🇳🌙🛰️</div>", unsafe_allow_html=True)
if st.button("Celebrate! 🎉"): st.snow(); st.balloons()

st.divider()
st.header("🧠 ISRO Quiz - 5 Questions!")
q1 = st.radio("1. Where first rocket 1963?", ["Thumba","Delhi","Sriharikota"], key="q1")
if q1=="Thumba": st.success("Correct! 🚀")
q2 = st.radio("2. Chandrayaan-3 land?", ["2023","2020","2024"], key="q2")
if q2=="2023": st.success("Yes! Aug 23, 2023! 🌙")
q3 = st.radio("3. Father of Indian space program?", ["Dr. Vikram Sarabhai","Kalam","Bhabha"], key="q3")
if q3=="Dr. Vikram Sarabhai": st.success("Yes! Dr. Sarabhai! 🚀")
q4 = st.radio("4. First control room was?", ["St. Mary Church","ISRO HQ","Studio"], key="q4")
if q4=="St. Mary Church": st.success("Yes! Church! ⛪")
q5 = st.radio("5. Next big mission?", ["Gaganyaan","Mars 2","PSLV"], key="q5")
if q5=="Gaganyaan": st.success("Hooray! Gaganyaan - Indians in space! 👩‍🚀")

st.divider()
st.header("📅 Timeline")
year = st.slider("Time travel!", 1963, 2024, 1963, key="yr")
if year==1963: st.write("🚲 1963: Bicycle rocket from Thumba!")
elif year<1980: st.write("🔬 1969: ISRO formed!")
elif year<2008: st.write("🛰️ 1980s: Satellites launch!")
elif year<2023: st.write("🚀 2014: Mangalyaan reaches Mars!")
else: st.write("🌙 2023: Moon South Pole!")

st.divider()
st.header("🎵 Space Vibes")
st.link_button("▶️ Play M83 Outro", "https://www.youtube.com/watch?v=S_CKyXG3kA0")
if st.button("🚀 Play Inside Site!"):
    st.snow()
    st.success("🎶 M83 - Outro | From Thumba to Stars ✨")
    st.balloons()

st.divider()
st.header("🌌 Live Space View")
m1,m2,m3 = st.columns(3)
m1.metric("🚀 Missions", "130+", "Growing")
m2.metric("🛰️ Satellites", "400+", "Orbit")
m3.metric("🌙 Moon", "2023", "Success!")
if st.button("🌠 Deep Space Mode"):
    st.snow()
    st.markdown("<div style='text-align:center;font-size:100px;'>🌌⭐🌟✨🌠</div>", unsafe_allow_html=True)

st.divider()
st.header("🚀 LEVEL 2 - REAL SIMULATOR")
thrust = st.slider("Thrust (kN)", 100, 2000, 800, key="th")
fuel_kg = st.slider("Fuel kg", 1000, 10000, 5000, key="fk")
if st.button("IGNITE! 🔥"):
    vel = thrust * 10 / fuel_kg * 100
    alt = vel * 5
    st.progress(min(int(vel),100))
    st.metric("Altitude", f"{int(alt)} km")
    if alt>100: st.success(f"SPACE! {int(alt)}km!"); st.balloons()
    else: st.warning(f"{int(alt)}km - Need 100km!")

st.subheader("2️⃣ Orbit Simulator")
angle = st.slider("Orbit Angle", 0, 360, 0, key="ag")
r=150
x=r*math.cos(math.radians(angle))
y=r*math.sin(math.radians(angle))
st.markdown(f"""<div style="width:300px;height:300px;border:2px solid white;border-radius:50%;margin:auto;position:relative;background:radial-gradient(circle, #1a1a3e 0%, #000 70%);">
<div style="position:absolute;left:50%;top:50%;width:40px;height:40px;background:linear-gradient(#4CAF50,#2196F3);border-radius:50%;transform:translate(-50%,-50%);"></div>
<div style="position:absolute;left:{150+x/2}px;top:{150+y/2}px;width:10px;height:10px;background:white;border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 10px white;"></div>
</div>""", unsafe_allow_html=True)

st.subheader("3️⃣ Star Density")
sd = st.slider("Deep space?", 0, 100, 50, key="sd")
st.write("Stars:" + "⭐"*(sd//10) + f" {sd}%")
if sd>80: st.success("Interstellar!"); st.snow()

st.divider()
st.header("🌌 NASA Picture of the Day - REAL + FALLBACK")
st.write("Trying real NASA image... if blocked shows cool simulation!")
try:
    st.image("https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=800", caption="Milky Way - NASA Style (Unsplash - works in college!)", width='stretch')
    st.success("✅ Real space photo loaded!")
except:
    st.markdown("""
    <div style="background:radial-gradient(ellipse at center, #1a1a3e 0%, #000 100%);padding:30px;border-radius:20px;text-align:center;border:2px solid #444;">
        <div style="font-size:80px;">🌌</div>
        <div style="width:250px;height:150px;background:#000;margin:auto;position:relative;border-radius:10px;overflow:hidden;">
            <div style="position:absolute;top:20px;left:30px;width:3px;height:3px;background:white;border-radius:50%;box-shadow:50px 10px white,100px 30px white,180px 20px white,60px 60px white,150px 80px white;"></div>
            <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:80px;height:80px;background:radial-gradient(#FFD700,#FF8C00);border-radius:50%;box-shadow:0 0 30px #FFD700;"></div>
        </div>
        <h3>Milky Way Simulation - Offline</h3>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.header("🇮🇳🤝🇺🇸 ISRO x NASA")
st.markdown("<div style='text-align:center;font-size:60px;'>🇮🇳🤝🇺🇸🛰️</div>", unsafe_allow_html=True)
st.metric("NISAR", "2024-2025", "ISRO + NASA")

st.divider()
st.header("🛰️ LIVE ISS Tracker - REAL + FALLBACK")
st.write("Real ISS image + live location!")
try:
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800", caption="ISS over Earth - Real Photo", width='stretch')
except:
    st.markdown("<div style='text-align:center;font-size:80px;'>🛰️🌍💫</div>", unsafe_allow_html=True)
if st.button("Find ISS Now!"):
    st.snow()
    st.success("ISS at: 8.5°N, 76.9°E - Over Thumba!")
    st.map(data={'lat': [8.5], 'lon': [76.9]})
    st.write("ISS speed: 28,000 km/h!")

st.divider()
st.header("🔴 Mars Rover - REAL + FALLBACK")
try:
    st.image("https://images.unsplash.com/photo-1446776877081-d282a0f896e2?w=800", caption="Mars Surface - Curiosity Style", width='stretch')
    st.success("✅ Real Mars photo loaded!")
except:
    st.markdown("""<div style="text-align:center;background:linear-gradient(#8B4513,#CD5C5C);padding:20px;border-radius:20px;"><div style="font-size:80px;">🤖</div><h3 style="color:white;">Curiosity on Mars! 🔴</h3><div style="font-size:40px;">🏜️🪨⛰️</div></div>""", unsafe_allow_html=True)
if st.button("📸 Get Mars Photo!"): st.snow(); st.balloons()

st.divider()
st.header("🌙 Kilimanoor to Moon")
fuel = st.slider("Fuel %", 0, 100, 10, key="fm")
st.progress(fuel)
st.metric("Reached", f"{fuel*3844} km")
st.markdown(f"<div style='text-align:center;font-size:30px;'>🚀{'─'*(fuel//10)}🌙</div>", unsafe_allow_html=True)
if fuel==100: st.snow(); st.balloons(); st.success("MOON REACHED! 🌕🇮🇳")

st.divider()
st.header("🛰️ MISSION CONTROL - By Advika")
astronauts = ["Advika - Commander", "Rakesh Sharma", "Ritu Karidhal"]
sel = st.selectbox("Astronaut", astronauts, key="as")
if sel: st.success(f"{sel} ready!"); st.markdown("<div style='text-align:center;font-size:80px;'>👩‍🚀🚀</div>", unsafe_allow_html=True)
st.subheader("🚀 Health Check")
f1 = st.checkbox("Fuel Full?"); o1 = st.checkbox("Oxygen OK?"); c1 = st.checkbox("Computer Online?"); cam = st.checkbox("Camera Working?")
if st.button("System Check"):
    score = (25 if f1 else 0)+(25 if o1 else 0)+(25 if c1 else 0)+(25 if cam else 0)
    st.progress(score)
    if score==100: st.snow(); st.balloons(); st.success("ALL GO!")
    else: st.warning(f"{score}% Ready")

st.subheader("📡 Message to ISS")
msg = st.text_input("Message to ISS:", key="ms")
if st.button("Send to Space"):
    if msg: st.snow(); st.success(f"Astronaut: 'Hello Kilimanoor! Got: {msg}'")
    else: st.warning("Type message!")

st.divider()
st.header("🌱 Meet Kuttan - Kilimanoor Tree Boy!")
st.markdown("""
<div style="text-align:center;">
    <div class="groot-box" style="width:220px;height:260px;background:linear-gradient(180deg,#A67C52 0%,#8B5A2B 40%,#6D4C41 100%);margin:auto;border-radius:30px 30px 20px 20px;position:relative;border:5px solid #4E342E;box-shadow:0 10px 0 #3E2723;">
        <div class="eye" style="position:absolute;top:50px;left:30px;width:60px;height:50px;background:radial-gradient(circle at 30% 30%, #222 0%, #000 70%);border-radius:50%;border:3px solid #3E2723;">
            <div style="position:absolute;top:10px;left:12px;width:18px;height:18px;background:white;border-radius:50%;box-shadow:0 0 8px white;"></div>
        </div>
        <div class="eye" style="position:absolute;top:50px;right:30px;width:60px;height:50px;background:radial-gradient(circle at 30% 30%, #222 0%, #000 70%);border-radius:50%;border:3px solid #3E2723;">
            <div style="position:absolute;top:10px;left:12px;width:18px;height:18px;background:white;border-radius:50%;box-shadow:0 0 8px white;"></div>
        </div>
        <div style="position:absolute;bottom:60px;left:50%;transform:translateX(-50%);width:70px;height:14px;background:#3E2723;border-radius:10px;"></div>
        <div style="position:absolute;top:-25px;left:30px;font-size:35px;">🌿</div>
        <div style="position:absolute;top:-30px;left:50%;transform:translateX(-50%);font-size:40px;">🌱</div>
        <div style="position:absolute;top:-25px;right:30px;font-size:35px;">🍃</div>
    </div>
    <h3>I am Kuttan! 🌱 From Kilimanoor!</h3>
    <p>ISRO's first tree-naut! 🚀</p>
</div>
""", unsafe_allow_html=True)
mood = st.selectbox("Kuttan feeling?", ["Happy 😊","Dancing 💃","Sleepy 😴","Hungry 🍃","Studying 📚"], key="mo")
if mood=="Happy 😊": st.markdown("<div style='text-align:center;font-size:80px;'>🌱😊✨</div>", unsafe_allow_html=True); st.success("Kuttan: I love Kilimanoor!"); st.balloons()
elif mood=="Dancing 💃": st.markdown("<div style='text-align:center;font-size:80px;'>💃🌱🕺</div>", unsafe_allow_html=True); st.snow()
elif mood=="Sleepy 😴": st.markdown("<div style='text-align:center;font-size:80px;'>🌱😴💤</div>", unsafe_allow_html=True)
elif mood=="Hungry 🍃":
    if st.button("Feed leaves"): st.markdown("<div style='text-align:center;font-size:80px;'>🌱🍃😋</div>", unsafe_allow_html=True); st.success("Yummy!"); st.balloons()
else: st.markdown("<div style='text-align:center;font-size:80px;'>🌱📚🤓</div>", unsafe_allow_html=True)

if st.button("High Five Kuttan! ✋🌱"): st.balloons(); st.snow(); st.success("Kuttan hugged you! 💚")

st.divider()
st.write("Made with 💚 by Advika & Kuttan | Thumba to Space 2026 | Real Photos (Unsplash - not blocked) + Offline Fallback")
   
    