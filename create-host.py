from __future__ import print_function
from dopy.manager import DoManager
import os

API_VERSION = 2
SIZE = '512mb'
REGION = 'nyc2'
PURPOSE = 'wordpress'
VERSION = '1'
IMAGE = 'ubuntu-14-04-x64'
USER_DATA = '''#cloud-config
users:
    - name: ansible
      ssh-authorized-keys:
        - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDOd/iTQUd6Hb/KTpDjjPJotOWHfTH71U5L7x9Y4y9bo7Zvtp/m1WZyR55Ut6uBfGHscD5WRNv6VFsRIHRRjiHP+pGkB4piSUNuOduEOL/FCzmytQLmg7mYZZRGHLYXIoFJV/kdXmjexXSySxJSSp5X5EcH/pLWcKhRK9HiX4IGOBZfNwxaL/VODxU989jNXuKPnF6XfuNVf9p7JYkc4zaDy4752pPCWU2oTfq6y5Ll0vqoSpb62gCUf94CYU5eQddIeZEutTi2UiuqbsA7sEvsZpp/iXXvkaCAWMNRY6VMy5AUavDpNk4tZ/ITcieCWYdfDPCBDcfXwgANlVorHGaR gdunn@san
      sudo: ['ALL=(ALL) NOPASSWD:ALL']
      groups: sudo
      shell: /bin/bash
runcmd:
  - sed -i -e '/^PermitRootLogin/s/^.*$/PermitRootLogin no/' /etc/ssh/sshd_config
  - sed -i -e '$aAllowUsers ansible' /etc/ssh/sshd_config
  - restart ssh
'''


do = DoManager(None, os.environ['DO_API_TOKEN'], API_VERSION)

results = do.new_droplet('{0}-{1}-{2}'.format(REGION, PURPOSE, VERSION), SIZE, IMAGE, REGION, user_data=USER_DATA)

for i in results.keys():
    print('{0}: {1}'.format(i, results[i]))
