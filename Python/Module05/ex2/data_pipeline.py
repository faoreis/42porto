from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class ExportCsv:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        stringcsv = ""
        print("CSV Output:")
        for item in data:
            if stringcsv == "":
                stringcsv = stringcsv + item[1]
            else:
                stringcsv = stringcsv + "," + item[1]
        print(stringcsv)


class ExportJson:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        stringjson = "{"
        print("JSON Output:")
        for item in data:
            item_x = '"item_' + str(item[0]) + '": "'
            if stringjson == "{":
                stringjson = stringjson + item_x + item[1] + '"'
            else:
                stringjson = stringjson + ", " + item_x + item[1] + '"'
        stringjson = stringjson + "}"
        print(stringjson)


class DataStream():
    def __init__(self):
        self.processor = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processor.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        if not (stream and self.processor):
            print("No processor found, no data")
        for item in stream:
            found = False
            for proc in self.processor:
                if proc.validate(item):
                    proc.ingest(item)
                    found = True
                    break
            if not found:
                print(
                    "DataStream error - Can't process element in stream:", item
                )

    def print_processors_stats(self) -> None:
        if self.processor:
            for proc in self.processor:
                name = proc.__class__.__name__
                print(
                    f"{name}: total {proc.index} items processed, "
                    f"remaining {len(proc.data)} on processor"
                )
        else:
            print("No processor found, no data")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processor:
            result = []
            for i in range(nb):
                try:
                    result.append(proc.output())
                except Exception:
                    break
            plugin.process_output(result)


def ft_test_plugin() -> None:
    print("\nInitialize Data Stream...")
    print("\n== DataStream statistics ==")
    tstream = DataStream()
    tstream.print_processors_stats()
    print("\nRegistering Processors")
    tstream.register_processor(NumericProcessor())
    tstream.register_processor(TextProcessor())
    tstream.register_processor(LogProcessor())
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING', 'log_message':
             'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message':
             'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print("\nSend first batch of data on stream:", batch)
    tstream.process_stream(batch)
    print("\n== DataStream statistics ==")
    tstream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    plugincsv = ExportCsv()
    tstream.output_pipeline(3, plugincsv)
    print("\n== DataStream statistics ==")
    tstream.print_processors_stats()
    print("\nSend another batch of data:", batch)
    batch = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE', 'log_message':
             'Certificateexpires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    tstream.process_stream(batch)
    print("\n== DataStream statistics ==")
    tstream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    pluginjson = ExportJson()
    tstream.output_pipeline(5, pluginjson)
    print("\n== DataStream statistics ==")
    tstream.print_processors_stats()


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    ft_test_plugin()
