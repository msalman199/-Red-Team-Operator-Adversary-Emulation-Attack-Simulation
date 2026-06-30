# lab_config.py
class LabConfig:
    '''Configuration for authentication coercion lab'''
    
    def __init__(self):
        self.attacker_ip = "127.0.0.1"
        self.target_ip = "127.0.0.2"
        self.domain = "TESTDOMAIN"
        self.interface = "lo"
    
    def display_config(self):
        '''Display current configuration'''
        # TODO: Print configuration details
        pass

if __name__ == "__main__":
    config = LabConfig()
    config.display_config()
