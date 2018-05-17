import json
import csv

def divide(n, d):
    return n / d if d else 0

def main():
    # with open('dataset_users.txt', 'r') as rf:
    #     with open('dataset_users_nodes.csv','w') as wfn:
    #         with open('dataset_users_edges.csv','w') as wfe:
    with open('dataset_users_Jun.txt', 'r') as rf:
        with open('dataset_users_nodes_Jun.csv','w') as wfn:
            with open('dataset_users_edges_Jun.csv','w') as wfe:
                line = rf.readline()
                userdict = json.loads(line)

                wn = csv.writer(wfn)
                we = csv.writer(wfe)

                wn.writerow(["user"
                            ,"registered"
                            ,"reputation"
                            ,"accept_rate"
                            ,"Q-total"
                            ,"Q-code_blocks"
                            ,"Q-tag_python"
                            ,"Q-tag_javascript"
                            ,"Q-tag_java"
                            ,"Q-tag_c++"
                            ,"Q-tag_c"
                            ,"Q-scores"
                            ,"Q-down_votes"
                            ,"Q-up_votes"
                            ,"Q-is_answered"
                            ,"Q-answer_count"
                            ,"Q-view_count"
                            ,"A-total"
                            ,"A-code_blocks"
                            ,"A-tag_python"
                            ,"A-tag_javascript"
                            ,"A-tag_java"
                            ,"A-tag_c++"
                            ,"A-tag_c"
                            ,"A-scores"
                            ,"A-down_votes"
                            ,"A-up_votes"
                            ,"A-accepted"
                            ,"A-time"])
                we.writerow(["source","target"]) #answerer, questioner

                for user in userdict:
                    wn.writerow([user #str
                                ,userdict[user]["registered"] #bool
                                ,userdict[user]["reputation"] #int
                                ,userdict[user]["accept_rate"] #int/percentage
                                ,userdict[user]["questions"]["total"] #int
                                ,divide(userdict[user]["questions"]["code_blocks"], userdict[user]["questions"]["total"]) #float/percentage
                                ,divide(userdict[user]["questions"]["tag_python"], userdict[user]["questions"]["total"]) #float/percentage
                                ,divide(userdict[user]["questions"]["tag_javascript"], userdict[user]["questions"]["total"]) #float/percentage
                                ,divide(userdict[user]["questions"]["tag_java"], userdict[user]["questions"]["total"]) #float/percentage
                                ,divide(userdict[user]["questions"]["tag_c++"], userdict[user]["questions"]["total"]) #float/percentage
                                ,divide(userdict[user]["questions"]["tag_c"], userdict[user]["questions"]["total"]) #float/percentage
                                ,userdict[user]["questions"]["scores"] #float/avg
                                ,userdict[user]["questions"]["down_votes"] #float/avg
                                ,userdict[user]["questions"]["up_votes"] #float/avg
                                ,divide(userdict[user]["questions"]["is_answered"], userdict[user]["questions"]["total"]) #float/avg
                                ,userdict[user]["questions"]["answer_count"] #float/avg
                                ,userdict[user]["questions"]["view_count"] #float/avg
                                ,userdict[user]["answers"]["total"] #int
                                ,divide(userdict[user]["answers"]["code_blocks"], userdict[user]["answers"]["total"]) #float/percentage
                                ,divide(userdict[user]["answers"]["tag_python"], userdict[user]["answers"]["total"]) #float/percentage
                                ,divide(userdict[user]["answers"]["tag_javascript"], userdict[user]["answers"]["total"]) #float/percentage
                                ,divide(userdict[user]["answers"]["tag_java"], userdict[user]["answers"]["total"]) #float/percentage
                                ,divide(userdict[user]["answers"]["tag_c++"], userdict[user]["answers"]["total"]) #float/percentage
                                ,divide(userdict[user]["answers"]["tag_c"], userdict[user]["answers"]["total"]) #float/percentage
                                ,userdict[user]["answers"]["scores"] #foat/avg
                                ,userdict[user]["answers"]["down_votes"] #float/avg
                                ,userdict[user]["answers"]["up_votes"] #float/avg
                                ,divide(userdict[user]["answers"]["accepted"], userdict[user]["answers"]["total"]) #float/percentage
                                ,userdict[user]["answers"]["time"]]) #float/avg
                    for q in userdict[user]["answers"]["questioners"]:
                        we.writerow([user,q]) #str, str
                    

                # print(item)
                # w.writerow(item.values())




if __name__ == '__main__':
    main()

