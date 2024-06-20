from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment


class PostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post.", author=self.user
        )
        self.post_url = reverse("post-detail", args=[self.post.id])

    def test_create_post(self):
        url = reverse("post-list-create")
        data = {"title": "New Post", "content": "This is a new post."}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.latest("id").title, "New Post")

    def test_list_posts(self):
        url = reverse("post-list-create")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_retrieve_post(self):
        response = self.client.get(self.post_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Post")

    def test_update_post(self):
        data = {"title": "Updated Post", "content": "This is an updated post."}
        response = self.client.put(self.post_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated Post")

    def test_delete_post(self):
        response = self.client.delete(self.post_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)


class CommentAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post.", author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post, author="commenter", text="This is a test comment."
        )
        self.comment_url = reverse("comment-list-create", args=[self.post.id])

    def test_create_comment(self):
        data = {"author": "new commenter", "text": "This is a new comment."}
        response = self.client.post(self.comment_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(Comment.objects.latest("id").text, "This is a new comment.")
