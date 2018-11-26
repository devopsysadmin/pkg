#!python
from argparse import ArgumentParser
from commons import run, ansicolor
from commons.response import Response
import sys

OUTPUT = 'json'
RESPONSE = Response()

def get_args():
	parser = ArgumentParser()
	parser.add_argument('action', choices=['add', 'del', 'up', 'upg'])
	parser.add_argument('params', nargs='?')
	parser.add_argument('-o', '--output', choices=['json', 'console'], default=OUTPUT)
	return parser.parse_args()

def pprint(msg, colors=None):
	if OUTPUT == 'console':
		ansicolor.prints(msg, colors)


def execute(cmd):
	pprint(cmd, ansicolor.fg('none', 'bold'))
	result = run(cmd)
	status = 'ok' if result.sc == 0 else 'error'
	RESPONSE.append(
					action='update',
					cmd=cmd,
					status=status, 
					message=result.stdout
				)
	pprint(result.stdout)

def install(params):
	execute('brew install %s' %params)

def remove(params):
	execute('brew uninstall %s' %params)

def update(params):
	execute('brew update')

def upgrade(params):
	execute('brew upgrade')
	execute('brew cask upgrade')


def main():
	global OUTPUT
	args = get_args()
	actions_map = {
		'add' : install,
		'del' : remove,
		'up' : update,
		'upg' : upgrade
	}
	OUTPUT = args.output
	actions_map[args.action](args.params)
	RESPONSE.dump(OUTPUT)

if __name__ == '__main__':
	main()