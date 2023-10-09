# langchain youtube searcher tool
# Get to the url and scrape some useful info
# Use streamlit to present the info



#! pip install youtube_search
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import requests
from ast import literal_eval

from langchain.tools import YouTubeSearchTool
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms import OpenAI



def get_video_infos(video_id):
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={os.environ["GOOGLE-API-KEY"]}'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()

            video_name = data['items'][0]['snippet']['localized']['title']
            thumbnails = data['items'][0]['snippet']['thumbnails']
            thumbnail_url = thumbnails['high']['url']
            
            view_count = data['items'][0]['statistics']['viewCount']
            like_count = data['items'][0]['statistics']['likeCount']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            # dislike_count = data['items'][0]['statistics']['dislikeCount']
        except:
            0
    else:
        0
    return {
        'video_name': video_name, 
        'view_count': view_count, 
        'like_count': like_count, 
        'thumbnail_url': thumbnail_url,
        'video_url': video_url
        }






def get_youtube_videos_with_prompt(prompt):
    tool = YouTubeSearchTool()

    tools = [
        Tool(
            name="Search",
            func=tool.run,
            description="useful for when you need to give links to youtube videos. Remember to return exactly 3 video ids as a python list.",
        )
    ]


    agent = initialize_agent(
        tools,
        OpenAI(temperature=0.5, openai_api_key=os.environ["OPENAI-API-KEY"]),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Get video ids as a list
    video_list = agent.run(prompt)
    video_list = literal_eval(video_list)

    # Scrape video info
    video_infos = []
    for video_id in video_list:
        try:
            video_infos.append(get_video_infos(video_id))
        except Exception as e:
            print(str(e), f'for video_id: {video_id}')


    return video_infos


if __name__ == "__main__":
    prompt = "Find some cool videos about cats"
    video_infos = get_youtube_videos_with_prompt(prompt)
    print(video_infos)