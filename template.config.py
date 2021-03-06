import os

# RoAMer related
THIS_FILE_PATH = str(os.path.abspath(__file__))
PROJECT_ROOT = str(os.path.abspath(os.sep.join([THIS_FILE_PATH, ".."])))
BIN_ROOT = str(os.path.abspath(os.sep.join([PROJECT_ROOT, "roamer", "bin"])))
UNPACKER_CONFIG = {
    "host_ip": '192.168.56.1',
    "host_port": 10000,
    "guest_ip": "1.1.1.1",
    "guest_port": 10000,
    "debug_sleep": 0,
    "socket_timeout": 480,

    "parameters": [
        {
            "name": "4x5_hook_spoofuser",
            "hook32": "TP_EM0_sleep.dll",
            "hook64": 0,
            "monitoring_intervals": 4,
            "monitoring_interval_length": 5,
            "monitoring_switches": [
                "processes"
            ],
            "dump_filters": [
                "pe_header_whitelist",
                "memmap_change",
                "only_executable_filter",
                "mapped_memory"
            ],
            "additional_pe_whitelist": {"dotNet1.dll": ["c4aa77a6556cc19a1f1e5f5dd85ef7966489d413c19ea7433d9a4e244ddb4450"],
                                        "dotNet2.dll": ["0bf521a45ff4ad7bb21220a069441a60d48874a61e30659bbb6a65f2d616d2fd"],
                                        "dotNet3.dll": ["5bb85f402bed10719d8fcf5151c7ac9e989ee6b6fed3232283a126dcb79fb633"],
                                        "dotNet4.dll": ["d3142c2dc9659e1ddd08efc42a084681ca1d8d33f51ee0a878a63ebf1d521ba2"],
                                        "dotNet5.dll": ["88d0b9411fe74c3d757495ac8f87a2542acf4bd7c1f723593f73c3c3bbe6381d"],
                                        "dotNet6.dll": ["7dac91e7e5a81dff093eb95fda1a022e2492476551e6ff33196dce1c9628cea9"],
                                        "dotNet7.dll": ["2e0a4960905e2f0d1956691ff31e7a75a4f06db0b0a989821fd52fb8d89ac5f5"],
                                        "dotNet8.dll": ["b371143568c9744f395400acaff6b73149d18906d8fce74d7a48d2f9cceb9989"]},
            "sample_start_delay": 5,
            "spoof_user": 1,
            "desktop_sample_pos_x": 40,
            "desktop_sample_pos_y": 40
        }   
    ]
}

# Virtualization related
## VM_CONTROLLER choose "VboxManageController" for VirtualBox or "KvmManageController" for KVM
VM_CONTROLLER = "VboxManageController"
VM_NAME = "vm_name"
SNAPSHOT_NAME = "snapshot_name"
