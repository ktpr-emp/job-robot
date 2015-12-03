# -*- coding: utf-8 -*-
# cf. http://qiita.com/k2tanaka/items/fc1d83a5bb751cd6dd83

import os
import paramiko

class ssh_connector:

    def __init__(self, server_name):
        config_file = os.path.join(os.getenv('HOME'), '.ssh/config')
        ssh_config = paramiko.SSHConfig()
        ssh_config.parse(open(config_file, 'r'))
        lkup = ssh_config.lookup(server_name)

        
    def ssh_connect(self):
        # ProxyCommandの設定使って接続
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        # このやり方がいいのかは謎
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(
            lkup['hostname'],
            username=lkup['user'],
            key_filename=lkup['identityfile'],
            sock=paramiko.ProxyCommand(lkup['proxycommand'])
        )

        # pythonでのcommand実行はsubprocessを使うべきらしい

        # stdin, stdout, stderr = ssh.exec_command("ls -l")
        # 結果は result = stdout.read()
        #       print result

        sftp = self.ssh.open_sftp()        
        return sftp

    def ssh_disconnect(self):
        self.ssh.close()

        
