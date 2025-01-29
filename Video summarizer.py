import streamlit as st 
from phi.agent import Agent 
from phi.model.google import Gemini 
from phi.tools.duckduckgo import DuckDuckGo
import google.generativeai as genai
from google.generativeai import upload_file,get_file

import os
import time
import tempfile
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    pass

st.set_page_config(
    page_title="Multimodel AI Agent - Video Summarizer",
    page_icon="",
    layout="wide"
)

st.title("Phidata Multimodel Video AI Agent")
st.header("Powered by Gemini 2.0 Flash Exp")

@st.cache_resource

def initialize_agent():
    return Agent(
        name="Video Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo(news=True,search=True)],
        markdown=True
    )
multimodel_agent = initialize_agent()

video_file = st.file_uploader(
    label="Upload a video file",
    type=["mp4","mov","avi"],
    help="Upload a video for AI Anlaysis",
)