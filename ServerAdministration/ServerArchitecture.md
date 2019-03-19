# Server architecture

In the following the server archiceture for the giraf project will be explained.

## Old servers

| Name | IP | Specs |
| :--- | :- | :---- |
| Master00 |192.38.56.37 | 2 GB RAM 2xCPU Disk: 22 GB OS: CentOS Linux release 7.5.1804 (Core) |
| Node01 | 172.19.0.244 | 2 GB RAM 1xCPU Disk: 22 GB OS: CentOS Linux release 7.5.1804 (Core) |
| Node02 | 172.19.0.245 | 2 GB RAM 1xCPU Disk: 22 GB OS: CentOS Linux release 7.5.1804 (Core) |
| Node03 | 192.38.56.36 | 2 GB RAM 1xCPU Disk 22 GB OS: CentOS Linux release 7.5.1804 (Core) |
| GitLab | 192.38.56.136 | 4 GB RAM 2xCPU Disk: 46 GB OS: CentOS Linux release 7.5.1804 (Core) |
| web01 | 192.38.56.38 | 2 GB RAM 1xCPU Disk: 22 GB OS: CentOS Linux release 7.4.1708 (Core)|
| Backup01 | 172.19.0.235 | 4 GB RAM 2xCPU Disk: 10 GB OS: CentOS Linux release 7.2.1511 (Core)|
Only user on theise servers are root and each serve has everything open to the internet and is hence under heavy attack from malicious users trying to bruteforce the passwords.


## New servers

| Name | Internal IP | External IP| Specs |
|:---- | :---------- | :--------- | :-----|
| giraf-master00.srv.aau.dk | 172.19.10.29 | 192.38.56.151 | Ram: 4 GB 2xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2 |
| giraf-master01.srv.aau.dk | 172.19.10.30 | 192.38.56.153 | Ram: 4 GB 2xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2 |
| giraf-node00.srv.aau.dk | 172.19.10.31 | N/A | Ram: 2 GB 1xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2 |
| giraf-node01.srv.aau.dk | 172.19.10.32 | N/A | Ram: 2 GB 1xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2 |
| giraf-node02.srv.aau.dk | 172.19.10.33 | N/A | Ram: 2 GB 1xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2 |
| giraf-node03.srv.aau.dk | 172.19.10.34 | N/A | Ram: 2 GB 1xCPU Disk: 24 GB OS: Ubuntu Server 18.04.2 |

The two public IP's for the project only has port 80 and port 443 open.
Each node has been configured to use the ```10.14.0.0/16``` subnet for the local docker daemon. For the swarm overlay network the ```10.10.0.0/16``` subnet is used.

On the servers the following users has been added as administrators:
bwenne16@student.aau.dk
tlha16@student.aau.dk
tivers16@student.aau.dk
lransh16@student.aau.dk
mkaaga14@student.aau.dk
jsande16@student.aau.dk
jtrand16@student.aau.dk

### To access the servers

To access the servers from any network including most AAU network the AAU ssh gateway must be used as follows:

```bash
ssh -t sshgw.aau.dk -l <USERNAME>@student.aau.dk  ssh 172.19.10.<ip>
```
