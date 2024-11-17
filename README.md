# Student Progression Outcome Prediction Tool

This repository contains a Python-based application designed to assist in predicting and analyzing student progression outcomes based on their credits. The tool leverages graphical visualization and systematic data handling to provide insights into student performance.

---

## Features

- **Credit Validation**: Validates student credit data to ensure the total credits sum up correctly.
- **Outcome Prediction**: Determines progression outcomes (Progress, Trailer, Retriever, Excluded) based on user-provided data.
- **Histogram Visualization**: Displays a graphical representation of outcomes using a histogram.
- **Data Storage**: Saves student progression data to a file for future reference.
- **Read and Display Data**: Reads saved data and displays it in a structured format.

---

## File Structure

1. **`Part_1.py`**:
   - Implements the basic functionality of the tool, including data input and histogram generation.
   - Introduces the credit validation and outcome prediction mechanisms.

2. **`Part_2.py`**:
   - Extends functionality by adding support for storing and displaying student data in a list.
   - Includes enhancements for viewing progression data systematically.

3. **`Part_3.py`**:
   - Adds functionality to save progression data to a file and read saved data.
   - Includes automatic unique file name generation for saved data.

4. **`graphics.py`**:
   - Provides graphical capabilities for rendering histograms and other visual elements.
   - Built on top of the `tkinter` library, designed for simple graphics.

5. **`progression_data_001.txt`**:
   - Example data file storing progression records, demonstrating how data is saved and retrieved.

---

## Requirements

- Python 3.6+
- Tkinter library (built into Python)
- Basic command-line interface for execution
