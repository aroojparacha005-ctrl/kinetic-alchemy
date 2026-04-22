import streamlit as st
from avatar_generator import AvatarGenerator
from sound_effects import SoundGenerator, SoundPlayer
import time

st.set_page_config(page_title="Kinetic Alchemy", layout="wide")

if "avatar" not in st.session_state:
    st.session_state.avatar = AvatarGenerator()
    st.session_state.sounds = SoundPlayer()

st.title("🧬 **KINETIC ALCHEMY: The Bio-Forge** 🧬")
st.subheader("Master Micronutrient Imbalances Through Clinical Diagnosis")

# Generate sounds button
with st.sidebar:
    st.header("⚙️ Settings")
    if st.button("🔊 Generate Audio"):
        gen = SoundGenerator()
        if gen.generate_all():
            st.success("✅ Sounds ready!")

st.write("---")
st.subheader("👤 Patient Case #1: Iron Deficiency Anemia")

col1, col2 = st.columns([1, 1])

with col1:
    st.write("**Clinical Presentation:**")
    st.info("""
    28-year-old female:
    • Persistent fatigue & weakness
    • Pale complexion
    • Dyspnea on exertion
    • Pale lips & nailbeds
    
    **Lab Results:**
    • Hemoglobin: 8.5 g/dL (Normal: 12-16)
    • Ferritin: 8 ng/mL (Low)
    • MCV: 72 fL (Microcytic)
    """)

with col2:
    st.write("**Avatar Status:**")
    st.session_state.avatar.render_in_streamlit("iron")

st.write("---")
st.subheader("🎯 Diagnosis Question:")
st.write("**What is the best initial treatment?**")

choice = st.radio("Select answer:", [
    "A) Vitamin B12 injections 1000 mcg weekly",
    "B) Ferrous sulfate 325 mg daily PO",
    "C) Intravenous iron dextran 1000 mg",
    "D) Folic acid 1 mg daily"
])

if st.button("✅ Submit Answer"):
    if "B)" in choice:
        st.success("✅ **CORRECT!**")
        st.session_state.sounds.play("success")
        time.sleep(0.5)
        st.balloons()
        st.write("---")
        st.session_state.avatar.render_in_streamlit("healthy")
        st.info("""
        **📚 Wardlaw's Perspective (Perspectives in Nutrition):**
        
        Iron deficiency anemia is treated with oral iron supplementation. Ferrous sulfate 325 mg daily is first-line therapy 
        due to superior absorption. Taken on an empty stomach for optimal bioavailability. Patient should expect hemoglobin 
        improvement within 4-8 weeks. Dietary sources: red meat, poultry, legumes, fortified cereals.
        """)
        st.success("**+10 Nutri-Points** | Level Progress: 1/50")
    else:
        st.error("❌ **INCORRECT**")
        st.session_state.sounds.play("failure")
        time.sleep(0.5)
        st.write("---")
        st.warning("😞 Patient needs the correct treatment!")
        st.info("""
        **Correct Answer: B) Ferrous sulfate 325 mg daily**
        
        **📚 Wardlaw's Perspective:**
        Iron deficiency is the most prevalent micronutrient deficiency globally. Oral iron is superior to IV unless 
        severe malabsorption exists. Ferrous forms are absorbed better than ferric.
        """)
        st.error("**0 Nutri-Points** | No Progress")

st.write("---")
st.subheader("📊 Your Statistics:")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Nutri-Points", "0", "+0")
c2.metric("Level", "Intern", "0/50")
c3.metric("Accuracy", "0%", "0/0")
c4.metric("Bagels", "0", "+0")
