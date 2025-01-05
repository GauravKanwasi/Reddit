# Funny Gaming Video Generator

## Overview
This project automates the creation of **funny gaming videos** by combining content from **Reddit posts**, converting **text** into **speech**, and adding **background videos** and **subtitles**. It pulls random posts from gaming-related subreddits, converts the text into a voiceover, and produces a video with the extracted text, an image or video overlay, and synchronized subtitles.

## Features
- Fetches random posts from a **gaming-related subreddit** (e.g., `r/gaming`).
- Converts the post text into **speech** using Google Cloud Text-to-Speech.
- Downloads the **background video** and **image overlay** from Reddit (if available).
- Adds **subtitles** based on the Reddit post’s text.
- Combines all elements into a **final video** with audio, background video, and subtitles.

## Components
This project is divided into the following components:

1. **`fetch_reddit_data.py`**  
   - Fetches a random post from a gaming subreddit.
   - Extracts the **text** (title and selftext), **image URL**, and **video URL** (if available) from the post.

2. **`text_to_speech.py`**  
   - Converts the extracted Reddit post text into **speech** using Google Cloud Text-to-Speech.
   - Saves the audio as `audio.mp3`.

3. **`prepare_video.py`**  
   - Downloads and prepares the **background video** (either from Reddit or a default video).
   - Downloads and resizes the **image** for overlay if the Reddit post contains an image.

4. **`add_subtitles_and_create_video.py`**  
   - Adds **subtitles** to the background video based on the Reddit post text.
   - Combines the **background video**, **image overlay**, **audio**, and **subtitles** into the final video file (`final_video.mp4`).

## Requirements
- **Python 3.6+**
- **Google Cloud Text-to-Speech API** (for text-to-speech functionality)
- **Pillow** (for image handling)
- **MoviePy** (for video creation and editing)
- **PRAW** (Python Reddit API Wrapper)
- **Requests** (for downloading images and videos)

You can install the required packages with:


## Setup and Usage

1. **Set up Google Cloud Text-to-Speech**:
   - Create a project on [Google Cloud](https://console.cloud.google.com/).
   - Enable the **Text-to-Speech API**.
   - Download the **API credentials** (a `.json` file) and set the environment variable:
     ```
     export GOOGLE_APPLICATION_CREDENTIALS="path_to_your_credentials.json"
     ```

2. **Run the Scripts**:
   - **Step 1**: Fetch Reddit data:
     ```
     python fetch_reddit_data.py
     ```
     This will output a random Reddit post's text, image URL, and video URL.

   - **Step 2**: Convert the Reddit post text to speech:
     ```
     python text_to_speech.py
     ```
     This will generate an `audio.mp3` file from the Reddit post's text.

   - **Step 3**: Prepare the background video and image overlay:
     ```
     python prepare_video.py
     ```
     This will download and prepare the background video and image overlay.

   - **Step 4**: Add subtitles and combine everything into a final video:
     ```
     python add_subtitles_and_create_video.py
     ```
     This will generate the `final_video.mp4` file with the Reddit post's text as subtitles, a background video, and an audio voiceover.

## Final Output
The result of this project will be a funny gaming video with:
- **Voiceover**: The Reddit post’s text read aloud.
- **Subtitles**: The post’s text displayed as subtitles on the video.
- **Background Video**: A gameplay video (either from Reddit or default).
- **Image Overlay**: If the Reddit post contains an image, it will be added to the video.

The final video is saved as `final_video.mp4`.

## Customization
- You can change the subreddit to target specific types of posts by modifying the `fetch_reddit_data.py` script.
- The background video can be customized by changing the default video or modifying the script to fetch specific types of gameplay videos.
- You can adjust the voice, language, and tone of the text-to-speech voice by modifying the `text_to_speech.py` script.

## Contributing
Feel free to open an issue or submit a pull request if you'd like to improve or contribute to this project!
