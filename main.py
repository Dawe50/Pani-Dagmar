import tornado.ioloop
import tornado.web
import asyncio
import zapis
import re
import schedule
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("indexpage.html")

class EnterDataHandler(tornado.web.RequestHandler):
    def post(self):
        mail = self.get_argument("mail")
        regex="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if(re.search(regex,mail)):
            self.render("odeslano.html")
            zapis.zapsat(mail)
        else:
            self.render("spatnymail.html")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/odeslano", EnterDataHandler),
        (r"/(header\.png)", tornado.web.StaticFileHandler, {"path": "src/"})
    ])

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

def poslat_mail():
    print("xxx")

schedule.every().tuesday.at("13:11").do(poslat_mail())
schedule.every(10).do(poslat_mail)

while True:
    schedule.run_pending()
    time.sleep(1)
