import json

# Define a function that generates Python code for a class
def generate_class_code(class_name, attributes):
    class_code = f"class {class_name}:\n"
    class_code += "    def __init__(self, " + ", ".join([f"{attr}: {type_}" for attr, type_ in attributes.items()]) + "):\n"
    for attr in attributes:
        class_code += f"        self.{attr} = {attr}\n"
    class_code += "\n"
    return class_code

# Load the model from a JSON file
with open('model.json', 'r') as f:
    model = json.load(f)

# Generate Python code for each class in the model
generated_code = ""
for class_info in model['classes']:
    class_name = class_info['name']
    attributes = class_info['attributes']
    class_code = generate_class_code(class_name, attributes)
    generated_code += class_code

# Output the generated code to a Python file
with open('generated_classes.py', 'w') as f:
    f.write(generated_code)

print("Classes have been generated and saved to 'generated_classes.py'.")
