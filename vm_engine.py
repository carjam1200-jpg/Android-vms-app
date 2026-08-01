"""
Android VMs App - Mini VM engine prototype

This is a starting point inspired by the idea of QEMU-style VM configuration.
It does not replace QEMU; it provides a simple framework for managing VM settings.
"""

from dataclasses import dataclass


@dataclass
class VirtualMachine:
    name: str
    cpu: str = "x86_64"
    memory_mb: int = 2048
    disk_image: str = "android.img"
    iso: str = "android.iso"

    def start(self):
        print(f"Starting VM: {self.name}")
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.memory_mb} MB")
        print(f"Disk: {self.disk_image}")
        print(f"ISO: {self.iso}")


if __name__ == "__main__":
    vm = VirtualMachine("Android Test VM")
    vm.start()
