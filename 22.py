import streamlit as st
from PIL import Image

image = Image.open('logo_direcciones_regionales.jpg')
st.image(image, caption='', use_column_width=True)

st.title("Encuesta de Evaluación Censal de Estudiantes 2015 por Direcciones Regionales de Educación")

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
<h2 style="color:white;text-align:left;">Evaluación Censal de Estudiantes 2015: </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)
st.title("Encuesta de Evaluación Censal de Estudiantes 2015 por Direcciones Regionales de Educación")

st.write('**¿La institución educativa implementó la Evaluación Censal de Estudiantes en 2015?**')
pregunta1 = st.selectbox(label="Pregunta 1", options=['Sí', 'No'], index=0, key="pregunta1")

st.write('**¿Se aplicó la evaluación a todos los estudiantes de la institución?**')
pregunta2 = st.selectbox(label="Pregunta 2", options=['Sí', 'No'], index=0, key="pregunta2")

st.write('**¿La institución educativa recibió los resultados de la Evaluación Censal de Estudiantes?**')
pregunta3 = st.selectbox(label="Pregunta 3", options=['Sí', 'No'], index=0, key="pregunta3")

st.write('**¿Se utilizaron los resultados de la evaluación para implementar mejoras en la institución educativa?**')
pregunta4 = st.selectbox(label="Pregunta 4", options=['Sí', 'No'], index=0, key="pregunta4")

st.write('**¿La dirección regional de educación realizó algún tipo de seguimiento o acompañamiento en relación a la Evaluación Censal de Estudiantes?**')
pregunta5 = st.selectbox(label="Pregunta 5", options=['Sí', 'No'], index=0, key="pregunta5")

st.write('**¿Se realizaron acciones de capacitación para los docentes sobre la Evaluación Censal de Estudiantes?**')
pregunta6 = st.selectbox(label="Pregunta 6", options=['Sí', 'No'], index=0, key="pregunta6")

st.write('**¿Se llevaron a cabo reuniones o espacios de intercambio de experiencias entre las instituciones educativas de la región sobre la Evaluación Censal de Estudiantes?**')
pregunta7 = st.selectbox(label="Pregunta 7", options=['Sí', 'No'], index=0, key="pregunta7")

st.write('**¿La dirección regional de educación utilizó los resultados de la Evaluación Censal de Estudiantes para la toma de decisiones a nivel regional?**')
pregunta8 = st.selectbox(label="Pregunta 8", options=['Sí', 'No'], index=0, key="pregunta8")

st.write('**¿Se realizaron acciones para difundir los resultados de la Evaluación Censal de Estudiantes a la comunidad educativa y la sociedad en general?**')
pregunta9 = st.selectbox(label="Pregunta 9", options=['Sí', 'No'], index=0, key="pregunta9")

st.write('**¿Se tomaron medidas para el mejoramiento de la calidad educativa a partir de los resultados de la Evaluación Censal de Estudiantes?**')
pregunta10 = st.selectbox(label="Pregunta 10", options=['Sí', 'No'], index=0, key="pregunta10")

def main():
    if st.button("**EJECUTAR**"):
        resultado = ''
        if (pregunta1 == 'Sí' and pregunta2 == 'Sí' and pregunta3 == 'Sí' and 
            pregunta4 == 'Sí' and pregunta5 == 'Sí' and pregunta6 == 'Sí' and 
            pregunta7 == 'Sí' and pregunta8 == 'Sí' and pregunta9 == 'Sí' and 
            pregunta10 == 'Sí'):
            resultado = 'La institución educativa y la dirección regional de educación han demostrado un buen nivel de implementación y aprovechamiento de la Evaluación Censal de Estudiantes 2015.'
        else:
            resultado = 'Es recomendable tomar medidas adicionales para mejorar la implementación y aprovechamiento de la Evaluación Censal de Estudiantes 2015 en la institución educativa y la dirección regional de educación.'
        
        st.write(resultado)

if __name__ == '__main__':
    main()
