from langchain_community.tools import YouTubeSearchTool

youtube = YouTubeSearchTool()

result = youtube.run("Melhores momentos Palmeiras 2023")

print(result)
