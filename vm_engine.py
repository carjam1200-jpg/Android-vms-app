"""
Android VMs App - Mini VM engine prototype

A QEMU-inspired VM configuration layer.
This generates a QEMU command that can boot an ISO image.
"""

from dataclasses import dataclass


@dataclass
class VirtualMachine:
    name: str
    cpu: str = "x86_64"
    memory_mb: int = 2048
    disk_image: str = "android.img"
    iso: str = "android.iso"
    machine: str = "q35"

    def qemu_command(self):
        """Generate a QEMU boot command for this VM."""
        return (
            f"qemu-system-{self.cpu} "
            f"-machine {self.machine} "
            f"-m {self.memory_mb} "
            f"-cdrom {self.iso} "
            f"-drive file={self.disk_image},format=qcow2 "
            "-boot d "
            "-enable-kvm"
        )

    def start(self):
        print(f"Starting VM: {self.name}")
        print(self.qemu_command())


if __name__ == "__main__":
    vm = VirtualMachine("Android Test VM", iso="android-x86.iso")
    vm.start()
