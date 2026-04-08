import os
import re

def minify_js(js_content):
    """
    Basic JavaScript minification by removing comments and extra whitespace
    
    Args:
        js_content (str): JavaScript content to minify
        
    Returns:
        str: Minified JavaScript content
    """
    # Remove single-line comments (but preserve URLs and regex)
    lines = js_content.split('\n')
    new_lines = []
    
    for line in lines:
        # Skip empty lines
        if line.strip() == '':
            continue
            
        # Remove inline comments but preserve string literals
        in_string = False
        string_char = ''
        new_line = ''
        i = 0
        
        while i < len(line):
            char = line[i]
            
            # Handle string literals
            if char in ('"', "'", '`') and (i == 0 or line[i-1] != '\\'):
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                    string_char = ''
                    
            # Remove comments if not in string
            elif char == '/' and not in_string and i + 1 < len(line) and line[i+1] == '/':
                break  # Skip the rest of the line
                
            # Remove block comments if not in string
            elif char == '/' and not in_string and i + 1 < len(line) and line[i+1] == '*':
                # Find end of block comment
                end_index = line.find('*/', i + 2)
                if end_index != -1:
                    i = end_index + 1  # Skip past the comment
                else:
                    # Comment continues to next line, skip current line
                    break
                    
            else:
                new_line += char
                
            i += 1
            
        # Add non-empty lines
        if new_line.strip() != '':
            new_lines.append(new_line.strip())
    
    # Join lines with semicolons where needed
    minified = ';'.join(new_lines)
    
    # Remove extra spaces around operators
    minified = re.sub(r'\s*([=+\-*/<>!&|{}()\[\];:,])\s*', r'\1', minified)
    
    # Remove extra whitespace
    minified = re.sub(r'\s+', ' ', minified)
    
    return minified.strip()

def process_js_files(directory):
    """
    Process all JavaScript files in directory
    
    Args:
        directory (str): Directory containing JavaScript files
    """
    # Walk through directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.js') and not file.endswith('.min.js'):
                input_path = os.path.join(root, file)
                
                try:
                    # Read JavaScript file
                    with open(input_path, 'r', encoding='utf-8') as f:
                        js_content = f.read()
                    
                    # Minify JavaScript
                    minified_js = minify_js(js_content)
                    
                    # Write minified JavaScript to new file
                    output_path = input_path.replace('.js', '.min.js')
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(minified_js)
                    
                    print(f"Minified: {input_path} -> {output_path}")
                    
                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")

if __name__ == "__main__":
    # Process JavaScript files in js directory
    js_dir = r"C:\Users\ymlt\Desktop\sinofuse-distributor-site\js"
    
    if os.path.exists(js_dir):
        print("Starting JavaScript minification...")
        process_js_files(js_dir)
        print("JavaScript minification completed!")
    else:
        print(f"Directory not found: {js_dir}")