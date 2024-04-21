from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<center><h1>Welcome to Our Home Budget App</h1></center>"        
        "<center><h3>Happy Coding!!</h3></center>"
        "<ul> "
        "<li><a href='kindsons_corner'>Kindsons's Corner</a></li>"
        "<li><a href='solomons_corner'>Solomon's Corner</a></li>"
        "<li><a href='cintias_corner'>Cintia's Corner</a></li>"
        "<li><a href='baldens_corner'>Balden's Corner</a></li>"
    )
