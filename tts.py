from gtts import gTTS as texto_a_voz
import os as sistema

texto = "Hola, en este video les mostraré como realizar el monitoreo diario de Azure"
idioma = "es"
idioma_alt = "en-us"
mp3_nombre = "archivo_de_prueba.mp3"

def AbrirAudioEn(an):
    sistema.system("cmd" + "/c start " + an)

myobj = texto_a_voz(text=texto, lang=idioma, slow=False)

myobj.save(mp3_nombre)

AbrirAudioEn(mp3_nombre)
