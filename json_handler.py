#!/usr/bin/python
# This class handles the storage of the generated markov chains as JSON files.

import json

class JSONHandler:

    @staticmethod
    def markov_to_json(markov_chain, filename):
        with open(filename, 'w') as f:
            return json.dump(f, {
                'version': 1,
                'type': 'markov_chain',
                'name': filename,
                'data': markov_chain
            })

    @staticmethod
    def json_to_markov(filename):
        with open(filename) as f:
            return json.load(f)

if __name__ == '__main__':
    from parser2 import Parser2
    print(Parser2('midi/river_flows.mid').get_chain())
