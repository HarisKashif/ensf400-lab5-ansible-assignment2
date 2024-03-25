import os
import yaml
import ansible_runner

class AnsibleManager:
    def __init__(self, config_path, inventory_file):
        self.config_path = config_path
        self.inventory_file = inventory_file
        os.environ['ANSIBLE_CONFIG'] = self.config_path

    def run_ping(self):
        return ansible_runner.run_command(executable_cmd='ansible', cmdline_args=['all:localhost', '-m', 'ping'])[0]

    def load_inventory(self):
        with open(self.inventory_file) as file:
            return yaml.load(file, Loader=yaml.FullLoader)

    def print_host_info(self, inventory):
        for group, info in inventory.items():
            print(f"\nGroup Name: {group}")
            for host, host_info in info['hosts'].items():
                print(f"\nHost Name: {host}")
                if host_info is not None:
                    if host != 'localhost':
                        print(f"    IP Address: {host_info['ansible_host']}")
                        print(f"    Connection Type: {host_info['ansible_connection']}")
                    else:
                        print(f"    Connection Type: {host_info['ansible_connection']}")
                else:
                    print("Information for this host has already been defined in another grouping.")

    def print_ping_results(self, ping_results):
        print("\n Ping Results:\n\n")
        print(ping_results)


def main():
    manager = AnsibleManager(config_path=os.path.join(os.getcwd(), 'ansible.cfg'), inventory_file='hosts.yml')
    inventory = manager.load_inventory()
    manager.print_host_info(inventory)
    ping_results = manager.run_ping()
    manager.print_ping_results(ping_results)


if __name__ == "__main__":
    main()
