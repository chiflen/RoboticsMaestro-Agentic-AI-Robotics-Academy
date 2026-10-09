"""Simulation-only state machine. Not a robot safety controller."""
from enum import Enum
class State(str, Enum):
    DISABLED="DISABLED"; READY="READY"; RUNNING="RUNNING"; PAUSED="PAUSED"; ESTOP="ESTOP"
ALLOWED = {
    State.DISABLED:{State.READY,State.ESTOP},
    State.READY:{State.RUNNING,State.DISABLED,State.ESTOP},
    State.RUNNING:{State.PAUSED,State.ESTOP},
    State.PAUSED:{State.RUNNING,State.DISABLED,State.ESTOP},
    State.ESTOP:set()
}
def transition(current: State, target: State) -> State:
    if target not in ALLOWED[current]:
        raise ValueError(f"Invalid transition: {current} -> {target}")
    return target
if __name__ == "__main__":
    s=State.DISABLED
    for t in [State.READY,State.RUNNING,State.PAUSED]:
        s=transition(s,t); print(s.value)
