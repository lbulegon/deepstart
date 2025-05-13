# Django + Uvicorn + ASGI


uv init deepstart

uv run hello.py

Alguns pacotes Python são expostos como ferramentas de linha de comando, como black para formatação de código, flake8 para linting, pytest para teste, mypy para verificação de tipo etc. O UV fornece duas interfaces especiais para gerenciar esses pacotes:
uv tool run black main.py 

uvx black main.py source 

Trocar a versao do Pyhton 
 
pyproject.toml  alterar requires-python = ">=3.12" 
depois

uv sync     
uv pip install -e . 


.venv/bin/activate  # Ativa o ambiente (Linux/macOS)
.venv\Scripts\activate  No Windows 

django-admin startproject setup .
python manage.py startapp app_deepstart
python manage.py makemigrations        
python manage.py migrate
python manage.py createsuperuser

python manage.py extrair_pdf docs/exemplo.pdf


OpenManus
https://apidog.com/blog/openmanus-open-source-manus-ai-alternative/?utm_source=google_dsa&utm_medium=g&utm_campaign=22062217351&utm_content=169453484141&utm_term=&gad_source=1&gad_campaignid=22062217351&gbraid=0AAAAA-gKXrB0dplfPhwCEmKKniVSIUdfX&gclid=Cj0KCQjwt8zABhDKARIsAHXuD7ZmxsFVheyNz2Yfx4NGwjT8-PniE6NTnR7hK9Lh7iFxo-el-MRgUB8aAsk_EALw_wcB

git clone https://github.com/mannaandpoem/OpenManus.git


# Deploy

 scp -r C:\Users\Liandro\Documents\Github\deepstart lbulegon@192.168.0.69:/home/ubuntu/