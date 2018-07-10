from time import gmtime, strftime

class HTMLGenerator(object):

    def generate(self,page_name,accuracy):
        f = open(page_name, 'w')

        message = """<html>
        <head><title>Results</title>
        <meta http-equiv="refresh" content="4"></head>
        <body><p> Your accuracy is """+ str(accuracy)+ """%</p>
        <p> Last generation time: """+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+ """</p></body>
        </html>"""
        print(message)
        f.write(message)
        f.close()