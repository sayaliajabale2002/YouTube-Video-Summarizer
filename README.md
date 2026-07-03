# YouTube-Video-Summarizer


This Streamlit application leverages a LangGraph state workflow and the Google Gemini 2.5 Flash Lite model to automatically extract and summarize YouTube video transcripts into a concise overview, a detailed breakdown, and key takeaways. It uses the youtube-transcript-api to fetch the video's captions based on a user-provided URL, passes the text through a compiled state graph node sequence, invokes the LangChain-initialized chat model for structured summarization, and renders the final AI-generated response dynamically within an intuitive, web-based UI.
