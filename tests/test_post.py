import unittest
from app.models import Post,User
from app import db

class PostModelTest(unittest.TestCase):
    def setUp(self):
        self.user_Alice=User(username="Alice", password="potato", email="alice@ms.com")
        self.new_post=Post(id=1,category="All", title="Great Things Take Time", blog="User Tests for blog posts", user=self.user_Alice)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.category,"All")
        self.assertEquals(self.new_post,title,"Great Things Take Time")
        self.assertEquals(self.new_post,blog,"User Tests for blog posts")
        self.assertEquals(self.new_post,user,self.user_Alice)

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

    def test_get_post_by_id(self):
        self.new_post.save_post()
        got_posts=Post.get_posts("All")
        self.assertTrue(len(got_posts)== 1)