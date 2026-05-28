FROM python:3.9-slim
# Standard: use lightweight Python image

WORKDIR /app
# Standard: set working directory inside container

COPY . /app
# Standard: copy project files into container

RUN pip install -r requirements.txt
# Standard: install Flask dependency

EXPOSE 5002
# Standard: expose port 5002

CMD ["python", "order.py"]
# Standard: run the Order Service