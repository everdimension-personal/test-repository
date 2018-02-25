import webapp2

print 'Start...'

class MainPage(webapp2.RequestHandler):
    def get(self):
        print 'hello'
        print 'another hello'
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('hello, udacity')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
