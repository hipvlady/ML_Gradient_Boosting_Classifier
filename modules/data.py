import pandas as pd

test_loc = 231


def set_filepath(stage):
    file_paths = {
        'train': 'data/Training_DataSet.csv',
        'test': 'data/Test_Dataset.csv'
    }

    common_transform_path = 'data/final/'

    if stage.lower() == 'train':
        # Transformation for the training stage
        transform_suffix = 'train_'
    else:
        # Transformation for the testing stage
        transform_suffix = 'test_'

    eda_dataset = file_paths[stage.lower()]
    data_transform_ds = file_paths[stage.lower()]
    transform_categorical_clean = f'{common_transform_path}{transform_suffix}categorical_clean.csv'
    transform_numerical_clean = f'{common_transform_path}{transform_suffix}numerical_clean.csv'
    transform_final = f'{common_transform_path}{transform_suffix}final_clean.csv'

    return eda_dataset, data_transform_ds, transform_categorical_clean, transform_numerical_clean, transform_final



def percent_missing(in_df):
    result = 100 * in_df.isnull().sum() / len(in_df)
    result = result[result > 0].sort_values()
    return result


def display_test(df, test_loc):
    result = df.loc[test_loc]
    print(result)


def group_colors(color):
    if not isinstance(color, str):
        return "Other"

    major_colors = ["White", "Black", "Silver", "Gray", "Red", "Blue", "Green", "Gold", "Brown", "Beige"]
    for major in major_colors:
        if major.lower() in color.lower():
            return major
    return "Other"


def normalize_color(color):
    if not isinstance(color, str):
        return "unknown"

    color = color.lower().strip()

    # Define mapping for color normalization
    mapping = {
        'black': ['black', 'jet black', 'black leather'],
        'beige': ['beige', 'sahara beige', 'beige cloth', 'beige leather'],
        'tan': ['tan', 'tan leather'],
        'gray': ['gray', 'light frost brown', 'lt frost beige black'],
        'brown': ['brown']
    }

    for main_color, variations in mapping.items():
        if color in variations:
            return main_color

    return color  # If color not in mapping, return the original color


def further_normalize_color(color):
    # Define common colors to retain
    common_colors = ['black', 'beige', 'tan', 'gray', 'brown', 'blue', 'white', 'red', 'green', 'yellow', 'orange', 'purple', 'unknown']

    # If the color is not in the list of common colors, label it as 'other'
    if color not in common_colors:
        return 'other'

    return color


def jeep_transmission_replacement(transmission):
    if isinstance(transmission, str):
        transmission_lower = transmission.lower()
        if any(word in transmission_lower for word in ["8-speed", "8-spd", "8hp70", "845re", "850re"]):
            return "8-Speed Automatic"
        elif "automatic" in transmission_lower or "auto" in transmission_lower:
            return "Automatic"
        else:
            return "Other"
    else:
        return "unknown"  # For NaN values


def jeep_bin_drive_type(VehDriveTrain):
    if pd.isnull(VehDriveTrain):
        return 'unknown'
    elif '4WD' in VehDriveTrain or '4X4' in VehDriveTrain or '4x4' in VehDriveTrain or 'Four Wheel Drive' in VehDriveTrain:
        return '4WD'
    elif 'AWD' in VehDriveTrain:
        return 'AWD'
    else:
        return 'unknown'


# Define the replacement function for Jeep's Vehicle_Trim
def jeep_trim_replacement(trim):
    if isinstance(trim, str):
        if any(word in trim for word in ["Premium", "Overland", "Summit"]):
            return "Premium Luxury"
        elif any(word in trim for word in ["Sport", "Base"]):
            return "Base"
        elif "Trailhawk" in trim:
            return "Trailhawk"
        else:
            return "Limited"
    else:
        return "unknown"  # For NaN values


def bucket_ratings(rating):
    if rating < 3:
        return "Low Rating"
    elif 3 <= rating < 4:
        return "Average Rating"
    elif 4 <= rating < 4.5:
        return "Good Rating"
    else:
        return "Excellent Rating"


def bucket_sellers(listing_count):
    if listing_count > 20:
        return "High Volume Sellers"
    elif 5 <= listing_count <= 20:
        return "Medium Volume Sellers"
    elif 2 <= listing_count <= 4:
        return "Low Volume Sellers"
    else:
        return "Rare Sellers"


def bucket_listing_sources(source_count):
    if source_count > 1000:
        return "High-Frequency Sources"
    elif source_count < 50:
        return "Other Sources"
    else:
        return "Medium-Frequency Sources"