FROM python:3.11-slim

WORKDIR /larousseIA

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh

EXPOSE 10000

CMD ["./start.sh"]