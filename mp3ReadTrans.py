import os
import whisper
import openai
import warnings
import torch

# Set device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Set DeepSeek API key and base URL
openai.api_key = "sk-e88c1d9f880c4d3391852bd54f63dad1"  # Please replace with your actual API key
openai.api_base = 'https://api.deepseek.com/v1'  # Ensure '/v1' is included

# Specify the model to use
model_name = 'deepseek-chat'  # Or 'deepseek-coder', depending on your need

# Load Whisper model (use a smaller model for faster processing)
whisper_model = whisper.load_model("small", device=device)

# Specify the folder path containing mp3 files
folder_path = "/home/rk/rockchip/biliVideo"  # Please replace with your actual folder path

# Ignore UserWarning warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Open the subtitles.txt file in write mode and set the encoding to utf-8
with open("subtitles.txt", "w", encoding="utf-8") as subtitle_file:
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Get the full path of the file
        file_path = os.path.join(folder_path, filename)
        # Check if the file is an mp3 file and is an actual file (not a folder)
        if os.path.isfile(file_path) and filename.lower().endswith(".mp3"):
            print(f"Processing {file_path} ...")
            # Use Whisper model to transcribe the audio file
            try:
                transcription_result = whisper_model.transcribe(
                    file_path, language='zh', verbose=True
                )
                transcribed_text = transcription_result["text"]
            except Exception as e:
                print(f"Transcription error: {e}")
                transcribed_text = "Transcription error."
                continue  # Skip the current file and proceed to the next

            print("Transcription completed, translating...")
            # Use DeepSeek API to translate the text
            try:
                response = openai.ChatCompletion.create(
                    model=model_name,
                    messages=[
                        {"role": "system", "content": "Please translate the following into Chinese:"},
                        {"role": "user", "content": transcribed_text}
                    ],
                    temperature=0.5,
                    max_tokens=2048
                )
                translated_text = response.choices[0].message.content.strip()
            except Exception as e:
                print(f"Translation error: {e}")
                translated_text = "Translation error."
    
            # Write the filename, original text, and translated text into the subtitles.txt file
            subtitle_file.write(f"Filename: {filename}\n")
            subtitle_file.write("Original text:\n")
            subtitle_file.write(transcribed_text + "\n")
            subtitle_file.write("Translation:\n")
            subtitle_file.write(translated_text + "\n\n")
            print(f"{filename} processing completed.\n")
