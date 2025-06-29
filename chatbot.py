from google import genai
import os
import transcript
# Ensure you have set the GOOGLE_API_KEY environment variable
cmd="YOU ARE A HELPFUL ASSISTANT.YOU ARE A GREAT NOTE MAKER AND MAKE WONDERFUL AND EASY TO LEARN NOTES WHICH ARE WELL STRUCTURED FOR A STUDENT AND PROFESSIONALS .SO THIS IS THE YOUTUBE VIDEO CAPTION FROM WHICH YOU HAVE TO GENRATE NOTES FOR EVEY TOPIC THAT IS TAUGHT HERE IF YOU CAN ADD SOMETHING PLEASE ADD SO THAT IT SHOULD BE CLEAR AND YES DONT WRITE ANY MESSAGES LIKE HERE IS HERE IS YOUR NOTES ETC. JUST START THE ANSWER. {prompt}"
def res(prompt: str):
    transcript_text = transcript.get_transcript(prompt)
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=cmd.format(prompt=transcript_text)
    )
    return response

print(res("https://www.youtube.com/watch?v=vVYlCnNjEWA"))