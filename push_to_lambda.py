import boto3
import os
import pprint
from make_zip import make_zip
import datetime

"""
You run this file to select which Lambda function to send to AWS -
it creates a zip file to send to AWS.
"""

current_directory = os.path.dirname(os.path.realpath(__file__))

# TODO - I Either "prezipped" or "zipped_packages" isn't needed
apps = {
    "jules": {
        "arn": 'arn:aws:lambda:us-east-1:705121905978:function:JulesTalks',
        "app_path": current_directory + '/app/',
        'region_name': 'us-east-1',
        "site_packages_path": current_directory + '/jenv/lib/python2.7/site-packages/',
        "prezipped": None
    }
}


def push_app_to_lambda(app_name):
    print("Pushing to lambda. Remember, if you're somewhere with slow upload speeds, you'll need to move to S3 using"
          "rubber ducky, then upload using the console. ")
    return push_to_lambda(
        app_name=app_name,
        app_directory=apps[app_name]['app_path'],
        region_name=apps[app_name]['region_name'],
        arn=apps[app_name]['arn'],
        site_packages_path=apps[app_name].get('site_packages_path'),
        prezipped=apps[app_name].get('zipped_packages'),
        temp_file_path=current_directory + '/lambda_uploads/' + app_name + '.zip'
    )


def push_to_lambda(app_name, app_directory, region_name, arn, site_packages_path, prezipped, temp_file_path):
    make_zip(make_file_path=temp_file_path, root_dir=app_directory, site_packages_path=site_packages_path,
             prezipped=prezipped)

    aws_access_key_id = os.environ.get('JULES_AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('JULES_AWS_SECRET_KEY')

    raw_input('pause after printing')

    client = boto3.client('lambda', region_name='us-east-1',
                          aws_access_key_id=os.environ.get('JULES_AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key='JULES_AWS_SECRET_KEY')

    client = boto3.client('lambda', region_name=region_name)

    with open(name=temp_file_path, mode='r') as in_file:
        data = in_file.read()

    start_time = datetime.datetime.utcnow()
    print(
        'Uploading {app_name} lambda package. This might take a while, uploads can be slow.'.format(app_name=app_name))

    response = client.update_function_code(
        FunctionName=arn,
        ZipFile=data,
    )
    end_time = datetime.datetime.utcnow()

    print('Tried to upload {app_name}. Here is the response:'.format(app_name=app_name))
    pprint.pprint(response)
    print('It took this much time to upload:')
    print(end_time - start_time)

    print('If you need it, the temp file can be found at {0}'.format(temp_file_path))


if __name__ == '__main__':
    response = None
    sorted_keys = apps.keys()
    sorted_keys.sort()
    print('just printed sorted keys after sorting')
    print("Choose one:\n", sorted_keys)
    while response not in apps.keys():
        response = raw_input('What appliction to zip and push to lambda?\n')
        if response not in apps.keys():
            print("That's not an ec2_app. Try ", sorted_keys)
    push_app_to_lambda(app_name=response)
