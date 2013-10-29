class ticket(object):
    def __init__(self,price,start = '',destination = '',date = '',Class = 'economy'):
        """initialize the ticket field"""
        self.start = start
        self.destination = destination
        self.date = date
        self.Class = Class
        self.price = price

    def __str__(self):
        """display all the field"""
 
        return  "start from %s to %s the date is:%s Class:%s and price:%d" % \
               (self.start,self.destination,self.date,self.Class,self.price)
