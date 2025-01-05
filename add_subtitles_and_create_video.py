from moviepy.editor import TextClip, concatenate_videoclips, AudioFileClip, VideoFileClip

def add_subtitles_to_video(video_clip, text, audio_file='audio.mp3'):
    # Create a text clip with subtitles
    text_clip = TextClip(text, fontsize=30, color='white', bg_color='black', size=(1920, 1080))
    text_clip = text_clip.set_duration(video_clip.duration).set_position('bottom').set_fps(24)
    
    # Load the audio file
    audio = AudioFileClip(audio_file)
    
    # Set the audio to the video
    video_clip = video_clip.set_audio(audio)
    
    # Overlay the text subtitles
    final_video = video_clip.overlay(text_clip)
    return final_video

def create_final_video(video_clip, output_file='final_video.mp4'):
    # Write the final video to a file
    video_clip.write_videofile(output_file, fps=24)

if __name__ == '__main__':
    video_clip = VideoFileClip('background_video.mp4')  # This would come from the prepare_video.py
    audio_file = 'audio.mp3'  # The audio generated from text
    post_text = 'This is a test post text from Reddit'

    # Add subtitles and combine audio/video
    final_video = add_subtitles_to_video(video_clip, post_text, audio_file)
    
    # Create the final video
    create_final_video(final_video)
