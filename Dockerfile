FROM nvcr.io/nvidia/pytorch:21.10-py3

WORKDIR /app

COPY ./requirements.txt app.py sd_utils.py ./

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]