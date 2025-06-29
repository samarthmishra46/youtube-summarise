from youtube_transcript_api import YouTubeTranscriptApi
proxies = {
    "https://geo.brdtest.com/mygeo.json": "http://brd-customer-hl_4dc132b4-zone-residential_proxy1:bider3t3u7x2@brd.superproxy.io:33335"
}

YouTubeTranscriptApi._session.proxies = proxies
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

