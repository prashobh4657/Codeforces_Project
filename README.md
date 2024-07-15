# User Data Analysis on Codeforces

## Table of Contents

- [Problem Statement](#problem-statement)
- [Description of Important Libraries and GUI Used](#description-of-important-libraries-and-gui-used)
- [Important Functions Used](#important-functions-used)
- [Datasets Used](#datasets-used)
- [Results](#results)
- [Conclusion](#conclusion)

## Problem Statement

This project focuses on analyzing user data from Codeforces, a popular coding platform, and representing the data graphically by observing various parameters. Additionally, the project compares the rating changes of two users in contests and depicts these changes graphically.

## Description of Important Libraries and GUI Used

### Tkinter

- **Tkinter**: The standard GUI library for Python.
  - Provides a fast and easy way to create GUI applications.
  - Offers a powerful object-oriented interface to the Tk GUI toolkit.

### NumPy & Matplotlib

- **Matplotlib**: Used along with NumPy data to plot various types of graphs.
  - `pyplot()`: Used to plot two-dimensional data.

### Pandas

- **Pandas**: A software library written for data manipulation and analysis.

### Easygui

- **Easygui**: A module for very simple and easy GUI programming in Python.

### Mplcursors

- **Mplcursors**: Provides interactive data selection cursors for Matplotlib.

## Important Functions Used

### File Handling

- `open()`
- `close()`
- `read()`
- `write()`

### Exception Handling

- `try`
- `except`

### Tkinter

- `Button()`
- `Canvas()`
- `Label()`
- `Menu()`
- `Text()`

### NumPy

- `array()`

### Matplotlib

- `plt.title()`
- `plt.plot()`
- `plt.xlabel()`, `plt.ylabel()`
- `plt.bar()`, `plt.pie()`
- `plt.show()`
- `plt.subplots()`

### Pandas

- `read_csv()`
- `df.dropna(inplace=True)` (for cleaning data)
- `df.at[]`

## Datasets Used

### Codeforces API Data

- Data retrieved from the Codeforces API includes:
  - Username, Name, Country, City, Rating, Contribution, and Rating Change of participated contests.

### Custom Dataset

- Created to store:
  - Outcomes of submissions.
  - Number of problems solved based on problem rating on Codeforces.

## Results

- Successfully analyzed user data on Codeforces by considering various parameters and depicted the observations graphically.
- Successfully compared the rating change curves of two users and represented them graphically.

## Conclusion

Through this Data Analysis Project, we have:

- Learned the concepts of File Handling, Object-Oriented Programming, and Exception Handling in Python.
- Gained experience with various libraries and GUIs such as Tkinter, Easygui, NumPy, Pandas, Matplotlib, and Mplcursors.
- Successfully represented the collected data graphically using Rating Change curves, Bar Graphs, and Pie Charts.
