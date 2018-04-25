import json
import time

def newUser(data):
    return {
     # "registered":  data["owner"]["user_type"]=="registered",    # registered or unregistered user
     "accept_rate": data["owner"].get("accept_rate",None), # percentage of questions (of the user) with accepted answer
     "reputation":  data["owner"]["reputation"],  # reputation of user
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
                   "time":[]                      # list of times in s between question and answer
                  }
    }

def main():
    with open('so_questions_answers_2017.txt', 'r') as rf:
        with open('dataset_users.txt','w') as wf:
            userdict = {}

            # userdictJan = {}
            # userdictFeb = {}
            # userdictMar = {}
            # userdictApr = {}
            # userdictMay = {}

            for line in rf:
                item = json.loads(line)

                # Only get data with correct tag(s)
                if "c" in item["tags"] or "c++" in item["tags"] or "java" in item["tags"] or "javascript" in item["tags"] or "python" in item["tags"]:
                    # date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(item["creation_date"]))
                    # print(item)
                    if item["owner"]["user_type"] == "registered":
	                    user_id = item["owner"]["user_id"]
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


                    for answer in item["answers"]:
                    	if answer["owner"]["user_type"] == "registered":
	                        user_id = answer["owner"]["user_id"]
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

                    
                    
            userdata = json.dumps(userdict) # controleren of het een enkele regel is, geen newlines
            wf.write(userdata) # schrijf naar file
                    
                    





                






if __name__ == '__main__':
    main()