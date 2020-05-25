from django.test import TestCase
from .models import *

# Create your tests here.
class imageTestClass(TestCase):
    
    def setUp(self):
        # Creating a new category and saving it
        self.travel= Category(Name = 'Travel')
        self.travel.save_category()

        # Creating a new location and saving it
        self.new_location = location(place = 'Nairobi')
        self.new_location.save()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_search_by_location(self):
        search_by_location = Location.get(id)
        self.assertTrue(len(search_by_location)>0)
    
    def test_search_results(self):
        search_results = Image.search_by_category(search_term)
        self.assertTrue(len(search_results) == 0)    

class LocationTestClass(TestCase):
    '''
    Test case for the Location class and it's behaviours.
    '''
    # Set up method
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_location = Location( locs = "Nairobi")

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        '''
        Test to confirm that the object is being instantiated correctly.
        '''
        self.assertTrue(isinstance(self.new_location, Location))

    def test_save_method(self):
        '''
        Method to check whether the locations are getting saved.
        '''
        self.new_location.save()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):
    '''
    Test case for the Category class and it's behaviours.
    '''
    # Set up method
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_category = Category( category = "Travel")

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        '''
        Test to confirm that the object is being instantiated correctly.
        '''
        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_method(self):
        '''
        Method to check whether the categories are getting saved.
        '''
        self.new_category.save()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)