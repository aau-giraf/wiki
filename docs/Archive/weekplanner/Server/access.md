# Access

In the following we will describe how to take ownership of the Giraf Servers for
the Giraf Project. We will also describe how to access the servers once ownership
has been transferred and how to pass on the servers to a new semester of Giraf Developers.

## Ownership Transfer

Once a new semester needs to take ownership of the servers for the Giraf project
an email with the new admins student mails must be send to [support@its.aau.dk](mailto:support@its.aau.dk)
with the Semester Coordinator Ulrik Nyman ([ulrik@cs.aau.dk](mailto:ulrik@cs.aau.dk))
as CC. Once Ulrik has verified the new admins they will be added to the Giraf Server
Admins Active Directory group at ITS.

## System

Once added to the group each admin can access the servers via SSH with the following
command:

```bash
ssh -t sshgw.aau.dk -l <USERNAME>@student.aau.dk  ssh 172.19.10.<IP>
```

The servers are on the following IP's:

|Name                       |Internal IP    |External IP   |
|---                        |---            |---           |
|giraf-master00.srv.aau.dk  |172.19.10.29   |192.38.56.151 |
|giraf-master01.srv.aau.dk  |172.19.10.30   |192.38.56.153 |
|giraf-node00.srv.aau.dk    |172.19.10.31   |N/A           |
|giraf-node01.srv.aau.dk    |172.19.10.32   |N/A           |
|giraf-node02.srv.aau.dk    |172.19.10.33   |N/A           |
|giraf-node03.srv.aau.dk    |172.19.10.34   |N/A           |

The entire project has two public IPs and with has a DNS A record to srv.giraf.cs.aau.dk.

## Power Management

If the servers does not power on after a system reboot the power management can
be accessed via the vSphere Client on [https://esx-vcsa03.srv.aau.dk/ui/](https://esx-vcsa03.srv.aau.dk/ui/).

To see the servers goto Menu -> VMs and Templates

## Access Problems

The vSphere Client site is only accessible from inside the AAU network and even
is not guaranteed to be accessible by ITS. To be sure the user must connect via
VPN to AAU. On Linux Mint the package ``network-manager-openconnect-gnome`` must
be installed to allow for access to the Cisco VPN. Once installed add a new VPN
of type CiscoAnyConnect and specify ``ssl-vpn1.aau.dk`` as the gateway. When trying
to connect the network manager will ask for your username and password, once provided
an external passcode must be entered. To get this the user must sign up for MSA
passcode at [https://mfa.aau.dk/](https://mfa.aau.dk/) just use SMS if nothing else
is preferred.

## Pass on the Servers

The admins are not removed from the admin list before they leave AAU and their
student mail is deleted. Hence the admins are expected to help the new semester
doing the project start up and give an short introduction to the work that has been
done.
