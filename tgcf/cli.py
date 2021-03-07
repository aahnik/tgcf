import typer
import logging
from tgcf.forwarder import forwarder

app = typer.Typer()


logging.basicConfig(level=logging.INFO)

@app.command()
def forward():
    ''' Forward all existing messages.
    '''
    forwarder()


@app.command()
def sync():
    ''' Start live syncing.
    '''
    print('sync')



if __name__ == '__main__':
    app()
