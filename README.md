# Ai_MySQL
Software for consulting and executing CRUD operations in MySQL through artificial intelligence prompts (Gemini).


Hello everyone, I created software during a DeepLearning.ai Bootcamp that performs queries and operations within a MySQL database. I also want to thank BRAINS - Brazilian AI Networking for introducing us to and guiding us through the learning content.

Basically, the software requests information such as the user, host, password, and schema it will use, as well as the API Key. Note that this project uses Gemini, specifically the Gemini 1.5 Flash model, along with other standard libraries to execute operations via MySQL.

Note: From what I understand, MySQL80 needs to be running in the background, but the MySQL application itself doesn’t necessarily need to stay open. However, I recommend opening it initially and then closing it once you’ve logged into the application.

I ask that everyone who finds it useful connects with me on [LinkedIn](https://www.linkedin.com/in/mateusfsrgsouza/). I’m a Systems Analysis student and, like many of you, still in the learning phase.

### Usage Instructions
First, enter the database credentials and the Gemini API Key. Then, perform a query via prompt, making sure to use the correct column and table names. Example: "Query the sales table for the price and state columns."

Below is the download link for the software file, but if you prefer to create it directly from Python, enter the following in the terminal:

```bash
pyinstaller --onefile --windowed appSQLV1.py
```
Make sure you're in the correct directory where the file is located. Due to the tkinter library, your antivirus may flag it as a false positive; if that happens, temporarily pause your antivirus or remove the .exe file from quarantine.


Don't forget to install the required libraries in Python!

[Download](https://drive.google.com/drive/folders/1vB45GArlkuz0HyOg8HcOzrBuaSDYcMIz?usp=drive_link)

_________________________________________________________________________________________________________________________________________________________
Olá a todos, criei um software enquanto estava em um Bootcamp da Deeplearning.ai que realiza consultas e operações dentro de um banco de dados MySQL. Quero agradecer também a BRAINS - Brazilian AI Networking por ter apresentado e nos guiado no conteúdo de aprendizado. 

Bom basicamente o software pede informações como o user, host, password e o schema que vai utilizar, também pede a API Key que vai utilizar, lembrando que foi um programa que utilizou Gemini. Utilizei o modelo Gemini 1.5 Flash, além de demais bibliotecas padrão para executar as operações via MySQL.

Obs: Pelo que entendi precisa estar rodando o MySQL80 nos serviços de fundo, mas a aplicação em si não necessariamente precisa estar aberta do MySQL, porém recomendo abrir a mesma e depois pode fechar quando logar na aplicação. 

Peço que todos que utilizarem ela e acharem de alguma forma útil se conectem comigo via [LinkedIn](https://www.linkedin.com/in/mateusfsrgsouza/), sou estudante de Analise de Sistemas, e estou em faze de aprendizado como muitos de vocês. 
