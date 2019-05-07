import rAuth

reddit = rAuth.get_reddit_object()
for submission in reddit.subreddit('onebag').top(time_filter="all"):
    if submission.link_flair_text is not None:
        if "Packing" in submission.link_flair_text:
            print(submission.title)

            for comment in submission.comments:

                if comment.body.count("*") > 3 or comment.body.count("-") > 3:
                    print("www.reddit.com" + str(submission.permalink))
                    print("Comments")
                    print(comment.body)
                    print(" ")
                else:
                    print("Malformed packing list : " +  "www.reddit.com" + str(submission.permalink))
                    print(" ")
                    break
