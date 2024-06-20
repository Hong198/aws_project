# FROM python:3.11.2-slim

# # 즉시 출력
# ENV PYTHONUNBUFFERED=1
# # .pyc (Python 컴파일된 바이트 코드) 파일을 생성하지 않도록 하는 역할
# ENV PYTHONDONTWRITEBYTECODE=1

# # 패키지 설치
# RUN apt-get update && apt-get install -y libpq-dev \
#     gcc \
#     python3-dev \
#     && apt-get clean

# WORKDIR /app

# RUN pip3 install --upgrade pip
# RUN pip3 install pipenv

# COPY Pipfile Pipfile.lock ./

# RUN pipenv requirements > requirements.txt
# RUN pip3 install -r requirements.txt
