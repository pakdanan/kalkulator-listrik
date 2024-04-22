import streamlit as st


def calculate_tarif_listrik(devices, operation_duration, tarif_dasar):
    total_power = 0
    for device_name in devices:
        power = devices[device_name]
        duration = operation_duration[device_name]
        power_consumed = power * duration
        total_power += power_consumed
        tarif_listrik = total_power*tarif_dasar/1000
    return tarif_listrik


def main():
    st.title("Kalkulator tarif listrik")

    # Input fields for devices and their power ratings
    number_of_devices = 3
    devices = {}
    operation_duration = {}
    for i in range(number_of_devices):
        device_name = f"Device {i}"
        power_rating = st.number_input(
            f"Daya listrik {device_name} (watt)", min_value=0, key=device_name)
        devices[device_name] = power_rating
        duration = st.number_input(
            f"Durasi {device_name} (jam)", min_value=0, key=f"{device_name}-duration")
        operation_duration[device_name] = duration

    tarif_dasars = {"R-1/TR daya 900 VA": 1352,
                    "R-1/TR daya 1.300 VA": 1444.70, "R-1/TR daya 2.200 VA": 1444.70, "R-2/TR daya 3.500-5.500 VA": 1699.53}

    # Selectbox to choose tarif dasar
    selected_tarif_dasar = st.selectbox(
        "Piih tarif dasar", list(tarif_dasars.keys()))

    # Calculate total power consumed
    if st.button("Calculate"):
        tarif_litrik = calculate_tarif_listrik(
            devices, operation_duration, selected_tarif_dasar)
        st.write(f"Tarif listrik: {tarif_litrik}")


if __name__ == "__main__":
    main()
