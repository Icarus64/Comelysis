import praw

from ytResponse import sentiScore

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"


def rdResponse(link):
    reddit = praw.Reddit(
        client_id="fP0wFkjLbOWV2eL6sjdU9Q",
        client_secret="yTEOfr2QOKb17gyJWAjesBk7a4rEjQ",
        user_agent="Comment Extraction by u/Pretty_Progress6570"
    )

    submission = reddit.submission(url=link)
    submission.comments.replace_more(limit=0, threshold=100)

    comList = []
    for top_level_comment in submission.comments:
        comList.append(top_level_comment)

    return comList

def mostUps(comList):
    ups = []
    for item in comList:
        ups.append(item.ups)
    maxIndex = ups.index(max(ups))
    return {
        'comment': comList[maxIndex].body,
        'upvotes': comList[maxIndex].ups,
        'commentID': comList[maxIndex].id
    }

def mostDowns(comList):
    downs = []
    for item in comList:
        downs.append(item.downs)
    minIndex = downs.index(min(downs))
    if not minIndex < 0:
        return None
    return {
        'comment': comList[minIndex].body,
        'downvotes': comList[minIndex].downs,
        'commentID': comList[minIndex].id
    }

def top5Coms(comList):
    top5 = []
    ups = []
    for item in comList:
        ups.append(item.ups)
    upSort = ups
    upSort.sort(reverse = True)

    for i in range(0,5):
        top5.append({
            'comment': comList[ups.index(upSort[i])].body,
            'upvotes': upSort[i],
            'Sentiment Score': sentiScore(comList[ups.index(upSort[i])].body)
        })

    return top5