import json
from g4f.client import Client
client = Client()


def find_create_statement(node, path=''):
    # Ensure node is a dictionary or list before proceeding
    if not isinstance(node, (dict, list)):
        return None

    if isinstance(node, dict):
        # Check for MethodInvocation with createStatement member
        if node.get('type') == 'MethodInvocation' and node.get('member') == 'createStatement':
            # Storing value if they are found in the AST
            member = 'createStatement'
            Domain = 'Connections'
            # Build the descriptive string for createStatement
            create_statement_str = f"MethodInvocation: createStatement found at {path}"
            # Assuming createStatement implies a Connection, build its description
            connection_str = f"Associated Connection object assumed at {path}"
            return create_statement_str, connection_str, member, Domain 

        # Recursively check dictionary children, updating path for accurate location
        for key, child in node.items():
            new_path = f"{path}/{key}" if path else key
            result = find_create_statement(child, new_path)
            if result:
                return result
    elif isinstance(node, list):
        # Recursively check list items, updating path for index
        for index, child in enumerate(node):
            new_path = f"{path}/{index}"
            result = find_create_statement(child, new_path)
            if result:
                return result

    return None

messages = [
    {"role": "system",
     "content": "You are attempting to classify the inputted description into one of the 31 labels based off of the similarity to it."},
    {"role": "system",
     "content": "As you guess this, your final response should only be one concise paragraph with the label chosen and why."},
    {"role": "system",
     "content": "Answer in the format of: Label: given label of this description"
                                        "Reason: reason why this label was chosen"}
]

def ask_gpt(classname, domainname):
    # Construct the prompt with the object description and option descriptions
    prompt = "Can you provide a "
    prompt += f" summary of this function: {classname}\n"
    prompt += " that is found "
    prompt += f"in the: {domainname}\n"
    prompt += f"class? Can you also make the summary a short paragraph?"
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        stream=True
    )
    return response

def main():
    file_path = '/Users/bignola/Documents/GitHub/AST-part3/output_ast2.json'

    # Load the JSON data from a file
    with open(file_path, 'r') as file:
        ast = json.load(file)

    # Find createStatement and its Connection, capturing their descriptions
    result = find_create_statement(ast)

    if result:
        create_statement_str, connection_str, member, Domain = result
        print('A "createStatement" method invocation connected to a "Connection" object was found in the AST.')
        print(create_statement_str)
        print(connection_str)
        print ( '------------')
        gpt_response = ask_gpt(member, Domain)
        counter = 0
        answer = ""
        for chunk in gpt_response:
            if chunk.choices[0].delta.content:
                answer += (chunk.choices[0].delta.content.strip('*') or "")
        print(answer)
    else:
        print('No "createStatement" method invocation connected to a "Connection" object found in the AST.')

if __name__ == "__main__":
    main()
