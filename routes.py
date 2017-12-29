from aiohttp import web
from views import index
from downloader import download

async def downloadHandler(request):
    data =  await request.post() # get request body
    try:
        download(data['link']) # download requested link
        return web.Response()
    except:
        return web.Response(status=400) # bad request


def setup_routes(app):
    app.router.add_get('/', index) # serve the html file
    app.router.add_post('/download', downloadHandler) # download request link
