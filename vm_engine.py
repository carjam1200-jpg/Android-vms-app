"""
Android VMs App - Mini VM engine prototype

A QEMU-inspired VM configuration layer.
Supports ISO booting, motherboard profiles, and Linux GRUB-style boot configs.
"""

from dataclasses import dataclass


MOTHERBOARDS = {
    "q35": "QEMU Q35 chipset",
    "i440fx": "QEMU i440FX chipset",
    "virt": "Generic virtual machine board",
}


GRUB_CONFIGS = {
    "linux": "set root=(hd0,1)\nlinux /vmlinuz root=/dev/sda1 quiet\ninitrd /initrd.img\nboot",
    "android-x86": "set root=(hd0,1)\nlinux /kernel root=/dev/ram0 androidboot.hardware=android_x86\ninitrd /initrd.img\nboot",
}


@dataclass
class VirtualMachine:
    name: str
    cpu: str = "x86_64"
    memory_mb: int = 2048
    disk_image: str = "android.img"
    iso: str = "android.iso"
    motherboard: str = "q35"
    grub_profile: str = "android-x86"

    def grub_config(self):
        return GRUB_CONFIGS.get(self.grub_profile, GRUB_CONFIGS["linux"])

    def qemu_command(self):
        """Generate a QEMU command that boots from an ISO."""
        return (
            f"qemu-system-{self.cpu} "
            f"-machine {self.motherboard} "
            f"-m {self.memory_mb} "
            f"-cdrom {self.iso} "
            f"-drive file={self.disk_image},format=qcow2 "
            "-boot d "
            "-enable-kvm"
        )

    def start(self):
        print(f"Starting VM: {self.name}")
        print(f"Motherboard: {MOTHERBOARDS.get(self.motherboard)}")
        print(self.qemu_command())
        print("GRUB config:")
        print(self.grub_config())


if __name__ == "__main__":
    vm = VirtualMachine("Android Test VM", iso="android-x86.iso")
    vm.start()
