import os
import subprocess
import sys

def run_performance_optimization():
    """
    Run all performance optimization scripts
    """
    scripts = [
        ("compress_images.py", "Starting image compression..."),
        ("minify_css.py", "Starting CSS minification..."),
        ("minify_js.py", "Starting JavaScript minification..."),
        ("minify_html.py", "Starting HTML minification...")
    ]
    
    for script, message in scripts:
        script_path = os.path.join(os.path.dirname(__file__), script)
        if os.path.exists(script_path):
            print(message)
            try:
                result = subprocess.run([sys.executable, script_path], 
                                      cwd=os.path.dirname(__file__),
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"Completed: {script}")
                else:
                    print(f"Error in {script}: {result.stderr}")
            except Exception as e:
                print(f"Failed to run {script}: {str(e)}")
        else:
            print(f"Script not found: {script}")

if __name__ == "__main__":
    print("Starting comprehensive performance optimization...")
    run_performance_optimization()
    print("Performance optimization completed!")