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
    from ..models.installation_patch_input_model_other_properties_type_0 import (
        InstallationPatchInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="InstallationPatchInputModel")


@_attrs_define
class InstallationPatchInputModel:
    """
    Attributes:
        identification (None | str | Unset):
        uuid (None | str | Unset):
        customer_name (None | str | Unset):
        customer_id (None | str | Unset):
        email_address (None | str | Unset):
        latitude (float | None | Unset):
        longitude (float | None | Unset):
        street (None | str | Unset):
        house_number (None | str | Unset):
        city (None | str | Unset):
        country (None | str | Unset):
        resident (None | str | Unset):
        installation_date (datetime.datetime | None | Unset):
        project (None | str | Unset):
        installation_type (None | str | Unset):
        zip_code (None | str | Unset):
        dashboard_id (None | str | Unset):
        dashboard_type (None | str | Unset):
        custom01 (None | str | Unset):
        custom02 (None | str | Unset):
        custom03 (None | str | Unset):
        custom04 (None | str | Unset):
        custom05 (None | str | Unset):
        custom_list_01 (None | str | Unset):
        custom_list_02 (None | str | Unset):
        custom_url_01 (None | str | Unset):
        custom_url_02 (None | str | Unset):
        alarm_priority (None | str | Unset):
        client_user_group (None | str | Unset):
        energy_tariff (None | str | Unset):
        installation_pool (None | str | Unset):
        other_properties (InstallationPatchInputModelOtherPropertiesType0 | None | Unset):
    """

    identification: None | str | Unset = UNSET
    uuid: None | str | Unset = UNSET
    customer_name: None | str | Unset = UNSET
    customer_id: None | str | Unset = UNSET
    email_address: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    street: None | str | Unset = UNSET
    house_number: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    resident: None | str | Unset = UNSET
    installation_date: datetime.datetime | None | Unset = UNSET
    project: None | str | Unset = UNSET
    installation_type: None | str | Unset = UNSET
    zip_code: None | str | Unset = UNSET
    dashboard_id: None | str | Unset = UNSET
    dashboard_type: None | str | Unset = UNSET
    custom01: None | str | Unset = UNSET
    custom02: None | str | Unset = UNSET
    custom03: None | str | Unset = UNSET
    custom04: None | str | Unset = UNSET
    custom05: None | str | Unset = UNSET
    custom_list_01: None | str | Unset = UNSET
    custom_list_02: None | str | Unset = UNSET
    custom_url_01: None | str | Unset = UNSET
    custom_url_02: None | str | Unset = UNSET
    alarm_priority: None | str | Unset = UNSET
    client_user_group: None | str | Unset = UNSET
    energy_tariff: None | str | Unset = UNSET
    installation_pool: None | str | Unset = UNSET
    other_properties: InstallationPatchInputModelOtherPropertiesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.installation_patch_input_model_other_properties_type_0 import (
            InstallationPatchInputModelOtherPropertiesType0,
        )

        identification: None | str | Unset
        if isinstance(self.identification, Unset):
            identification = UNSET
        else:
            identification = self.identification

        uuid: None | str | Unset
        if isinstance(self.uuid, Unset):
            uuid = UNSET
        else:
            uuid = self.uuid

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        customer_id: None | str | Unset
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        street: None | str | Unset
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        house_number: None | str | Unset
        if isinstance(self.house_number, Unset):
            house_number = UNSET
        else:
            house_number = self.house_number

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        resident: None | str | Unset
        if isinstance(self.resident, Unset):
            resident = UNSET
        else:
            resident = self.resident

        installation_date: None | str | Unset
        if isinstance(self.installation_date, Unset):
            installation_date = UNSET
        elif isinstance(self.installation_date, datetime.datetime):
            installation_date = self.installation_date.isoformat()
        else:
            installation_date = self.installation_date

        project: None | str | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        else:
            project = self.project

        installation_type: None | str | Unset
        if isinstance(self.installation_type, Unset):
            installation_type = UNSET
        else:
            installation_type = self.installation_type

        zip_code: None | str | Unset
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        dashboard_id: None | str | Unset
        if isinstance(self.dashboard_id, Unset):
            dashboard_id = UNSET
        else:
            dashboard_id = self.dashboard_id

        dashboard_type: None | str | Unset
        if isinstance(self.dashboard_type, Unset):
            dashboard_type = UNSET
        else:
            dashboard_type = self.dashboard_type

        custom01: None | str | Unset
        if isinstance(self.custom01, Unset):
            custom01 = UNSET
        else:
            custom01 = self.custom01

        custom02: None | str | Unset
        if isinstance(self.custom02, Unset):
            custom02 = UNSET
        else:
            custom02 = self.custom02

        custom03: None | str | Unset
        if isinstance(self.custom03, Unset):
            custom03 = UNSET
        else:
            custom03 = self.custom03

        custom04: None | str | Unset
        if isinstance(self.custom04, Unset):
            custom04 = UNSET
        else:
            custom04 = self.custom04

        custom05: None | str | Unset
        if isinstance(self.custom05, Unset):
            custom05 = UNSET
        else:
            custom05 = self.custom05

        custom_list_01: None | str | Unset
        if isinstance(self.custom_list_01, Unset):
            custom_list_01 = UNSET
        else:
            custom_list_01 = self.custom_list_01

        custom_list_02: None | str | Unset
        if isinstance(self.custom_list_02, Unset):
            custom_list_02 = UNSET
        else:
            custom_list_02 = self.custom_list_02

        custom_url_01: None | str | Unset
        if isinstance(self.custom_url_01, Unset):
            custom_url_01 = UNSET
        else:
            custom_url_01 = self.custom_url_01

        custom_url_02: None | str | Unset
        if isinstance(self.custom_url_02, Unset):
            custom_url_02 = UNSET
        else:
            custom_url_02 = self.custom_url_02

        alarm_priority: None | str | Unset
        if isinstance(self.alarm_priority, Unset):
            alarm_priority = UNSET
        else:
            alarm_priority = self.alarm_priority

        client_user_group: None | str | Unset
        if isinstance(self.client_user_group, Unset):
            client_user_group = UNSET
        else:
            client_user_group = self.client_user_group

        energy_tariff: None | str | Unset
        if isinstance(self.energy_tariff, Unset):
            energy_tariff = UNSET
        else:
            energy_tariff = self.energy_tariff

        installation_pool: None | str | Unset
        if isinstance(self.installation_pool, Unset):
            installation_pool = UNSET
        else:
            installation_pool = self.installation_pool

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(self.other_properties, InstallationPatchInputModelOtherPropertiesType0):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identification is not UNSET:
            field_dict["identification"] = identification
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
        from ..models.installation_patch_input_model_other_properties_type_0 import (
            InstallationPatchInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_identification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identification = _parse_identification(d.pop("identification", UNSET))

        def _parse_uuid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uuid = _parse_uuid(d.pop("uuid", UNSET))

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customerName", UNSET))

        def _parse_customer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_id = _parse_customer_id(d.pop("customerId", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("emailAddress", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_house_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_number = _parse_house_number(d.pop("houseNumber", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_resident(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resident = _parse_resident(d.pop("resident", UNSET))

        def _parse_installation_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                installation_date_type_0 = datetime.datetime.fromisoformat(data)

                return installation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        installation_date = _parse_installation_date(d.pop("installationDate", UNSET))

        def _parse_project(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project = _parse_project(d.pop("project", UNSET))

        def _parse_installation_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installation_type = _parse_installation_type(d.pop("installationType", UNSET))

        def _parse_zip_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zip_code = _parse_zip_code(d.pop("zipCode", UNSET))

        def _parse_dashboard_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dashboard_id = _parse_dashboard_id(d.pop("dashboardId", UNSET))

        def _parse_dashboard_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dashboard_type = _parse_dashboard_type(d.pop("dashboardType", UNSET))

        def _parse_custom01(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom01 = _parse_custom01(d.pop("custom01", UNSET))

        def _parse_custom02(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom02 = _parse_custom02(d.pop("custom02", UNSET))

        def _parse_custom03(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom03 = _parse_custom03(d.pop("custom03", UNSET))

        def _parse_custom04(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom04 = _parse_custom04(d.pop("custom04", UNSET))

        def _parse_custom05(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom05 = _parse_custom05(d.pop("custom05", UNSET))

        def _parse_custom_list_01(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_list_01 = _parse_custom_list_01(d.pop("customList01", UNSET))

        def _parse_custom_list_02(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_list_02 = _parse_custom_list_02(d.pop("customList02", UNSET))

        def _parse_custom_url_01(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_url_01 = _parse_custom_url_01(d.pop("customUrl01", UNSET))

        def _parse_custom_url_02(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_url_02 = _parse_custom_url_02(d.pop("customUrl02", UNSET))

        def _parse_alarm_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alarm_priority = _parse_alarm_priority(d.pop("alarmPriority", UNSET))

        def _parse_client_user_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_user_group = _parse_client_user_group(d.pop("clientUserGroup", UNSET))

        def _parse_energy_tariff(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        energy_tariff = _parse_energy_tariff(d.pop("energyTariff", UNSET))

        def _parse_installation_pool(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installation_pool = _parse_installation_pool(d.pop("installationPool", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> InstallationPatchInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = InstallationPatchInputModelOtherPropertiesType0.from_dict(
                    data
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InstallationPatchInputModelOtherPropertiesType0 | None | Unset, data)

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

        installation_patch_input_model = cls(
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

        installation_patch_input_model.additional_properties = d
        return installation_patch_input_model

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
