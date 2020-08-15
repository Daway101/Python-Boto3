import boto3

class HtmlDocument:
    #that lets you initialize some HTML for a new document.
    def __init__(self,content):
        self.content = content

class HtmlManager:
    #that defines functions that let you create a new HTML document, 
    # and save the document to your files.
    # write-html.py

    def __init__(self):
        self.document = None

    def create_html(self):
        
        message = """<html>
        <head>Welcome to my World!</head>
        <body><p> My name is Dawa. Follow along as we write a cloud-based application using the boto3 Amazon SDK.</p>
        <p> This file will be uploaded to Amazon S3. </p>
        </body>
        </html>"""
        newdoc = HtmlDocument(message)
        self.document = newdoc
        print(newdoc)

        
    def save_html_file(self):
        f = open('Dawa.html','w')
        f.write(self.document.content)
        f.close()


class AWSmanager:
    def __init__(self):
        self.s3=boto3.resource('s3')
   
    def listBucketFile(self, bucketName):
        bucket = self.s3.Bucket(bucketName)
        files = bucket.objects.all()
        for file in files:
            print(file.key) dawa
        
    #define connections to boto3 and save file to s3
    def save_to_s3(self):   
        s3 = boto3.client('s3')
        boto3.client('s3').upload_file('Dawa.html', 'lmtd-class', 'Dawa.html')

manager = HtmlManager()
manager.create_html()
manager.save_html_file()

aws_manager= AWSmanager()
aws_manager.save_to_s3()
aws_manager.listBucketFile("lmtd-class")