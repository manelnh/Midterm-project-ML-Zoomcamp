## Heart Disease Detecttion Project
### Context
* Machine learning has become an essential component in the functioning of various sectors and application domains, particularly in healthcare,
where significant advancements are needed to improve and save lives. Within healthcare, I chose to focus on cardiovascular diseases (CVDs),
as they are the leading cause of death worldwide. I am excited to contribute to this promising area aimed at enhancing quality of life, even
though this project is relatively decent.

* The primary objective is to use patient features such as age, cholesterol levels, resting blood pressure, and more to predict whether a patient suffers from heart disease (or heart failure). Multiple models will be trained, hyperparameters tuned, and the best predictive model selected to assist in early diagnosis and ultimately improve patient outcomes.
### Dataset
The dataset used in this  project is publicly available on Kaggle
https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction 

> [!Note]
> How to get data?
> * You have to load the dataset from the given link.
> * Then, when you open the notebook, you need to upload the dataset from your local desktop
    and transform it to a DataFrame as shown in the code.
### How to run the project?
 Note that I'll guide you to the way you effectively run the project and also how to create it if you are insterested!
 So, it will be detailed with specific command lines.
 For the person who will review this project and run it, all you have to do is:
 * download this project in ZIP file
 * Open VS code --> New terminal
 * Run Docker Desktop
 * Run --> `docker run -p 8000:8000 heart-disease-app`
 * Navigate to the browser --> `localhost:8000/docs`
 * Get the prediction by clicking on `try it out`
 #### 1. Check the notebook: 
First, I recommend reviewing the notebook before running the project in a web browser. This will provide a clearer understanding of the model implementation and the methodology used.
#### 2. Important insctructions to follow:
* Open all the existing files in VS code or other similar tool, personally I prefer VS code.
* Ensure Docker Desktop is running before executing any command lines.
* Open a terminal in VS Code or any other terminal, and navigate to the project directory (e.g., cd myapp).  
#### 3. Virtual environment set: instructions for the creation
* Pull the image to be built in docker from Docker hub --> **docker pull python:3.11-slim**.
* Use Poetry to manage dependencies inside your project directory.
     - Poetry handles the virtual environment creation, activation, and dependency installation.
     - It generates the pyproject.toml file listing all required dependencies.
     - How?
         -  Command Line -- > `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
            #$env:Path += ";C:\Users\MANEL\AppData\Roaming\pypoetry\venv\Scripts"`
         - Command Line --> `poetry init` --> Then you will be asked to enter information for your file, at this point I recommend
           skipping entering dependencies because it will generate an error, so add your dependencies after the creation of the project using
           --> `poetry add fastapi scikit-learn uvicorn requests` and more, then you add other dependencies manually,
           but make sure to type --> `poetry lock` after every update of the pyproject.toml!
         - Uvicorn is a lightweight and fast ASGI server used to run FastAPI applications.
#### 4. build your container 
* Note that the web service app I used is FastAPI app
* Make sure to create a port = 8000
* --> `docker build -t project_name .` (In my case its `heart-disease-app`): Don't forget the **dot** at the end !
* Run your fastapi in web browser using --> `docker run -p 8000:8000 heart-disease-app`
* Go to your browser, type --> localhost:8000/docs to get your fastpi contrainerized.
* click on predict button --> try it out and then you will get :
                             - feature1: - the probability that the given patient is suffering from heart disease.
                             - feature2: Boolean variable --> if probabilityis >= 0.5 --> True ( patient suffers from a heart failure)
                               otherwise it returns False.
* You can also get output results using this response command in your terminal:


>> $patient = @{                            
>>     "age" = 65
>>     "sex" = "m"
>>     "chestpaintype" = "asy"
>>     "restingbp" = 160
>>     "cholesterol" = 0
>>     "fastingbs" = 1
>>     "restingecg" = "st"
>>     "maxhr" = 122
>>     "exerciseangina" = "n"
>>     "oldpeak" = 1.2
>>     "st_slope" = "flat"}
>>
>> $response = Invoke-RestMethod -Uri http://localhost:8000/predict -Method POST -Body ($patient | ConvertTo-Json) -ContentType "application/json"
>> $response
* Or --> docker exec -it container_name python3 /myapp/serve.py

