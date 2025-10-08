
import gradio as gr
from transformers import pipeline

# 1. Load the pre-trained NER pipeline
print("Loading NER model...")
ner_pipeline = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    tokenizer="dslim/bert-base-NER",
    aggregation_strategy="simple"
)
print("Model loaded successfully!")


# 2. Define the prediction function
def ner_prediction(text):
    """
    Takes text input, runs NER, and formats the output for Gradio's HighlightedText.
    """
    ner_results = ner_pipeline(text)
    
    if not ner_results:
        return [(text, None)]
        
    highlighted_output = []
    last_index = 0
    for entity in ner_results:
        highlighted_output.append((text[last_index:entity['start']], None))
        highlighted_output.append((entity['word'], entity['entity_group']))
        last_index = entity['end']
    
    highlighted_output.append((text[last_index:], None))
    
    return highlighted_output


# 3. Build the Gradio Interface
app = gr.Interface(
    fn=ner_prediction,
    inputs=gr.Textbox(
        lines=5, 
        label="Input Text", 
        placeholder="Enter a sentence here..."
    ),
    outputs=gr.HighlightedText(
        label="Named Entities",
        color_map={"PER": "#FF6347", "ORG": "#87CEEB", "LOC": "#98FB98", "MISC": "#FFD700"}
    ),
    title="Interactive Named Entity Recognition (NER) with BERT",
    description="""
    This app uses the pre-trained 'dslim/bert-base-NER' model to identify and highlight named entities. 
    Enter text to see Persons (PER), Organizations (ORG), Locations (LOC), and Miscellaneous (MISC) entities.
    """,
    examples=[
        ["The British Prime Minister Rishi Sunak will visit Paris to meet with Emmanuel Macron next Tuesday."],
        ["Apple, based in Cupertino, California, was co-founded by Steve Jobs."],
        ["The NASA rover Perseverance successfully collected its first rock sample on Mars."]
    ]
)

# 4. Launch the app (This line is for running locally and will be handled by Hugging Face Spaces)
if __name__ == "__main__":
    app.launch()
