from flask import Blueprint, jsonify, request
from ytResponse import ytResp, comList, sentiScore, mostLiked, leastLiked, likedList, top5Com

youtubeComments = Blueprint("youtubeComments", __name__)

@youtubeComments.route("/commentAnalysis", methods=["POST"])
def comAnalysis():
    comObj = ytResp(
        request.args.get('link')
    )

    comLst = comList(comObj)
    text = ""
    for item in comLst:
        text += item
    sentScore = sentiScore(text)
    return jsonify({
        'top5Comments': top5Com(comLst, likedList(comObj)),
        'sentiScore': sentScore,
        'mostLiked': mostLiked(comObj),
        'leastLiked': leastLiked(comObj)
    })
    

    