"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path


from applications.home.views import Home


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),


    # contact
    path('contact/', include('applications.contact.urls'), name='contact'),

    # committee
    path('committee/', include('applications.committee.urls'), name='committee'),

    # committee_assessment
    path('committee_assessment/', include('applications.committee_assessment.urls'), name='committee_assessment'),

    # information
    path('information/', include('applications.information.urls'), name='information'),

    # jury
    path('jury/', include('applications.jury.urls'), name='jury'),

    # jury_assessment
    path('jury_assessment/', include('applications.jury_assessment.urls'), name='jury_assessment'),

    # panel
    path('panel/', include('applications.panel.urls'), name='panel'),

    # parameters
    path('parameters/', include('applications.parameters.urls'), name='parameters'),

    # postulation
    path('postulation/', include('applications.postulation.urls'), name='postulation'),

    # postulation_filter
    path('postulation_filter/', include('applications.postulation_filter.urls'), name='postulation_filter'),

    # reports
    path('reports/', include('applications.reports.urls'), name='reports'),

    # visits
    path('visits/', include('applications.visits.urls'), name='visits'),

    # home
    path('', Home.as_view(), name='home'),
]

# media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

