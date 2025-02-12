import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load a pre-trained Hugging Face model using the pipeline
chatbot = pipeline("text-generation", model="gpt2")

# Define healthcare-specific response logic
def healthcare_chatbot(user_input):
    # Simple rule-based keywords to respond
    if "symptom" in user_input.lower():
        return "🤒 It sounds like you have some symptoms. Could you describe them in more detail? I can try to guide you!"
    elif "appointment" in user_input.lower():
        return "📅 Sure! Would you like to book an in-person or virtual appointment?"
    elif "medication" in user_input.lower():
        return "💊 Always follow your prescribed medication schedule. Do you need information about a specific medicine?"
    elif "fever" in user_input.lower():
        return "🌡️ If you have a fever, make sure to stay hydrated and rest. Have you checked your temperature recently?"
    elif "back pain" in user_input.lower():
        return "🧘 Back pain can be relieved by stretching and maintaining good posture. Would you like some exercise recommendations?"
    elif "headache" in user_input.lower():
        return "🤕 Try drinking water and resting in a quiet room. If it's a migraine, does light or noise make it worse?"
    elif "cold" in user_input.lower():
        return "🤧 Colds usually go away on their own. Have you been experiencing a sore throat or cough as well?"
    else:
        # For other inputs, use the Hugging Face model to generate a response
        response = chatbot(user_input, max_length=50, num_return_sequences=1)
        generated_text = response[0]['generated_text']
        
        # Check if the generated response is relevant
        if "fever" in generated_text.lower() or "symptom" in generated_text.lower():
            return "🤖 AI Response: " + generated_text
        else:
            return "I'm not quite sure about that. Can you rephrase or provide more details? 🤔"

# Streamlit web app interface
def main():
    # Set up the web app title and input area
    st.title("Healthcare Assistant Chatbot")
    
    # Display a simple text input for user queries
    user_input = st.text_input("How can I assist you today?", "")
    
    # Display chatbot response
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
