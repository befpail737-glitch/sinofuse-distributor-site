import os
import re

def minify_html(html_content):
    """
    Basic HTML minification by removing unnecessary whitespace and comments
    
    Args:
        html_content (str): HTML content to minify
        
    Returns:
        str: Minified HTML content
    """
    # Remove HTML comments (but preserve conditional comments)
    html_content = re.sub(r'<!--[^\\[](.*?)-->', '', html_content, flags=re.DOTALL)
    
    # Remove whitespace between tags
    html_content = re.sub(r'>\s+<', '><', html_content)
    
    # Remove leading and trailing whitespace
    html_content = html_content.strip()
    
    return html_content

def process_html_files(directory):
    """
    Process all HTML files in directory
    
    Args:
        directory (str): Directory containing HTML files
    """
    # Walk through directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                input_path = os.path.join(root, file)
                
                try:
                    # Read HTML file
                    with open(input_path, 'r', encoding='utf-8') as f:
                        html_content = f.read()
                    
                    # Minify HTML
                    minified_html = minify_html(html_content)
                    
                    # Write minified HTML back to file
                    with open(input_path, 'w', encoding='utf-8') as f:
                        f.write(minified_html)
                    
                    print(f"Minified: {input_path}")
                    
                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")

if __name__ == "__main__":
    # Process HTML files in root directory
    html_dir = r"C:\Users\ymlt\Desktop\sinofuse-distributor-site"
    
    if os.path.exists(html_dir):
        print("Starting HTML minification...")
        process_html_files(html_dir)
        print("HTML minification completed!")
    else:
        print(f"Directory not found: {html_dir}")