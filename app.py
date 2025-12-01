import gradio as gr
from analyze import analyze_sentiment

# Load external CSS file
def load_css():
    with open("style.css", "r") as f:
        return f"<style>{f.read()}</style>"

custom_css = load_css()

def sentiment_interface(text):
    result = analyze_sentiment(text)
    label = result["sentiment"]
    score = result["score"]
    return f"Sentiment: {label}\nConfidence: {score:.2f}"

with gr.Blocks() as demo:
    gr.HTML(custom_css)  # inject CSS safely
    
    gr.HTML("""
        <div class="title-card">
            <h1>💖 Sentiment Analysis 💖</h1>
        </div>
    """)

    with gr.Column(elem_id="main-card"):
        txt = gr.Textbox(placeholder="Write something cute...", lines=5, label="")
        btn = gr.Button("Analyze ✨")
        output = gr.Textbox(label="Result")

        btn.click(sentiment_interface, inputs=txt, outputs=output)

demo.launch()
