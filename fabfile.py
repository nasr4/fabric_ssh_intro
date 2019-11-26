from fabric import task

@task
def sshhello(ctx):
    ctx.run("echo 'hello world'")

@task
def sshtouchfile(ctx):
    ctx.run("touch /tmp/a && ls -l /tmp/a; date")
