from google.appengine.ext import ndb

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
