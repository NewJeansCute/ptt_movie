from datetime import datetime
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ptt"]
movies = db["movies"]

while True:
    try:
        print("\n1: Get the list of 15 articles. 2: Get the specified article. 3: Exit.")
        action = int(input("Enter an action: "))

        if action == 1:
            article_list = list(
                movies.aggregate(
                    [
                        {"$sample": {"size": 15}},
                        {"$project": {"_id": 0, "article_id": 1, "title": 1}}
                    ]
                )
            )

            print(f"article_id     title")

            for article in article_list:
                print(f"{article['article_id'] : <15}{article['title']}")

        elif action == 2:
            while True:
                try:
                    article_id = int(input("Enter an article_id or 0 to switch to other actions: "))
                    article = movies.find_one({"article_id": article_id}, {"_id": 0})

                    if article_id == 0:
                        break

                    else:
                        if article:
                            for k, v in article.items():
                                if k == "pushes":
                                    print("pushes\n")

                                    for i in v:
                                        push_time = datetime.strftime(i['push_time'], '%m-%d %H:%M')
                                        push_string = f"{i['push_tag']} {i['push_userid']} {i['push_content']} {push_time}"
                                        print(push_string, "\n")
                                
                                else:
                                    print(k, "\n")
                                    print(v, "\n")

                        else:
                            print("Article not found, try again or enter 0 to switch to other actions.")

                except:
                    print("Only accept integers, try again.")

        elif action == 3:
            print("Bye.")
            break
        
        else:
            print("Enter a valid number, try again.")

    except:
        print("Only accept integers, try again.")