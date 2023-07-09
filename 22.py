import streamlit as st
from PIL import Image

image = Image.open('fenomeno_nino.jpg')
st.image(image, caption='', use_column_width=True)

st.title("Encuesta de Vulnerabilidad de Instituciones Educativas ante el Fenómeno del Niño")

html_temp = """
<div style="background-color:#26c5de;opacity: 0.80;padding:0.2 px">
<h2 style="color:white;text-align:left;">Datos personales: </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

st.write('**¿Cuál es tu edad?**')
edad = st.slider(label="", min_value=1, max_value=100, value=18, step=1)

st.write('**¿Cuál es tu género?**')
genero = st.selectbox(label="", options=['Masculino', 'Femenino'], index=0)

st.write('**¿En qué región vives?**')
region = st.selectbox(label="", options=['Región 1', 'Región 2', 'Región 3'], index=0)

st.write('**¿En qué distrito vives?**')
distrito = st.selectbox(label="",
                        options=['Distrito 1', 'Distrito 2', 'Distrito 3'],
                        index=0)

html_temp = """
<div style="background-color:#26c5de;padding:0.2 px">
<h2 style="color:white;text-align:left;">Evaluación de la vulnerabilidad de las instituciones educativas: </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

st.write('**[1] Pregunta 1**')
pregunta1 = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[2] Pregunta 2**')
pregunta2 = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[3] Pregunta 3**')
pregunta3 = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[4] Pregunta 4**')
pregunta4 = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[5] Pregunta 5**')
pregunta5 = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[6] Pregunta 6**')
pregunta6 = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[7] Pregunta 7**')
pregunta7 = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[8] Pregunta 8**')
pregunta8 = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[9] Pregunta 9**')
pregunta9 = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[10] Pregunta 10**')
pregunta10 = st.selectbox(label="", options=['Sí', 'No'], index=0)

def main():
    if st.button("**EJECUTAR**"):
        resultado = ''
        if (pregunta1 == 'Sí' and pregunta2 == 'Sí' and pregunta3 == 'Sí' and
            pregunta4 == 'Sí' and pregunta5 == 'Sí' and pregunta6 == 'Sí' and
            pregunta7 == 'Sí' and pregunta8 == 'Sí' and pregunta9 == 'Sí' and
            pregunta10 == 'Sí'):
            resultado = 'La institución educativa está bien preparada para enfrentar deslizamientos e inundaciones durante el Fenómeno del Niño.'
        else:
            resultado = 'Es recomendable tomar medidas adicionales para mejorar la preparación y mitigar los riesgos en la institución educativa.'
        
        st.write(resultado)


st.text("-------------------------------------------------------------------------")
st.text("Laboratorio de ciencia de datos")
st.text("Konecta_Perú")


if __name__ == '__main__':
    main()
