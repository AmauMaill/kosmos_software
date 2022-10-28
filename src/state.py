from dataclasses import dataclass


@dataclass
class States:
    """Taken from main.py, might not been usefull."""

    STARTING = 0
    STANDBY = 1
    WORKING = 2
    STOPPING = 3
    SHUTDOWN = 4


class StateController:
    """
    StateController will be the interface between the ILS and the
    different actions that KOSMOS will perform.

    The idea is:
        - ILS records an input
        - The input is passed to StateController
        - StateController switch on and off required states
    """

    def __str__(self) -> str:
        return "StateController"

    def start(self):
        """
        KOSMOS is starting. Perform following actions:
            - Arm engine
            - Feedback state
        """
        return "Prepare KOSMOS..."

    def prepare(self):
        """
        KOSMOS is preparing for work. Perform following actions:
            - Prepare CSV
            - Prepare video recording
            - Feedback state
        """
        return "Prepare workers..."

    def work(self):
        """
        KOSMOS is working.
        """
        return "Launch workers..."

    def stop(self):
        """
        KOSMOS is ending work.
        """
        return "Stop workers..."

    def shutdown(self):
        """
        KOSMOS is shutting down.
        """
        return "Stop KOSMOS..."
