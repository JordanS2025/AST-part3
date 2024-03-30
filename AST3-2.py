import json

def find_connection_and_return_package(node, package=None):
    # If this node contains the package information, extract it.
    if node.get('type') == 'CompilationUnit' and node.get('package') is not None:
        package = node['package'].get('name')
    
    # Determine if the current node is related to a "Connection".
    # You may need to adjust this condition depending on the structure of your nodes
    # and how they reference "Connection".
    if 'Connection' in node.get('name', '') or 'Connection' in node.get('path', ''):
        return package  # Return the package name if a "Connection" related node is found.

    # Recursively search through children nodes.
    for child_key in node:
        child = node[child_key]
        if isinstance(child, list):  # If the child is a list, iterate and recurse.
            for item in child:
                if isinstance(item, dict):
                    result = find_connection_and_return_package(item, package)
                    if result is not None:  # If a package name has been found, return it.
                        return result
        elif isinstance(child, dict):  # If the child is a dict, directly recurse.
            result = find_connection_and_return_package(child, package)
            if result is not None:  # Again, return if a package name has been found.
                return result

    return None  # Return None if no relevant node is found by the end of the traversal.


file_path = 'output_ast2.json'

# Load the JSON data from a file
with open(file_path, 'r') as file:
    ast = json.load(file)

create_statement_node = find_connection_and_return_package(ast)
print(f'Package: {create_statement_node}')