from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment


class PostAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token_url = reverse("token_obtain_pair")
        self.posts_url = reverse("post-list-create")
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post.", author=self.user
        )
        self.post_url = reverse("post-detail", args=[self.post.id])
        self._authenticate()

    def _authenticate(self):
        response = self.client.post(
            self.token_url,
            {"username": "testuser", "password": "testpass"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_create_post(self):
        data = {"title": "New Post", "content": "This is a new post."}
        response = self.client.post(self.posts_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.latest("id").title, "New Post")

    def test_list_posts(self):
        response = self.client.get(self.posts_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

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
        self.token_url = reverse("token_obtain_pair")
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post.", author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post, author=self.user.username, text="This is a test comment."
        )
        self.comments_url = reverse("comment-list-create", args=[self.post.id])
        self._authenticate()

    def _authenticate(self):
        response = self.client.post(
            self.token_url,
            {"username": "testuser", "password": "testpass"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_create_comment(self):
        data = {"author": self.user.username, "text": "This is a new comment."}
        response = self.client.post(self.comments_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(Comment.objects.latest("id").text, "This is a new comment.")

    def test_list_comments(self):
        response = self.client.get(self.comments_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
