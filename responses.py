# responses.py
import random
import datetime

transaction_status = {"steps_completed": 0, "total_steps": 3}

# Function to generate a response based on the detected intent
def handle_intent(intent, user_input):
    global transaction_status
    if intent == "budget_inquiry":
        transaction_status["steps_completed"] += 1
        return "Thank you for sharing your budget. We’ll use this information to align with your requirements."
    elif intent == "service_inquiry":
        transaction_status["steps_completed"] += 1
        return "Could you provide more specifics about the service you're interested in?"
    elif intent == "detailed_info_request":
        transaction_status["steps_completed"] += 1
        return "For a smooth consultation, please have an idea of the service you need and any specific requirements."
    elif intent == "fallback":
        return "I'm sorry, I didn’t understand that. Can you rephrase or ask for 'help'?"
    else:
        return "I'm here to help with budget, service inquiries, and preparation details for our consultation."


# Personalize the chatbot greeting
def personalize_greeting():
    current_hour = datetime.datetime.now().hour
    greeting = "Good morning" if current_hour < 12 else "Good afternoon" if current_hour < 18 else "Good evening"
    return f"{greeting}! How can I assist you today?"

# Provide conversational markers
def conversational_marker():
    halfway = transaction_status["total_steps"] // 2
    if transaction_status["steps_completed"] == halfway:
        return "You're halfway there!"
    elif transaction_status["steps_completed"] == transaction_status["total_steps"] - 1:
        return "Only one step left!"
    return ""

# Track progress in a transaction
def track_progress():
    if transaction_status["steps_completed"] == transaction_status["total_steps"]:
        return "All steps are complete! Ready to finalize your request."
    steps_left = transaction_status["total_steps"] - transaction_status["steps_completed"]
    return f"You have {steps_left} step(s) left to complete your request."

def suggest_next_steps():
    return "You can ask about budgets, services, or consultation preparation. For example: 'What services do you provide?' or 'My budget is £500'."

