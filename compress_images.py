import os
from PIL import Image
import pillow_avif

def compress_image(input_path, output_path, quality=85):
    """
    Compress image and convert to WebP format
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path to output compressed image
        quality (int): Compression quality (1-100)
    """
    try:
        # Open image
        with Image.open(input_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                # For images with transparency, convert to RGBA
                if img.mode == 'P':
                    img = img.convert('RGBA')
                
                # Save as WebP with transparency
                img.save(output_path.replace('.jpg', '.webp').replace('.png', '.webp'), 
                        'WEBP', quality=quality, lossless=False, method=6)
            else:
                # Convert to RGB for better compression
                img = img.convert('RGB')
                # Save as WebP
                img.save(output_path.replace('.jpg', '.webp').replace('.png', '.webp'), 
                        'WEBP', quality=quality, lossless=False, method=6)
                
        print(f"Compressed: {input_path} -> {output_path.replace('.jpg', '.webp').replace('.png', '.webp')}")
        return True
        
    except Exception as e:
        print(f"Error compressing {input_path}: {str(e)}")
        return False

def process_images_in_directory(directory):
    """
    Process all images in directory
    
    Args:
        directory (str): Directory containing images
    """
    # Supported image extensions
    extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif')
    
    # Walk through directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                input_path = os.path.join(root, file)
                output_path = os.path.join(root, file)
                
                # Compress image
                compress_image(input_path, output_path)

if __name__ == "__main__":
    # Process images in assets directory
    assets_dir = r"C:\Users\ymlt\Desktop\sinofuse-distributor-site\assets\images"
    
    if os.path.exists(assets_dir):
        print("Starting image compression...")
        process_images_in_directory(assets_dir)
        print("Image compression completed!")
    else:
        print(f"Directory not found: {assets_dir}")