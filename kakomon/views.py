from django.views.generic import TemplateView

""" Top画面 """


class IndexView(TemplateView):
    template_name = "kakomon/index.html"
