
class HtmlMananger:
    #that defines functions that let you create a new HTML document, 
    # and save the document to your files.
    # write-html.py
    def create_html():
        f = open('helloworld.html','w')
        message = """<html>
        <head></head>
        <body><p>Hello World!</p></body>
        </html>"""

        f.write(message)
        f.close()

    create_html()

# class AWSManager:
#     #defines the connections to boto3 and some functions that let you save your file to S3.