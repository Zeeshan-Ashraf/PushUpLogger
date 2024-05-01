from dataclasses import dataclass, field


@dataclass
class Health:
    SAMPLE_DATA: dict = field(default_factory=dict)

    def healthCheck(self):
        self.SAMPLE_DATA = {"msg": "test"}
        return self.SAMPLE_DATA

    def helloWorld(self):
        return "Hello World"
