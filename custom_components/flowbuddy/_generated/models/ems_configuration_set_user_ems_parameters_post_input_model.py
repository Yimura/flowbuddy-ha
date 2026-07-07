from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.ems_configuration_set_user_ems_parameters_post_input_model_other_properties_type_0 import (
        EmsConfigurationSetUserEmsParametersPostInputModelOtherPropertiesType0,
    )


T = TypeVar("T", bound="EmsConfigurationSetUserEmsParametersPostInputModel")


@_attrs_define
class EmsConfigurationSetUserEmsParametersPostInputModel:
    """
    Attributes:
        user_requested_max_charge_current (float | None | Unset):
        user_requested_max_grid_current (float | None | Unset):
        user_requested_ev_battery_mode (int | None | Unset):
        user_requested_max_grid_power (int | None | Unset):
        user_requested_battery_peak_reserve_soc (int | None | Unset):
        user_requested_lower_price_threshold (float | None | Unset):
        user_requested_upper_price_threshold (float | None | Unset):
        user_requested_ev_mode (None | str | Unset):
        user_requested_deactivate_heat_pump_on_high_prices (bool | None | Unset):
        user_requested_activate_heat_pump_on_low_prices (bool | None | Unset):
        enable_curtailing (bool | None | Unset):
        other_properties (EmsConfigurationSetUserEmsParametersPostInputModelOtherPropertiesType0 | None | Unset):
    """

    user_requested_max_charge_current: float | None | Unset = UNSET
    user_requested_max_grid_current: float | None | Unset = UNSET
    user_requested_ev_battery_mode: int | None | Unset = UNSET
    user_requested_max_grid_power: int | None | Unset = UNSET
    user_requested_battery_peak_reserve_soc: int | None | Unset = UNSET
    user_requested_lower_price_threshold: float | None | Unset = UNSET
    user_requested_upper_price_threshold: float | None | Unset = UNSET
    user_requested_ev_mode: None | str | Unset = UNSET
    user_requested_deactivate_heat_pump_on_high_prices: bool | None | Unset = UNSET
    user_requested_activate_heat_pump_on_low_prices: bool | None | Unset = UNSET
    enable_curtailing: bool | None | Unset = UNSET
    other_properties: (
        EmsConfigurationSetUserEmsParametersPostInputModelOtherPropertiesType0 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ems_configuration_set_user_ems_parameters_post_input_model_other_properties_type_0 import (
            EmsConfigurationSetUserEmsParametersPostInputModelOtherPropertiesType0,
        )

        user_requested_max_charge_current: float | None | Unset
        if isinstance(self.user_requested_max_charge_current, Unset):
            user_requested_max_charge_current = UNSET
        else:
            user_requested_max_charge_current = self.user_requested_max_charge_current

        user_requested_max_grid_current: float | None | Unset
        if isinstance(self.user_requested_max_grid_current, Unset):
            user_requested_max_grid_current = UNSET
        else:
            user_requested_max_grid_current = self.user_requested_max_grid_current

        user_requested_ev_battery_mode: int | None | Unset
        if isinstance(self.user_requested_ev_battery_mode, Unset):
            user_requested_ev_battery_mode = UNSET
        else:
            user_requested_ev_battery_mode = self.user_requested_ev_battery_mode

        user_requested_max_grid_power: int | None | Unset
        if isinstance(self.user_requested_max_grid_power, Unset):
            user_requested_max_grid_power = UNSET
        else:
            user_requested_max_grid_power = self.user_requested_max_grid_power

        user_requested_battery_peak_reserve_soc: int | None | Unset
        if isinstance(self.user_requested_battery_peak_reserve_soc, Unset):
            user_requested_battery_peak_reserve_soc = UNSET
        else:
            user_requested_battery_peak_reserve_soc = self.user_requested_battery_peak_reserve_soc

        user_requested_lower_price_threshold: float | None | Unset
        if isinstance(self.user_requested_lower_price_threshold, Unset):
            user_requested_lower_price_threshold = UNSET
        else:
            user_requested_lower_price_threshold = self.user_requested_lower_price_threshold

        user_requested_upper_price_threshold: float | None | Unset
        if isinstance(self.user_requested_upper_price_threshold, Unset):
            user_requested_upper_price_threshold = UNSET
        else:
            user_requested_upper_price_threshold = self.user_requested_upper_price_threshold

        user_requested_ev_mode: None | str | Unset
        if isinstance(self.user_requested_ev_mode, Unset):
            user_requested_ev_mode = UNSET
        else:
            user_requested_ev_mode = self.user_requested_ev_mode

        user_requested_deactivate_heat_pump_on_high_prices: bool | None | Unset
        if isinstance(self.user_requested_deactivate_heat_pump_on_high_prices, Unset):
            user_requested_deactivate_heat_pump_on_high_prices = UNSET
        else:
            user_requested_deactivate_heat_pump_on_high_prices = (
                self.user_requested_deactivate_heat_pump_on_high_prices
            )

        user_requested_activate_heat_pump_on_low_prices: bool | None | Unset
        if isinstance(self.user_requested_activate_heat_pump_on_low_prices, Unset):
            user_requested_activate_heat_pump_on_low_prices = UNSET
        else:
            user_requested_activate_heat_pump_on_low_prices = (
                self.user_requested_activate_heat_pump_on_low_prices
            )

        enable_curtailing: bool | None | Unset
        if isinstance(self.enable_curtailing, Unset):
            enable_curtailing = UNSET
        else:
            enable_curtailing = self.enable_curtailing

        other_properties: dict[str, Any] | None | Unset
        if isinstance(self.other_properties, Unset):
            other_properties = UNSET
        elif isinstance(
            self.other_properties,
            EmsConfigurationSetUserEmsParametersPostInputModelOtherPropertiesType0,
        ):
            other_properties = self.other_properties.to_dict()
        else:
            other_properties = self.other_properties

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
        from ..models.ems_configuration_set_user_ems_parameters_post_input_model_other_properties_type_0 import (
            EmsConfigurationSetUserEmsParametersPostInputModelOtherPropertiesType0,
        )

        d = dict(src_dict)

        def _parse_user_requested_max_charge_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        user_requested_max_charge_current = _parse_user_requested_max_charge_current(
            d.pop("userRequestedMaxChargeCurrent", UNSET)
        )

        def _parse_user_requested_max_grid_current(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        user_requested_max_grid_current = _parse_user_requested_max_grid_current(
            d.pop("userRequestedMaxGridCurrent", UNSET)
        )

        def _parse_user_requested_ev_battery_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_requested_ev_battery_mode = _parse_user_requested_ev_battery_mode(
            d.pop("userRequestedEvBatteryMode", UNSET)
        )

        def _parse_user_requested_max_grid_power(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_requested_max_grid_power = _parse_user_requested_max_grid_power(
            d.pop("userRequestedMaxGridPower", UNSET)
        )

        def _parse_user_requested_battery_peak_reserve_soc(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_requested_battery_peak_reserve_soc = _parse_user_requested_battery_peak_reserve_soc(
            d.pop("userRequestedBatteryPeakReserveSoc", UNSET)
        )

        def _parse_user_requested_lower_price_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        user_requested_lower_price_threshold = _parse_user_requested_lower_price_threshold(
            d.pop("userRequestedLowerPriceThreshold", UNSET)
        )

        def _parse_user_requested_upper_price_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        user_requested_upper_price_threshold = _parse_user_requested_upper_price_threshold(
            d.pop("userRequestedUpperPriceThreshold", UNSET)
        )

        def _parse_user_requested_ev_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_requested_ev_mode = _parse_user_requested_ev_mode(d.pop("userRequestedEvMode", UNSET))

        def _parse_user_requested_deactivate_heat_pump_on_high_prices(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_requested_deactivate_heat_pump_on_high_prices = (
            _parse_user_requested_deactivate_heat_pump_on_high_prices(
                d.pop("userRequestedDeactivateHeatPumpOnHighPrices", UNSET)
            )
        )

        def _parse_user_requested_activate_heat_pump_on_low_prices(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_requested_activate_heat_pump_on_low_prices = (
            _parse_user_requested_activate_heat_pump_on_low_prices(
                d.pop("userRequestedActivateHeatPumpOnLowPrices", UNSET)
            )
        )

        def _parse_enable_curtailing(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_curtailing = _parse_enable_curtailing(d.pop("enableCurtailing", UNSET))

        def _parse_other_properties(
            data: object,
        ) -> EmsConfigurationSetUserEmsParametersPostInputModelOtherPropertiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                other_properties_type_0 = EmsConfigurationSetUserEmsParametersPostInputModelOtherPropertiesType0.from_dict(
                    data
                )

                return other_properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EmsConfigurationSetUserEmsParametersPostInputModelOtherPropertiesType0
                | None
                | Unset,
                data,
            )

        other_properties = _parse_other_properties(d.pop("otherProperties", UNSET))

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
