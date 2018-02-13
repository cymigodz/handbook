import datetime
import firebase_admin
#Authentication
from firebase_admin import credentials
#Database
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/home/ubuntu/workspace/firebase/adminkey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://handbook-26031.firebaseio.com/'
})

class Post:
    REF_POSTS = "/blog/posts"
    REF_POSTSID = "/blog/postsid"

    KEY_SHOW = "info/show"
    KEY_TITLE = "title"
    KEY_TAGS = "tag"
    KEY_TIME = "info/time"
    KEY_BODY = "body"
    KEY_FOOTER = "footer"
    
    def __init__(self):
        self.show = True
        self.title = "Empty Title"
        self.tags = ["example"]
        self.tagtypes = ["primary"]
        self.time = datetime.datetime.now()
        self.body = "<h3>Example body title</h3><br><p>Example Paragraph</p>"
        self.footer = ""
        
    def __init__(self, show, title, tags, tagtypes, time, body, footer):
        self.show = show
        self.title = title
        self.tags = tags
        self.tagtypes = tagtypes
        self.time = time
        self.body = body
        self.footer = footer
        

class Blog:
# Blog class is a collection of functions targetting firebase
# database, to retrieve blog posts under "home" page

    @staticmethod
    def getPageList(page, sort, perPage):
    # Sort the posts by sort provided
    # Divide posts into pages by perPage provided
    # return all the posts in page provided 
        
        ref = db.reference(Post.REF_POSTSID)
        #Reference to posts in database
        
        query = ref.order_by_key()
        #by default order_by_key gives ascending order
        #latest posts are always the higher key number
        #easier way to understand is to change "last" to "newest"
        # and "first" to "oldest"
        # ref.order_by_key() : sort from old to new
        # limit_to_last(page*perPage) : get everything from page 1 to your page
        
        snapshot = query.get()
        for key, val in snapshot.items():
            print(val)
        posts = []
        return posts
        
    @staticmethod
    def getPost(id):
        ref = db.reference(Post.REF_POSTS)
        query = ref.order_by_key().equal_to(id)
        snapshot = query.get()
        
        for key, val in snapshot.items():
            print(val)
            
        return

        
        
Blog.getPageList(1,1,1)
Blog.getPost("20180208073629044998")