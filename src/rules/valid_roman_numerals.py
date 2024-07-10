import json
import logging

from src.rules.rule import Rule


def _load_numeral_map(map_file_path: str) -> dict:
    try:
        with open(map_file_path) as f:
            return json.loads(f.read())
    except Exception as e:
        raise Exception("Cannot load roman numeral map! {}".format(map_file_path))


class RuleValidRomanNumerals(Rule):

    def __init__(self, map_file_path: str):
        super()
        self.description = "Should only contain valid Roman Numerals."
        self.numeral_map: dict = _load_numeral_map(map_file_path)
        self.log = logging.getLogger(__name__)

    def is_valid(self, input_str: str):
        validation_result = True
        for i in input_str:
            if i not in self.numeral_map.keys():
                self.log.error("{} is not a valid roman numeral!".format(i))
                validation_result = False

        return validation_result
