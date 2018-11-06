"""
Platform-specific APIs.

Public APIs are documented in platform.base.
"""

from ..platformflags import IsWin32, IsLinux, IsFreeBsd, IsDarwin

from .base import listxattr, getxattr, setxattr, ENOATTR
from .base import acl_get, acl_set
from .base import set_flags, get_flags
from .base import SaveFile, SyncFile, sync_dir, fdatasync, safe_fadvise
from .base import swidth, API_VERSION
from .base import process_alive, get_process_id, local_pid_alive, fqdn, hostname, hostid

OS_API_VERSION = API_VERSION

if not IsWin32:
    from .posix import process_alive, local_pid_alive
    # posix swidth implementation works for: linux, freebsd, darwin, openindiana, cygwin
    from .posix import swidth
    from .posix import get_errno
    from .posix import uid2user, user2uid, gid2group, group2gid, getosusername

if IsLinux:  # pragma: linux only
    from .linux import API_VERSION as OS_API_VERSION
    from .linux import listxattr, getxattr, setxattr
    from .linux import acl_get, acl_set
    from .linux import set_flags, get_flags
    from .linux import SyncFile
elif IsFreeBsd:  # pragma: freebsd only
    from .freebsd import API_VERSION as OS_API_VERSION
    from .freebsd import listxattr, getxattr, setxattr
    from .freebsd import acl_get, acl_set
elif IsDarwin:  # pragma: darwin only
    from .darwin import API_VERSION as OS_API_VERSION
    from .darwin import listxattr, getxattr, setxattr
    from .darwin import acl_get, acl_set
