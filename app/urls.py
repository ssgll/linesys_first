from app import index

from app.views import pageIndex


index.add_url_rule(rule="/", endpoint=None, view_func=pageIndex, methods=["POST", "GET"])
