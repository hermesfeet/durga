import os
import shutil
import zipfile

current_directory = os.path.dirname(os.path.realpath(__file__))

'''
Lambda functions come with standard Python and the package Boto3 to connect to other AWS services.
Some Lambda functions need to access packages included in standard Python - there are 2 methods
to include these packages:

1) Zip all the files and folders in the site packages folder of a virtual environment.

2) Use a pre-zipped file.  We do this because the files from the virtual environment need to be
created on EC2.

So make_zip.py takes any lambda function code (in the bot directory, the loggers, etc) and then optionally
zips up any site packages you want (or you can give this a pre-zipped file).
'''


def zipdir(path, ziph):
    """
    I'm pretty sure this flattens the directory.
    See https://docs.python.org/2/library/os.html
    """
    for root, dirs, files in os.walk(path, followlinks=True):
        for f in files:
            filename = os.path.join(root, f)
            arcname = filename.replace(path, '')
            if f[0] != '.' and f[-4:] != '.pyc':
                print('adding file ', filename)
                ziph.write(filename=filename, arcname=arcname)


def make_zip(make_file_path, root_dir, site_packages_path, prezipped):
    assert (make_file_path[-4:] == '.zip')
    try:
        os.remove(make_file_path)
    except OSError:
        pass

    if prezipped:
        print("Creating zip from a zip file that was taken from the EC2 instance. We do this because the pg2 "
              "site package files for Lambda/Ubuntu don't exactly match those for Mac.")
        shutil.copyfile(prezipped, make_file_path)
        z = zipfile.PyZipFile(file=make_file_path, mode='a')
        zipdir(path=root_dir, ziph=z)
        z.close()
        print("Done making zip from pre-zipped file. Zip stored at {0}".format(make_file_path))
        print("Zip size was {0} MB".format(round(float(os.path.getsize(make_file_path)) / 1000000), 2))

    else:
        basename = make_file_path[0:-4]
        print('basename', basename)
        # shutil.make_archive(base_name=basename, format='zip', root_dir=root_dir)
        z = zipfile.PyZipFile(file=make_file_path, mode='w')
        zipdir(path=root_dir, ziph=z)
        z.close()
        # raw_input('at this point the zip should only have the ec2_app files, not the packages')

        if site_packages_path:
            z = zipfile.PyZipFile(file=make_file_path, mode='a')
            zipdir(path=site_packages_path, ziph=z)
            z.close()

        print("Done making zip. Zip stored at {0}".format(make_file_path))
        print("Zip size was {0} MB".format(round(float(os.path.getsize(make_file_path))/1000000), 2))

        # if I do need to copy, I'll copy from here

transfer = """
scp -i ~/dogbert.pem ubuntu@ec2-52-42-233-14.us-west-2.compute.amazonaws.com:/home/ubuntu/voiceapi/deleteme.zip  ~/voiceapi/process_base.zip
"""