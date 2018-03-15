import requests
import json
from time import sleep

def main():
    hasmore = True
    # page = 1
    # page = 295
    # page = 594
    page = 894

    with open("so_questions_2017.txt", "a") as f:
        while hasmore:
            # Filters in question:
            # accepted_answer_id, answer_count, body, bounty_amount, bounty_closes_date,
            # closed_date, closed_details closed_reason, comment_count, comments, 
            # community_owned_date, creation_date, down_vote_count, is_answered, 
            # last_activity_date, last_edit_date, link, locked_date, migrated_from, 
            # migrated_to, owner, protected_date, question_id, score, tags, tile, 
            # up_vote_count, view_count

            # pagesize = 1
            # fromdate = 2017-01-01
            # todate   = 2017-12-31
            # sort     = creation
            # order    = asc

            # response = requests.get("https://api.stackexchange.com/2.2/questions?page=" + str(page) + "&pagesize=100&fromdate=1483228800&todate=1514678400&order=asc&sort=creation&site=stackoverflow&filter=!bLf7X*XzLOx(vF")
            response = requests.get("https://api.stackexchange.com/2.2/questions?key=c0rhJNc*ftoArm1v10Xz7Q((&page=" + str(page) + "&pagesize=100&fromdate=1483228800&todate=1514678400&order=asc&sort=creation&site=stackoverflow&filter=!3ykawFyAwYVMHwpV1")
            print("== Request {:5d} ============================".format(page))
            sleep(1) # For now: sleep one whole second
            # sleep(0.05) # 50 millisecond wait; 30 requests per second = 33 ms between requests

            page += 1

            if response.status_code != 200:
                print("HTTP Error = ", response.status_code)
                break

            try:
                data = json.loads(response.text) #dictionary
            except json.decoder.JSONDecodeError as e:
                print("Could not load response JSON: {}".format(e))
                print("Response was:")
                print(response.text)
                break

            # Check if the API returned an error
            if "error_id" in data:
                print("API Error = ", data.get("error_id", "<unknown id>"), ",", data.get("error_name", "<unknown name>"), ":", data.get("error_message", "<unknown message>"))
                break
            # error_id      = 502
            # error_name    = throttle_violation
            # error message = too many requests from this IP, more requests available in 79710 seconds

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
                    question_str = json.dumps(item) # controleren of het een enkele regel is, geen newlines
                    f.write(question_str + "\n") # schrijf naar file
            else:
                print("No \"items\" in response!")

            # Does the API have more pages of questions ahead?
            hasmore = data.get("has_more", False) # If true, there are more results

            if "quota_remaining" in data:
                quota_remaining = data["quota_remaining"]
                if quota_remaining < 1:
                    print("Maximum quota reached, wait 24 hours. Start again from page {}.".format(page) )
                    break

  


    # <code>........</code>             -> inline code
    # <pre><code>........</code></pre>  -> code block

    # - Don't make more than 30 requests per second
    # - Without a key you can make 300 requests per day, with a key you can make 10,000 requests per day
    #     -- With an access token, the 10,000 request limit is just for your app for that user. *
    #     -- Without an access token, the 10,000 request limit is shared between apps on the IP Address.
    # - You must obey the backoff field which is in the wrapper object, if the field is there then you must wait the number of seconds it contains before you make an identical request.
    # - Making an indentical request more than once a minute is unlikely to return new results



if __name__ == '__main__':
    main()