from celery import Celery

app = Celery(
        'celery_project', broker='amqp://', 
        backend='amqp://'
    )

app.conf.update(Celery_TAST_RESULT_EXPIRES=3600,)

if __name__ == '__main__':
    app.start()