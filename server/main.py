from flask import Flask,jsonify, request
import os
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs

import googleapiclient.discovery

from pytube import YouTube

import re
import datetime

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
    #validelink(link)
    print("YouTube")
    link = request.get_json()
    usrLink = link["inputLink"]
    #vquality = link['videoQuality']
    print('link', usrLink)

    

    vid_id = get_video_id(usrLink)
    print(vid_id)

    vid_title = get_video_title(vid_id)
    print(vid_title)

    thumbnail_url = get_video_img(vid_id)
    print(thumbnail_url)

    

    # Add your logic to process the link here

    results = {'Vid_title': vid_title,
            'Thumbnail_url':thumbnail_url}
    
    #download_video(usrLink,vquality)
    
    return jsonify(results)

@app.route("/data2", methods=['POST'])
@cross_origin()
def getLink2():
    print("YouTube")
    link = request.get_json()
    #validelink(link)
    usrLink = link["inputLink"]
    vquality = link['videoQuality']
    print('link', usrLink)

    

    vid_id = get_video_id(usrLink)
    print(vid_id)

    vid_title = get_video_title(vid_id)
    print(vid_title)

    thumbnail_url = get_video_img(vid_id)
    print(thumbnail_url)

    

    # Add your logic to process the link here

    results = {'Vid_title': vid_title,
            'Thumbnail_url':thumbnail_url}
    
    download_video(usrLink,vquality)

    print("down")
    
    return jsonify(results)



@app.route('/extenstion', methods=['GET'])
def extentionResult():

    print('Extenstion 📧📧')
    input_link = request.args.get('userinput', default="",type=str)
    

    print('input_link',input_link)
    usrLink = input_link
    print("url",usrLink)

    vid_id = get_video_id(usrLink)
    vid_id = vid_id[0] if isinstance(vid_id, list) else vid_id  # Get the first element if it's a list
    print(vid_id)

    vid_title = get_video_title(vid_id)
    print(vid_title)

    thumbnail_url = get_video_img(vid_id)
    print(thumbnail_url)

    vquality = "144p"
    

    result = {
        "URL": usrLink,
        "Vid_title":vid_title,
        "Thumbnail_url":thumbnail_url
    }

    #download_video(usrLink,vquality)
    #print("down")

    return jsonify(result)



@app.route('/extenstion2', methods=['GET'])
def extentionResul2t():

    input_link = request.args.get('userinput', default="",type=str)
    usrLink = input_link
    vquality = request.args.get('video_quality', default="", type=str)


    print(vquality)

    vid_id = get_video_id(usrLink)
    vid_id = vid_id[0] if isinstance(vid_id, list) else vid_id  # Get the first element if it's a list
    print(vid_id)

    vid_title = get_video_title(vid_id)
    print(vid_title)

    thumbnail_url = get_video_img(vid_id)
    print(thumbnail_url)

    #vquality = "144p"

    download_video(usrLink,vquality)
    print("down")




x = datetime.datetime.now()

@app.route('/test')
def get_time():
    return{
        "Time" : x
    }

    


def get_video_id(yt_url):

    youtube_hostnames = ("www.youtube.com", "youtube.com", "m.youtube.com", "youtu.be")
    parsed_url = urlparse(yt_url)

    if parsed_url.hostname in youtube_hostnames:
        query_params = parse_qs(parsed_url.query)

        if "v" in query_params:
            return query_params["v"[0]]
        elif parsed_url.path.startswith("/embed"):
            return parsed_url.path.split("/")[-1]
        elif parsed_url.path.startswith("/watch"):
            return parsed_url.path.split("/")[-1]
        elif parsed_url.hostname == "youtu.be":
            return parsed_url.path[1:]
    return None

def get_video_title(video_id):

    request = youtube.videos().list(id=video_id, part="snippet")
    response = request.execute()

    request2 = youtube.videos().list(id=video_id, part="statistics")
    response2 = request2.execute()

    title = response["items"][0]["snippet"]["title"]
    channelTitle = response["items"][0]["snippet"]["channelTitle"]
    #description = response["items"][0]["snippet"]["description"]
    #publish_time = response["items"][0]["snippet"]["publish_time"]
    coment_count = response2["items"][0]["statistics"]["viewCount"]
    thumbnail_url = response["items"][0]["snippet"]["thumbnails"]["default"]["url"]

    return title


def get_video_img(video_id):

    request = youtube.videos().list(id=video_id, part="snippet")
    response = request.execute()

    request2 = youtube.videos().list(id=video_id, part="statistics")
    response2 = request2.execute()

    thumbnail_url = response["items"][0]["snippet"]["thumbnails"]["default"]["url"]

    return  thumbnail_url


def download_video(video_id,vquality):
    ytObject = YouTube(video_id)

    if vquality  == 'MP3':
        video = ytObject.streams.get_audio_only()
        video.download()
        print("Downloaded 👍.")

    else :
        streams = ytObject.streams.filter(res=vquality)

        if streams:
            video = streams[0]
            video.download()
            print("Downloaded 👍.")
        else:
            print("No Video.")


def download_video2(video_id):
    ytObject = YouTube('8xlDwukxjnA')


    video = ytObject.streams.get_audio_only()

    video.download()
    print("Downloaded.")     


def validelink(input):

    def valid_yt(url):
        host_names = ("www.youtube.com", "youtube.com", "m.youtube.com", "youtu.be")
        parsed_url = urlparse(url)

        if parsed_url.hostname in host_names:

            query_params = parse_qs(parsed_url.query)

            if "v" in query_params:
                return True
            elif parsed_url.path.startswith("/embed"):
                return True
            return False
        else:
            return False
        
    if valid_yt(input):
        return input
    else:
        return ("INVALID LINK")




if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))