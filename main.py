from constants import *
from inspector import inspector
from shared_mem import shared_mem
from workstation import workstation
import threading

shm = shared_mem()
ws1 = workstation(WORKSTATION1, shm).start()
ws2 = workstation(WORKSTATION2, shm).start()
ws3 = workstation(WORKSTATION3, shm).start()
i1 = inspector(INSPECTOR1, shm).start()
i2 = inspector(INSPECTOR2, shm).start()
