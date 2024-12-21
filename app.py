# se importan las librerias 
import os
import streamlit as st
from gtts import gTTS

def tts(text, lang="es"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("output.mp3")
    return "output.mp3"


# generar la pagina web con streamlit

# titulo de la pag
st.title("generador de texto a voz")

# input para ingresar el texto
text = st.text_area('Ingresar el texto:')
# seleccionar el idioma
language = st.selectbox('Seleccione un idioma', ['es', 'en', 'fr'])

# boton para generar el audio
if st.button('Generar audio'):
    if text:
        # generar el audio
        audio_file = tts(text, lang=language)
        # reproducir el audio
        st.audio(audio_file, format='audio/mp3')
        st.success("Audio generado con exito")
    else:
        st.warning("Por favor ingrese un texto")
        

