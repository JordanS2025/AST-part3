from g4f.client import Client
import nest_asyncio
from collections import Counter
import re
nest_asyncio.apply()

client = Client()
messages = [
    {"role": "system",
     "content": "You are attempting to classify the inputted description into one of the 31 labels based off of the similarity to it."},
    {"role": "system",
     "content": "As you guess this, your final response should only be one concise paragraph with the label chosen and why."},
    {"role": "system",
     "content": "Answer in the format of: Label: given label of this description"
                                        "Reason: reason why this label was chosen"}
]


def ask_gpt(class_description, label_options):
    # Construct the prompt with the object description and option descriptions
    prompt = "Does this class description: "
    prompt += f"Object Description: {class_description}\n"
    prompt += " more fit with which of these options: "
    prompt += f"Options: {label_options}\n"
    prompt += f"and give the best 3 domain names with description."
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        stream=True
    )
    return response

# Function to preprocess text (simple version)
def preprocess_text(text):
    return re.sub(r'\s+', ' ', text).lower()  # Simple normalization

# Function to calculate domain similarity
def calculate_similarity(text):
    preprocessed_text = preprocess_text(text)
    word_counts = Counter(preprocessed_text.split())
    
    domain_scores = {}
    total_keywords = sum(len(keywords) for keywords in options.values())
    for domain, keywords in options.items():
        score = sum(word_counts.get(word.lower(), 0) for word in keywords)
        domain_scores[domain] = score
    
    # Normalize scores to be between 0 and 1
    max_score = max(domain_scores.values(), default=1)
    domain_similarity = {domain: score / max_score for domain, score in domain_scores.items()}
    
    return domain_similarity


# Javax.sql.Connection description
description = "A connection (session) with a specific database."
# Labels and their descriptions
options = {
    "Application": "third party apps or plugins for specific use attached to the system",
    "Application Performance Manager": "monitors performance or benchmark",
    "Big Data": "API's that deal with storing large amounts of data. with variety of formats",
    "Cloud": "APUs for software and services that run on the Internet",
    "Computer Graphics": "Manipulating visual content",
    "Data Structure": "Data structures patterns (e.g., collections, lists, trees)",
    "Databases": "Databases or metadata",
    "Software Development and IT": "Libraries for version control, continuous integration and continuous delivery",
    "Error Handling": "response and recovery procedures from error conditions",
    "Event Handling": "answers to event like listeners",
    "Geographic Information System": "Geographically referenced information",
    "Input/Output": "read, write data",
    "Interpreter": "compiler or interpreter features",
    "Internationalization": "integrate and infuse international, intercultural, and global dimensions",
    "Logic": "frameworks, patterns like commands, controls, or architecture-oriented classes",
    "Language": "internal language features and conversions",
    "Logging": "log registry for the app",
    "Machine Learning": "ML support like build a model based on training data",
    "Microservices/Services": "Independently deployable smaller services. Interface between two different applications so that they can communicate with each other",
    "Multimedia": "Representation of information with text, audio, video",
    "Multithread": "Support for concurrent execution",
    "Natural Language Processing": "Process and analyze natural language data",
    "Network": "Web protocols, sockets RMI APIs",
    "Operating System": "APIs to access and manage a computer's resources",
    "Parser": "Breaks down data into recognized pieces for further analysis",
    "Search": "API for web searching",
    "Security": "Crypto and secure protocols",
    "Setup": "Internal app configurations",
    "User Interface": "Defines forms, screens, visual controls",
    "Utility": "third party libraries for general use",
    "Test": "test automation"
}
gpt_response = ask_gpt(description, options)
counter = 0
answer = ""
for chunk in gpt_response:
    if chunk.choices[0].delta.content:
        answer += (chunk.choices[0].delta.content.strip('*') or "")
print(answer)

similarity_scores = calculate_similarity(description)

for domain, score in similarity_scores.items():
    print(f"{domain}: {score}")
