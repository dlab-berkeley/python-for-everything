# Getting the OVF (Open Virtualization Format) for Ubuntu Saucy

Gzip'd tar available here: http://cloud-images.ubuntu.com/releases/saucy/release/ubuntu-13.10-server-cloudimg-i386.tar.gz
May just need the .ovf and -disk1.img located there.

None of that works

# The ISO way:

Probably need something like this to boot the desktop image (which is probably
why the ubuntu-desktop task doesn't work :/)

  "boot_command": [
     "<esc><esc><esc><enter><wait>",
     "/casper/vmlinuz.efi noapic ",
     "preseed/url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/preseed.cfg ",
     "debian-installer=en_US auto locale=en_US kbd-chooser/method=us ",
     "hostname={{user `hostname`}} ",
     "fb=false debconf/frontend=noninteractive ",
     "keyboard-configuration/modelcode=SKIP keyboard-configuration/layout=USA ",
     "keyboard-configuration/variant=USA console-setup/ask_detect=false ",
     "initrd=/casper/initrd.lz ",
     "boot=casper automatic-ubiquity -- <enter>"
     ],

Claims you need to modify preseed.cfg as per http://www.mybinarylife.net/2011/07/ubuntu-1104-custom-ubiquity-installer.html

# Other issues

If you're not on a mac, you can just delete the guest_additions_url bit

The smbus error is no worry:
http://askubuntu.com/questions/298290/smbus-bios-error-while-booting-ubuntu-13-04-in-virtualbox
