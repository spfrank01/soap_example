from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11

class CCTVService(ServiceBase):
    @srpc(String, _returns=Iterable(String))
    def peopleInCCTV(CCTVName):
        if CCTVName == 'CCTV1':
            yield 'Frank'
            yield 'Oat'
        elif CCTVName == 'CCTV2':
            yield 'Frank'
        elif CCTVName == 'CCTV3':
            yield 'None'
        else:
            None

    @srpc(_returns=Iterable(String))
    def CCTVList():
        yield 'CCTV01'
        yield 'CCTV02'
        yield 'CCTV03'

application = Application([CCTVService],
    tns='spyne.examples.cctv',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server('127.0.0.1', 7789, wsgi_app)
    server.serve_forever()