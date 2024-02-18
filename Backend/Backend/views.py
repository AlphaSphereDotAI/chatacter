<<<<<<< HEAD
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is {now}.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
=======
from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is {now}.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
>>>>>>> origin/main
