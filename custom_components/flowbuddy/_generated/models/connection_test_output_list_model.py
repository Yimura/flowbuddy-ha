from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.connection_test_output_model import ConnectionTestOutputModel


T = TypeVar("T", bound="ConnectionTestOutputListModel")


@_attrs_define
class ConnectionTestOutputListModel:
    """
    Attributes:
        connection_tests (list[ConnectionTestOutputModel] | Unset):
    """

    connection_tests: list[ConnectionTestOutputModel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_test_output_model import ConnectionTestOutputModel

        connection_tests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connection_tests, Unset):
            connection_tests = []
            for connection_tests_item_data in self.connection_tests:
                connection_tests_item = connection_tests_item_data.to_dict()
                connection_tests.append(connection_tests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_tests is not UNSET:
            field_dict["connectionTests"] = connection_tests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_test_output_model import ConnectionTestOutputModel

        d = dict(src_dict)
        _connection_tests = d.pop("connectionTests", UNSET)
        connection_tests: list[ConnectionTestOutputModel] | Unset = UNSET
        if _connection_tests is not UNSET:
            connection_tests = []
            for connection_tests_item_data in _connection_tests:
                connection_tests_item = ConnectionTestOutputModel.from_dict(
                    connection_tests_item_data
                )

                connection_tests.append(connection_tests_item)

        connection_test_output_list_model = cls(
            connection_tests=connection_tests,
        )

        connection_test_output_list_model.additional_properties = d
        return connection_test_output_list_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
