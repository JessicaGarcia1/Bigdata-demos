import streamlit as st

st.title('Hello Word')
st.header('streamlit')
st.write('by Jessica')

import streamlit as st

# Título de la encuesta
st.title('Encuesta sobre Hobbies')

# Instrucciones
st.write('Por favor, selecciona tus hobbies preferidos.')

# Crear un formulario con opciones de hobbies
hobbies = ['Leer', 'Correr', 'Nadar', 'Cine', 'Cocinar', 'Viajar', 'Pintar', 'Jugar videojuegos']
seleccion_hobbies = st.multiselect('¿Cuáles son tus hobbies?', hobbies)

# Mostrar las respuestas seleccionadas
if seleccion_hobbies:
    st.write("Tus hobbies seleccionados son:")
    for hobby in seleccion_hobbies:
        st.write(f"- {hobby}")
else:
    st.write("No seleccionaste ningún hobby.")

# Pregunta adicional sobre la frecuencia de los hobbies
frecuencia = st.radio('¿Con qué frecuencia practicas tus hobbies?', ('Diariamente', 'Semanalmente', 'Mensualmente', 'Casi nunca'))

# Mostrar la respuesta sobre la frecuencia
st.write(f'Practicas tus hobbies: {frecuencia}')

# Sección de comentarios adicionales
comentarios = st.text_area("¿Tienes algún comentario adicional sobre tus hobbies?")

# Mostrar los comentarios
if comentarios:
    st.write("Tus comentarios:")
    st.write(comentarios)
