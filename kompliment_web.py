import streamlit as st
import random

st.set_page_config(page_title="💬 Компліментатор", page_icon="✨")

st.title("💬 Натисни — і отримай комплімент!")

імена = ["Віка", "Оля", "Іван", "Макс"]
прикметники = ["чудова", "талановита", "неймовірна", "весела", "розумна"]
порівняння = ["як сонце", "як зоря", "як магніт", "як натхнення"]

if st.button("💖 Дай мені комплімент"):
    імʼя = random.choice(імена)
    прикмета = random.choice(прикметники)
    порівн = random.choice(порівняння)

    st.success(f"{імʼя}, ти {прикмета} — {порівн} ✨")
