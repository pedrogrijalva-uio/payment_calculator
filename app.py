import json
import os

ROOT_DIR = os.path.dirname(__file__)

if __name__ == "__main__":
    payments_rules_file = ROOT_DIR+"/src/rules/payments_rules.json"

    with open(payments_rules_file, 'r') as json_file:
        payments_rules = json.loads(json_file.read())

