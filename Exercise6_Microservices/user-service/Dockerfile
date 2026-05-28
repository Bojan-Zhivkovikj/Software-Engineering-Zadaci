FROM python:3.9-slim
# Standard: use lightweight Python image

WORKDIR /app
# Standard: set working folder inside the container

COPY . /app
# Standard: copy all files from user-service into container

RUN pip install -r requirements.txt
# Standard: install Flask from requirements.txt

EXPOSE 5001
# Standard: document that this service uses port 5001

CMD ["python", "user.py"]
# Standard: start the User Service