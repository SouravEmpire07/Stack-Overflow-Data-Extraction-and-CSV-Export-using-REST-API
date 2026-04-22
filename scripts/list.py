import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

title = []
for post in data:
    title.append(post['title'])
print(title[:3])
for p in title:
    print(p)

count = {} #Q9

for post in data:
    user = post['userId']
    
    if user in count:
        count[user] += 1
    else:
        count[user] = 1

print(count)