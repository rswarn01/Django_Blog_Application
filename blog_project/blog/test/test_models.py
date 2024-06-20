from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post.", author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertIsNotNone(self.post.published_date)


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post.", author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post, author=self.user.username, text="This is a test comment."
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.post.title, "Test Post")
        self.assertEqual(self.comment.author, "testuser")
        self.assertEqual(self.comment.text, "This is a test comment.")
        self.assertIsNotNone(self.comment.created_date)
