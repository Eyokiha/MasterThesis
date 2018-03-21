import requests
import json
from time import sleep

def main():

    with open("so_questions_answers_2017.txt", "a") as fWrite:
        with open("so_questions_2017.txt", "r") as fRead:
            questionNr = 1

            # Start from later point in file
            # for i in range(questionNr):
            #     line = fRead.readline()

            breakFromNestedLoop = False
            q = "No data yet"

            while True:
                questions = []
                questionIDs = ""
                for n in range(100):
                    line = fRead.readline()
                    print("== Question {:5d} ============================".format(questionNr))
                    jsonLine = json.loads(line)
                    if q != "":

                    questions.append(jsonLine)
                    questionIDs += ";" + jsonLine["question_id"]                

                hasmore = True
                page    = 1

                while hasmore:
                    # link for id in question
                    response = requests.get("https://api.stackexchange.com/2.2/questions/" + questionIDs + "/answers?page=" + str(page) + "&pagesize=100&fromdate=1483228800&todate=1514678400&order=asc&sort=creation&site=stackoverflow&filter=!b1MMEbc8bCJrBX")
                    print("== Request {:5d} ============================".format(page))
                    sleep(1) # For now: sleep one whole second
                    # sleep(0.05) # 50 millisecond wait; 30 requests per second = 33 ms between requests

                    page += 1

                    if response.status_code != 200:
                        print("HTTP Error = ", response.status_code)
                        breakFromNestedLoop = True
                        break

                    try:
                        data = json.loads(response.text) #dictionary
                    except json.decoder.JSONDecodeError as e:
                        print("Could not load response JSON: {}".format(e))
                        print("Response was:")
                        print(response.text)
                        breakFromNestedLoop = True
                        break

                    # Check if the API returned an error
                    if "error_id" in data:
                        print("API Error = ", data.get("error_id", "<unknown id>"), ",", data.get("error_name", "<unknown name>"), ":", data.get("error_message", "<unknown message>"))
                        breakFromNestedLoop = True
                        break

                    # Did the API tell us to stop requesting for some time?
                    if "backoff" in data:
                        backoff = data["backoff"]

                        # Backoff geeft aan hoeveel seconden we moeten wachten voor de volgende request
                        # voor de zekerheid maar meteen doen. En voor de zekerheid wachten we nog een extra seconde.
                        print("Backing off for {}+2 seconds...".format(backoff))
                        sleep(backoff+2)

                    # Write the questions from the response to file
                    if "items" in data:
                        for item in data["items"]:
                            question = next((item for item in questions if item["question_id"] == item["question_id"]), None)
                            question["answers"] = item
                            question_and_answer_str = json.dumps(question) # controleren of het een enkele regel is, geen newlines
                            fWrite.write(question_and_answer_str + "\n") # schrijf naar file
                    else:
                        print("No \"items\" in response!")

                    # Does the API have more pages of questions ahead?
                    hasmore = data.get("has_more", False) # If true, there are more results

                    if "quota_remaining" in data:
                        quota_remaining = data["quota_remaining"]
                        if quota_remaining < 1:
                            print("Maximum quota reached, wait 24 hours. Start again from page {}.".format(page) )
                            breakFromNestedLoop = True
                            break
                if breakFromNestedLoop:
                    break


if __name__ == '__main__':
    main()