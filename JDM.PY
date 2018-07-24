import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

from google.appengine.ext import ndb

./google-cloud-sdk/install.sh

pip install --upgrade google-cloud-bigquery



class Clothes(ndb.Model):
    shirts = ndb.StringProperty(required=True)
    pants = ndb.IntegerProperty(required=True)
    shoes = ndb.IntegerProperty(required=True)

name = input ('Enter your name')

def clothes(self):
    shirts = input ('Enter shirt size S M L XXL XXXL XXXXL')
    pants = input ('Enter pants size')
    shoes = input ('Enter shoes size')
    return(clothes)

shirts.put()
pants.put()
shoes.put()


