from dataclasses import dataclass
from typing import List, Optional, Type, TypeVar, Generic


ObjectT = TypeVar('ObjectT')


@dataclass
class TimeStampedSequence(Generic[ObjectT]):
    object_type: Type[ObjectT]
    object_list: List[Optional[ObjectT]]
    time_list: List[float]
    topic_name: Optional[str] = None

    @classmethod
    def create_empty(cls, object_type: Type[ObjectT], topic_name=None):
        return cls(object_type, [], [], topic_name)

    def append(self, obj: Optional[ObjectT], time: float):
        self.object_list.append(obj)
        self.time_list.append(time)

    def __len__(self):
        return len(self.object_list)

    def __post_init__(self):
        assert len(self.object_list) == len(self.time_list)

    def is_valid(self):
        return not (None in self.object_list)