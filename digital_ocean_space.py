def upload_to_space(source_file, destination_file, length=None, width=None, height=None):
    import boto3
    from boto3 import session
    from botocore.client import Config
    from boto3.s3.transfer import S3Transfer
    import os
    #Use the API Keys you generated at Digital Ocean
    ACCESS_ID = '[ACCESS_ID]'
    SECRET_KEY = '[SECRET_KEY]'

    # Initiate session
    session = session.Session()
    client = session.client('s3',
                            region_name='nyc3', #enter your own region_name
                            endpoint_url='https://nyc3.digitaloceanspaces.com', #enter your own endpoint url
                            
                            aws_access_key_id=ACCESS_ID,
                            aws_secret_access_key=SECRET_KEY)


    # client.create_bucket(Bucket='n2aa-replay')

    transfer = S3Transfer(client)

    # client.put_object(Bucket='n2aa-replay',
    #                 Key='youtube' +"/"+ key,
    #                 # Body=b'The contents of the file.',
    #                 ACL='public-read')

    # Uploads a file called 'name-of-file' to your Space called 'name-of-space'
    # Creates a new-folder and the file's final name is defined as 'name-of-file' 
    transfer.upload_file(source_file, 'ecodes-video-uploads', destination_file,
                            extra_args={
                                'ACL': 'public-read',
                                'Metadata': {
                                    'x-amz-meta-length': str(length),
                                    'x-amz-meta-width': str(width),
                                    'x-amz-meta-height': str(height)
                                }
                            }
                        )

    
    #This makes the file you are have sp    ecifically uploaded public by default. 
    # response = client.put_object_acl(ACL='public-read', Bucket='n2aa-replay', Key="%s/%s" % ('n2aa-replay', key))
    # response = client.put_object_acl(ACL='public-read', Bucket='n2aa-replay', Key=destination_file)
    # response = client.put_object( ACL='public-read', Bucket='n2aa-replay', Key=destination_file,
    #                                 Metadata={
    #                                     'x-amz-meta-length': str(length)
    #                                 }
    #                             )

    os.remove(source_file)
    # print("File Removed!")

    # response = client.list_objects(Bucket='n2aa-replay')
    # print(response)
    # for obj in response['Contents']:
    #     print(obj['Key'])