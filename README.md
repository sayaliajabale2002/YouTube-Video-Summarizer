# YouTube-Video-Summarizer


This Streamlit application leverages a LangGraph state workflow and the Google Gemini 2.5 Flash Lite model to automatically extract and summarize YouTube video transcripts into a concise overview, a detailed breakdown, and key takeaways. It uses the youtube-transcript-api to fetch the video's captions based on a user-provided URL, passes the text through a compiled state graph node sequence, invokes the LangChain-initialized chat model for structured summarization, and renders the final AI-generated response dynamically within an intuitive, web-based UI.

To get started:
1) Navigate into the project folder
2) Set up a Python virtual environment
3) Install the dependencies with pip install -r requirements.txt
4) Create a .env file in the root directory containing your GOOGLE_API_KEY=your-key-here
5) Launch the web application locally by running streamlit run app.py 
