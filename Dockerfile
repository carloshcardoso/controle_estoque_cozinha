
# Usar uma imagem base oficial do Python
FROM python:3.8-slim

# Definir o diretório de trabalho no container
WORKDIR /app.py

# Copiar os arquivos de requisitos primeiro, para aproveitar o cache do Docker
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto para o diretório de trabalho no container
COPY . .

# Expõe a porta 5000
EXPOSE 5000

# Comando para executar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
