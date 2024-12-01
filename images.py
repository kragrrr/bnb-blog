import os
import re
import shutil

# Paths
posts_dir = "/Users/krish/Documents/Obsidian Vault/posts"
attachments_dir = "/Users/krish/Documents/Obsidian Vault/attachments"
static_images_dir = "/Users/krish/Development/bnb-blog/static/images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            # markdown_image = f"![Image Description](/attachments/{image.replace(' ', '%20')})"
            # content = content.replace(f"![Image Description]({image})", markdown_image)
            markdown_image = f"[Image Description](/attachments/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            print(f"Processing image: {image}")
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")