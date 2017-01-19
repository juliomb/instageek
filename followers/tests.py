from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from rest_framework.test import APITestCase
from rest_framework import status

from followers.models import Relationship
from followers.utils import get_followers, get_following


class RelationshipTests(TestCase):

    def setUp(self):
        """
        runs before any test
        """
        self.user1 = User.objects.create_user('luke', 'skywalker@starwars.com', 'skywalker')
        self.user2 = User.objects.create_user('anakin', 'anni@starwars.com', 'skywalker')
        Relationship.objects.create(origin=self.user1, target=self.user2) # user1 follows user2


    def test_get_followers_returns_ursers_follow_a_given_user(self):

        followers = get_followers(self.user2)
        self.assertEqual([self.user1], followers)


    def test_get_following_return_users_that_a_given_user_follows(self):

        following = get_following(self.user1)
        self.assertEqual([self.user2], following)



@override_settings(ROOT_URLCONF='followers.urls')
class APITests(APITestCase):

    USERS_PASSWORD = 'skywalker'
    FOLLOWING_API_URL = '/following/'

    def setUp(self):

        self.user1 = User.objects.create_user('luke', 'skywalker@starwars.com', self.USERS_PASSWORD)
        self.user2 = User.objects.create_user('anakin', 'anni@starwars.com', self.USERS_PASSWORD)
        self.user3 = User.objects.create_user('chewie', 'chewie@starwars.com', self.USERS_PASSWORD)
        self.user4 = User.objects.create_user('han', 'solo@starwars.com', self.USERS_PASSWORD)
        self.user5 = User.objects.create_user('r2d2', 'chewie@starwars.com', self.USERS_PASSWORD)
        self.user6 = User.objects.create_user('c3po', 'solo@starwars.com', self.USERS_PASSWORD)
        self.user7 = User.objects.create_user('leia', 'chewie@starwars.com', self.USERS_PASSWORD)
        self.user8 = User.objects.create_user('finn', 'solo@starwars.com', self.USERS_PASSWORD)

        Relationship.objects.create(origin=self.user1, target=self.user2)
        Relationship.objects.create(origin=self.user1, target=self.user3)
        Relationship.objects.create(origin=self.user1, target=self.user4)
        Relationship.objects.create(origin=self.user1, target=self.user5)
        Relationship.objects.create(origin=self.user1, target=self.user6)
        Relationship.objects.create(origin=self.user1, target=self.user7)
        Relationship.objects.create(origin=self.user1, target=self.user8)

        Relationship.objects.create(origin=self.user3, target=self.user1)
        Relationship.objects.create(origin=self.user3, target=self.user2)
        Relationship.objects.create(origin=self.user3, target=self.user4)


    def test_following_users_endpoint_fails_when_user_is_not_authenticated(self):

        Relationship.objects.create(origin=self.user1, target=self.user2)  # user1 follows user2
        response = self.client.get(self.FOLLOWING_API_URL)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_users_doesnt_follow_any_user_and_empty_list_is_returned(self):

        self.client.login(username=self.user2.username, password=self.USERS_PASSWORD)
        response = self.client.get(self.FOLLOWING_API_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


    def test_user_follows_three_users_and_three_users_are_returned(self):

        self.client.login(username=self.user3.username, password=self.USERS_PASSWORD)
        response = self.client.get(self.FOLLOWING_API_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)


    def test_user_follows_seven_users_and_seven_users_are_returned(self):

        self.client.login(username=self.user1.username, password=self.USERS_PASSWORD)
        response = self.client.get(self.FOLLOWING_API_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 7)
