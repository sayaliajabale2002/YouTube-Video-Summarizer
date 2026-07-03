from youtube_transcript_api import YouTubeTranscriptApi
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
import streamlit as st
import shutil 

st.title("YouTube Video Summarizer")

load_dotenv()

class State(TypedDict):
    video_url : str
    context: str
    summary : str


# # Extract Transcript
def get_transcript(state: State):
    #extracting video id
    url = state["video_url"]
    if"v=" in url:
        video_id = url.split("v=")[1]

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)
    # text_list = []
    # for item in transcript:
    #     text_list.append(item["text"])
    # text = " ".join(text_list)

    context = " ".join([item.text for item in transcript])
    return {"context" : context}


# LLM MODEL
llm_model = init_chat_model(model="gemini-2.5-flash-lite",model_provider="google-genai")

def summarize_text(state: State):
    prompt = f'''
    Summarize the following transcript.

    Provide:
    1. Short Summary
    2. Detaied Summary
    3. Key Takeaways

    from Transcript: {state["context"]}
    '''

    response = llm_model.invoke(prompt)
    return {"summary": response}

graph = StateGraph(State)
graph.add_node("transcript",get_transcript)
graph.add_node("summary",summarize_text)
graph.add_edge(START,"transcript")
graph.add_edge("transcript","summary")
graph.add_edge("summary",END)

agent = graph.compile()

# # url = {"video_url": "https://www.youtube.com/watch?v=nBpPe9UweWs"}
# # https://www.youtube.com/watch?v=JzPfMbG1vrE
# # summary = agent.invoke(url)
# # print(summary)

urlinput = st.text_input("YouTube URL...")
if st.button("Get Summary"):
    if urlinput is not None:
        url = {"video_url": urlinput}
        summary = agent.invoke(url)
        st.write(summary["summary"].content)

