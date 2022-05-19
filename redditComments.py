from flask import Blueprint, jsonify, request
from redditResponse import rdResponse, mostDowns, mostUps, top5Coms
from ytResponse import sentiScore 

redditComments = Blueprint("redditComments", __name__)

@redditComments.route('/commentAnalysis', methods = ['POST'])
def comAnalysis():
    comList = rdResponse(
        request.args.get('link')
    )
    allText = ""
    for item in comList:
        allText += item.body
    
    sentScore = sentiScore(allText)
    return jsonify({
        'top5Comments': top5Coms(comList=comList),
        'Sentiment Score': sentScore,
        'mostUpvoted': mostUps(comList=comList),
        'mostDownvoted': mostDowns(comList=comList)
    })

