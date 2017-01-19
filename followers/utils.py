from django.contrib.auth.models import User


def get_followers(user):
    followers = list()
    for relationship in user.relationship_target.select_related('origin'):
        followers.append(relationship.origin)
    return followers


def get_following(user):
    following = list()
    for relationship in user.relationship_origin.select_related('target'):
        following.append(relationship.target)
    return following
