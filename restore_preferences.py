import os
from config import get_backup_dir
from utils import execute_shell

def restore():
    backup_dir = get_backup_dir()
    domains = get_domains()
    for domain in domains:
        filename = domain + ".plist"
        print "Importing: " + domain
        execute_shell(["defaults", "import", domain,
                       os.path.join(backup_dir, filename)])


def get_domains():
    domains = []
    backup_dir = get_backup_dir()
    for filename in sorted(os.listdir(backup_dir)):
        if ".plist" in filename:
            domains.append(filename.replace(".plist", ""))
    return domains


if __name__ == '__main__':
    restore()
