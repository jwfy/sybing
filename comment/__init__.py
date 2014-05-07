from comment.models import CustomComment
from comment.forms import CustomCommentForm


def get_model():
    return CustomComment

def get_form():
    return CustomCommentForm