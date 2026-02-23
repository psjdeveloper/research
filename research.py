
import ast

code = """
x: int = 5
y: str = "hello"
z: int = "hi"
"""

# Parse the code into AST
tree = ast.parse(code)

for node in tree.body:
    if isinstance(node, ast.AnnAssign):
        var_name = node.target.id
        var_type = node.annotation.id
        
        # Safely evaluate the value without using eval
        # Only allow literals
        if isinstance(node.value, ast.Constant):
            value = node.value.value
            value_type = type(value).__name__
        else:
            value_type = "unknown"

        print(var_name, var_type, value_type)

        # Check type consistency
        if var_type != value_type:
            print(f"Type error: {var_name} should be {var_type} but got {value_type}")

