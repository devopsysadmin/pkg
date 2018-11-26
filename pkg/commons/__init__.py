import os, sys, subprocess, shlex

class NameSpace (object):
    def __init__ (self, **kwargs):
        self.__dict__.update(kwargs)
    def __repr__ (self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))
    def __eq__ (self, other):
        return self.__dict__ == other.__dict__
    def dict(self):
    	return self.__dict__

def run_py2(cmd):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	stdout, _ = p.communicate()
	return NameSpace(sc=p.returncode, stdout=stdout)

def run_py3(cmd):
	p = subprocess.run(cmd, capture_output=True)
	stdout = p.stdout.decode('utf8')
	return NameSpace(sc=p.returncode, stdout=stdout)

def run(cmd):
	if sys.version_info < (2, 7, 99):
		runcmd = run_py2
	elif sys.version_info < (3, 99):
		runcmd = run_py3

	if isinstance(cmd, str):
		cmd = shlex.split(cmd)
	return runcmd(cmd)
