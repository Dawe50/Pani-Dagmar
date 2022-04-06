import schedule
import time
import generator

def poslat_mail():
    generator.generaator()

schedule.every(10).seconds.do(poslat_mail)

while True:
    schedule.run_pending()
    time.sleep(1)
