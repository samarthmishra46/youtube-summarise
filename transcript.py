from youtube_transcript_api import YouTubeTranscriptApi

# Extract video ID from YouTube URL
def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    return url.split("/")[-1]

# Get transcript
def get_transcript(video_url):
    video_id = get_video_id(video_url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Convert transcript to plain text
    transcript_text = "\n".join([t['text'] for t in transcript])
    return transcript_text

# Example usage

