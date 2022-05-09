# JarvisAI
For our capstone project we are building a Jarvis AI library that Python has to offer. This library can perform numerous tasks, such as opening websites, games, and other applications. It allows you to speak into the microphone and listens to what you ask for. What we ultimately want to accomplish is to create a GUI showcasing the abilities of this library.

# Setup
Download and install Anaconda:
https://www.anaconda.com/download/

The python version we used was 3.9.7:
conda activate my_env 
conda install python=3.9.7

Install Tensorflow CPU 3.6.0 (Also ensure you have the latest pip):
python -m pip install --upgrade pip
conda create -n CV pip tensorflow==3.6.0

To import libraries, we first ran the command: conda activate CV

Below we will include a list of libraries we used to make this possible.
Library         Version         Command
---------- | ------------- | ---------------------------------
numpy      |    1.21.0     |    pip install numpy==1.21.0
pyopengltk |    0.0.4      |    pip install pyopengltk==0.0.4
PyOpenGL   |    3.1.6      |    pip install pyopengl==3.1.6
JarvisAI   |    3.7.1      |    pip install jarvisai==3.7.1
