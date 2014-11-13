from django.test import TestCase
from fabric import models
# Create your tests here.
class TestTry(TestCase):
 #   def setUp(self):



    def testOne(self):
        edition = models.Product.objects.filter(pk=2)
        print edition
        editionName = edition
        #editionResource = edition.resource.all()

       # editionVcpu = edition.resource.get(name='vCPU')
        #editionRam = edition.resource.get(name='Ram')
        #editionStorage = edition.resource.get(name='Storage')

        #print editionVcpu

        self.assertEqual(editionName, editionName)
        #self.assertEqual(editionRam, 'Ram')
        #self.assertEqual(editionStorage, 'Storage')