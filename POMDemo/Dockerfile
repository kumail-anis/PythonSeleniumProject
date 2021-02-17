FROM selenium/standalone-chrome
WORKDIR /usr/src/app/POMDemo
COPY requirements.txt .
RUN sudo apt-get update
RUN sudo apt-get install google-chrome-stable -y
RUN sudo apt-get install python 3.9 -y
RUN sudo apt-get install python3-pip -y
RUN sudo apt-get install python3.9-venv -y
RUN sudo -H pip3 install -U selenium

RUN sudo python3.9 -m venv /usr/bin/virtual

COPY . .
CMD ["python3", "Tests/LoginTest.py"]