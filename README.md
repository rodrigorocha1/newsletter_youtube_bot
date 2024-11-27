# Projeto: Newsletter de Vídeos do YouTube com Base na Transcrição

## 1. Introdução

Este projeto propõe gerar uma transcrição personalizada com IA, com base na transcrição bruta dos vídeos do YouTube e gravar as transcrições em um banco de dados SQLite. Além disso, a transcrição é exibida em um dashboard interativo utilizando o Streamlit.

## 2. Fluxo do Projeto

1. **Entrada do Usuário:**
   - O usuário digita o nome do canal (Ex: @TLESGames).
   - O usuário digita a data e hora de publicação do vídeo.
   
2. **Busca de Canal e Vídeo:**
   - O sistema realiza uma busca no YouTube usando a API do YouTube.
   - O vídeo correspondente à data e hora fornecida é identificado e os detalhes são registrados no banco de dados.

3. **Transcrição:**
   - O sistema gera uma transcrição bruta do vídeo utilizando a API do Google Gemini.
   - A transcrição é então tratada e personalizada pela IA para gerar um conteúdo relevante para o usuário.

4. **Exibição da Transcrição:**
   - O conteúdo tratado é exibido no dashboard do Streamlit para que o usuário visualize a transcrição.

## 3. Diagrama de Classe

![Diagrama de Classe](https://github.com/rodrigorocha1/newsletter_youtube_bot/blob/main/out/diagrama/diagrama_mvc/diagrama_mvc.png?raw=true)

A arquitetura utilizada no projeto segue o padrão **MVC (Model-View-Controller)**:

- **Model:** Responsável por gerenciar as conexões com o banco de dados SQLite e tratar exceções de conexão.
- **View:** A interface do usuário é feita utilizando o Streamlit, que exibe os dados do vídeo e da transcrição.
- **Controller:** Recebe os inputs da view, faz a conexão com o model e trata a lógica de negócios. A lógica de integração com as APIs do YouTube e do Google Gemini é implementada aqui.
- **Service Layer:** Uma camada de serviço para conectar as APIs do YouTube e do Google Gemini utilizando o LangChain, permitindo a reutilização e modularidade do código.

## 4. Demonstração do APP

O aplicativo oferece um dashboard interativo onde o usuário pode:
- Inserir o nome do canal e a data de publicação do vídeo.
- Visualizar a transcrição tratada do vídeo diretamente na interface.



### Exemplos de Uso:

1. O usuário entra com o nome de um canal no YouTube (Ex: `@TLESGames`) e a data e hora de publicação.
2. O sistema realiza a busca no YouTube, recupera a transcrição bruta do vídeo e a trata para exibir de forma personalizada.
3. A transcrição é então exibida em um dashboard interativo no Streamlit.
[Link para a Demonstração](https://youtu.be/w9WBX2nGrcY)

---

### Tecnologias Utilizadas:

- **Streamlit:** Para a construção da interface do usuário (View).
- **SQLite:** Para armazenamento das transcrições e dados dos vídeos.
- **Google Gemini API:** Para gerar transcrições detalhadas dos vídeos.
- **YouTube API:** Para buscar e obter vídeos de um canal específico.
- **LangChain:** Para facilitar a integração e reutilização de componentes entre as APIs.

### 5.Observações
Criar .env com as seguintes variáveis de ambiente
```
YOUTUBE_API_KEY
GOOGLE_API_KEY
```
Criar script no banco de dados mysql
```
CREATE TABLE canais(
	id_canal string,
	nome_canal string,
	url_canal string
);

CREATE TABLE "VIDEOS" (
	id_video VARCHAR NOT NULL, 
	id_canal VARCHAR, 
	nm_video VARCHAR, 
	transcricao VARCHAR, 
	PRIMARY KEY (id_video), 
	FOREIGN KEY(id_canal) REFERENCES "CANAIS" (id_canal)
);

CREATE INDEX "ix_VIDEOS_id_video" ON "VIDEOS" (id_video);


```
