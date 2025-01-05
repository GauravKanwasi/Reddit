import praw
import random

def fetch_game_post():
    reddit = praw.Reddit(client_id='your_client_id',
                         client_secret='your_client_secret',
                         user_agent='your_user_agent')

    # Choose a gaming-related subreddit
    subreddit = reddit.subreddit('gaming')  # You can choose other gaming subreddits like 'r/gamingsetups', etc.
    posts = subreddit.hot(limit=5)  # Get the top 5 hot posts

    selected_post = random.choice(list(posts))

    # Get the URL of the image and video, and the post text
    post_image_url = selected_post.url if selected_post.url.endswith(('.jpg', '.png', '.gif')) else None
    post_video_url = selected_post.url if selected_post.url.endswith(('.mp4', '.webm')) else None
    post_text = selected_post.title + " " + selected_post.selftext

    return post_image_url, post_video_url, post_text

if __name__ == '__main__':
    post_image_url, post_video_url, post_text = fetch_game_post()
    print(f"Post Text: {post_text}")
    print(f"Image URL: {post_image_url}")
    print(f"Video URL: {post_video_url}")
