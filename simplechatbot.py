!pip install google.genai
from google import genai
client = genai.Client(api_key="AQ.Ab8RN6IQpRHoEBiU-gJkLDLeezVTAFglMrpGK5dmGzSLxcM4FQ")

print("AI chatbot")
print("Hello! How can I help you today? TYPE 'BYE' TO EXIT")

while True:
  user_input = input("\nYou: ")
  if user_input.lower() == "bye":
    print("Chatbot: Goodbye!")
    break

  response = client.models.generate_content(
      model="gemini-3.8-flash",
      contents=user_input
  )
  print("Chatbot:", response.text)
