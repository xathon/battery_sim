"""Constants for the battery_sim component."""
from typing import Final

DOMAIN = "battery_sim"

BATTERY_TYPE = "battery"

QUARTER_HOURLY = "quarter-hourly"
HOURLY = "hourly"
DAILY = "daily"
WEEKLY = "weekly"
MONTHLY = "monthly"
BIMONTHLY = "bimonthly"
QUARTERLY = "quarterly"
YEARLY = "yearly"

DATA_UTILITY = "battery_sim_data"

CONF_BATTERY = "battery"
CONF_IMPORT_SENSOR = "import_sensor"
CONF_EXPORT_SENSOR = "export_sensor"
CONF_BATTERY_SIZE = "size_kwh"
CONF_BATTERY_MAX_DISCHARGE_RATE = "max_discharge_rate_kw"
CONF_BATTERY_MAX_CHARGE_RATE = "max_charge_rate_kw"
CONF_BATTERY_EFFICIENCY = "efficiency"
CONF_ENERGY_TARIFF = "energy_tariff"
ATTR_VALUE = "value"

ATTR_SOURCE_ID = "source"
ATTR_STATUS = "status"
PRECISION = 3
ATTR_ENERGY_SAVED = "total_energy_saved"
ATTR_ENERGY_SAVED_TODAY = "energy_saved_today"
ATTR_ENERGY_SAVED_WEEK = "energy_saved_this_week"
ATTR_ENERGY_SAVED_MONTH = "energy_saved_this_month"
ATTR_DATE_RECORDING_STARTED = "date_recording_started"
ATTR_ENERGY_BATTERY_OUT = "battery_energy_out"
ATTR_ENERGY_BATTERY_IN = "battery_energy_in"
ATTR_MONEY_SAVED = "total_money_saved"
CHARGING = "charging"
DISCHARGING = "discharging"
CHARGING_RATE = "current_rate_of_charging_kw"
DISCHARGING_RATE = "currrent_rate_of_discharging_kw"
ATTR_CHARGE_PERCENTAGE = "percentage"
GRID_EXPORT_SIM = "simulated_grid_export_after_battery_charging"
GRID_IMPORT_SIM = "simulated_grid_import_after_battery_charging"
ICON_CHARGING = "mdi:battery-charging-50"
ICON_DISCHARGING = "mdi:battery-50"

BATTERY_OPTIONS = {
    "Tesla Powerwall": {
        CONF_BATTERY_SIZE: 13.5,
        CONF_BATTERY_MAX_DISCHARGE_RATE: 5.0,
        CONF_BATTERY_MAX_CHARGE_RATE: 3.68,
        CONF_BATTERY_EFFICIENCY: 0.9 },
    "LG Chem": {
        CONF_BATTERY_SIZE: 9.3,
        CONF_BATTERY_MAX_DISCHARGE_RATE: 5.0,
        CONF_BATTERY_MAX_CHARGE_RATE: 3.3,
        CONF_BATTERY_EFFICIENCY: 0.95 },
    "Sonnen Eco": {
        CONF_BATTERY_SIZE: 5.0,
        CONF_BATTERY_MAX_DISCHARGE_RATE: 2.5,
        CONF_BATTERY_MAX_CHARGE_RATE: 2.5,
        CONF_BATTERY_EFFICIENCY: 0.9},
    "Pika Harbour": {
        CONF_BATTERY_SIZE: 8.6,
        CONF_BATTERY_MAX_DISCHARGE_RATE: 4.2,
        CONF_BATTERY_MAX_CHARGE_RATE: 4.2,
        CONF_BATTERY_EFFICIENCY: 0.965},
    "Custom":{}
    }