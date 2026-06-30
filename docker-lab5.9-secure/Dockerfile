FROM python:3.10

WORKDIR /app

# Create non-root user
RUN useradd -m appuser

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# change ownership
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]