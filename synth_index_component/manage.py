import os

from flask_script import Manager, Shell, Server

from app import create_app


app = create_app()


manager = Manager(app)


def _make_context():
    return {'app': app}


@manager.command
def test():
    import pytest
    exit_code = pytest.main(['tests', '-q'])
    return exit_code


manager.add_command('server', Server())
manager.add_command('shell', Shell(make_context=_make_context))


if __name__ == '__main__':
    manager.run()
