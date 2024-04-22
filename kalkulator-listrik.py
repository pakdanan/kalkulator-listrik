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
    st.header("Devices and Power Ratings")
    devices = {}
    for i in range(1, 5):
        device_name = st.text_input(f"Device {i} name")
        power_rating = st.number_input(
            f"Power rating of {device_name} (in watts)", min_value=0, key=f"device-{i}")
        if device_name:
            devices[device_name] = power_rating

    # Input fields for operation durations
    st.header("Operation Durations")
    operation_duration = {}
    for device in devices.keys():
        duration = st.number_input(
            f"Operation duration of {device} (in hours)", min_value=0, key=f"device-duration-{i}")
        operation_duration[device] = duration

    # Calculate total power consumed
    if st.button("Calculate"):
        total_power = calculate_total_power_consumed(
            devices, operation_duration)
        st.write(f"Total power consumed: {total_power} watt-hours")


if __name__ == "__main__":
    main()
