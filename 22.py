import streamlit as st

st.title("Encuesta de Vulnerabilidad de Instituciones Educativas ante el Fenómeno del Niño")

st.write('**¿La institución educativa cuenta con un plan de contingencia ante deslizamientos e inundaciones?**')
pregunta1 = st.selectbox(label="Pregunta 1", options=['Sí', 'No'], index=0, key="pregunta1")

st.write('**¿Se realizan simulacros periódicos en la institución educativa para prepararse ante deslizamientos e inundaciones?**')
pregunta2 = st.selectbox(label="Pregunta 2", options=['Sí', 'No'], index=0, key="pregunta2")

st.write('**¿La infraestructura de la institución educativa cuenta con medidas de prevención y mitigación ante deslizamientos e inundaciones?**')
pregunta3 = st.selectbox(label="Pregunta 3", options=['Sí', 'No'], index=0, key="pregunta3")

st.write('**¿La institución educativa cuenta con personal capacitado para actuar en casos de deslizamientos e inundaciones?**')
pregunta4 = st.selectbox(label="Pregunta 4", options=['Sí', 'No'], index=0, key="pregunta4")

st.write('**¿La comunidad educativa está informada sobre las medidas de seguridad en caso de deslizamientos e inundaciones?**')
pregunta5 = st.selectbox(label="Pregunta 5", options=['Sí', 'No'], index=0, key="pregunta5")

st.write('**¿La institución educativa tiene acceso a recursos y herramientas para monitorear las condiciones climáticas?**')
pregunta6 = st.selectbox(label="Pregunta 6", options=['Sí', 'No'], index=0, key="pregunta6")

st.write('**¿La institución educativa cuenta con un sistema de alerta temprana para deslizamientos e inundaciones?**')
pregunta7 = st.selectbox(label="Pregunta 7", options=['Sí', 'No'], index=0, key="pregunta7")

st.write('**¿La infraestructura de la institución educativa está ubicada en una zona de riesgo de deslizamientos e inundaciones?**')
pregunta8 = st.selectbox(label="Pregunta 8", options=['Sí', 'No'], index=0, key="pregunta8")

st.write('**¿Se han realizado mejoras en la infraestructura de la institución educativa para prevenir deslizamientos e inundaciones?**')
pregunta9 = st.selectbox(label="Pregunta 9", options=['Sí', 'No'], index=0, key="pregunta9")

st.write('**¿La institución educativa cuenta con un sistema de evacuación en caso de deslizamientos e inundaciones?**')
pregunta10 = st.selectbox(label="Pregunta 10", options=['Sí', 'No'], index=0, key="pregunta10")

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

if __name__ == '__main__':
    main()
