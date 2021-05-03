import unittest
from app.models import Post, Comment,User
from app import db

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        '''
        set up method that will run before every test runs
        '''
        self.new_comment = Comment(id=1,comment="Test Comment", user=self.user_Alice, post_id=self.new_post)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

     def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_Alice)
        self.assertEquals(self.new_comment.post_id,self.new_post)


