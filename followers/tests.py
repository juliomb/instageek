from django.contrib.auth.models import User
from django.test import TestCase

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
