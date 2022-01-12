import justpy as jp

def app():
    page = jp.QuasarPage()
    title = jp.QDiv(a=page, text="title", classes="text-h4 text-center")
    return page

jp.justpy(app)

