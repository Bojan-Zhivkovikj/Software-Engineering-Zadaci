FROM python:3.9-slim
# STAYS SAME: lightweight Python image

WORKDIR /app
# STAYS SAME: working folder inside container

COPY . /app
# STAYS SAME: copy project files into container

RUN pip install -r requirements.txt
# STAYS SAME: install dependencies

EXPOSE 5000
# MIGHT CHANGE: Flask default port is 5000

CMD ["python", "app.py"]
# MIGHT CHANGE: app.py changes only if your main file has another name