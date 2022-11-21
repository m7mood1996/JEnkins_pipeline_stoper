from jenkinsapi.jenkins import Jenkins
import sys
import requests
API_TOKEN = '11f4f5124b1188e47ac7784bd64ab69eaf'
jenkins_url = 'http://localhost:8080'
USER = 'm7mood1996'
def get_server_instance():
    server = Jenkins(jenkins_url,USER, API_TOKEN)
    return server
    
'''Get job details of each job that is running on the Jenkins instance'''
def get_job_details(current_job_name):
    # Refer Example #1 for definition of function 'get_server_instance'
    print('Connecting to the Jenkins Server...')
    server = get_server_instance()
    print('_'*50)
    for job_name, job_instance in server.get_jobs():
        print ('Job Name: ', job_instance.name)
        print ('Job is running' if job_instance.is_running() else 'Job is not running' )
        print('_'*50)
        if job_instance.is_running() and not job_instance.name == current_job_name:
            response = requests.post(job_instance.baseurl +'/lastBuild/buildNumber', auth=(USER, API_TOKEN))
            response = requests.post(job_instance.baseurl +'/'+response.text + '/stop', auth=(USER, API_TOKEN))
    

def main(current_job_name):
    print('Starting...')
    get_job_details(current_job_name)


if __name__ == '__main__':
    main(sys.argv[1])