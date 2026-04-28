from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self.data = []
        self.index = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise Exception("No data available to output")
        result = self.data.pop(0)
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(d, (int, float)) for d in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, (int, float)):
            self.data.append((self.index, str(data)))
            self.index += 1
        else:
            for d in data:
                self.data.append((self.index, str(d)))
                self.index += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(d, str) for d in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, str):
            self.data.append((self.index, (data)))
            self.index += 1
        else:
            for d in data:
                self.data.append((self.index, d))
                self.index += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if (
            isinstance(data, dict)
            and all(
                    isinstance(k, str)
                    and isinstance(v, str) for k, v in data.items()
                )
        ):
            return True
        elif isinstance(data, list):
            for item in data:
                if not (
                    isinstance(item, dict)
                    and all(
                        isinstance(k, str)
                        and isinstance(v, str) for k, v in item.items()
                    )
                ):
                    return False
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, dict):
            self.data.append(
                (self.index, f'{data["log_level"]} : {data["log_message"]}')
            )
            self.index += 1
        else:
            for d in data:
                self.data.append(
                    (self.index, f'{d["log_level"]} : {d["log_message"]}')
                )
                self.index += 1


def ft_test_numeric() -> None:
    print("\nTesting Numeric Processor...")
    ndata = NumericProcessor()
    print("Trying to validate input '42':", ndata.validate(42))
    print("Trying to validate input 'Hello':", ndata.validate("Hello"))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        ndata.ingest("foo")
    except Exception as error:
        print(f"Got exception: {error}")
    try:
        nulist = [1, 2, 3, 4, 5]
        print("Processing data:", nulist)
        ndata.ingest(nulist)
        print("Extracting 3 values...")
        for i in range(3):
            output = ndata.output()
            print(f"Numeric value {output[0]}: {output[1]}")
    except Exception as error:
        print(f"Got exception: {error}")


def ft_test_text() -> None:
    print("\nTesting Text Processor...")
    ndata = TextProcessor()
    print("Trying to validate input '42':", ndata.validate(42))
    print("Trying to validate input 'Hello':", ndata.validate("Hello"))
    print("Test invalid ingestion of string '42' without prior validation:")
    try:
        ndata.ingest(42)
    except Exception as error:
        print(f"Got exception: {error}")
    try:
        nulist = ['Hello', 'Nexus', 'World']
        print("Processing data:", nulist)
        ndata.ingest(nulist)
        print("Extracting 1 value...")
        for i in range(1):
            output = ndata.output()
            print(f"Text value {output[0]}: {output[1]}")
    except Exception as error:
        print(f"Got exception: {error}")


def ft_test_log() -> None:
    print("\nTesting Log Processor...")
    ndata = LogProcessor()
    print("Trying to validate input '42':", ndata.validate(42))
    print("Trying to validate input 'Hello':", ndata.validate("Hello"))
    print("Test invalid ingestion of string '42' without prior validation:")
    try:
        ndata.ingest(42)
    except Exception as error:
        print(f"Got exception: {error}")
    try:
        nulist = [
            {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
        ]

        print("Processing data:", nulist)
        ndata.ingest(nulist)
        print("Extracting 2 value...")
        for i in range(2):
            output = ndata.output()
            print(f"Text value {output[0]}: {output[1]}")
    except Exception as error:
        print(f"Got exception: {error}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    ft_test_numeric()
    ft_test_text()
    ft_test_log()
