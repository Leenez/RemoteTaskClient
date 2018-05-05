"""
Add binary-mode options to SSHClient.exec_command(...) for binary stdout, stderr channels.

See: https://github.com/paramiko/paramiko/issues/291
"""


import paramiko

def _patched_exec_command(self, 
                          command, 
                          bufsize=-1, 
                          timeout=None, 
                          get_pty=False, 
                          stdin_binary=True, 
                          stdout_binary=False, 
                          stderr_binary=False):
    
    chan = self._transport.open_session()
    if get_pty:
        chan.get_pty()
    chan.settimeout(timeout)
    chan.exec_command(command)
    stdin = chan.makefile('wb' if stdin_binary else 'w', bufsize)
    stdout = chan.makefile('rb' if stdin_binary else 'r', bufsize)
    stderr = chan.makefile_stderr('rb' if stdin_binary else 'r', bufsize)
    return stdin, stdout, stderr

paramiko.SSHClient.exec_command = _patched_exec_command

