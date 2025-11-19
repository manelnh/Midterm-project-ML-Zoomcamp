FROM python:3.11-slim

WORKDIR /myapp

RUN apt-get update && apt-get install -y curl build-essential

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock* /myapp/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root --no-ansi

COPY rf_model.bin /myapp/
COPY ./ /myapp/

EXPOSE 8000

CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]



#docker pull aditi03/heart_disease_detect:v1
#install poetry tool and its dependencies in my directory:
#(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
#$env:Path += ";C:\Users\MANEL\AppData\Roaming\pypoetry\venv\Scripts"
#poetry --version
#create pyproject.toml: poetry init: enter required infos
#poetry add fastapi uvicorn scikit-learn: create virtual env
#if library didnt exist, repeat the commands above and type poetry lock 
#docker build -t heart-disease-app .
#docker run heart-disease-app(docker run -p 8000:8000 heart-disease-app)

#output using response command: 

#$patient = @{
    #"age" = 65
    #"sex" = "m"
    #"chestpaintype" = "asy"
    #"restingbp" = 160
    #"cholesterol" = 0
    #"fastingbs" = 1
    #"restingecg" = "st"
    #"maxhr" = 122
    #"exerciseangina" = "n"
    #"oldpeak" = 1.2
    #"st_slope" = "flat"}

#$response = Invoke-RestMethod -Uri http://localhost:9001/predict -Method POST -Body ($patient | ConvertTo-Json) -ContentType "application/json"

#$response 

#output calling predict_lead_test.py file that exists in the container : 
#to check wether files are is container or not:
#docker exec -it container_name /bin/sh
#docker exec -it container_name python3 /app/predict_lead_test.py
