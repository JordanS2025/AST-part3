# AST Project

## Authors
- Jordan Scott
- David Smical
- Eli Streimatter



## Overview
This project aims to classify inputted descriptions into one of 31 labels based on their similarity. It utilizes natural language processing techniques and machine learning models to achieve this classification.

## Installation
To run this project, you need to install the following Python packages via pip:
- g4f
- nest_asyncio

Additionally, if any errors occur during execution, you may need to update your system packages using the following commands:
```bash
sudo apt-get update
sudo apt-get install --fix-missing libexpat1-dev
```

## Usage
The core functionality of the project is split into two main Python scripts:
1. `AST3.py`: This script classifies inputted descriptions using a machine learning model and outputs the classification results.
2. `AST3-2.py`: This script processes abstract syntax trees (ASTs) of code and identifies specific patterns, providing summary descriptions.

### Running the Scripts
To run the scripts, execute the `main.py` file. Ensure that the file locations for Python 3 and the individual scripts are correctly specified in the `main.py` file.

**Note**: Line 68 of `AST3-2.py` needs to be updated with the correct file location of the output file (`output_ast2.json`).

```bash
python3 main.py
```

## File Structure
The project directory structure is as follows:
- `main.py`: Entry point for executing the project.
- `AST3.py`: Script for classifying inputted descriptions.
- `AST3-2.py`: Script for processing ASTs and identifying patterns.
- `output_ast2.json`: JSON file containing an example abstract syntax tree (AST).
- `README.md`: Documentation for the project.