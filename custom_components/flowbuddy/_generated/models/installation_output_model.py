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
    from ..models.client_user_group_reference_model import ClientUserGroupReferenceModel
    from ..models.communicator_reference_model import CommunicatorReferenceModel
    from ..models.energy_tariff_reference_model import EnergyTariffReferenceModel
    from ..models.installation_pool_reference_model import InstallationPoolReferenceModel
    from ..models.installation_type_reference_model import InstallationTypeReferenceModel
    from ..models.location_reference_model import LocationReferenceModel


T = TypeVar("T", bound="InstallationOutputModel")


@_attrs_define
class InstallationOutputModel:
    """
    Attributes:
        resource_uri (str | Unset):
        identification (str | Unset): Unique identifier for your installation
        uuid (str | Unset): Deprecated, no longer used
        customer_name (str | Unset):
        customer_id (str | Unset):
        email_address (str | Unset):
        latitude (float | Unset):
        longitude (float | Unset):
        street (str | Unset):
        house_number (str | Unset):
        zip_code (str | Unset):
        city (str | Unset):
        country (str | Unset):
        resident (str | Unset):
        installation_date (datetime.datetime | None | Unset):
        project (str | Unset):
        dashboard_id (str | Unset):
        dashboard_type (str | Unset):
        dashboard_created_on (datetime.datetime | None | Unset):
        alarm_priority (str | Unset): The alarmpriority defines which thresholds should be used to create alarms. You
            can define different categories with different thresholds. (e.g. an installation with HIGH priority will receive
            a network alarm after 6 hours, while LOW priority will receive an alarm after 48 hours.)
        alarm_status (str | Unset):
        custom01 (str | Unset): Custom info field
        custom02 (str | Unset): Custom info field
        custom03 (str | Unset): Custom info field
        custom04 (str | Unset): Custom info field
        custom05 (str | Unset): Custom info field
        custom_list_01 (str | Unset):
        custom_list_02 (str | Unset):
        custom_url_01 (str | Unset): Custom link field
        custom_url_02 (str | Unset): Custom link field
        enable_scheduling (bool | Unset):
        external_id (str | Unset):
        location (LocationReferenceModel | Unset):
        installation_type (InstallationTypeReferenceModel | Unset):
        communicator (CommunicatorReferenceModel | Unset):
        client_user_group (ClientUserGroupReferenceModel | Unset):
        energy_tariff (EnergyTariffReferenceModel | Unset):
        installation_pool (InstallationPoolReferenceModel | Unset):
    """

    resource_uri: str | Unset = UNSET
    identification: str | Unset = UNSET
    uuid: str | Unset = UNSET
    customer_name: str | Unset = UNSET
    customer_id: str | Unset = UNSET
    email_address: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    street: str | Unset = UNSET
    house_number: str | Unset = UNSET
    zip_code: str | Unset = UNSET
    city: str | Unset = UNSET
    country: str | Unset = UNSET
    resident: str | Unset = UNSET
    installation_date: datetime.datetime | None | Unset = UNSET
    project: str | Unset = UNSET
    dashboard_id: str | Unset = UNSET
    dashboard_type: str | Unset = UNSET
    dashboard_created_on: datetime.datetime | None | Unset = UNSET
    alarm_priority: str | Unset = UNSET
    alarm_status: str | Unset = UNSET
    custom01: str | Unset = UNSET
    custom02: str | Unset = UNSET
    custom03: str | Unset = UNSET
    custom04: str | Unset = UNSET
    custom05: str | Unset = UNSET
    custom_list_01: str | Unset = UNSET
    custom_list_02: str | Unset = UNSET
    custom_url_01: str | Unset = UNSET
    custom_url_02: str | Unset = UNSET
    enable_scheduling: bool | Unset = UNSET
    external_id: str | Unset = UNSET
    location: LocationReferenceModel | Unset = UNSET
    installation_type: InstallationTypeReferenceModel | Unset = UNSET
    communicator: CommunicatorReferenceModel | Unset = UNSET
    client_user_group: ClientUserGroupReferenceModel | Unset = UNSET
    energy_tariff: EnergyTariffReferenceModel | Unset = UNSET
    installation_pool: InstallationPoolReferenceModel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.client_user_group_reference_model import ClientUserGroupReferenceModel
        from ..models.communicator_reference_model import CommunicatorReferenceModel
        from ..models.energy_tariff_reference_model import EnergyTariffReferenceModel
        from ..models.installation_pool_reference_model import InstallationPoolReferenceModel
        from ..models.installation_type_reference_model import InstallationTypeReferenceModel
        from ..models.location_reference_model import LocationReferenceModel

        resource_uri = self.resource_uri

        identification = self.identification

        uuid = self.uuid

        customer_name = self.customer_name

        customer_id = self.customer_id

        email_address = self.email_address

        latitude = self.latitude

        longitude = self.longitude

        street = self.street

        house_number = self.house_number

        zip_code = self.zip_code

        city = self.city

        country = self.country

        resident = self.resident

        installation_date: None | str | Unset
        if isinstance(self.installation_date, Unset):
            installation_date = UNSET
        elif isinstance(self.installation_date, datetime.datetime):
            installation_date = self.installation_date.isoformat()
        else:
            installation_date = self.installation_date

        project = self.project

        dashboard_id = self.dashboard_id

        dashboard_type = self.dashboard_type

        dashboard_created_on: None | str | Unset
        if isinstance(self.dashboard_created_on, Unset):
            dashboard_created_on = UNSET
        elif isinstance(self.dashboard_created_on, datetime.datetime):
            dashboard_created_on = self.dashboard_created_on.isoformat()
        else:
            dashboard_created_on = self.dashboard_created_on

        alarm_priority = self.alarm_priority

        alarm_status = self.alarm_status

        custom01 = self.custom01

        custom02 = self.custom02

        custom03 = self.custom03

        custom04 = self.custom04

        custom05 = self.custom05

        custom_list_01 = self.custom_list_01

        custom_list_02 = self.custom_list_02

        custom_url_01 = self.custom_url_01

        custom_url_02 = self.custom_url_02

        enable_scheduling = self.enable_scheduling

        external_id = self.external_id

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        installation_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.installation_type, Unset):
            installation_type = self.installation_type.to_dict()

        communicator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.communicator, Unset):
            communicator = self.communicator.to_dict()

        client_user_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_user_group, Unset):
            client_user_group = self.client_user_group.to_dict()

        energy_tariff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.energy_tariff, Unset):
            energy_tariff = self.energy_tariff.to_dict()

        installation_pool: dict[str, Any] | Unset = UNSET
        if not isinstance(self.installation_pool, Unset):
            installation_pool = self.installation_pool.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_uri is not UNSET:
            field_dict["resourceUri"] = resource_uri
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
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
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
        if dashboard_id is not UNSET:
            field_dict["dashboardId"] = dashboard_id
        if dashboard_type is not UNSET:
            field_dict["dashboardType"] = dashboard_type
        if dashboard_created_on is not UNSET:
            field_dict["dashboardCreatedOn"] = dashboard_created_on
        if alarm_priority is not UNSET:
            field_dict["alarmPriority"] = alarm_priority
        if alarm_status is not UNSET:
            field_dict["alarmStatus"] = alarm_status
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
        if enable_scheduling is not UNSET:
            field_dict["enableScheduling"] = enable_scheduling
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if location is not UNSET:
            field_dict["location"] = location
        if installation_type is not UNSET:
            field_dict["installationType"] = installation_type
        if communicator is not UNSET:
            field_dict["communicator"] = communicator
        if client_user_group is not UNSET:
            field_dict["clientUserGroup"] = client_user_group
        if energy_tariff is not UNSET:
            field_dict["energyTariff"] = energy_tariff
        if installation_pool is not UNSET:
            field_dict["installationPool"] = installation_pool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_user_group_reference_model import ClientUserGroupReferenceModel
        from ..models.communicator_reference_model import CommunicatorReferenceModel
        from ..models.energy_tariff_reference_model import EnergyTariffReferenceModel
        from ..models.installation_pool_reference_model import InstallationPoolReferenceModel
        from ..models.installation_type_reference_model import InstallationTypeReferenceModel
        from ..models.location_reference_model import LocationReferenceModel

        d = dict(src_dict)
        resource_uri = d.pop("resourceUri", UNSET)

        identification = d.pop("identification", UNSET)

        uuid = d.pop("uuid", UNSET)

        customer_name = d.pop("customerName", UNSET)

        customer_id = d.pop("customerId", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        street = d.pop("street", UNSET)

        house_number = d.pop("houseNumber", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        resident = d.pop("resident", UNSET)

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

        project = d.pop("project", UNSET)

        dashboard_id = d.pop("dashboardId", UNSET)

        dashboard_type = d.pop("dashboardType", UNSET)

        def _parse_dashboard_created_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dashboard_created_on_type_0 = datetime.datetime.fromisoformat(data)

                return dashboard_created_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dashboard_created_on = _parse_dashboard_created_on(d.pop("dashboardCreatedOn", UNSET))

        alarm_priority = d.pop("alarmPriority", UNSET)

        alarm_status = d.pop("alarmStatus", UNSET)

        custom01 = d.pop("custom01", UNSET)

        custom02 = d.pop("custom02", UNSET)

        custom03 = d.pop("custom03", UNSET)

        custom04 = d.pop("custom04", UNSET)

        custom05 = d.pop("custom05", UNSET)

        custom_list_01 = d.pop("customList01", UNSET)

        custom_list_02 = d.pop("customList02", UNSET)

        custom_url_01 = d.pop("customUrl01", UNSET)

        custom_url_02 = d.pop("customUrl02", UNSET)

        enable_scheduling = d.pop("enableScheduling", UNSET)

        external_id = d.pop("externalId", UNSET)

        _location = d.pop("location", UNSET)
        location: LocationReferenceModel | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = LocationReferenceModel.from_dict(_location)

        _installation_type = d.pop("installationType", UNSET)
        installation_type: InstallationTypeReferenceModel | Unset
        if isinstance(_installation_type, Unset):
            installation_type = UNSET
        else:
            installation_type = InstallationTypeReferenceModel.from_dict(_installation_type)

        _communicator = d.pop("communicator", UNSET)
        communicator: CommunicatorReferenceModel | Unset
        if isinstance(_communicator, Unset):
            communicator = UNSET
        else:
            communicator = CommunicatorReferenceModel.from_dict(_communicator)

        _client_user_group = d.pop("clientUserGroup", UNSET)
        client_user_group: ClientUserGroupReferenceModel | Unset
        if isinstance(_client_user_group, Unset):
            client_user_group = UNSET
        else:
            client_user_group = ClientUserGroupReferenceModel.from_dict(_client_user_group)

        _energy_tariff = d.pop("energyTariff", UNSET)
        energy_tariff: EnergyTariffReferenceModel | Unset
        if isinstance(_energy_tariff, Unset):
            energy_tariff = UNSET
        else:
            energy_tariff = EnergyTariffReferenceModel.from_dict(_energy_tariff)

        _installation_pool = d.pop("installationPool", UNSET)
        installation_pool: InstallationPoolReferenceModel | Unset
        if isinstance(_installation_pool, Unset):
            installation_pool = UNSET
        else:
            installation_pool = InstallationPoolReferenceModel.from_dict(_installation_pool)

        installation_output_model = cls(
            resource_uri=resource_uri,
            identification=identification,
            uuid=uuid,
            customer_name=customer_name,
            customer_id=customer_id,
            email_address=email_address,
            latitude=latitude,
            longitude=longitude,
            street=street,
            house_number=house_number,
            zip_code=zip_code,
            city=city,
            country=country,
            resident=resident,
            installation_date=installation_date,
            project=project,
            dashboard_id=dashboard_id,
            dashboard_type=dashboard_type,
            dashboard_created_on=dashboard_created_on,
            alarm_priority=alarm_priority,
            alarm_status=alarm_status,
            custom01=custom01,
            custom02=custom02,
            custom03=custom03,
            custom04=custom04,
            custom05=custom05,
            custom_list_01=custom_list_01,
            custom_list_02=custom_list_02,
            custom_url_01=custom_url_01,
            custom_url_02=custom_url_02,
            enable_scheduling=enable_scheduling,
            external_id=external_id,
            location=location,
            installation_type=installation_type,
            communicator=communicator,
            client_user_group=client_user_group,
            energy_tariff=energy_tariff,
            installation_pool=installation_pool,
        )

        installation_output_model.additional_properties = d
        return installation_output_model

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
