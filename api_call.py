import os
from dotenv import load_dotenv  # Import dotenv to load environment variables
import google.generativeai as genai

# Load environment variables from your .env or custom file
load_dotenv(dotenv_path='myenv_api_keys.env')  # Replace with your file name if necessary

# Now access the environment variable safely
api_key = os.getenv("GEMINI_API_KEY")

def getResponse(prompt):
  if not api_key:
      return "Error: GEMINI_API_KEY is not set!"
  else:
      # Configure the API key
      genai.configure(api_key=api_key)

      # Create the model configuration
      generation_config = {
          "temperature": 1,
          "top_p": 0.95,
          "top_k": 40,
          "max_output_tokens": 8192,
          "response_mime_type": "text/plain",
      }

      # Initialize the model
      model = genai.GenerativeModel(
          model_name="gemini-1.5-flash",
          generation_config=generation_config,
      )

      # Start a chat session
      chat_session = model.start_chat(
          history=[]
      )

      # Send a message and print the response
      response = chat_session.send_message(prompt)
      return response.text
