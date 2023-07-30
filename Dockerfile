FROM python:3.10

# 
WORKDIR /code

# 
COPY app-pokemon-damage-calculator/requirements.txt /code/app-pokemon-damage-calculator/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/app-pokemon-damage-calculator/requirements.txt

# 
COPY ./app-pokemon-damage-calculator/app /code/app
