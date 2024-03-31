import json

def find_connection(node):
    if node is None:
        return None

    # Check if the node's name or path contains "Connection"
    if 'name' in node and node['name'] is not None and 'Connection' in node['name']:
        return node['name']
    elif 'path' in node and node['path'] is not None and 'Connection' in node['path']:
        return node['path']
    
    # Check the children nodes recursively.
    if isinstance(node, dict):
        for key, child in node.items():
            result = find_connection(child)
            if result:
                return result
    elif isinstance(node, list):
        for child in node:
            result = find_connection(child)
            if result:
                return result

    return None

def main():
    file_path = 'output_ast2.json'

    # Load the JSON data from a file
    with open(file_path, 'r') as file:
        ast = json.load(file)

    # Find the node containing "Connection" in the AST
    connection_node = find_connection(ast)

    if connection_node:
        print(f'Node containing "Connection" found: {connection_node}')
    else:
        print('No node containing "Connection" found in the AST.')

if __name__ == "__main__":
    main()
