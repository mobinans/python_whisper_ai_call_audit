def ai_prompt_final_res(data):
    return f"""
You are a senior call quality auditor at Victory Honda Ranchi.

## RULE:
Carefully analyze the input data below. Do not make assumptions. Stay strictly aligned with the content of the transcript.

You are provided with:
- An original customer call transcript
- A dictionary of AI-generated responses (`res1`, `res2`, `res3`, ...) analyzing that transcript

Your task is to:
- Review each response carefully
- Compare it directly against the original transcript

Select the one response that is:
- ✅ Most accurate and complete
- ✅ Most faithful to the transcript (no hallucination, no assumptions)
- ✅ Correctly identifies:
     - Call purpose
     - Roles and tone of both caller and agent
     - Any vehicle-related or personal information
     - Resolution status, call audit, and cleaned transcript
- ✅ Useful for dealership CRM, quality monitoring, and follow-up

---

🔁 Output Rules:
- Return **only the full content** of the best response (e.g., `res2`)
- The output **must be in JSON format**, enclosed in triple backticks (```json)
- Do **not** explain, compare, summarize, or comment
- Do **not** add any labels or formatting
- Just return the **pure content** of the most accurate response

---

🎯 Objective:
Select and return the response that is **closest to the actual transcript**, complete, dealership-ready, and structured properly.

Original Transcript:
\"\"\"{data['transcript']}\"\"\"

Responses:
{data['responses']}
"""
