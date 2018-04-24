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
import time
# time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(epoch)) Replace time.localtime with time.gmtime for GMT time. Or using datetime: import datetime; datetime.datetime.utcfromtimestamp(epoch).replace(tzinfo=datetime.timezone.utc)

def percentage(part, whole):
  return 100 * float(part)/float(whole)


def main():
    # with open("so_questions_answers_2017 (10th copy).txt", "r") as f:
    with open("so_questions_answers_2017 - 1000000.txt", "r") as f:
        total       = 0
        answered    = 0
        npython     = 0
        njavascript = 0
        njava       = 0
        ncpp        = 0
        nc          = 0
        n1          = 0
        n2          = 0
  
        TTmaxAnsweredCount  = 0
        ANmaxAnsweredCount  = 0
        PYmaxAnsweredCount  = 0
        JSmaxAnsweredCount  = 0
        JVmaxAnsweredCount  = 0
        CPmaxAnsweredCount  = 0
        CCmaxAnsweredCount  = 0
        TAmaxAnsweredCount  = 0
        ALmaxAnsweredCount  = 0

        TTavgAnsweredCount  = 0
        ANavgAnsweredCount  = 0
        PYavgAnsweredCount  = []
        JSavgAnsweredCount  = []
        JVavgAnsweredCount  = []
        CPavgAnsweredCount  = []
        CCavgAnsweredCount  = []
        TAavgAnsweredCount  = []
        ALavgAnsweredCount  = []

        TTuserCount  = 0
        ANuserCount  = 0
        PYuserCount  = 0
        JSuserCount  = 0
        JVuserCount  = 0
        CPuserCount  = 0
        CCuserCount  = 0
        TAuserCount  = 0
        ALuserCount  = 0

        PYuserListAnswers = []
        JSuserListAnswers = []
        JVuserListAnswers = []
        CPuserListAnswers = []
        CCuserListAnswers = []
        AllUserListAnswers = []

        PYuserListQuestions = []
        JSuserListQuestions = []
        JVuserListQuestions = []
        CPuserListQuestions = []
        CCuserListQuestions = []


        for line in f:
            item = json.loads(line)
            total += 1

            if item["owner"]["user_type"]=="registered":
                AllUserListAnswers.append(item["owner"]["user_id"])
            else:
                AllUserListAnswers.append("##UNREGISTERED##:"+el["owner"]["display_name"])

            for el in item["answers"]:
                if el["owner"]["user_type"]=="registered":
                    AllUserListAnswers.append(el["owner"]["user_id"])
                else:
                    AllUserListAnswers.append("##UNREGISTERED##:"+el["owner"]["display_name"])

            if item["is_answered"]:
                answered += 1

            if "python" in item["tags"]:
                npython += 1
                PYmaxAnsweredCount = max(len(item["answers"]), PYmaxAnsweredCount)
                PYavgAnsweredCount.append(len(item["answers"]))
                PYuserCount += 1

            if "javascript" in item["tags"]:
                njavascript += 1
                JSmaxAnsweredCount = max(len(item["answers"]), JSmaxAnsweredCount)
                JSavgAnsweredCount.append(len(item["answers"]))
                JSuserCount += 1

            if "java" in item["tags"]:
                njava += 1
                JVmaxAnsweredCount = max(len(item["answers"]), JVmaxAnsweredCount)
                JVavgAnsweredCount.append(len(item["answers"]))
                JVuserCount += 1

            if "c++" in item["tags"]:
                ncpp += 1
                CPmaxAnsweredCount = max(len(item["answers"]), CPmaxAnsweredCount)
                CPavgAnsweredCount.append(len(item["answers"]))
                CPuserCount += 1

            if "c" in item["tags"]:
                nc += 1
                CCmaxAnsweredCount = max(len(item["answers"]), CCmaxAnsweredCount)
                CCavgAnsweredCount.append(len(item["answers"]))
                CCuserCount += 1

            if "c" in item["tags"] or "c++" in item["tags"] or "java" in item["tags"] or "javascript" in item["tags"] or "python" in item["tags"]:
                n1 += 1
                TAmaxAnsweredCount = max(len(item["answers"]), TAmaxAnsweredCount)
                TAavgAnsweredCount.append(len(item["answers"]))
                TAuserCount += 1

                if item["is_answered"]:
                    n2 += 1
                    ALmaxAnsweredCount = max(len(item["answers"]), ALmaxAnsweredCount)
                    ALavgAnsweredCount.append(len(item["answers"]))
                    ALuserCount += 1

                    # TTuserList = []
                    # ANuserList = []
                    if "python" in item["tags"]:
                        if item["owner"]["user_type"]=="registered":
                            PYuserListQuestions.append(item["owner"]["user_id"])
                        else:
                            PYuserListQuestions.append("##UNREGISTERED##:"+el["owner"]["display_name"])

                        for el in item["answers"]:
                            if el["owner"]["user_type"]=="registered":
                                PYuserListAnswers.append(el["owner"]["user_id"])
                            else:
                                PYuserListAnswers.append("##UNREGISTERED##:"+el["owner"]["display_name"])


                    if "javascript" in item["tags"]:
                        if item["owner"]["user_type"]=="registered":
                            JSuserListQuestions.append(item["owner"]["user_id"])
                        else:
                            JSuserListQuestions.append("##UNREGISTERED##:"+el["owner"]["display_name"])

                        for el in item["answers"]:
                            if el["owner"]["user_type"]=="registered":
                                JSuserListAnswers.append(el["owner"]["user_id"])
                            else:
                                JSuserListAnswers.append("##UNREGISTERED##:"+el["owner"]["display_name"])


                    if "java" in item["tags"]:
                        if item["owner"]["user_type"]=="registered":
                            JVuserListQuestions.append(item["owner"]["user_id"])
                        else:
                            JVuserListQuestions.append("##UNREGISTERED##:"+el["owner"]["display_name"])

                        for el in item["answers"]:
                            if el["owner"]["user_type"]=="registered":
                                JVuserListAnswers.append(el["owner"]["user_id"])
                            else:
                                JVuserListAnswers.append("##UNREGISTERED##:"+el["owner"]["display_name"])


                    if "c++" in item["tags"]:
                        if item["owner"]["user_type"]=="registered":
                            CPuserListQuestions.append(item["owner"]["user_id"])
                        else:
                            CPuserListQuestions.append("##UNREGISTERED##:"+el["owner"]["display_name"])

                        for el in item["answers"]:
                            if el["owner"]["user_type"]=="registered":
                                CPuserListAnswers.append(el["owner"]["user_id"])
                            else:
                                CPuserListAnswers.append("##UNREGISTERED##:"+el["owner"]["display_name"])


                    if "c" in item["tags"]:
                        if item["owner"]["user_type"]=="registered":
                            CCuserListQuestions.append(item["owner"]["user_id"])
                        else:
                            CCuserListQuestions.append("##UNREGISTERED##:"+el["owner"]["display_name"])

                        for el in item["answers"]:
                            if el["owner"]["user_type"]=="registered":
                                CCuserListAnswers.append(el["owner"]["user_id"])
                            else:
                                CCuserListAnswers.append("##UNREGISTERED##:"+el["owner"]["display_name"])
                    # TAuserList = []
                    # ALuserList = []
            date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(item["creation_date"]))






        # print(dataset[-1])

        # print("total: {:6d}".format(                       total)
        # print("answered: {:6d} {:6.2f}".format(            answered,    percentage(answered, total)),'%')
        # print("python: {:6d} {:6.2f}".format(              npython,     percentage(npython, total)),'%')
        # print("javascript: {:6d} {:6.2f}".format(          njavascript, percentage(njavascript, total)),'%')
        # print("java: {:6d} {:6.2f}".format(                njava,       percentage(njava, total)),'%')
        # print("c++: {:6d} {:6.2f}".format(                 ncpp,        percentage(ncpp, total)),'%')
        # print("c: {:6d} {:6.2f}".format(                   nc,          percentage(nc, total)),'%')
        # print("with tags: {:6d} {:6.2f}".format(           n1,          percentage(n1, total)),'%')
        # print("with tags & answered: {:6d} {:6.2f}".format(n2,          percentage(n2, total)),'%')

        print(date)
        print()

        print("total:",                total)
        print("answered:",             answered)
        print("python:",               npython)
        print("javascript:",           njavascript)
        print("java:",                 njava)
        print("c++:",                  ncpp)
        print("c:",                    nc)
        print("with tags:",            n1)
        print("with tags & answered:", n2)
        print()

        # print("PYmaxAnsweredCount:", PYmaxAnsweredCount, percentage(PYmaxAnsweredCount, TTmaxAnsweredCount))
        # print("JSmaxAnsweredCount:", JSmaxAnsweredCount, percentage(JSmaxAnsweredCount, TTmaxAnsweredCount))
        # print("JVmaxAnsweredCount:", JVmaxAnsweredCount, percentage(JVmaxAnsweredCount, TTmaxAnsweredCount))
        # print("CPmaxAnsweredCount:", CPmaxAnsweredCount, percentage(CPmaxAnsweredCount, TTmaxAnsweredCount))
        # print("CCmaxAnsweredCount:", CCmaxAnsweredCount, percentage(CCmaxAnsweredCount, TTmaxAnsweredCount))
        # print("TAmaxAnsweredCount:", TAmaxAnsweredCount, percentage(TAmaxAnsweredCount, TTmaxAnsweredCount))
        # print("ALmaxAnsweredCount:", ALmaxAnsweredCount, percentage(ALmaxAnsweredCount, TTmaxAnsweredCount))
        # print()

        print("PYavgAnsweredCount:", mean(PYavgAnsweredCount))
        print("JSavgAnsweredCount:", mean(JSavgAnsweredCount))
        print("JVavgAnsweredCount:", mean(JVavgAnsweredCount))
        print("CPavgAnsweredCount:", mean(CPavgAnsweredCount))
        print("CCavgAnsweredCount:", mean(CCavgAnsweredCount))
        print("TAavgAnsweredCount:", mean(TAavgAnsweredCount))
        print("ALavgAnsweredCount:", mean(ALavgAnsweredCount))
        print()

        print("PYuserCount:", PYuserCount)
        print("JSuserCount:", JSuserCount)
        print("JVuserCount:", JVuserCount)
        print("CPuserCount:", CPuserCount)
        print("CCuserCount:", CCuserCount)
        print("TAuserCount:", TAuserCount)
        print("ALuserCount:", ALuserCount)
        print()

        # print(dataset[0])
        # train_x, test_x, train_y, test_y = split_dataset(dataset, 0.7, HEADERS[1:-1], HEADERS[-1])

        # PYuserList
        # JSuserList
        # JVuserList
        # CPuserList
        # CCuserList

        # set removes duplicates
        # print("Python - Javascript", (200.0 * len(set(PYuserList) & set(JSuserList)) / (len(PYuserList) + len(JSuserList))) )
        # ANSWERS
        print("OVERLAP USERS")
        print("Answers")
        print("Python     - Javascript ", (200.0 * len(set(PYuserListAnswers) & set(JSuserListAnswers)) / (len(set(PYuserListAnswers)) + len(set(JSuserListAnswers)))) )
        print("Python     - Java       ", (200.0 * len(set(PYuserListAnswers) & set(JVuserListAnswers)) / (len(set(PYuserListAnswers)) + len(set(JVuserListAnswers)))) )
        print("Python     - C++        ", (200.0 * len(set(PYuserListAnswers) & set(CPuserListAnswers)) / (len(set(PYuserListAnswers)) + len(set(CPuserListAnswers)))) )
        print("Python     - C          ", (200.0 * len(set(PYuserListAnswers) & set(CCuserListAnswers)) / (len(set(PYuserListAnswers)) + len(set(CCuserListAnswers)))) )
        print("Javascript - Java       ", (200.0 * len(set(JSuserListAnswers) & set(JVuserListAnswers)) / (len(set(JSuserListAnswers)) + len(set(JVuserListAnswers)))) )
        print("Javascript - C++        ", (200.0 * len(set(JSuserListAnswers) & set(CPuserListAnswers)) / (len(set(JSuserListAnswers)) + len(set(CPuserListAnswers)))) )
        print("Javascript - C          ", (200.0 * len(set(JSuserListAnswers) & set(CCuserListAnswers)) / (len(set(JSuserListAnswers)) + len(set(CCuserListAnswers)))) )
        print("Java       - C++        ", (200.0 * len(set(JVuserListAnswers) & set(CPuserListAnswers)) / (len(set(JVuserListAnswers)) + len(set(CPuserListAnswers)))) )
        print("Java       - C          ", (200.0 * len(set(JVuserListAnswers) & set(CCuserListAnswers)) / (len(set(JVuserListAnswers)) + len(set(CCuserListAnswers)))) )
        print("C++        - C          ", (200.0 * len(set(CPuserListAnswers) & set(CCuserListAnswers)) / (len(set(CPuserListAnswers)) + len(set(CCuserListAnswers)))) )
        print()

        print("Questions")
        print("Python     - Javascript ", (200.0 * len(set(PYuserListQuestions) & set(JSuserListQuestions)) / (len(set(PYuserListQuestions)) + len(set(JSuserListQuestions)))) )
        print("Python     - Java       ", (200.0 * len(set(PYuserListQuestions) & set(JVuserListQuestions)) / (len(set(PYuserListQuestions)) + len(set(JVuserListQuestions)))) )
        print("Python     - C++        ", (200.0 * len(set(PYuserListQuestions) & set(CPuserListQuestions)) / (len(set(PYuserListQuestions)) + len(set(CPuserListQuestions)))) )
        print("Python     - C          ", (200.0 * len(set(PYuserListQuestions) & set(CCuserListQuestions)) / (len(set(PYuserListQuestions)) + len(set(CCuserListQuestions)))) )
        print("Javascript - Java       ", (200.0 * len(set(JSuserListQuestions) & set(JVuserListQuestions)) / (len(set(JSuserListQuestions)) + len(set(JVuserListQuestions)))) )
        print("Javascript - C++        ", (200.0 * len(set(JSuserListQuestions) & set(CPuserListQuestions)) / (len(set(JSuserListQuestions)) + len(set(CPuserListQuestions)))) )
        print("Javascript - C          ", (200.0 * len(set(JSuserListQuestions) & set(CCuserListQuestions)) / (len(set(JSuserListQuestions)) + len(set(CCuserListQuestions)))) )
        print("Java       - C++        ", (200.0 * len(set(JVuserListQuestions) & set(CPuserListQuestions)) / (len(set(JVuserListQuestions)) + len(set(CPuserListQuestions)))) )
        print("Java       - C          ", (200.0 * len(set(JVuserListQuestions) & set(CCuserListQuestions)) / (len(set(JVuserListQuestions)) + len(set(CCuserListQuestions)))) )
        print("C++        - C          ", (200.0 * len(set(CPuserListQuestions) & set(CCuserListQuestions)) / (len(set(CPuserListQuestions)) + len(set(CCuserListQuestions)))) )
        print()

        PYuserListBoth = PYuserListAnswers + PYuserListQuestions
        JSuserListBoth = JSuserListAnswers + JSuserListQuestions
        JVuserListBoth = JVuserListAnswers + JVuserListQuestions
        CPuserListBoth = CPuserListAnswers + CPuserListQuestions
        CCuserListBoth = CCuserListAnswers + CCuserListQuestions

        print("Both")
        print("Python     - Javascript ", (200.0 * len(set(PYuserListBoth) & set(JSuserListBoth)) / (len(set(PYuserListBoth)) + len(set(JSuserListBoth)))) )
        print("Python     - Java       ", (200.0 * len(set(PYuserListBoth) & set(JVuserListBoth)) / (len(set(PYuserListBoth)) + len(set(JVuserListBoth)))) )
        print("Python     - C++        ", (200.0 * len(set(PYuserListBoth) & set(CPuserListBoth)) / (len(set(PYuserListBoth)) + len(set(CPuserListBoth)))) )
        print("Python     - C          ", (200.0 * len(set(PYuserListBoth) & set(CCuserListBoth)) / (len(set(PYuserListBoth)) + len(set(CCuserListBoth)))) )
        print("Javascript - Java       ", (200.0 * len(set(JSuserListBoth) & set(JVuserListBoth)) / (len(set(JSuserListBoth)) + len(set(JVuserListBoth)))) )
        print("Javascript - C++        ", (200.0 * len(set(JSuserListBoth) & set(CPuserListBoth)) / (len(set(JSuserListBoth)) + len(set(CPuserListBoth)))) )
        print("Javascript - C          ", (200.0 * len(set(JSuserListBoth) & set(CCuserListBoth)) / (len(set(JSuserListBoth)) + len(set(CCuserListBoth)))) )
        print("Java       - C++        ", (200.0 * len(set(JVuserListBoth) & set(CPuserListBoth)) / (len(set(JVuserListBoth)) + len(set(CPuserListBoth)))) )
        print("Java       - C          ", (200.0 * len(set(JVuserListBoth) & set(CCuserListBoth)) / (len(set(JVuserListBoth)) + len(set(CCuserListBoth)))) )
        print("C++        - C          ", (200.0 * len(set(CPuserListBoth) & set(CCuserListBoth)) / (len(set(CPuserListBoth)) + len(set(CCuserListBoth)))) )
        print()

        print("Tagged:", len(set(PYuserListBoth+JSuserListBoth+JVuserListBoth+CPuserListBoth+CCuserListBoth)))
        print("Total: ", len(set(AllUserListAnswers)))


if __name__ == '__main__':
    main()