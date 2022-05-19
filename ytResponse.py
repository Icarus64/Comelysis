import os
import googleapiclient.discovery

from textblob import TextBlob

def ytResp(vidId):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyBZLqhr-PnTOyy-5PA-FEgvF99h_3K78s8"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=100,
        order="relevance",
        textFormat="html",
        videoId=vidId
    )

    return request.execute()

def comList(comObj):
    comList = []
    for item in comObj['items']:
        comList.append(item['snippet']['topLevelComment']['snippet']['textOriginal'])
    return comList

def sentiScore(comText):
    tb = TextBlob(comText)
    return {'polarity': tb.sentiment.polarity, 'subjectivity':tb.sentiment.subjectivity}

def mostLiked(comObj):
    likest = likedList(comObj)
    cmList = comList(comObj)
    return {
        "comment": cmList[likest.index(max(likest))],
        "likeCount": max(likest),
        "commentID": comObj['items'][likest.index(max(likest))]['snippet']['topLevelComment']['id']
        }

def leastLiked(comObj):
    likest = likedList(comObj)
    cmList = comList(comObj)
    return {
        "comment": cmList[likest.index(min(likest))],
        "likeCount": min(likest),
        "commentID": comObj['items'][likest.index(min(likest))]['snippet']['topLevelComment']['id']
        }

def likedList(comObj):
    likesList = []
    for item in comObj['items']:
        likesList.append(
            item['snippet']['topLevelComment']['snippet']['likeCount']
        )
    return likesList

def top5Com(comList, likest):
    likeSort = likest
    likeSort.sort(reverse = True)
    comLikeList = []
    for i in range(0,5):
        comLikeList.append(
            {
                'comment': comList[likest.index(likeSort[i])],
                'LikeCount': likeSort[i],
                'Sentiment Score': sentiScore(comList[likest.index(likeSort[i])])
            }
        )
    return comLikeList

