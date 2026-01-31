# import google.generativeai as genai


# # Configure Gemini API key
# #  Gemini API key is hidden for security purposes


# # Choose a model
# model = genai.GenerativeModel("models/gemini-2.5-pro")

# # Simple test prompt
# prompt = "Hello! Please respond as a polite NARS virtual assistant."

# try:
#     response = model.generate_content(prompt)
#     print("API Response:\n", response.text)
# except Exception as e:
#     print("Error:", e)
import google.generativeai as genai

# Configure Gemini API key

# Select a model
model = genai.GenerativeModel("models/gemini-2.5-flash-preview-05-20")

def check_api():
    """Check if Gemini API works."""
    test_prompt = "Hello! This is a test to check if API is working."
    try:
        response = model.generate_content(test_prompt)
        print("✅ API is working. Sample response:")
        print(response.text)
        return True
    except Exception as e:
        print("❌ API error:", e)
        return False

# Call check_api before user chat
if check_api():
    user_message = input("Enter your message: ")
    try:
        reply = model.generate_content(user_message)
        print("Gemini reply:", reply.text)
    except Exception as e:
        print("Error while generating reply:", e)
else:
    print("API not working. Please check your key or quota.")
