# Agent-Based Building Evacuation Simulation

This project simulates an agent‑based evacuation scenario where agents (people) attempt to escape a building on fire. The simulation models walls, bottlenecks, safe zones, and fire spread on a 2D grid.

## Features
- Agent‑based movement with configurable strategies
- Fire spread dynamics with exponential growth
- Bottleneck handling (queues) for limited passage
- Optional graphical visualization with real‑time simulation time display
- Command‑line interface for flexible experiment configuration

## Installation
```bash
# Create a virtual environment (optional but recommended)
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On Unix/macOS
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Quick Start (NSD‑EXPO)
1. Double‑click `run_demo.bat` to launch a demo with 20 agents and default visualization settings.
2. The simulation will run and display a plot with the current simulation time in the title.

## Command‑Line Usage
```bash
python evacuate.py -i in/twoexitbottleneck.txt -n 30 -g   # run with graphics
python evacuate.py -n 50 -f   # run without fire spread
```

### Arguments
| Argument | Description |
|---|---|
| `-i`, `--input` | Floor‑plan file (default: `in/twoexitbottleneck.txt`) |
| `-n`, `--numpeople` | Number of agents (default: 10) |
| `-r`, `--random_state` | Random seed (default: 8675309) |
| `-t`, `--max_time` | Simulation stop time (optional) |
| `-f`, `--no_spread_fire` | Disable fire spreading |
| `-g`, `--no_graphical_output` | Disable graphics |
| `-v`, `--verbose` | Show detailed logs |
| `-b`, `--bottleneck_delay` | Delay between agents leaving a bottleneck |
| `-a`, `--animation_delay` | Delay per animation frame (seconds) |
| `-d`, `--fire_rate` | Exponent controlling fire spread speed |

## Updated Visualization
The GUI now displays the current simulation time in the plot title, e.g., `Fire Evacuation Simulation (Time: 12.34s)`. This helps track progress during long runs.

**New behavior:** after a run completes the final simulation frame remains on screen and the program will block until you close the figure window. This lets you inspect the last state rather than having the window disappear automatically.

## Known Issues & Fixes
- **TypeError** caused by using a NumPy array as a dictionary key has been fixed by storing agent locations as immutable tuples.
- Improved logging and clearer output for debugging.

## Contributing
Feel free to open issues or submit pull requests. Ensure code follows the existing style and updates the README accordingly.

## License
This project is licensed under the MIT License.

---

**Authors**
-ANIMESH MISHRA

