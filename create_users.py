import json
import time
from collections import Counter


def divide(n, d):
    return n / d if d else 0

def newUser(data):
    return {
     "registered":  data["owner"]["user_type"]=="registered",  # registered or unregistered user
     "reputation":  data["owner"].get("reputation",0),         # reputation of user
     "accept_rate": data["owner"].get("accept_rate",0),        # percentage of questions (of the user) with accepted answer
     "questions": {"total": 0,                    # total nr of questions of user
                   "code_blocks": 0,              # nr of questions that include code blocks
                   "tag_python": 0,               # nr of questions with tag python
                   "tag_javascript": 0,           # nr of questions with tag javascript
                   "tag_java": 0,                 # nr of questions with tag java
                   "tag_c++": 0,                  # nr of questions with tag c++
                   "tag_c": 0,                    # nr of questions with tag c
                   "scores": [],                  # list of question scores
                   "down_votes": [],              # list of down votes per question
                   "up_votes": [],                # list of up votes per question
                   "is_answered": 0,              # nr of questions with answer
                   "answer_count": [],            # list of answer counts per question
                   "view_count": []               # list of view counts per question
                  },
     "answers":   {"total": 0,
                   "code_blocks": 0,              # nr of answers that include code blocks
                   "tag_python": 0,               # nr of answers with tag python
                   "tag_javascript": 0,           # nr of answers with tag javascript
                   "tag_java": 0,                 # nr of answers with tag java
                   "tag_c++": 0,                  # nr of answers with tag c++
                   "tag_c": 0,                    # nr of answers with tag c
                   "scores": [],                  # list of answer scores
                   "down_votes": [],              # list of downvotes per answer
                   "up_votes": [],                # list of up votes per answer
                   "accepted": 0,                 # nr of accepted answers
                   "time": [],                    # list of times in s between question and answer
                   "questioners": []              # list of user id's of whom the user answered a question
                  }
    }


def fillUser(item, userdict):
    # Only get data with correct tag(s)
    if "c" in item["tags"] or "c++" in item["tags"] or "java" in item["tags"] or "javascript" in item["tags"] or "python" in item["tags"]:
        # date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(item["creation_date"]))
        # print(item)
        user_id = item["owner"].get("user_id", item["owner"]["display_name"])
        # if item["owner"]["user_type"] == "registered":
        if not user_id in userdict:
            userdict[user_id] = newUser(item)
        
        userdict[user_id]["questions"]["total"]           += 1
        userdict[user_id]["questions"]["code_blocks"]     += int('<pre><code>' in item["body"])
        userdict[user_id]["questions"]["tag_python"]      += int("python"      in item["tags"])
        userdict[user_id]["questions"]["tag_javascript"]  += int("javascript"  in item["tags"])
        userdict[user_id]["questions"]["tag_java"]        += int("java"        in item["tags"])
        userdict[user_id]["questions"]["tag_c++"]         += int("c++"         in item["tags"])
        userdict[user_id]["questions"]["tag_c"]           += int("c"           in item["tags"])
        userdict[user_id]["questions"]["scores"].append(item["score"])
        userdict[user_id]["questions"]["down_votes"].append(item["down_vote_count"])
        userdict[user_id]["questions"]["up_votes"].append(item["up_vote_count"])
        userdict[user_id]["questions"]["is_answered"]     += int(item["is_answered"])
        userdict[user_id]["questions"]["answer_count"].append(item["answer_count"])
        userdict[user_id]["questions"]["view_count"].append(item["view_count"])

        questioner = user_id

        for answer in item["answers"]:
            # if answer["owner"]["user_type"] == "registered":
            user_id = answer["owner"].get("user_id", answer["owner"]["display_name"])
            if not user_id in userdict:
                userdict[user_id] = newUser(answer)
            
            userdict[user_id]["answers"]["total"]           += 1
            userdict[user_id]["answers"]["code_blocks"]     += int('<pre><code>' in answer["body"])
            userdict[user_id]["answers"]["tag_python"]      += int("python"      in item["tags"])
            userdict[user_id]["answers"]["tag_javascript"]  += int("javascript"  in item["tags"])
            userdict[user_id]["answers"]["tag_java"]        += int("java"        in item["tags"])
            userdict[user_id]["answers"]["tag_c++"]         += int("c++"         in item["tags"])
            userdict[user_id]["answers"]["tag_c"]           += int("c"           in item["tags"])
            userdict[user_id]["answers"]["scores"].append(answer["score"])
            userdict[user_id]["answers"]["down_votes"].append(answer["down_vote_count"])
            userdict[user_id]["answers"]["up_votes"].append(answer["up_vote_count"])
            userdict[user_id]["answers"]["accepted"]        += int(answer["is_accepted"])
            userdict[user_id]["answers"]["time"].append(item["creation_date"] - answer["creation_date"])
            userdict[user_id]["answers"]["questioners"].append(questioner)

    return userdict


