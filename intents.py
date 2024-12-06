# intents.py
from preprocessing import preprocess_text

# Dictionary defining sample phrases for each intent category
intents = {
    "budget_inquiry": ["My budget is around 5000.", "How much does it cost?", "I have a budget of $3000.", "My budget is £100"],
    "service_inquiry": [
        "I need a website developed.",
        "I want an app for my business.",
        "Can you help with logo design?",
        "I need a web",
        "need a website",
        "need a website developed",
        "app"
    ],
    "detailed_info_request": ["What details do you need for the project?", "What should I prepare for the consultation?"],
    "fallback": ["help", "I don't understand", "Can you repeat?", "Not sure what I need."]
}


# Generate training data based on the defined intents
def prepare_training_data():
    X_train = []
    y_train = []
    for intent, phrases in intents.items():
        for phrase in phrases:
            X_train.append(preprocess_text(phrase))
            y_train.append(intent)
    return X_train, y_train
