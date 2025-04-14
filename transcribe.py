import whisper
import os
from openai import OpenAI
import asyncio
import gdown
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#whisper model path
# "C:\Users\mobin\.cache\whisper"

#Install whisper AI model
# pip install openai-whisper

#create virtual enviroment env
# python3.10 -m venv whisper-env

#to activate virtual enviroment cmd
# whisper-env\Scripts\activate

#to run the specific Python file
# python transcribe.py

async def whisperData(audio_name):
    # audio_path = os.path.join(r"C:\audio", audio_name)  # Make sure the file exists
    
    gdown.download(audio_name, "audio.mp3", quiet=False)
    
    model = whisper.load_model("medium") # Or 'small', 'medium', 'large'
    audio = whisper.load_audio("audio.mp3")
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    _, probs = model.detect_language(mel)
    lang = max(probs, key=probs.get)
    result = model.transcribe("audio.mp3", language=lang, task="translate")
    outcome = result["text"] # result = model.transcribe("audiotest.mp3", language="hi", task="transcribe")
    # print(result["text"])
    await asyncio.sleep(1)
    return outcome


async def openAIFunc(prompt):
    #initialize the OpenAI Client
    my_api_key = api_key
    client = OpenAI(api_key=my_api_key)  # Replace with your real API key
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # "gpt-3.5-turbo" or "gpt-4"
    messages=[
        {"role": "user", 
         "content": prompt
         }
    ]) 
    # print(response.choices[0].message.content)
    return response.choices[0].message.content
    
asyncio.run(openAIFunc())