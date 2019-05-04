FROM python:3

ADD sort-file.py /
ADD input.csv /

CMD [ "python", "./sort-file.py" ]