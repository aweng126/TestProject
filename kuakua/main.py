# -*- coding: UTF-8 -*-
import random
from flask import Flask
app = Flask(__name__)

dlist = []

def get_data_from_file(file):
    dlist = []
    sentence = ""
    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            if line.strip() != "" and "沙雕" not in line:
                sentence = sentence + line
            else:
                dlist.append(sentence)
                sentence = ""
    return dlist


def get_random_data():
    global dlist
    if len(dlist) == 0:
        dlist = get_data_from_file("finaldata.txt")
    num = len(dlist)
    idx = random.randint(1, num)
    return dlist[idx]


@app.route('/')
def index():
    return get_random_data()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
