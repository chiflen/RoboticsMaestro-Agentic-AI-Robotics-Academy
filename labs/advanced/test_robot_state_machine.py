import pytest
from robot_state_machine import State, transition

def test_valid_start_sequence():
    assert transition(State.DISABLED, State.READY) == State.READY
    assert transition(State.READY, State.RUNNING) == State.RUNNING

def test_running_can_pause():
    assert transition(State.RUNNING, State.PAUSED) == State.PAUSED

def test_estop_is_terminal_in_demo():
    with pytest.raises(ValueError):
        transition(State.ESTOP, State.READY)

def test_invalid_transition_rejected():
    with pytest.raises(ValueError):
        transition(State.DISABLED, State.RUNNING)
