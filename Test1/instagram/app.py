from flask import Flask
post =[]

p=[]
@app.route('/add', methods=['GET','POST'])
def addPost():
    username = input("Enter post username")
    caption= input("Enter your caption")


    posts={
        'id': username,
        'name' : caption
    }
    post.append(posts)
    print("post added succesfully")
@app.route('/')
def  viewPost():
    for i in post:
        print({i['username']}, {i['username']}) 
@app.route('/username', methods=['DELETE'])
def delPost():
    username=input("Enter the username")
    for i in post:
        if i['username'] == username:
            post.remove(i)
            print("Deleted")
            return


 




