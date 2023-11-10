import logging
from django.shortcuts import render
from .tasks import simple_task_1, simple_task_2


def index(request):
    return render(request, 'index.html')


logger = logging.getLogger(__name__)


def view1(request):
    logger.info('Starting view1()')
    if request.method == 'POST':
        simple_task_1.delay()
        logger.info('Finished view1()')
        return render(request, 'index.html', context={'button1': True})


def view2(request):
    if request.method == 'POST':
        simple_task_2.delay()
        return render(request, 'index.html', context={'button2': True})
