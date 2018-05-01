import json
import csv

def main():
    with open('dataset_users.txt', 'r') as rf:
        with open('dataset_users_nodes.csv','w') as wfn:
            with open('dataset_users_edges.csv','w') as wfe:
                line = rf.readline()
                userdict = json.loads(line)

                wn = csv.writer(wfn)
                we = csv.writer(wfe)

                wn.writerow(["reputation"
                            ,"accept_rate"
                            ,"Q:total"
                            ,"Q:code_blocks"
                            ,"Q:tag_python"
                            ,"Q:tag_javascript"
                            ,"Q:tag_java"
                            ,"Q:tag_c++"
                            ,"Q:tag_c"
                            ,"Q:scores"
                            ,"Q:down_votes"
                            ,"Q:up_votes"
                            ,"Q:is_answered"
                            ,"Q:answer_count"
                            ,"Q:view_count"
                            ,"A:total"
                            ,"A:code_blocks"
                            ,"A:tag_python"
                            ,"A:tag_javascript"
                            ,"A:tag_java"
                            ,"A:tag_c++"
                            ,"A:tag_c"
                            ,"A:scores"
                            ,"A:down_votes"
                            ,"A:up_votes"
                            ,"A:accepted"
                            ,"A:time"])
                we.writerow(["answerer","questioner"])

                for user in userdict:
                    wn.writerow([user
                                ,userdict[user]["registered"]
                                ,userdict[user]["reputation"]
                                ,userdict[user]["accept_rate"]
                                ,userdict[user]["questions"]["total"]
                                ,userdict[user]["questions"]["code_blocks"]
                                ,userdict[user]["questions"]["tag_python"]
                                ,userdict[user]["questions"]["tag_javascript"]
                                ,userdict[user]["questions"]["tag_java"]
                                ,userdict[user]["questions"]["tag_c++"]
                                ,userdict[user]["questions"]["tag_c"]
                                ,userdict[user]["questions"]["scores"]
                                ,userdict[user]["questions"]["down_votes"]
                                ,userdict[user]["questions"]["up_votes"]
                                ,userdict[user]["questions"]["is_answered"]
                                ,userdict[user]["questions"]["answer_count"]
                                ,userdict[user]["questions"]["view_count"]
                                ,userdict[user]["answers"]["total"]
                                ,userdict[user]["answers"]["code_blocks"]
                                ,userdict[user]["answers"]["tag_python"]
                                ,userdict[user]["answers"]["tag_javascript"]
                                ,userdict[user]["answers"]["tag_java"]
                                ,userdict[user]["answers"]["tag_c++"]
                                ,userdict[user]["answers"]["tag_c"]
                                ,userdict[user]["answers"]["scores"]
                                ,userdict[user]["answers"]["down_votes"]
                                ,userdict[user]["answers"]["up_votes"]
                                ,userdict[user]["answers"]["accepted"]
                                ,userdict[user]["answers"]["time"]])
                    for q in userdict[user]["answers"]["questioners"]:
                        we.writerow([user,q])
                    

                # print(item)
                # w.writerow(item.values())




if __name__ == '__main__':
    main()

