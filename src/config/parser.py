import json
from typing import Dict, List, Any, Iterable


class Parser:
    """Parse and validate the Pac-Man JSON configuration file.
        The parser loads the configuration, removes comment lines, checks
        configuration keys and values, and replaces missing or invalid values
        with safe default values.
    """

    def __init__(self, file_name: str) -> None:
        """ Initialize the parser.
        Args:
            file_name: the path to the json configuration file
        """
        self.file_name: str = file_name
        self.data: Dict[str, Any] = {}
        self.default_conf: Dict[str, Any] = {

            "highscore_filename": "score.json",
            "levels": [
                {
                    "name": "level01",
                    "width": 14,
                    "height": 10,
                    "pacgum": 42,
                    "seed": 42,
                    "level_max_time": 90
                },
                {
                    "name": "level02",
                    "width": 16,
                    "height": 12,
                    "pacgum": 55,
                    "level_max_time": 90
                },
                {
                    "name": "level03",
                    "width": 18,
                    "height": 14,
                    "pacgum": 70,
                    "level_max_time": 90
                },
                {
                    "name": "level04",
                    "width": 20,
                    "height": 14,
                    "pacgum": 85,
                    "level_max_time": 85
                },
                {
                    "name": "level05",
                    "width": 20,
                    "height": 16,
                    "pacgum": 100,
                    "level_max_time": 85
                },
                {
                    "name": "level06",
                    "width": 22,
                    "height": 16,
                    "pacgum": 115,
                    "level_max_time": 80
                },
                {
                    "name": "level07",
                    "width": 22,
                    "height": 18,
                    "pacgum": 130,
                    "level_max_time": 80
                },
                {
                    "name": "level08",
                    "width": 24,
                    "height": 18,
                    "pacgum": 145,
                    "level_max_time": 75
                },
                {
                    "name": "level09",
                    "width": 24,
                    "height": 20,
                    "pacgum": 160,
                    "level_max_time": 75
                },
                {
                    "name": "level10",
                    "width": 26,
                    "height": 20,
                    "pacgum": 180,
                    "level_max_time": 70
                }
            ],
            "lives": 3,
            "points_per_pacgum": 10,
            "points_per_superpacgum": 100,
            "points_per_ghost": 200
        }

    def check_missing(self, config_keys: Iterable[str],
                      default_keys: Iterable[str]) -> List[str]:
        """ Find the keys that are present in default but missing from config
        Args:
            config_keys: keys found in the configuration
            default_keys: keys that are expected on the configuration
        Returns:
            A list contain the missing keys
        """
        config_keys = set(config_keys)
        default_keys = set(default_keys)
        return list(default_keys - config_keys)

    def check_keys(self, config_data: Dict[str, Any]) -> None:
        """Check configuration keys and apply defaults for missing keys.

        Unknown keys are ignored with a warning. Missing keys are added
        using their corresponding default values.

        Args:
            config_data: Configuration data loaded from the JSON file.
        """
        for key in config_data.keys():
            if key not in self.default_conf.keys():
                print(f"\nWarning: Unknown key '{key}', ignoring it.")
                continue
            self.data[key] = config_data[key]

        missing = (self.check_missing(config_data.keys(),
                   self.default_conf.keys()))
        for m in missing:
            print(f"\nWarning: Missing key '{m}', "
                  f"using default value")
            self.data[m] = self.default_conf[m]

    def check_values(self, config_data: Dict[str, Any]) -> None:
        """Validate the values of the main configuration keys.

        Invalid values are replaced with their corresponding default
        values. Level-specific values are validated separately.

        Args:
            config_data: Configuration data loaded from the JSON file.
        """
        for key, value in config_data.items():
            if key == 'highscore_filename':
                if not value.endswith('.json'):
                    print(f"\nWarning: {key} must be json file, "
                          f"using default value {self.default_conf[key]}")
                    self.data[key] = self.default_conf[key]

            if key in ('lives', 'points_per_pacgum',
                       'points_per_superpacgum', 'points_per_ghost'):
                if not isinstance(value, int) or value <= 0:
                    print(f"\nWarning: {key} must be a strict positive "
                          "integer, using default "
                          f"value {self.default_conf[key]}")
                    self.data[key] = self.default_conf[key]

            if key == 'levels':
                self.check_levels(value)

    def check_level_values(self, levels_data: List[Dict[str, Any]],
                           default_levels: List[Dict[str, Any]]) -> None:
        """Validate the values of each level configuration.

        Invalid level values are replaced with their corresponding
        default values.

        Args:
            levels_data: List of level configurations from the user.
            default_levels: List of default level configurations.
        """
        for i, level in enumerate(levels_data, start=0):
            for key, value in level.items():
                if key == 'name':
                    if not isinstance(value, str):
                        print("Warning: Invalid level name, "
                              f"using default value {default_levels[i][key]}")
                        self.data['levels'][i][key] = default_levels[i][key]

                elif key == 'level_max_time':
                    if not isinstance(value, int) or value <= 0:
                        print(f"Warning: {key} value must be a strict "
                              "positive integer, using default value "
                              f"{default_levels[i][key]}")
                        self.data['levels'][i][key] = default_levels[i][key]

                elif key in ('width', 'height'):
                    if (
                        (key == 'width' and
                         (not isinstance(value, int) or value < 14))
                        or (key == 'height' and
                            (not isinstance(value, int) or value < 10))
                    ):
                        print(
                            f"Warning: Invalid {key} at the level {i + 1}. "
                            f"Minimum width is 14 and minimum height is 10. "
                            f"Using default value: {default_levels[i][key]}"
                        )
                        self.data['levels'][i][key] = default_levels[i][key]

                elif key == 'seed':
                    if type(value) not in (int, float, str, bytes, bytearray):
                        print("Warning: Invalid seed",
                              f"using default value {default_levels[i][key]}")
                        self.data['levels'][i][key] = default_levels[i][key]

                elif key == 'pacgum':
                    width = self.data['levels'][i]['width']
                    height = self.data['levels'][i]['height']
                    max_pacgums = (width * height + 4 + 4 + 1)
                    if (not isinstance(value, int) or
                            value <= 0 or value > max_pacgums):
                        print(f"Warning: invalid pacgums number on level "
                              f"{i + 1}, using defaut value "
                              f"{default_levels[i][key]}")
                        self.data['levels'][i][key] = default_levels[i][key]

    def check_levels(self, levels_data: List[Dict[str, Any]]) -> None:
        """Validate the levels configuration.

        The levels value must be a list containing at least ten levels.
        Missing levels are filled using the default level configurations.
        Each level is then checked for unknown, missing, and invalid values.

        Args:
            levels_data: List of level configurations from the JSON file.
        """
        default_levels = self.default_conf['levels']
        # check if the levels are list
        if not isinstance(levels_data, list):
            print("\nWarning: the levels must be a list, "
                  f"using default value {self.default_conf['levels']}")
            self.data['levels'] = default_levels

        # check if the levels list have at least 10 levels
        elif len(levels_data) < 10:
            print("Warning: number of levels must be at lest 10, "
                  "fill the missing levels")
            i = len(levels_data)
            while i < len(default_levels):
                levels_data.append(default_levels[i])
                i += 1
            self.data['levels'] = levels_data

    # check each level key:
        else:
            l: List[Dict[str, Any]] = list()
            for i, level in enumerate(levels_data, start=0):
                val: Dict[str, Any] = {}
                for key in level:
                    if key not in default_levels[i].keys():
                        print(f"\nWarning: Unknown key '{key}' in level "
                              f"{i + 1}, ignoring it.")
                        continue
                    val[key] = level[key]
                missing = (self.check_missing(levels_data[i].keys(),
                           default_levels[i].keys()))
                for m in missing:
                    print(f"Warning: Missing key '{m}' in level {i + 1}, "
                          f"using default value")
                    val[m] = default_levels[i][m]
                l.append(val)
            self.data['levels'] = l
        # check the value of each level
        self.check_level_values(levels_data, default_levels)

    def parse(self) -> Dict[str, Any]:
        """Read, parse, and validate the JSON configuration file.

        Lines beginning with '#' are ignored before parsing the JSON.
        The resulting configuration is checked for unknown, missing,
        and invalid keys and values.
        """
        with open(self.file_name) as f:
            lines = []
            for line in f:
                if not line or line.strip().startswith('#'):
                    continue
                lines.append(line)
            config_data = json.loads("".join(lines))
            self.check_keys(config_data)
            self.check_values(config_data)
            return self.data
