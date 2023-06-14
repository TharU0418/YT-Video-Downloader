from flask import Flask,jsonify, request
import os
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

import googleapiclient.discovery

from pytube import YouTube

app = Flask(__name__)

CORS(app)

load_dotenv()

api_key = os.environ.get("API_KEY")
api_service_name = "youtube"
api_version = "v3"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey= api_key)
print("YT API connected.")


@app.route("/data", methods=['POST'])
@cross_origin()
def getLink():
    print("YouTube")
    link = request.get_json()
    usrLink = link["inputLink"]
    print('link', usrLink)

    vid_id = get_video_id(usrLink)
    print(vid_id)

    #vid_title = get_video_title(vid_id)
    #print(vid_title)

    #download_video(usrLink)

    # Add your logic to process the link here

    return jsonify({'vid_title': vid_id})  



def get_video_id(yt_url):

    youtube_hostnames = ("www.youtube.com", "youtube.com", "m.youtube.com", "youtu.be")
    parsed_url = urlparse(yt_url)

    if parsed_url.hostname in youtube_hostnames:
        query_params = parse_qs(parsed_url.query)

        if "v" in query_params:
            return query_params["v"[0]]
        elif parsed_url.path.startswith("/embed"):
            return parsed_url.path.split("/")[-1]
        elif parsed_url.hostname == "youtu.be":
            return parsed_url.path[1:]
    return None

def get_video_title(video_id):

    request = youtube.videos().list(id=video_id, part="snippet")
    response = request.execute()

    title = response["items"][0]["snippet"]["title"]
    channelTitle = response["items"][0]["snippet"]["channelTitle"]
    description = response["items"][0]["snippet"]["description"]
    publish_time = response["items"][0]["snippet"]["publish_time"]
    

    return title


def download_video(video_id):
    ytObject = YouTube(video_id)

    video = ytObject.streams.get_highest_resolution()

    video.download()

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))