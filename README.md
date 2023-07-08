# Towel Video Splitter 📹✂️

Towel Video Splitter is a simple GUI tool for splitting video files into segments of a specified duration.

## 1. Using Towel Video Splitter in Terminal 🖥️

Before you can run Towel Video Splitter, you need to have Python and the required dependencies installed. 

Here's how you can run it:

### 1.1 Install Python 🐍

1. If you haven't already, install Python on your system. You can download it from the [official website](https://www.python.org/downloads/). 

### 1.2 Install Dependencies 📦

1. Open Terminal.
2. Install the required Python packages with pip:
```bash
pip install moviepy tk
```

### 1.3 Run the Script 🏃‍♀️

1. Navigate to the directory containing the `splitgui.py` file:
```bash
cd /path/to/directory
```
2. Run the script:
```bash
python splitgui.py
```
3. The GUI should appear. Select a video file and enter the duration for the splits. Click `Split` to start the process.

## 2. Packaging with PyInstaller 📦

### 2.1 Install PyInstaller 🧰

1. If you haven't already, install PyInstaller. This tool converts Python scripts into standalone applications:
```bash
pip install pyinstaller
```

### 2.2 Generate a .spec File 🔨

1. Generate a .spec file for your script. This file will be used to configure the build process:
```bash
pyi-makespec --onefile --windowed splitgui.py
```
2. This will generate a `splitgui.spec` file in the same directory.

### 2.3 Modify the .spec File 📝

1. Open `splitgui.spec` in a text editor.
2. Add the following line near the top of the file to increase the maximum recursion depth (this is a workaround for a potential recursion error during the build process):
```python
import sys; sys.setrecursionlimit(sys.getrecursionlimit() * 5)
```

### 2.4 Build the Application 🏗️

1. Build the application using the .spec file:
```bash
pyinstaller splitgui.spec
```
2. If the build process is successful, the application will be located in the `dist` directory.

## That's it! 🎉

You should now have a standalone Mac application for Towel Video Splitter. Double-click `splitgui.app` in the `dist` directory to run it.
