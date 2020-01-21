import dropbox
import os
import ntpath

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        #upload a file to Dropbox using API v2
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
        
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def main():
    transferData = TransferData(os.environ.get('DROPBOX_ACCESS_TOKEN'))
    ntpath.basename(os.environ.get('ATTACHMENT'))
    file_from = os.environ.get('ATTACHMENT')
    # The full path to upload the file to, including the file name
    file_to = '/' + os.environ.get('PROJECT_NAME') + '/' + path_leaf(file_from) 
   # print(file_to)
    transferData.upload_file(file_from, file_to)
    dbx = dropbox.Dropbox(os.environ.get('DROPBOX_ACCESS_TOKEN'))
    f = open("link.txt", "w")
    f.write("https://www.dropbox.com/home/Apps/Code95AndroidAPK/" + os.environ.get('PROJECT_NAME') )
    f.close()

if __name__ == '__main__':
    main()


      #try:
    #    shared_link_metadata = dbx.sharing_create_shared_link_with_settings('/'+os.environ.get('PROJECT_NAME'))
     #   print(shared_link_metadata.url)
     #   
    #except:
     #   pass