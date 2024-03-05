from plot_utilities import create_plot, parse_input_file

def create_time_plot(data, labels, output_name):
    create_plot(data, labels, output_name, 'GTBENCH Median Runtime with 95% Confidence Intervals', 'Domain X size', 'Median runtime', 'Median Time 95% Confidence Upper', 'Median Time 95% Confidence Lower', 'Domain Size (NxNxN)', 'Median Runtime')

def create_columns_plot(data, labels, output_name):
    create_plot(data, labels, output_name, 'GTBENCH Columns per Second with 95% Confidence Intervals', 'Domain X size', 'Columns per Second', 'Columns per Second 95% Confidence Upper', 'Columns per Second 95% Confidence Lower', 'Domain Size (NxNxN)', 'Columns per Second')

def create_elements_plot(data, labels, output_name):
    create_plot(data, labels, output_name, 'GTBENCH Elements per Second with 95% Confidence Intervals', 'Domain X size', 'Elements per Second', 'Elements per Second 95% Confidence Upper', 'Elements per Second 95% Confidence Lower', 'Domain Size (NxNxN)', 'Elements per Second')


data = {}

input = {
    "GH200": {
        "files": ["santis_cpu_ifirst_domain_sweep_up_512.out", "santis_cpu_kfirst_domain_sweep_up_512.out"],
        "labels": ["cpu_ifirst", "cpu_kfirst"]
    },
    "AMD EPYC 7742": {
        "files": ["clariden_cpu_ifirst_domain_sweep.out", "clariden_cpu_kfirst_domain_sweep.out"],
        "labels": ["cpu_ifirst", "cpu_kfirst"]
    }
}


for system in input.keys():
    data[system] = {}
    input_system = input[system]
    for file, variant in zip(input_system["files"], input_system["labels"]):
        data[system][variant] = parse_input_file(file)
        print(data[system][variant])

labels = list(input.keys())

create_time_plot(data, labels, "santis_clariden_cpu_ikfirst_time.png")
create_columns_plot(data, labels, "santis_clariden_cpu_ikfirst_columns.png")
create_elements_plot(data, labels, "santis_clariden_cpu_ikfirst_elements.png")
