# Youtube Transcript Summarization!!!
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
print("Give a Youtube Video Link:")
# Example Link :  https://www.youtube.com/watch?v=L0t69f8UcmU
youtube_video = input()
video_id = youtube_video.split("=")[1]
from IPython.display import YouTubeVideo
YouTubeVideo(video_id)
YouTubeTranscriptApi.get_transcript(video_id) 
transcript = YouTubeTranscriptApi.get_transcript(video_id)
result = ""
for i in transcript:
    result += ' ' + i['text']
print("Input Text: \n" + result)
print(len(result))
summarizer = pipeline('summarization')
num_iters = int(len(result)/1000)
summarized_text = []
print("\nSummarized text :\n")
for i in range(0, num_iters + 1):
  start = 0
  start = i * 1000
  end = (i + 1) * 1000
  out = summarizer(result[start:end],min_length=10 , max_length=45)
  out = out[0]
  out = out['summary_text']
  print(out)

