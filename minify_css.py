import os
import re

def minify_css(css_content):
    """
    Minify CSS content by removing unnecessary whitespace and comments
    
    Args:
        css_content (str): CSS content to minify
        
    Returns:
        str: Minified CSS content
    """
    # Remove CSS comments (except conditional comments)
    css_content = re.sub(r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', '', css_content)
    
    # Remove whitespace around symbols
    css_content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css_content)
    
    # Remove whitespace at the start and end of lines
    css_content = re.sub(r'^\s+', '', css_content, flags=re.MULTILINE)
    css_content = re.sub(r'\s+$', '', css_content, flags=re.MULTILINE)
    
    # Remove extra spaces
    css_content = re.sub(r'\s+', ' ', css_content)
    
    # Remove semicolon before closing brace
    css_content = re.sub(r';}', '}', css_content)
    
    return css_content.strip()

def process_css_files(directory):
    """
    Process all CSS files in directory
    
    Args:
        directory (str): Directory containing CSS files
    """
    # Walk through directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.css'):
                input_path = os.path.join(root, file)
                
                try:
                    # Read CSS file
                    with open(input_path, 'r', encoding='utf-8') as f:
                        css_content = f.read()
                    
                    # Minify CSS
                    minified_css = minify_css(css_content)
                    
                    # Write minified CSS back to file
                    with open(input_path, 'w', encoding='utf-8') as f:
                        f.write(minified_css)
                    
                    print(f"Minified: {input_path}")
                    
                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")

if __name__ == "__main__":
    # Process CSS files in css directory
    css_dir = r"C:\Users\ymlt\Desktop\sinofuse-distributor-site\css"
    
    if os.path.exists(css_dir):
        print("Starting CSS minification...")
        process_css_files(css_dir)
        print("CSS minification completed!")
    else:
        print(f"Directory not found: {css_dir}")