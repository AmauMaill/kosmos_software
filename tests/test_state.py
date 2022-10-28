from src.state import StateController


class TestStateController:
    """
    Tests for the StateController class.
    """

    state_controller = StateController()

    def test_start(self):
        want = "Prepare KOSMOS..."
        got = self.state_controller.start()
        assert got == want

    def test_prepare(self):
        want = "Prepare workers..."
        got = self.state_controller.prepare()
        assert got == want

    def test_work(self):
        want = "Launch workers..."
        got = self.state_controller.work()
        assert got == want

    def test_stop(self):
        want = "Stop workers..."
        got = self.state_controller.stop()
        assert got == want

    def test_shutdown(self):
        want = "Stop KOSMOS..."
        got = self.state_controller.shutdown()
        assert got == want
