from celery import shared_task
from boilerplate.apps.posts.models import Post

@shared_task(name="increase_post_visit_count", bind=True)
def increase_post_visit_count(self, post_id: int):
    try:
        post = Post.objects.get(id=post_id)
        post.visit_count += 1
        post.save(update_fields=["visit_count"])
        print(f"Post {post_id} visit_count updated to {post.visit_count}")
    except Post.DoesNotExist:
        print(f"Post with id {post_id} does not exist.")
    except Exception as e:
        print(f"Error updating post visit_count: {e}")
