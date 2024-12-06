# classifier.py
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from intents import prepare_training_data
from preprocessing import preprocess_text

# Initialize the vectorizer and transformer
vectorizer = CountVectorizer()
tfidf_transformer = TfidfTransformer()
classifier = None

# Function to train the classifier
def train_classifier():
    global classifier
    X_train, y_train = prepare_training_data()
    X_train_counts = vectorizer.fit_transform(X_train)
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    classifier = LogisticRegression()
    classifier.fit(X_train_tfidf, y_train)

# Function to predict intent from user input
def predict_intent(user_input):
    processed_input = preprocess_text(user_input)
    input_counts = vectorizer.transform([processed_input])
    input_tfidf = tfidf_transformer.transform(input_counts)
    return classifier.predict(input_tfidf)[0]

# Function to evaluate the classifier
def evaluate_classifier(X_test, y_test):
    y_pred = classifier.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("F1-Score:", f1_score(y_test, y_pred, average='weighted'))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
