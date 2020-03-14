from app import index
from flask import render_template_string


def pageIndex():
    return render_template_string(
        """
        Hello World!
        """
    )
