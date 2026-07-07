from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.installation_put_input_model_other_properties import (
        InstallationPutInputModelOtherProperties,
    )


T = TypeVar("T", bound="InstallationPutInputModel")


@_attrs_define
class InstallationPutInputModel:
    """
    Attributes:
        identification (str):
        uuid (str | Unset):
        customer_name (str | Unset):
        customer_id (str | Unset):
        email_address (str | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        street (str | Unset):
        house_number (str | Unset):
        city (str | Unset):
        country (str | Unset):
        resident (str | Unset):
        installation_date (datetime.datetime | Unset):
        project (str | Unset):
        installation_type (str | Unset):
        zip_code (str | Unset):
        dashboard_id (str | Unset):
        dashboard_type (str | Unset):
        custom01 (str | Unset):
        custom02 (str | Unset):
        custom03 (str | Unset):
        custom04 (str | Unset):
        custom05 (str | Unset):
        custom_list_01 (str | Unset):
        custom_list_02 (str | Unset):
        custom_url_01 (str | Unset):
        custom_url_02 (str | Unset):
        alarm_priority (str | Unset):
        client_user_group (str | Unset):
        energy_tariff (str | Unset):
        installation_pool (str | Unset):
        other_properties (InstallationPutInputModelOtherProperties | Unset):
    """

    identification: str
    uuid: str | Unset = UNSET
    customer_name: str | Unset = UNSET
    customer_id: str | Unset = UNSET
    email_address: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    street: str | Unset = UNSET
    house_number: str | Unset = UNSET
    city: str | Unset = UNSET
    country: str | Unset = UNSET
    resident: str | Unset = UNSET
    installation_date: datetime.datetime | Unset = UNSET
    project: str | Unset = UNSET
    installation_type: str | Unset = UNSET
    zip_code: str | Unset = UNSET
    dashboard_id: str | Unset = UNSET
    dashboard_type: str | Unset = UNSET
    custom01: str | Unset = UNSET
    custom02: str | Unset = UNSET
    custom03: str | Unset = UNSET
    custom04: str | Unset = UNSET
    custom05: str | Unset = UNSET
    custom_list_01: str | Unset = UNSET
    custom_list_02: str | Unset = UNSET
    custom_url_01: str | Unset = UNSET
    custom_url_02: str | Unset = UNSET
    alarm_priority: str | Unset = UNSET
    client_user_group: str | Unset = UNSET
    energy_tariff: str | Unset = UNSET
    installation_pool: str | Unset = UNSET
    other_properties: InstallationPutInputModelOtherProperties | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_put_input_model_other_properties import (
            InstallationPutInputModelOtherProperties,
        )

        identification = self.identification

        uuid = self.uuid

        customer_name = self.customer_name

        customer_id = self.customer_id

        email_address = self.email_address

        latitude = self.latitude

        longitude = self.longitude

        street = self.street

        house_number = self.house_number

        city = self.city

        country = self.country

        resident = self.resident

        installation_date: str | Unset = UNSET
        if not isinstance(self.installation_date, Unset):
            installation_date = self.installation_date.isoformat()

        project = self.project

        installation_type = self.installation_type

        zip_code = self.zip_code

        dashboard_id = self.dashboard_id

        dashboard_type = self.dashboard_type

        custom01 = self.custom01

        custom02 = self.custom02

        custom03 = self.custom03

        custom04 = self.custom04

        custom05 = self.custom05

        custom_list_01 = self.custom_list_01

        custom_list_02 = self.custom_list_02

        custom_url_01 = self.custom_url_01

        custom_url_02 = self.custom_url_02

        alarm_priority = self.alarm_priority

        client_user_group = self.client_user_group

        energy_tariff = self.energy_tariff

        installation_pool = self.installation_pool

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identification": identification,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if street is not UNSET:
            field_dict["street"] = street
        if house_number is not UNSET:
            field_dict["houseNumber"] = house_number
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if resident is not UNSET:
            field_dict["resident"] = resident
        if installation_date is not UNSET:
            field_dict["installationDate"] = installation_date
        if project is not UNSET:
            field_dict["project"] = project
        if installation_type is not UNSET:
            field_dict["installationType"] = installation_type
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if dashboard_id is not UNSET:
            field_dict["dashboardId"] = dashboard_id
        if dashboard_type is not UNSET:
            field_dict["dashboardType"] = dashboard_type
        if custom01 is not UNSET:
            field_dict["custom01"] = custom01
        if custom02 is not UNSET:
            field_dict["custom02"] = custom02
        if custom03 is not UNSET:
            field_dict["custom03"] = custom03
        if custom04 is not UNSET:
            field_dict["custom04"] = custom04
        if custom05 is not UNSET:
            field_dict["custom05"] = custom05
        if custom_list_01 is not UNSET:
            field_dict["customList01"] = custom_list_01
        if custom_list_02 is not UNSET:
            field_dict["customList02"] = custom_list_02
        if custom_url_01 is not UNSET:
            field_dict["customUrl01"] = custom_url_01
        if custom_url_02 is not UNSET:
            field_dict["customUrl02"] = custom_url_02
        if alarm_priority is not UNSET:
            field_dict["alarmPriority"] = alarm_priority
        if client_user_group is not UNSET:
            field_dict["clientUserGroup"] = client_user_group
        if energy_tariff is not UNSET:
            field_dict["energyTariff"] = energy_tariff
        if installation_pool is not UNSET:
            field_dict["installationPool"] = installation_pool
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_put_input_model_other_properties import (
            InstallationPutInputModelOtherProperties,
        )

        d = dict(src_dict)
        identification = d.pop("identification")

        uuid = d.pop("uuid", UNSET)

        customer_name = d.pop("customerName", UNSET)

        customer_id = d.pop("customerId", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        street = d.pop("street", UNSET)

        house_number = d.pop("houseNumber", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        resident = d.pop("resident", UNSET)

        _installation_date = d.pop("installationDate", UNSET)
        installation_date: datetime.datetime | Unset
        if isinstance(_installation_date, Unset):
            installation_date = UNSET
        else:
            installation_date = datetime.datetime.fromisoformat(_installation_date)

        project = d.pop("project", UNSET)

        installation_type = d.pop("installationType", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        dashboard_id = d.pop("dashboardId", UNSET)

        dashboard_type = d.pop("dashboardType", UNSET)

        custom01 = d.pop("custom01", UNSET)

        custom02 = d.pop("custom02", UNSET)

        custom03 = d.pop("custom03", UNSET)

        custom04 = d.pop("custom04", UNSET)

        custom05 = d.pop("custom05", UNSET)

        custom_list_01 = d.pop("customList01", UNSET)

        custom_list_02 = d.pop("customList02", UNSET)

        custom_url_01 = d.pop("customUrl01", UNSET)

        custom_url_02 = d.pop("customUrl02", UNSET)

        alarm_priority = d.pop("alarmPriority", UNSET)

        client_user_group = d.pop("clientUserGroup", UNSET)

        energy_tariff = d.pop("energyTariff", UNSET)

        installation_pool = d.pop("installationPool", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: InstallationPutInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = InstallationPutInputModelOtherProperties.from_dict(_other_properties)

        installation_put_input_model = cls(
            identification=identification,
            uuid=uuid,
            customer_name=customer_name,
            customer_id=customer_id,
            email_address=email_address,
            latitude=latitude,
            longitude=longitude,
            street=street,
            house_number=house_number,
            city=city,
            country=country,
            resident=resident,
            installation_date=installation_date,
            project=project,
            installation_type=installation_type,
            zip_code=zip_code,
            dashboard_id=dashboard_id,
            dashboard_type=dashboard_type,
            custom01=custom01,
            custom02=custom02,
            custom03=custom03,
            custom04=custom04,
            custom05=custom05,
            custom_list_01=custom_list_01,
            custom_list_02=custom_list_02,
            custom_url_01=custom_url_01,
            custom_url_02=custom_url_02,
            alarm_priority=alarm_priority,
            client_user_group=client_user_group,
            energy_tariff=energy_tariff,
            installation_pool=installation_pool,
            other_properties=other_properties,
        )

        installation_put_input_model.additional_properties = d
        return installation_put_input_model

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
