import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

for post in data[:5]:
    print(post['title'])
for post in data[3:6]:
    print("Title:", post['title'])
    print("Body:", post['body'])
    print("------") 
for post in data[:6]:
    print("ID:",post['id'])
    print("Title:",post['title'])
print("total number of post:-", len(data))  
for post in data:
    if post['userId'] == 1:
        print("Id:", post['id'],"\n","Title:",post['title'],"\n","Body:", post['body'],"\n")
    if len(post['title']) > 30:
        print("Id:",post['id'],"\n","Title:",post['title'],"\n")
        print ("titles longer than 30:", len([post for post in data if len(post['title']) > 30]))
filtered_posts = [post for post in data if len(post['title']) > 30]

for post in filtered_posts:
    print("Id:", post['id'])
    print("Title:", post['title'])
    print()

print("Total titles longer than 30:", len(filtered_posts))
even = [post for post in data if post['id'] % 2 == 0]
for post in even:
        print("Id:", post['id'],"\n","Title:",post['title'],"\n")
print("Total even ids:", len(even))




        
        
