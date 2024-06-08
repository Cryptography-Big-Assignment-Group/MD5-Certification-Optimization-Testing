import json
import os
import matplotlib.pyplot as plt

def load_results(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def plot_uniformity_test(data):
    chi2_stat = data.get('chi2_stat', 0)
    p_value = data.get('p_value', 1)
    frequencies = data.get('frequencies', [])

    print("Uniformity Test Results:")
    print(f"  Chi2 Statistic: {chi2_stat}")
    print(f"  p-value: {p_value}")

    if frequencies:
        plt.hist(frequencies, bins=50)
        plt.title('Uniformity Test Histogram')
        plt.xlabel('Frequency')
        plt.ylabel('Count')
        plt.show()
    else:
        print("No frequency data available to plot.")

def plot_avalanche_effect_test(data):
    mean_distance = data.get('mean_distance', 0)
    distances = data.get('distances', [])

    print("Avalanche Effect Test Results:")
    print(f"  Mean Hamming Distance: {mean_distance}")

    if distances:
        plt.hist(distances, bins=50)
        plt.title('Avalanche Effect Test Histogram')
        plt.xlabel('Hamming Distance')
        plt.ylabel('Count')
        plt.show()
    else:
        print("No distance data available to plot.")

def plot_collision_test(data):
    num_samples = data.get('num_samples', 0)
    collisions = data.get('collisions', 0)
    collision_probability = data.get('collision_probability', 0)

    print("Collision Test Results:")
    print(f"  Number of Samples: {num_samples}")
    print(f"  Collisions: {collisions}")
    print(f"  Collision Probability: {collision_probability}")

    plt.bar(['Collision Probability'], [collision_probability])
    plt.title('Collision Test')
    plt.ylabel('Probability')
    plt.show()

def list_exp_folders(output_dir):
    return [folder for folder in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, folder)) and folder.startswith('exp')]

def main():
    output_dir = 'output'
    exp_folders = list_exp_folders(output_dir)

    if not exp_folders:
        print("No experiment folders found.")
        return

    print("Available experiment folders:")
    for i, folder in enumerate(exp_folders):
        print(f"{i + 1}. {folder}")

    try:
        choice = int(input("Select an experiment folder by number: ")) - 1
        if choice < 0 or choice >= len(exp_folders):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    selected_folder = exp_folders[choice]
    result_file_path = os.path.join(output_dir, selected_folder, 'results_summary.json')

    if os.path.exists(result_file_path):
        results = load_results(result_file_path)

        if 'uniformity' in results:
            plot_uniformity_test(results['uniformity'])
        else:
            print("No uniformity test data found in results.")

        if 'avalanche' in results:
            plot_avalanche_effect_test(results['avalanche'])
        else:
            print("No avalanche effect test data found in results.")

        if 'collision' in results:
            plot_collision_test(results['collision'])
        else:
            print("No collision test data found in results.")
    else:
        print(f"Result file not found: {result_file_path}")

if __name__ == "__main__":
    main()
