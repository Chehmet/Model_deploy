# Task for PMLDL Assignment 1: Deployment

This assignment concerns the topic of MLOps and consists of the **main task** and **extra task** for bonus points. In the main task, you are asked to **deploy a machine learning model**. Additionally, as an extra task, you can elaborate on the deployment part and create a **simple automated MLOps pipeline** with the tools that you learnt in the lab.

Solving the main task is enough to get a full grade for this assignment. Meanwhile, solving the extra task will provide additional 5 bonus points to the course grade. The result of your assignment should be a **GitHub repository** with the code implementing the tasks.

# Main Task

In this task you need to **deploy a model in an API** and **create a web application** that interacts with the API. The model API accepts the requests from the web application and sends back the responses. The web application must at least contain the input fields, button for make a prediction, and the area with the prediction itself. To do that, you are supposed to use Docker containers, FastAPI and Streamlit frameworks. __Implementing data and model engineering pipelines is not required for this task__. Your task is only to deploy the model API and the web application.

## Recommended Steps to Complete the Main Task

Here we provide the steps to deploy your model. However, you can do it in different ways, just make sure that your repository is structured (has the hierarchy of files of folders that is logical) and works.


1. Create a GitHub repository. Make sure that your repository is __public__. Clone the repository. The directory of the cloned repository is now your working directory.
2. Write some Python code to train a machine learning model. Save the code in the `code/models` folder. Save the file with trained model in the `models` folder.
3. Write a Python script that implements the model API using FastAPi. Write a Dockerfile for the API. Store both of these files in the `code/deployment/api` folder.
4. Write a Python script that implements the web application using Streamlit. Write a Dockerfile for the application. Store both of these files in the `code/deployment/app` folder.
5. Write a docker-compose file that includes the API and the web application. Store the docker-compose file in the `code/deployment` folder.
6. Build and run docker-compose.
7. Commit the files and push them to GitHub.

## Expected Repository Structure

Here is the structure of the repository that you are encouraged to follow:

```yaml
├── code
│   ├── datasets
│   ├── deployment
│   │   ├── api
│   │   └── app
│   └── models
├── data
└── models
```

## Other Notes

* You are allowed to use any model and dataset, except Iris dataset, which was presented in the lab. Keep in mind that using Iris dataset will lead to **deduction of 50% of the points gained**.
* You are also allowed to use the frameworks other than FastAPI and Streamlit. Nevertheless, the usage of Docker is a must-have. Ignoring the usage of Docker will lead to **0 points** for the assignment.
* If the your trained model is too large for GitHub, then you are allowed to not to push the model to GitHub

## Submission

Submit the solution of the task as a **link to the GitHub repository**. After the deadline of the link submission there will be arranged a **meeting with TAs** where you have to show that your deployment works.

## Main Task Grading Criteria

* **Model API container** works correctly - 2 points
* **Web application container** works correctly - 2 points
* The repository is **structured** (has the hierarchy of files of folders that is logical) - 1 point

## Useful Links for Main Task

* [Docker Tutorial for Beginners](https://docker-curriculum.com/)
* [FastAPI Website](https://fastapi.tiangolo.com/)
* [Get Started with Streamlit](https://docs.streamlit.io/get-started)
