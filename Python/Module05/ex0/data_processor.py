from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:


class NumericProcessor(DataProcessor):

class TextProcessor(DataProcessor):

class LogProcessor(DataProcessor):