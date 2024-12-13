import os

def find_checkpoints(base_path="/"):
    for root, dirs, files in os.walk(base_path):
        for dir in dirs:
            if dir.startswith("llama_model"):
                print(f"Found checkpoint: {os.path.join(root, dir)}")

find_checkpoints("C:\\")  

# Use "/" for Linux/Mac or "C:\\" for Windows