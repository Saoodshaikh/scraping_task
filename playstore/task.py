from celery import shared_task  
  
@shared_task(bind=True)  
def test_func(self):  
    for i in range(1,100000000):  
        print(i)  
    return "Completed"  