def avgUser(userdict):
    for user_id in userdict:
        # Averaging scores
        userdict[user_id]["questions"]["scores"]       = divide(sum(userdict[user_id]["questions"]["scores"])       , len(userdict[user_id]["questions"]["scores"]))
        userdict[user_id]["questions"]["down_votes"]   = divide(sum(userdict[user_id]["questions"]["down_votes"])   , len(userdict[user_id]["questions"]["down_votes"]))
        userdict[user_id]["questions"]["up_votes"]     = divide(sum(userdict[user_id]["questions"]["up_votes"])     , len(userdict[user_id]["questions"]["up_votes"]))
        userdict[user_id]["questions"]["answer_count"] = divide(sum(userdict[user_id]["questions"]["answer_count"]) , len(userdict[user_id]["questions"]["answer_count"]))
        userdict[user_id]["questions"]["view_count"]   = divide(sum(userdict[user_id]["questions"]["view_count"])   , len(userdict[user_id]["questions"]["view_count"]))
        
        userdict[user_id]["answers"]["scores"]     = divide(sum(userdict[user_id]["answers"]["scores"])     , len(userdict[user_id]["answers"]["scores"]))
        userdict[user_id]["answers"]["down_votes"] = divide(sum(userdict[user_id]["answers"]["down_votes"]) , len(userdict[user_id]["answers"]["down_votes"]))
        userdict[user_id]["answers"]["up_votes"]   = divide(sum(userdict[user_id]["answers"]["up_votes"])   , len(userdict[user_id]["answers"]["up_votes"]))
        userdict[user_id]["answers"]["time"]       = divide(sum(userdict[user_id]["answers"]["time"])       , len(userdict[user_id]["answers"]["time"]))
        
        userdict[user_id]["answers"]["questioners"] = dict(Counter(userdict[user_id]["answers"]["questioners"]))

    return userdict


def main():
    with open('so_questions_answers_2017.txt', 'r') as rf:
        with open('dataset_users.txt','w') as wf:
            userdict    = {}
            userdictJan = {}
            userdictFeb = {}
            userdictMar = {}
            userdictApr = {}
            userdictMay = {}
            userdictJun = {}

            for line in rf:
                item  = json.loads(line)
                userdict = fillUser(item, userdict)

                month = time.strftime("%b", time.localtime(item["creation_date"]))
                if month == "Jan":
                    userdictJan = fillUser(item, userdictJan)
                if month == "Feb":
                    userdictFeb = fillUser(item, userdictFeb)
                if month == "Mar":
                    userdictMar = fillUser(item, userdictMar)
                if month == "Apr":
                    userdictApr = fillUser(item, userdictApr)
                if month == "May":
                    userdictMay = fillUser(item, userdictMay)
                if month == "Jun":
                    userdictJun = fillUser(item, userdictJun)
                
            # userdata = json.dumps(userdict)
            # wf.write(userdata)


    # with open('dataset_users.txt','r') as rf:
    #     with open('dataset_users_avgd.txt','w') as wf:
    #         line = rf.readline()
    #         userdict = json.loads(line)

            userdict    = avgUser(userdict)
            userdictJan = avgUser(userdictJan)
            userdictFeb = avgUser(userdictFeb)
            userdictMar = avgUser(userdictMar)
            userdictApr = avgUser(userdictApr)
            userdictMay = avgUser(userdictMay)
            userdictJun = avgUser(userdictJun)
            
            userdata    = json.dumps(userdict)
            userdataJan = json.dumps(userdictJan)
            userdataFeb = json.dumps(userdictFeb)
            userdataMar = json.dumps(userdictMar)
            userdataApr = json.dumps(userdictApr)
            userdataMay = json.dumps(userdictMay)
            userdataJun = json.dumps(userdictJun)

            wf.write(userdata)


if __name__ == '__main__':
    main()