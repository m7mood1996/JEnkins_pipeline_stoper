from jenkinsapi.jenkins import Jenkins
API_TOKEN = '11f4f5124b1188e47ac7784bd64ab69eaf'
def get_server_instance():
    jenkins_url = 'http://localhost:8080'
    server = Jenkins(jenkins_url,'m7mood1996', API_TOKEN)
    return server
    
'''Get job details of each job that is running on the Jenkins instance'''
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    print('Connecting to the Jenkins Server...')
    server = get_server_instance()
    for job_name, job_instance in server.get_jobs():
        print ('Job Name: ', job_instance.name)
        print ('Job Description: ' ,job_instance.get_description())
        print ('Is Job running: ' ,job_instance.is_running())
        print ('Is Job enabled: ' ,job_instance.is_enabled())


def main():
    print('Starting...')
    get_job_details()


if __name__ == '__main__':
    main()