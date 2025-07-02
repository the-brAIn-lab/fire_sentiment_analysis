import praw

# Set up Reddit API client
reddit = praw.Reddit(
    client_id="http://localhost:8080",
    client_secret="OWxn-YzLwhj0nDMPb7Ai72gQxVJjmg",
    user_agent="prescribed-burning",  # e.g., "prescribed_burn_study"
)

# Search for relevant posts
subreddits = ["environment", "conservation", "firefighting", "environmentalism", "climate", 
              "nature", "urbanplanning", "geography", "forestry", "earth", "sustainability",
              "gardening", "wildfires", "landscapephotography", "agriculture", "rural"]  # Add relevant subreddits
search_term = "prescribed burns"
results = []

for subreddit in subreddits:
    print(f"Searching in r/{subreddit}...")
    for post in reddit.subreddit(subreddit).search(search_term, limit=50):  # Limit to 50 posts
        post_data = {
            "title": post.title,
            "score": post.score,
            "url": post.url,
            "num_comments": post.num_comments,
            "comments": [],
        }
        # Fetch comments
        post.comments.replace_more(limit=0)
        for comment in post.comments.list()[:10]:  # Limit to 10 comments per post
            post_data["comments"].append(comment.body)
        results.append(post_data)

# Save results to a file
import json
with open("reddit_prescribed_burns.json", "w") as f:
    json.dump(results, f, indent=4)

print("Data saved to reddit_prescribed_burns.json")