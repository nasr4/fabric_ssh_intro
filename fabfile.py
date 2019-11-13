from fabric import task

@task
def sshhello(ctx):
    ctx.run("echo 'hello world'")
