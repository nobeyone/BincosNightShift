import cv2
import os
import sys
import numpy as np
from PIL import Image
import imagehash
from tqdm import tqdm  # Import tqdm for progress bar

def extract_unique_frames(video_path, output_dir, hash_size=8, hash_func='phash'):
    """
    Extracts unique frames from a video and saves them as PNG images.
    
    Args:
        video_path (str): Path to the input video file.
        output_dir (str): Directory where unique frames will be saved.
        hash_size (int, optional): Hash size for image hashing. Defaults to 8.
        hash_func (str, optional): Hash function to use ('ahash', 'phash', 'dhash', 'whash'). Defaults to 'phash'.
    """
    if not os.path.isfile(video_path):
        print(f"Error: Video file '{video_path}' not found.")
        return
    
    os.makedirs(output_dir, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Cannot open video '{video_path}'.")
        return
    
    frame_count = 0
    unique_count = 0
    hashes = set()
    
    hash_function = {
        'ahash': imagehash.average_hash,
        'phash': imagehash.phash,
        'dhash': imagehash.dhash,
        'whash': imagehash.whash
    }.get(hash_func, imagehash.phash)
    
    print("Processing video for unique frames...")
    
    # Get total frame count for progress bar
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Create a tqdm progress bar
    with tqdm(total=total_frames, desc="Processing frames", unit="frame") as pbar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            
            # Convert frame from BGR (OpenCV format) to RGB (PIL format)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            
            # Compute hash
            frame_hash = hash_function(pil_image, hash_size=hash_size)
            
            if frame_hash not in hashes:
                hashes.add(frame_hash)
                unique_count += 1
                # Save unique frame as PNG
                output_path = os.path.join(output_dir, f"frame_{unique_count:05d}.png")
                pil_image.save(output_path)
            
            # Update progress bar
            pbar.update(1)
    
    cap.release()
    print(f"Done! Total frames processed: {frame_count}. Unique frames saved: {unique_count}.")

# Example integration: running the function
if __name__ == "__main__":
    video_file = "blockbuster.mkv"
    output_directory = "unique_frames"
    
    extract_unique_frames(video_file, output_directory, hash_size=20, hash_func='phash')
