import os
import xml.etree.ElementTree as ET

# Define the directories and file types to skip
skip_dirs = {'.git', 'venv', '__pycache__', 'cache'}
skip_files = {'.gitignore', '.gitattributes'}

# Define code file extensions and additional important file types to include
code_extensions = {
    '.py', '.js', '.html', '.css', '.java', '.c', '.cpp', '.go', '.ts', '.json', '.xml', '.yaml', '.yml',
    '.sh', '.bat', '.ini', '.conf', '.cfg', '.env', '.properties', '.sql', '.md', '.rb', '.pl', '.php'
}

# Also include certain files by name, regardless of extension
include_files = {'Dockerfile', 'Makefile', 'Vagrantfile', 'README', 'LICENSE', '.env'}

# Create the XML root
root = ET.Element("repository")

def is_code_file(file_name):
    # Check if the file has a recognized code-related extension or is in the include_files set
    return any(file_name.endswith(ext) for ext in code_extensions) or file_name in include_files

def add_to_xml_tree(parent, path, content):
    file_element = ET.SubElement(parent, "file")
    ET.SubElement(file_element, "path").text = path
    ET.SubElement(file_element, "content").text = content

def save_to_files(text_output, xml_output, base_directory):
    # Save text output
    text_file_path = os.path.join(base_directory, "repo-content.txt")
    xml_file_path = os.path.join(base_directory, "repo-content.xml")

    with open(text_file_path, 'w', encoding='utf-8') as f:
        f.write(text_output)

    # Save XML output
    tree = ET.ElementTree(xml_output)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

def generate_file_tree(directory, skip_dirs, skip_files):
    file_tree = []
    for root_dir, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in skip_dirs]  # Skip unwanted directories
        for file_name in files:
            if file_name in skip_files or not is_code_file(file_name):
                continue
            file_path = os.path.relpath(os.path.join(root_dir, file_name), directory)
            file_tree.append(file_path)
    return file_tree

def main():
    # Use the directory where the script is located as the base directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    text_output = []

    for root_dir, dirs, files in os.walk(current_dir):
        dirs[:] = [d for d in dirs if d not in skip_dirs]  # Skip unwanted directories

        for file_name in files:
            if file_name in skip_files or not is_code_file(file_name):
                continue

            file_path = os.path.relpath(os.path.join(root_dir, file_name), current_dir)
            text_output.append(f"--- {file_path} ---\n")

            with open(os.path.join(root_dir, file_name), 'r', encoding='utf-8') as f:
                content = f.read()
                text_output.append(content + "\n\n")
                add_to_xml_tree(root, file_path, content)

    # Generate the directory tree at the bottom of the file
    file_tree = generate_file_tree(current_dir, skip_dirs, skip_files)
    text_output.append("\n--- Directory Tree ---\n")
    for path in file_tree:
        text_output.append(path + "\n")

    # Save the outputs in the current directory
    save_to_files(''.join(text_output), root, current_dir)
    print(f"Output saved to {os.path.join(current_dir, 'repo-content.txt')} and {os.path.join(current_dir, 'repo-content.xml')}")

if __name__ == "__main__":
    main()
