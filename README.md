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

