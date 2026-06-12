# Natural Language Processing (NLP) Desktop Application

## Overview

This project is a Python-based desktop application developed using Tkinter that performs various Natural Language Processing (NLP) tasks through an interactive graphical user interface. The application allows users to register, log in, and access multiple NLP features.

## Features

### User Authentication

* User Registration
* User Login
* Password Validation
* Local Database Storage

### Sentiment Analysis

Analyzes the sentiment of a given text and classifies it as:

* Positive
* Negative
* Neutral

**Example:**
Input: "I love this movie. It is amazing!"
Output: Positive 😊

### Emotion Detection

Identifies emotions expressed in text such as:

* Joy
* Sadness
* Anger
* Fear
* Surprise

**Example:**
Input: "I am very excited about my results."
Output: Joy 😄

### Named Entity Recognition (NER)

Extracts important entities from text including:

* Person Names
* Organizations
* Locations
* Dates

**Example:**
Input: "Sundar Pichai works at Google in California."

Output:

* Sundar Pichai → Person
* Google → Organization
* California → Location

## Technologies Used

* Python
* Tkinter
* Hugging Face Inference API
* JSON
* Object-Oriented Programming (OOP)
* Git & GitHub

## Project Structure

```text
Natural-Language-Processing/
│
├── app.py
├── main.py
├── myapi.py
├── mydb.py
├── db.json
├── resource.py
├── resources/
│   └── favicon.ico
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/seemranshaw26-bot/Natural-Language-Processing.git
```

2. Navigate to the project folder:

```bash
cd Natural-Language-Processing
```

3. Install required packages:

```bash
pip install huggingface_hub
```

4. Create a `secret.py` file and add your Hugging Face API token:

```python
APIKEY = "YOUR_HUGGINGFACE_TOKEN"
```

5. Run the application:

```bash
python main.py
```

## Learning Outcomes

* GUI Development using Tkinter
* API Integration with Hugging Face
* User Authentication System
* NLP Application Development
* Git and GitHub Version Control
* Object-Oriented Programming in Python

## Future Improvements

* Text Summarization
* Language Translation
* Speech-to-Text Integration
* User Activity History
* Database Integration with SQLite/MySQL

## Author

Seemraan Shaw

MSc in Statistics
