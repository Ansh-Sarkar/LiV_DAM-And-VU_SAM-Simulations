M, K = 1000000, 1000

# HAR - Horizontal Angular Resolution
# VAR - Vertical Angular Resolution
LIDAR_CONFIG = {
    "hdl-32e": {
        "fov-hxv": {
            "H": 360,
            "V": 41.3
        },
        "HAR": {
            "5Hz": 0.08,
            "10Hz": 0.17,
            "20Hz": 0.35
        },
        "VAR": 1.33,
        "maxRange": {
            "unit": "m",
            "value": 100
        },
        "accuracy": {
            "unit": "cm",
            "value": 2
        },
        "scanRate": {
            "unit": "pps",
            "single": 695 * K,
            "double": 1.39 * M
        },
        "dataInterface": ["ETH"],
        "power": {
            "unit": "W",
            "value": 12
        },
        "voltage": {
            "unit": "V",
            "LB": 9,
            "UB": 18
        },
        "mass": 1000,
        "size": {
            "unit": "mm",
            "l": 85,
            "b": 85,
            "h": 144
        }
    },
    "puck-lite": {
        "fov-hxv": {
            "H": 360,
            "V": 30
        },
        "HAR": {
            "5Hz": 0.1,
            "10Hz": 0.2,
            "20Hz": 0.4
        },
        "VAR": 2,
        "maxRange": {
            "unit": "m",
            "value": 100
        },
        "accuracy": {
            "unit": "cm",
            "value": 3
        },
        "scanRate": {
            "unit": "pps",
            "single": 300 * K,
            "double": 600 * K
        },
        "dataInterface": ["ETH"],
        "power": {
            "unit": "W",
            "value": 8
        },
        "voltage": {
            "unit": "V",
            "LB": 9,
            "UB": 18
        },
        "mass": 590,
        "size": {
            "unit": "mm",
            "l": 103,
            "b": 103,
            "h": 72
        }
    },
    "puck": {
        "fov-hxv": {
            "H": 360,
            "V": 30
        },
        "HAR": {
            "5Hz": 0.1,
            "10Hz": 0.2,
            "20Hz": 0.4
        },
        "VAR": 2,
        "maxRange": {
            "unit": "m",
            "value": 100
        },
        "accuracy": {
            "unit": "cm",
            "value": 3
        },
        "scanRate": {
            "unit": "pps",
            "single": 300 * K,
            "double": 600 * K
        },
        "dataInterface": ["ETH"],
        "power": {
            "unit": "W",
            "value": 8
        },
        "voltage": {
            "unit": "V",
            "LB": 9,
            "UB": 18
        },
        "mass": 830,
        "size": {
            "unit": "mm",
            "l": 103,
            "b": 103,
            "h": 72
        }
    },
    "puck-hi-res": {
        "fov-hxv": {
            "H": 360,
            "V": 20
        },
        "HAR": {
            "5Hz": 0.1,
            "10Hz": 0.2,
            "20Hz": 0.4
        },
        "VAR": 1.33,
        "maxRange": {
            "unit": "m",
            "value": 100
        },
        "accuracy": {
            "unit": "cm",
            "value": 3
        },
        "scanRate": {
            "unit": "pps",
            "single": 300 * K,
            "double": 600 * K
        },
        "dataInterface": ["ETH"],
        "power": {
            "unit": "W",
            "value": 8
        },
        "voltage": {
            "unit": "V",
            "LB": 9,
            "UB": 18
        },
        "mass": 830,
        "size": {
            "unit": "mm",
            "l": 103,
            "b": 103,
            "h": 72
        }
    },
    "ultra-puck": {
        "fov-hxv": {
            "H": 360,
            "V": 40
        },
        "HAR": {
            "5Hz": 0.1,
            "10Hz": 0.2,
            "20Hz": 0.4
        },
        "VAR": 0.33,
        "maxRange": {
            "unit": "m",
            "value": 200
        },
        "accuracy": {
            "unit": "cm",
            "value": 3
        },
        "scanRate": {
            "unit": "pps",
            "single": 600 * K,
            "double": 1.2 * M
        },
        "dataInterface": ["ETH"],
        "power": {
            "unit": "W",
            "value": 10
        },
        "voltage": {
            "unit": "V",
            "LB": 10.5,
            "UB": 18
        },
        "mass": 925,
        "size": {
            "unit": "mm",
            "l": 103,
            "b": 103,
            "h": 87
        }
    },
    "alpha-prime": {
        "fov-hxv": {
            "H": 360,
            "V": 40
        },
        "HAR": {
            "5Hz": 0.1,
            "10Hz": 0.2,
            "20Hz": 0.4
        },
        "VAR": 0.11,
        "maxRange": {
            "unit": "m",
            "value": 245
        },
        "accuracy": {
            "unit": "cm",
            "value": 3
        },
        "scanRate": {
            "unit": "pps",
            "single": 2.4 * M,
            "double": 4.8 * M
        },
        "dataInterface": ["ETH"],
        "power": {
            "unit": "W",
            "value": 22
        },
        "voltage": {
            "unit": "V",
            "LB": 9,
            "UB": 28
        },
        "mass": 3500,
        "size": {
            "unit": "mm",
            "l": 160,
            "b": 155,
            "h": 185
        }
    }
}
