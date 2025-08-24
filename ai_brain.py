# import os
# from dotenv import load_dotenv
# import base64

# load_dotenv()

# #Setup the Groq Key
# GROQ_API_KEY=os.environ.get("GROQ_API_KEY")


# # Convert image into required fromate
# # image_path="image.jpg"
# def image_encoder(image_path):
#     img=open(image_path,"rb")
#     base64_image=base64.b64encode(img.read()).decode("utf-8")
#     return base64_image

# # Setup Groq Model
# from groq import Groq
# # user_input="What is this image about?"
# def analyze_image(user_input,base64_image):
#     client = Groq()
#     model="meta-llama/llama-4-scout-17b-16e-instruct"
#     messages=[
#                 {
#                 "role": "user",
#                 "content": [
#                     {
#                     "type": "text", 
#                     "text":user_input
#                     },
#                     {
#                     "type": "image_url",
#                     "image_url": {
#                         "url":f"data:image/jpeg;base64,{base64_image}"
#                     }
#                     }
#             ]}
#         ]
        
#     completion = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=0.3
       
    
#     )


#     return completion.choices[0].message.content
 
import os
from dotenv import load_dotenv

load_dotenv()
#Setup grok API key
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
print("hello")
#setup Groq Model
from groq import Groq
def ask_text_model(user_input:str):
    client=Groq(api_key=GROQ_API_KEY)
    model="llama-3.1-8b-instant"
    messages=[
        {
        "role":"user",
        "content":user_input
        }
    ]
    
    completion=client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.3
        
    )
    return completion.choices[0].message.content

# if __name__=="__main__":
#     user_input="tell me about the lahore"
#     responce=ask_text_model(user_input=user_input)
#     print("Responce:",responce)