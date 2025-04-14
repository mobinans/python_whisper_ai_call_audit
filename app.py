from transcribe import whisperData, openAIFunc
from ai_prompt import get_call_analysis_prompt
from ai_prompt_for_final_res import ai_prompt_final_res

import asyncio

async def app():
    link = "https://drive.google.com/uc?export=download&id=1qlVs-btsLq8cA4b28edhtlDOh9cAdspx"
    callingContent = await whisperData(link)
    print("START")
    
    responses_from_ai = {}
    
    for i in range(5):
        response = await openAIFunc(get_call_analysis_prompt(callingContent))
        responses_from_ai[f"res{i+1}"] = response
        
    collected_data = {"transcript": callingContent, "responses":responses_from_ai}
    final_response = await openAIFunc(ai_prompt_final_res(collected_data))
    print(final_response)
    
    print("END")
    
asyncio.run(app())