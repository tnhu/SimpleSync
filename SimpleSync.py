#
# Sublime Text SimpleSync plugin
#
# Help the orphans, street children, disadvantaged people
#   and physically handicapped in Vietnam (http://bit.ly/LPgJ1m)
#
# @copyright (c) 2012 Tan Nhu, tnhu AT me . COM
# @version 0.0.1
# @licence MIT
# @link https://github.com/tnhu/SimpleSync
#
from __future__ import print_function, unicode_literals
import sublime
import sublime_plugin
import subprocess
import threading

#
# Run a process
# @param cmd process command
#
def runProcess(cmd):
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  while (True):
    retcode = p.poll()             #returns None while subprocess is running
    line    = p.stdout.readline()
    yield line.decode('utf-8')

    if (retcode is not None):
      break

#
# Get sync item(s) for a file
# @param local_file full path of a local file
# @return sync item(s)
#
def getSyncItem(local_file):
  # Populate settings
  settings = sublime.load_settings("SimpleSync.sublime-settings")
  sync     = settings.get("sync")

  ret = []

  for item in sync:
    if local_file.startswith(item["local"]):
      ret += [item]

  return ret

#
# ScpCopier does actual copying using threading to avoid UI blocking
#
class ScpCopier(threading.Thread):
  def __init__(self, host, username, local_file, remote_file, port=22):
    self.host        = host
    self.port        = port
    self.username    = username
    self.local_file  = local_file
    self.remote_file = remote_file

    threading.Thread.__init__(self)

  def run(self):
    remote  = self.username + "@" + self.host + ":" + self.remote_file

    print("SimpleSync: ", self.local_file, " -> ", remote)

    for line in runProcess(["scp", "-r", "-P", str(self.port) , self.local_file, remote]):
      print(line, end='')

#
# LocalCopier does local copying using threading to avoid UI blocking
#
class LocalCopier(threading.Thread):
  def __init__(self, local_file, remote_file):
    self.local_file  = local_file
    self.remote_file = remote_file
    threading.Thread.__init__(self)

  def run(self):
    print("SimpleSync: ", self.local_file, " -> ", self.remote_file)

    for line in runProcess(['cp', self.local_file, self.remote_file]):
      print(line, end='')

#
# Subclass sublime_plugin.EventListener
#
class SimpleSync(sublime_plugin.EventListener):
  def on_post_save(self, view):
    local_file = view.file_name()
    syncItems  = getSyncItem(local_file)

    if (len(syncItems) > 0):
      for item in syncItems:
        remote_file = local_file.replace(item["local"], item["remote"])

        if (item["type"] == "ssh"):
          ScpCopier(item["host"], item["username"], local_file, remote_file, port=item["port"]).start()
        elif (item["type"] == "local"):
          LocalCopier(local_file, remote_file).start()
