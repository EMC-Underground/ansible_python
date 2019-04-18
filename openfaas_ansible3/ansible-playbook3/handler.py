import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)

import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.playbook_executor import PlaybookExecutor

def handle(req):
    playbook_path = "./playbook.yml"
    inventory_path = "./hosts"

    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff', 'listhosts', 'listtasks', 'listtags', 'extra_vars', 'syntax'])
    loader = DataLoader()
    options = Options(connection='local', module_path='%s/' % (ROOT_DIR), forks=100, become=None, become_method=None, become_user=None, check=False,
                    diff=False, listhosts=False, listtasks=False, listtags=False, syntax=False, extra_vars='passed=admin' 'passed2=mdmname')
    passwords = dict(vault_pass='secret')

    inventory = InventoryManager(loader=loader, sources=[inventory_path])
    variable_manager = VariableManager(loader=loader, inventory=inventory,)
    variable_manager.extra_vars = {'passed': 'craig', 'passed2': 'aaron'}
    executor = PlaybookExecutor(
                playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader,
                options=options, passwords=passwords)
    results = executor.run()
    print (results)
    return req
#def main():
#    handle()


#sys.exit(main())

