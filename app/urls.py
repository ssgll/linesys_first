from app import index

from app.views import pageIndex


index.add_url_rule(rule="/index/", endpoint=None, view_func=pageIndex, methods=["POST", "GET"])
