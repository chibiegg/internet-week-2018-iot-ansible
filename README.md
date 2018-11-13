

## Raspberry Pi

```bash
ansible-playbook -i hosts -s raspi.yml
```


## MEMO

### qemu

```
qemu-system-arm -kernel raspbian_bootpart/kernel-qemu-4.14.50-stretch \
-dtb raspbian_bootpart/versatile-pb.dtb -m 256 -M versatilepb -cpu arm1176 \
-serial stdio \
-append "rw console=ttyAMA0 root=PARTUUID=2ee8b6fe-02 rootfstype=ext4 loglevel=8 rootwait fsck.repair=yes memtest=1" \
-drive file=2018-10-09-raspbian-stretch.img,format=raw \
-redir tcp:5022::22 -no-reboot -vnc :1
```
