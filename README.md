# JarvisAI
The main objective of this project was to create a personal assistant for users on the Windows operating system. This program works by utilizing the different functions of the library Jarvis AI, and pushing it into a graphical user interface (GUI). What makes this GUI special is that it can be used either by text or speech input. While having such a versatile program, we strived to assemble it in a way that was visually appealing while incorporating 3D rendering on the side of the command canvas.

This project was important, as it showcased the knowledge that we gained over the couple years at SUNY Polytechnic Institute, while also providing a way to use the personal assistant to make every day tasks easy. The program allows for many functions; telling the date, time, weather, topics, news, as well as opening websites and applications, and lastly emailing. We wanted to ensure that the program is very versatile.


# Setup
Download and install Anaconda:
https://www.anaconda.com/download/

The python version we used was 3.9.7:
```
conda activate my_env 
conda install python=3.9.7
````

Install Tensorflow CPU 3.6.0 (Also ensure you have the latest pip):
```
python -m pip install --upgrade pip
conda create -n CV pip tensorflow==3.6.0
````

To import libraries, we first ran the command: ```conda activate CV```

Below we will include a list of libraries we used to make this possible.
```
Library         Version         Command
---------- | ------------- | ---------------------------------
numpy      |    1.21.0     |    pip install numpy==1.21.0
pyopengltk |    0.0.4      |    pip install pyopengltk==0.0.4
PyOpenGL   |    3.1.6      |    pip install pyopengl==3.1.6
JarvisAI   |    3.7.1      |    pip install jarvisai==3.7.1
````
