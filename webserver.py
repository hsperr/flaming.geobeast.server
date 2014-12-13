import falcon
from wsgiref import simple_server
from ConfigParser import SafeConfigParser

from GeoBeastRepository import GeoBeastRepository
import traceback

from geolocation.google_maps import GoogleMaps


config =SafeConfigParser()
config.read('conf/server.conf')

google_maps = GoogleMaps(api_key=config.get('Maps', 'key'))
repo = GeoBeastRepository()

class GeoBeastSpawn(object):
    def on_get(self, req, resp):
        try:
            lat, lng = req.get_param('pos').split(',')
            lat=float(lat)
            lng=float(lng)
            location = google_maps.search(lat=lat, lng=lng).first()
            formatted_address = location.formatted_address

            resp.status = falcon.HTTP_200
            resp.body = (str(repo.get_spawn_for_address(formatted_address)))
        except:
            raise falcon.HTTPError(falcon.HTTP_400, 'Somethings wrong:'+traceback.format_exc())

app = falcon.API()

spawner=GeoBeastSpawn()

app.add_route('/get_spawn', spawner)

if __name__ == '__main__':
    addr = config.get('Server', 'address')
    port = config.get('Server', 'port')
    print 'Running on:', addr, port
    httpd = simple_server.make_server(addr, int(port), app)
    httpd.serve_forever()
