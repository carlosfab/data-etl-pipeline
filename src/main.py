# --- Imports ---
from pipeline.extract import extract_from_excel
from pipeline.transform import transform_to_single_dataframe
from pipeline.load import load_to_excel
from paths import INPUT_DIR, OUTPUT_DIR

# --- Main ---
if __name__ == '__main__':
    data_frame_list = extract_from_excel(INPUT_DIR)
    data_frame = transform_to_single_dataframe(data_frame_list)
    load_to_excel(data_frame, OUTPUT_DIR, 'output')
