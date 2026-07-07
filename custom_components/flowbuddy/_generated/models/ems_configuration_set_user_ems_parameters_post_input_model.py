from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.ems_configuration_set_user_ems_parameters_post_input_model_other_properties import (
        EmsConfigurationSetUserEmsParametersPostInputModelOtherProperties,
    )


T = TypeVar("T", bound="EmsConfigurationSetUserEmsParametersPostInputModel")


@_attrs_define
class EmsConfigurationSetUserEmsParametersPostInputModel:
    """
    Attributes:
        user_requested_max_charge_current (float | Unset):
        user_requested_max_grid_current (float | Unset):
        user_requested_ev_battery_mode (int | Unset):
        user_requested_max_grid_power (int | Unset):
        user_requested_battery_peak_reserve_soc (int | Unset):
        user_requested_lower_price_threshold (float | Unset):
        user_requested_upper_price_threshold (float | Unset):
        user_requested_ev_mode (str | Unset):
        user_requested_deactivate_heat_pump_on_high_prices (bool | Unset):
        user_requested_activate_heat_pump_on_low_prices (bool | Unset):
        enable_curtailing (bool | Unset):
        other_properties (EmsConfigurationSetUserEmsParametersPostInputModelOtherProperties | Unset):
    """

    user_requested_max_charge_current: float | Unset = UNSET
    user_requested_max_grid_current: float | Unset = UNSET
    user_requested_ev_battery_mode: int | Unset = UNSET
    user_requested_max_grid_power: int | Unset = UNSET
    user_requested_battery_peak_reserve_soc: int | Unset = UNSET
    user_requested_lower_price_threshold: float | Unset = UNSET
    user_requested_upper_price_threshold: float | Unset = UNSET
    user_requested_ev_mode: str | Unset = UNSET
    user_requested_deactivate_heat_pump_on_high_prices: bool | Unset = UNSET
    user_requested_activate_heat_pump_on_low_prices: bool | Unset = UNSET
    enable_curtailing: bool | Unset = UNSET
    other_properties: EmsConfigurationSetUserEmsParametersPostInputModelOtherProperties | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ems_configuration_set_user_ems_parameters_post_input_model_other_properties import (
            EmsConfigurationSetUserEmsParametersPostInputModelOtherProperties,
        )

        user_requested_max_charge_current = self.user_requested_max_charge_current

        user_requested_max_grid_current = self.user_requested_max_grid_current

        user_requested_ev_battery_mode = self.user_requested_ev_battery_mode

        user_requested_max_grid_power = self.user_requested_max_grid_power

        user_requested_battery_peak_reserve_soc = self.user_requested_battery_peak_reserve_soc

        user_requested_lower_price_threshold = self.user_requested_lower_price_threshold

        user_requested_upper_price_threshold = self.user_requested_upper_price_threshold

        user_requested_ev_mode = self.user_requested_ev_mode

        user_requested_deactivate_heat_pump_on_high_prices = (
            self.user_requested_deactivate_heat_pump_on_high_prices
        )

        user_requested_activate_heat_pump_on_low_prices = (
            self.user_requested_activate_heat_pump_on_low_prices
        )

        enable_curtailing = self.enable_curtailing

        other_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_properties, Unset):
            other_properties = self.other_properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_requested_max_charge_current is not UNSET:
            field_dict["userRequestedMaxChargeCurrent"] = user_requested_max_charge_current
        if user_requested_max_grid_current is not UNSET:
            field_dict["userRequestedMaxGridCurrent"] = user_requested_max_grid_current
        if user_requested_ev_battery_mode is not UNSET:
            field_dict["userRequestedEvBatteryMode"] = user_requested_ev_battery_mode
        if user_requested_max_grid_power is not UNSET:
            field_dict["userRequestedMaxGridPower"] = user_requested_max_grid_power
        if user_requested_battery_peak_reserve_soc is not UNSET:
            field_dict["userRequestedBatteryPeakReserveSoc"] = (
                user_requested_battery_peak_reserve_soc
            )
        if user_requested_lower_price_threshold is not UNSET:
            field_dict["userRequestedLowerPriceThreshold"] = user_requested_lower_price_threshold
        if user_requested_upper_price_threshold is not UNSET:
            field_dict["userRequestedUpperPriceThreshold"] = user_requested_upper_price_threshold
        if user_requested_ev_mode is not UNSET:
            field_dict["userRequestedEvMode"] = user_requested_ev_mode
        if user_requested_deactivate_heat_pump_on_high_prices is not UNSET:
            field_dict["userRequestedDeactivateHeatPumpOnHighPrices"] = (
                user_requested_deactivate_heat_pump_on_high_prices
            )
        if user_requested_activate_heat_pump_on_low_prices is not UNSET:
            field_dict["userRequestedActivateHeatPumpOnLowPrices"] = (
                user_requested_activate_heat_pump_on_low_prices
            )
        if enable_curtailing is not UNSET:
            field_dict["enableCurtailing"] = enable_curtailing
        if other_properties is not UNSET:
            field_dict["otherProperties"] = other_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ems_configuration_set_user_ems_parameters_post_input_model_other_properties import (
            EmsConfigurationSetUserEmsParametersPostInputModelOtherProperties,
        )

        d = dict(src_dict)
        user_requested_max_charge_current = d.pop("userRequestedMaxChargeCurrent", UNSET)

        user_requested_max_grid_current = d.pop("userRequestedMaxGridCurrent", UNSET)

        user_requested_ev_battery_mode = d.pop("userRequestedEvBatteryMode", UNSET)

        user_requested_max_grid_power = d.pop("userRequestedMaxGridPower", UNSET)

        user_requested_battery_peak_reserve_soc = d.pop("userRequestedBatteryPeakReserveSoc", UNSET)

        user_requested_lower_price_threshold = d.pop("userRequestedLowerPriceThreshold", UNSET)

        user_requested_upper_price_threshold = d.pop("userRequestedUpperPriceThreshold", UNSET)

        user_requested_ev_mode = d.pop("userRequestedEvMode", UNSET)

        user_requested_deactivate_heat_pump_on_high_prices = d.pop(
            "userRequestedDeactivateHeatPumpOnHighPrices", UNSET
        )

        user_requested_activate_heat_pump_on_low_prices = d.pop(
            "userRequestedActivateHeatPumpOnLowPrices", UNSET
        )

        enable_curtailing = d.pop("enableCurtailing", UNSET)

        _other_properties = d.pop("otherProperties", UNSET)
        other_properties: EmsConfigurationSetUserEmsParametersPostInputModelOtherProperties | Unset
        if isinstance(_other_properties, Unset):
            other_properties = UNSET
        else:
            other_properties = (
                EmsConfigurationSetUserEmsParametersPostInputModelOtherProperties.from_dict(
                    _other_properties
                )
            )

        ems_configuration_set_user_ems_parameters_post_input_model = cls(
            user_requested_max_charge_current=user_requested_max_charge_current,
            user_requested_max_grid_current=user_requested_max_grid_current,
            user_requested_ev_battery_mode=user_requested_ev_battery_mode,
            user_requested_max_grid_power=user_requested_max_grid_power,
            user_requested_battery_peak_reserve_soc=user_requested_battery_peak_reserve_soc,
            user_requested_lower_price_threshold=user_requested_lower_price_threshold,
            user_requested_upper_price_threshold=user_requested_upper_price_threshold,
            user_requested_ev_mode=user_requested_ev_mode,
            user_requested_deactivate_heat_pump_on_high_prices=user_requested_deactivate_heat_pump_on_high_prices,
            user_requested_activate_heat_pump_on_low_prices=user_requested_activate_heat_pump_on_low_prices,
            enable_curtailing=enable_curtailing,
            other_properties=other_properties,
        )

        ems_configuration_set_user_ems_parameters_post_input_model.additional_properties = d
        return ems_configuration_set_user_ems_parameters_post_input_model

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
