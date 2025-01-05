import requests
from moviepy.editor import VideoFileClip, ImageClip
from PIL import Image
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def prepare_background_video(post_video_url=None, default_video='default_gameplay_video.mp4'):
    if post_video_url:
        # Load the provided background video (if available)
        video_clip = VideoFileClip(post_video_url)
    else:
        # If no video, use a default video
        video_clip = VideoFileClip(default_video)
    
    video_clip = video_clip.resize(height=1080)
    return video_clip

def prepare_image_overlay(post_image_url=None):
    if post_image_url:
        # If there is an image in the post, download it
        img = download_image(post_image_url)
        img.save('post_image.jpg')
        image_clip = ImageClip('post_image.jpg')
        image_clip = image_clip.set_duration(10).resize(height=200).set_position(('center', 'top'))
        return image_clip
    return None

if __name__ == '__main__':
    # Example usage:
    video_clip = prepare_background_video()
    image_clip = prepare_image_overlay(post_image_url='https://someimage.url')
    video_clip.preview()
