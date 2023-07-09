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

st.write('**[1] ¿La institución educativa cuenta con un plan de contingencia ante deslizamientos e inundaciones?**')
plan_contingencia = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[2] ¿Se realizan simulacros periódicos en la institución educativa para prepararse ante deslizamientos e inundaciones?**')
simulacros = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[3] ¿La infraestructura de la institución educativa cuenta con medidas de prevención y mitigación ante deslizamientos e inundaciones?**')
infraestructura = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[4] ¿La institución educativa cuenta con personal capacitado para actuar en casos de deslizamientos e inundaciones?**')
personal_capacitado = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[5] ¿La comunidad educativa está informada sobre las medidas de seguridad en caso de deslizamientos e inundaciones?**')
comunidad_informada = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[6] ¿La institución educativa tiene acceso a recursos y herramientas para monitorear las condiciones climáticas?**')
acceso_recursos = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[7] ¿La institución educativa cuenta con un sistema de alerta temprana para deslizamientos e inundaciones?**')
alerta_temprana = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[8] ¿La infraestructura de la institución educativa está ubicada en una zona de riesgo de deslizamientos e inundaciones?**')
zona_riesgo = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[9] ¿Se han realizado mejoras en la infraestructura de la institución educativa para prevenir deslizamientos e inundaciones?**')
mejoras_infraestructura = st.selectbox(label="", options=['Sí', 'No'], index=0)

st.write('**[10] ¿La institución educativa cuenta con un sistema de evacuación en caso de deslizamientos e inundaciones?**')
evacuacion = st.selectbox(label="", options=['Sí', 'No'], index=0)

def main():
    if st.button("**EJECUTAR**"):
        resultado = ''
        if (plan_contingencia == 'Sí' and simulacros == 'Sí' and infraestructura == 'Sí' and 
            personal_capacitado == 'Sí' and comunidad_informada == 'Sí' and acceso_recursos == 'Sí' and 
            alerta_temprana == 'Sí' and zona_riesgo == 'Sí' and mejoras_infraestructura == 'Sí' and 
            evacuacion == 'Sí'):
            resultado = 'La institución educativa está bien preparada para enfrentar deslizamientos e inundaciones durante el Fenómeno del Niño.'
        else:
            resultado = 'Es recomendable tomar medidas adicionales para mejorar la preparación y mitigar los riesgos en la institución educativa.'
        
        st.write(resultado)


st.text("-------------------------------------------------------------------------")
st.text("Laboratorio de ciencia de datos")
st.text("Konecta_Perú")


if __name__ == '__main__':
    main()