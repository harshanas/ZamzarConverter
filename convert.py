import argparse, sys, requests, time, os, json
from requests.auth import HTTPBasicAuth


def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses Command")
    parser.add_argument("-s", "--source", help="Path of the file to be converted")
    parser.add_argument("-f", "--format", help="Format you need the file to get converted")

    options = parser.parse_args(args)
    return options


def init_job(api_key, source_file, target_format):
    endpoint = "https://sandbox.zamzar.com/v1/jobs"
    file_content = {'source_file': open(source_file, 'rb')}
    data_content = {'target_format': target_format}
    res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
    return res.json()


def job_info(api_key, job_id):
    endpoint = "https://sandbox.zamzar.com/v1/jobs/{}".format(job_id)
    res = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
    return res.json()


def download_file(api_key, file_id, local_filename):
    endpoint = "https://sandbox.zamzar.com/v1/files/{}/content".format(file_id)

    response = requests.get(endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))

    try:
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

            print("Ended Conversion...")

    except IOError:
        print("Error in Downloading File :(")


def no_errors(jobId):
    if 'errors' in jobId:
        return False
    else:
        return True


if __name__ == "__main__":
    options = getOptions()
    configFile = open("config.json", "r")
    config = json.loads(configFile.read())

    api_key = config['api_key']
    source_file = options.source
    target_format = options.format

    initJobData = init_job(api_key, source_file, target_format)
    jobId = initJobData['id']

    if (no_errors(initJobData)):
        print("Started Conversion...")
        job_status = job_info(api_key, jobId)

        while (job_status['status'] != "successful"):
            time.sleep(15)
            job_status = job_info(api_key, jobId)
        file_path = os.path.splitext(source_file)[0]
        download_file(api_key, job_status['target_files'][0]['id'], file_path + "." + job_status['target_format'])
    else:
        print(jobId)