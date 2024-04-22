import streamlit as st


def calculate_total_power_consumed(devices, operation_duration):
    total_power = 0
    for device, power in devices.items():
        duration = operation_duration[device]
        power_consumed = power * duration
        total_power += power_consumed
    return total_power


def main():
    st.title("Total Power Consumed Calculator")

    # Input fields for devices and their power ratings
    devices = {}
    operation_duration = {}
    for i in range(4):
        device_name = st.text_input(f"Device {i+1} name")
        power_rating = st.number_input(
            f"Power rating of {device_name} (in watts)", min_value=0)
        if device_name:
            devices[device_name] = power_rating
            duration = st.number_input(
                f"Operation duration of {device_name} (in hours)", min_value=0)
            operation_duration[device_name] = duration

    # Calculate total power consumed
    if st.button("Calculate"):
        total_power = calculate_total_power_consumed(
            devices, operation_duration)
        st.write(f"Total power consumed: {total_power} watt-hours")


if __name__ == "__main__":
    main()
