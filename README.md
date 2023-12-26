<h1 align="center">Boston House Price Prediction <br> End to End Machine learning Project</h1>


<h2 align="center">Software and Tools Used</h2>  

1. [Jupyter Notebook](https://jupyter.org/)
2. [Vs Code](https://code.visualstudio.com/download)
3. [Postman](https://www.postman.com/downloads/)
4. [Github](https://github.com/)
5. [Github CLI](https://cli.github.com/)
6. [Docker](https://docs.docker.com/engine/install/)
7. [Amazon Web Service(AWS)](https://aws.amazon.com/console/)

---  

<h3 align="center">Project Life Cycle</h3>  

1. Requirement (or) Data gathering.
2. Exploratory Data Analysics.
3. Feature Engineernig (not required in this project).
4. Feature Selection (not required in this project).
5. Model Training and Evaluation.
6. Model Hyperparamter Tuning (not required in this project).
7. Web Application Creation using Flask.
8. Add Code to Github.
9. Model Deployment on AWS.  

---

<h3 align="center">Directory Structure</h3>  

```  
├── models  
├── notebook  
├── templates  
├── static  
|     ├── css  
├── README.md  
├── .gitignore  
├── requirements.txt  
├── application  
```

---

<h3 align="center">Virtual Environment</h3>  

1. Creation -> ```python -m venv .venv```  
2. Activate Virtual Environment -> ```.venv\Scripts\activate``` (or) Can be selected manually in vs code

---

<h3 align="center">API Testing Using PostMan</h3>  

1. Develop a API using Flask.
2. Test it in PostMan.
    1. Open postman.
    2. Click on "+" icon.
    3. Select the route method i.e "POST".
    4. Add the api url.
    5. Go to "Body" then choose "raw" then choose "json".
    6. Now, Write json input data and send it to api.
    7. Then we will get a response.

---

<h3 align="center">Deployment on AWS</h3>  

- Here, We push our docker image to AWS ECR(Elastic Container Repository).
- Then we run that image using AWS ECS(Elastic Container Services).
- In this project we also build CICD pipeline using github actions.

---