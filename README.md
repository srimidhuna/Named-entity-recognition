🧠 Named Entity Recognition (NER) Web App using BERT and Gradio
📘 Overview

This project demonstrates a Named Entity Recognition (NER) web application built using a pretrained BERT model from Hugging Face and Gradio for interactive visualization.

The app identifies and highlights entities such as:

PER → Person

ORG → Organization

LOC → Location

MISC → Miscellaneous (other named entities)

It provides a user-friendly interface to input any text and view detected entities with color-coded highlights.

⚙️ Features

Uses dslim/bert-base-NER, a fine-tuned BERT model for NER.

Built with Gradio for an interactive browser-based interface.

Automatically highlights entity types directly in the output text.

Requires no additional training — uses a pretrained transformer model.

🧩 Requirements

Install the following dependencies before running the app:

Python 3.8+

transformers

torch

gradio

You can install them using:

pip install transformers torch gradio

📁 Project Structure
ner_app/
│
├── app.py                # Main application file (your code)
├── README.md             # Documentation
└── requirements.txt      # List of dependencies (optional)

🚀 How to Run

Clone or download the project.

Open a terminal in the project folder.

Run the application:

python app.py


Once it loads, Gradio will open in your browser.
You’ll see a textbox where you can type sentences like:

“Barack Obama was born in Hawaii and worked at the White House.”

The app will highlight detected entities:

Barack Obama → PERSON

Hawaii → LOCATION

White House → ORGANIZATION

🧠 Model Information

Model Name: dslim/bert-base-NER

Base Model: bert-base-cased

Task: Named Entity Recognition

Source: Hugging Face Model Hub



APP LINK : https://huggingface.co/spaces/srimidhuna/Named_Entity_Recognition
