import streamlit as st
from transformers import pipeline

st.title('Sentiment Analysis App')
st.write('*Just enter your text and the model will classify it as ‘POSITIVE’ or ‘NEGATIVE’ sentiment, along with a confidence score.*')
st.write('*Note: it will take up to 30 seconds to run the app.*')

form = st.form(key='sentiment-form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')

if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')

st.write('*itseffi © 2023 - 2024*')
