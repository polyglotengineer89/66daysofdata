from celery_project import app
from house_price import get_house_price

class BaseTask(app.Task):
    """Abstract base class for all tasks in my app."""

    abstract = True

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        """Log the exceptions to sentry at retry."""
        sentrycli.captureException(exc)
        super(BaseTask, self).on_retry(exc, task_id, args, kwargs, einfo)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Log the exceptions to sentry."""
        sentrycli.captureException(exc)
        super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)

        
@app.task(
    bind=True,
    max_retries=3,
    soft_time_limit=5,
    base=BaseTask)
def add(self):
    get_house_price()

# celery task
# get_page -> as constructor == priority (url)
# get data = general

# write to xlx
