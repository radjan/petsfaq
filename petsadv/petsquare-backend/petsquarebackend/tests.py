import unittest
import transaction

from pyramid import testing

from .models import DBSession

from routes import api_routes


class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')

        from .models.location import Location_TB
        from .models import (
            Base,
            DBSession
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            success, model = Location_TB.create(name='one', description='1', gps='1,5', address='taipei', userid=1)
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def _callFUT(self, request):
        from .apis.location import LocationAPI
        import pyramid
        api = LocationAPI(request=request, context=None)
        return api.locations_list()

    def test_it(self):
        #from .views import my_view
        from .models.location import Location_TB
        from .apis.location import LocationAPI
        api_routes(self.config)
        request = testing.DummyRequest()
        request.matchdict = {'offset':1}
        response = self._callFUT(request)

        self.assertEqual(response['data'][0].name, 'one')
        self.assertEqual(response['data'][0].description, '1')
        self.assertEqual(response['data'][0].gps, '1,5')
        self.assertEqual(response['data'][0].address, 'taipei')
        self.assertEqual(response['data'][0].userid, 1)

