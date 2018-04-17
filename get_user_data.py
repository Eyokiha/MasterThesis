# Required Python Packages
# import pandas as pd

# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix

import json
from statistics import mean

# X, y = make_classification(n_samples=1000, n_features=4,
#                            n_informative=2, n_redundant=0,
#                            random_state=0, shuffle=False)
# clf = RandomForestClassifier(max_depth=2, random_state=0)
# clf.fit(X, y)
# print(clf.feature_importances_)
# print(clf.predict([[0, 0, 0, 0]]))

# All keys:
# tags
# comments
# owner
# comment_count
# is_answered
# view_count
# down_vote_count
# up_vote_count
# answer_count
# score
# last_activity_date
# creation_date
# last_edit_date
# question_id
# body_markdown
# link
# title
# body

# Convert human time -> epoch time:
# import time; int(time.mktime(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))) - time.timezone
# Convert epoch time -> human time:
# import time; time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch)) Replace time.localtime with time.gmtime for GMT time. Or using datetime: import datetime; datetime.datetime.utcfromtimestamp(epoch).replace(tzinfo=datetime.timezone.utc)

# def percentage(part, whole):
#   return 100 * float(part)/float(whole)

import time
# time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch))
# Replace time.localtime with time.gmtime for GMT time. Or using datetime: 
# import datetime
# datetime.datetime.utcfromtimestamp(epoch).replace(tzinfo=datetime.timezone.utc)


def main():
    with open("so_questions_answers_2017 (copy).txt", "r") as f:
        userAnswerers   = {}
        userQuestioners = {}

        for line in f:
            item = json.loads(line)
            qEpoch = item[creation_date]
            qDate = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(qEpoch))
            
            if item["is_answered"]:
                for elem in item["answers"]:
                    userID = elem["owner"]["user_id"]
                    if not userID in userDict:
                        userDict[userID] = [0,0,[]] 
                    userDict[userID][0] += 1
                    userDict[userID][1] += 1
                    userDict[userID][2].append()




        # - userDict[userID] ->
        # 0 question count
        # 1 answer count
        # 2 [times between a question and their answer] - sum/len=avg
        # 3 


        # print(dataset[0])
        # train_x, test_x, train_y, test_y = split_dataset(dataset, 0.7, HEADERS[1:-1], HEADERS[-1])



if __name__ == '__main__':
    main()