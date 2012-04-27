c = BuildmasterConfig = {}
c['slavePortnum'] = 9012

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8012, allowForce=True)
]

c['buildbotURL'] = 'http://dev-master01.build.scl1.mozilla.com:8012/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole("tcp:1237:interface=127.0.0.1", "cltbld", "password")

from config import BRANCHES, SLAVES, PROJECTS
ACTIVE_BRANCHES = BRANCHES.keys()
ACTIVE_PROJECTS = PROJECTS.keys()
ACTIVE_RELEASE_BRANCHES = ['mozilla-beta', 'mozilla-release']
ACTIVE_MOBILE_RELEASE_BRANCHES = ['mozilla-beta', 'mozilla-release']

# Set up our fast slaves
# No need to reload, this is reloaded by builder_master.cfg
import buildbotcustom.misc
buildbotcustom.misc.fastRegexes.extend([
    'linux-ix-',
    'linux64-ix-',
    ])
ENABLE_RELEASES = True
RESERVED_SLAVES = "reserved_slaves_sm03"

QUEUEDIR = "/dev/shm/queue"
