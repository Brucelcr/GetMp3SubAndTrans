# GetMp3SubtitleAndTranslate

This script uses Whisper(developed by Openai) to get the subtitles from the video and translate it into English using  DeepSeek(AI Translating model)
* Can handle one or multiple videos

# Why creating this script?

The reason for creating this script is that I noticed there aren't many similar scripts available online. Typically, solutions either focus solely on translation or only on recognizing subtitles from videos. Moreover, most of the available solutions rely on outdated large models, leading to poor accuracy in both recognition and translation. Therefore, I decided to create my own script, using more up-to-date large models. 
Additionally, this script integrates both recognition and translation into a single process, significantly improving efficiency and reducing the complexity of deployment and use.

# Advantages of this model:

1. **Utilizes Whisper**: Whisper is currently one of the most advanced large models for speech recognition. It can accurately and quickly recognize subtitles from MP3 or WAV files and supports a wide range of languages. This model is developed by OpenAI and is fully open-source and free to use.

2. **Advanced translation with DeepSeek**: For translation, this script uses DeepSeek, which is also one of the most advanced translation models available today. It excels in translating Chinese to English and offers a significant improvement over older, mechanical translation models. Additionally, this model supports multiple languages.


I’ll check the contents of the file you uploaded and provide a guide for using and deploying it. Let me first look at the code.

Here’s a general guide on how to use and deploy the `mp3ReadTrans.py` file based on its content:


# How to run this script on your machine

Before running this script, make sure you have the following:

1. **Python 3.x installed** on your system.
2. **CUDA-enabled GPU** if you want to leverage GPU acceleration for faster Whisper model inference. Otherwise, it will default to CPU.
3. The following Python packages installed:
   - `torch`
   - `whisper`
   - `openai`

### Installation Instructions

1. **Install Python Dependencies:**

   First, install the necessary dependencies:

   ```bash
   pip install torch whisper openai
   ```

   Ensure that `ffmpeg` is installed on your system for handling audio files.

2. **Set Up API Keys:**

   Replace the placeholder in the script with your actual DeepSeek API key:

   ```python
   openai.api_key = "your-api-key-here"  # Replace with your API key
   ```

3. **Prepare Audio Files:**

   Store the MP3 files you want to process in the folder specified in the `folder_path` variable:

   ```python
   folder_path = "/path/to/your/audio/files"  # Modify to your actual directory
   ```

4. **Adjust Models:**

   The script uses Whisper's "small" model for transcription. You can adjust the model size based on your resource availability:

   ```python
   whisper_model = whisper.load_model("small", device=device)
   ```

   Replace `"small"` with other options like `"base"`, `"large"`, etc., for different speed/accuracy trade-offs.


## Usage Instructions

1. **Running the Script:**

   Execute the script with Python:

   ```bash
   python mp3ReadTrans.py
   ```

2. **Transcription and Translation:**

   - The script processes all MP3 files in the specified folder.
   - For each MP3 file, the script:
     1. Transcribes the audio to Chinese text using the Whisper model.
     2. Translates the transcription using the DeepSeek API via OpenAI.
     3. Writes both the original and translated text to a `subtitles.txt` file.

3. **Output:**

   The output for each file will be saved in a `subtitles.txt` file, which includes:
   - The original transcription
   - The translated text


### Notes:
- Ensure that you replace the default folder paths and API keys with your actual data.
- If you encounter any issues with CUDA, it might be due to GPU configuration. You can force CPU usage by setting `device = "cpu"` in the script.
- The script is designed to handle errors gracefully. If any file fails to transcribe or translate, it skips to the next file while logging the error.


### Deployment Suggestions

- **Local Deployment:**
  You can run the script directly on your local machine. Make sure the folder path to the MP3 files and API keys are correctly set up.

- **Cloud Deployment:**
  You can also deploy this script on cloud platforms like AWS, GCP, or Azure, where GPU instances (like AWS EC2 with a GPU) can significantly speed up the transcription process.


