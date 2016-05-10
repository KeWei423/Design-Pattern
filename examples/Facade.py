# Complex parts
class CPU:
    def freeze(self):
        print("Process CPU")

    def jump(self, position):
        print("CPU Jump")

    def execute(self):
        print("CPU executes")

class Memory:
    def load(self, position, data):
        print('Memory: Load {} from {}'.format(position, data))

class HardDrive:
    def read(self, lba, size):
        return 'HardDrive: Read {} with size {}'.format(lba, size)

# Facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        print("start computer")
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(0, 1024))
        self.cpu.jump(10)
        self.cpu.execute()

# Client
if __name__ == '__main__':
    facade = Computer()
    facade.start_computer()