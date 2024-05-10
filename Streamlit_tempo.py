import streamlit as st
import requests

# Função para obter a temperatura atual usando a API OpenWeatherMap
def obter_temperatura_atual(cidade, chave_api):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        temperatura = dados['main']['temp']
        return temperatura
    else:
        st.error(f"Falha ao obter a temperatura atual: {resposta.status_code}")
        return None

# Chave da API OpenWeatherMap (substitua pela sua chave de API real)
chave_api = 'd8582587540d1a70d892da02e0afbf44'

# Título da página
st.title('App de Temperatura Atual')

# Entrada do usuário para a cidade
cidade = st.text_input('Digite o nome da cidade:', key='cidade')

# Botão para obter a temperatura atual
if st.button('Obter Temperatura'):
    if cidade:
        temperatura_atual = obter_temperatura_atual(cidade, chave_api)
        if temperatura_atual is not None:
            st.success(f"A temperatura atual em {cidade} é: {temperatura_atual}°C")
        else:
            st.error('Não foi possível obter a temperatura. Verifique o nome da cidade e tente novamente.')
    else:
        st.error('Por favor, digite o nome de uma cidade.')

# Rodapé
st.write('Criado pelo Instrutor Márcio W Farias')
