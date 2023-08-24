# 
FROM python:3.9.15
# 
WORKDIR /code
# 
COPY ./requirements.txt /code/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# 
COPY ./ServerApp  /code/ServerApp
COPY ./UIApp /code/UIApp

# 
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
