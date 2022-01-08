{"filter":false,"title":"urls.py","tooltip":"/config/urls.py","undoManager":{"mark":25,"position":25,"stack":[[{"start":{"row":0,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["from django.urls import path","from . import views","from django.contrib import admin","","","app = 'first_news'","urlpatterns = [","    path('', views.first_object, name='first_object'),","    path('article/<int:pk>/', views.secound_object,name='secound_object'),","    path('article/new/', views.thrd_object, name='thrd_object'),","    path('comment/create/<int:pk>/',views.force_object,name='force_object'),","    ]",""],"id":93}],[{"start":{"row":7,"column":3},"end":{"row":10,"column":76},"action":"remove","lines":[" path('', views.first_object, name='first_object'),","    path('article/<int:pk>/', views.secound_object,name='secound_object'),","    path('article/new/', views.thrd_object, name='thrd_object'),","    path('comment/create/<int:pk>/',views.force_object,name='force_object'),"],"id":94},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"remove","lines":[" "]},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":[" "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":[" "],"id":95},{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":96},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":19},"action":"remove","lines":["from . import views"],"id":97},{"start":{"row":0,"column":28},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["p"],"id":98},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["a"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["t"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["h"]}],[{"start":{"row":6,"column":8},"end":{"row":6,"column":10},"action":"insert","lines":["()"],"id":99}],[{"start":{"row":6,"column":9},"end":{"row":6,"column":11},"action":"insert","lines":["''"],"id":100}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":[","],"id":101}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["i"],"id":102},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["n"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["c"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["l"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["u"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["d"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":19},"end":{"row":6,"column":21},"action":"insert","lines":["()"],"id":103}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["f"],"id":104},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["i"]}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":22},"action":"remove","lines":["fi"],"id":105},{"start":{"row":6,"column":20},"end":{"row":6,"column":30},"action":"insert","lines":["first_news"]}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["."],"id":106},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["u"]},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["r"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["l"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["¥"],"id":107},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"remove","lines":["s"],"id":108},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"remove","lines":["¥"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"remove","lines":["e"]}],[{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["s"],"id":109}],[{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["'"],"id":110}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["'"],"id":111}],[{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"insert","lines":[","],"id":112},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"insert","lines":["i"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"insert","lines":["n"]},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"insert","lines":["c"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"insert","lines":["l"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"insert","lines":["u"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"insert","lines":["d"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"remove","lines":["e"],"id":113},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"remove","lines":["d"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"remove","lines":["u"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"remove","lines":["l"]},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"remove","lines":["c"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"remove","lines":["n"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"remove","lines":["i"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"remove","lines":[","]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":["n"]}],[{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"insert","lines":["n"],"id":114}],[{"start":{"row":0,"column":28},"end":{"row":0,"column":29},"action":"insert","lines":[","],"id":115},{"start":{"row":0,"column":29},"end":{"row":0,"column":30},"action":"insert","lines":["i"]},{"start":{"row":0,"column":30},"end":{"row":0,"column":31},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"insert","lines":["l"],"id":116},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"insert","lines":["u"]},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"insert","lines":["d"]},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"remove","lines":["e"],"id":117},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"remove","lines":["d"]},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"remove","lines":["u"]},{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"remove","lines":["l"]}],[{"start":{"row":0,"column":31},"end":{"row":0,"column":32},"action":"insert","lines":["c"],"id":118},{"start":{"row":0,"column":32},"end":{"row":0,"column":33},"action":"insert","lines":["l"]},{"start":{"row":0,"column":33},"end":{"row":0,"column":34},"action":"insert","lines":["u"]},{"start":{"row":0,"column":34},"end":{"row":0,"column":35},"action":"insert","lines":["d"]},{"start":{"row":0,"column":35},"end":{"row":0,"column":36},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":36},"end":{"row":0,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1641575050681,"hash":"1e68bed34120ad8cf037c2a7c6ba14c2e59e1724"}