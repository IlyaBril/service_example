from fabric import task

@task
def deploy(ctx):
    print("Deploying service to PROD!!!")