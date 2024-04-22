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


st.title("Kalkulator tarif listrik")

# Input fields for devices, their power ratings and durations
number_of_devices = st.number_input(f"Jumlah perangkat", min_value=1)

devices = {}
operation_duration = {}
for i in range(number_of_devices):
    device_name = f"Perangkat {i+1}"
    power_rating = st.number_input(
        f"Daya listrik {device_name} (watt)", min_value=0, key=device_name)
    devices[device_name] = power_rating
    duration = st.number_input(
        f"Durasi {device_name} (jam)", min_value=0, key=f"{device_name}-duration")
    operation_duration[device_name] = duration

tarif_dasars = {"R-1/TR daya 900 VA": 1352, "R-1/TR daya 1.300 VA": 1444.70, "R-1/TR daya 2.200 VA": 1444.70,
                "R-2/TR daya 3.500-5.500 VA": 1699.53, "R-3/TR daya 6.600 VA ke atas": 1699.53}

# Selectbox to choose tarif dasar
selected_tarif_dasar = st.selectbox(
    "Tarif dasar", list(tarif_dasars.keys()))

# anggaran_listrik_min = st.number_input(f"Anggaran Listrik")
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Calculate tarif listrik
if st.button("Hitung"):
    tarif_litrik = calculate_tarif_listrik(
        devices, operation_duration, tarif_dasars[selected_tarif_dasar])
    # Branching conditions to check the range of total power consumed
    # if tarif_litrik < anggaran_listrik:
    #     st.info("Konsumsi listrik Anda masih aman")
    # elif tarif_litrik = anggaran_listrik:
    #     st.write("Your power consumption is moderate.")
    # else:
    #     st.write("Your power consumption is high.")
    st.write(f"Tarif listrik: Rp {tarif_litrik}")
