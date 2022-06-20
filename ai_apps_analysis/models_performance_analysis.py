import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 2000)

current_path = '/Users/yinghua.li/Documents/Pycharm/AIApps/data/analysis_result/'
log_name_list = ['performance.log', 'performance2.log', 'performance3.log', 'performance4.log', 'performance5.log', 'performance6.log']
size_name_list = ['performance.txt', 'performance2.txt', 'performance3.txt', 'performance4.txt', 'performance5.txt', 'performance6.txt']
log_name_list = [current_path+i for i in log_name_list]
size_name_list = [current_path+i for i in size_name_list]


def get_data(path_log, path_txt):
    f = open(path_log, "r")
    lines = f.readlines()
    lines_log_list = [line.strip() for line in lines if len(line) > 5]

    f = open(path_txt, "r")
    lines = f.readlines()
    lines_txt_list = [line.strip() for line in lines if len(line) > 5]

    lines_txt_list = lines_txt_list[: len(lines_log_list)]
    df = pd.DataFrame(columns=['log', 'size'])
    df['size'] = lines_txt_list
    df['log'] = lines_log_list
    return df


def get_all_data():
    data_list = []
    for i in range(len(log_name_list)):
        data_list.append(get_data(log_name_list[i], size_name_list[i]))
    df = pd.concat(data_list, ignore_index=True)
    return df


def udf_get_time_warmup(s):
    time_warmup = s.split('Warmup:')[-1].split(',')[0].strip()
    return float(time_warmup)


def udf_get_time_init(s):
    time_init = s.split('Init:')[-1].split(',')[0].strip()
    return int(time_init)


def udf_get_time_inference(s):
    time_inference = s.split('Overall')[0].split('Inference:')[-1].strip()
    return float(time_inference)


def udf_get_overall_memory_usage(s):
    overall_memory_usage = s.split('Overall max resident set size =')[-1].split('MB')[0].strip()
    return float(overall_memory_usage)


def udf_get_memory_init(s):
    memory_init = s.split('in-use allocated/mmapped size =')[-1].split('MB')[0].strip()
    return float(memory_init)


def plot(x, y):
    plt.ylabel('FLOPs')
    plt.xlabel('AI Models Size (MB)')
    plt.scatter(x, y, s=[1] * len(x),  c='black')
    plt.show()


def udf_get_size_tag(s):
    return int(str(s)[0])


def udf_size(s):
    return float(s)


def plot(df, col_name, ylabel_name, save_path):
    x = []
    y = []
    for size, group_pdf in df.groupby('size_tag'):
        pdf = group_pdf.sort_values(by=[col_name], ascending=True).copy()
        n = len(pdf)
        tmp_y = list(pdf[col_name])
        tmp_x = list(pdf['size'])
        tmp_y = tmp_y[int(n*0.2): int(n*0.8)]
        tmp_x = tmp_x[int(n*0.2): int(n*0.8)]
        x += tmp_x
        y += tmp_y
    print(len(x))
    plt.tick_params(labelsize=8)
    plt.rcParams['figure.figsize'] = (8.0, 6.0)
    plt.ylabel(ylabel_name, fontsize=14)
    plt.xlabel('AI Models Size (MB)', fontsize=14)
    plt.scatter(x, y, s=[1] * len(x),  c='black')
    plt.savefig(save_path)


def main():

    df = get_all_data()
    df['time_init'] = df['log'].apply(udf_get_time_init)
    df['time_warmup'] = df['log'].apply(udf_get_time_warmup)
    df['time_inference'] = df['log'].apply(udf_get_time_inference)
    df['overall_memory_usage'] = df['log'].apply(udf_get_overall_memory_usage)
    df['memory_init'] = df['log'].apply(udf_get_memory_init)
    df['size_tag'] = df['size'].apply(udf_get_size_tag)
    df['size'] = df['size'].apply(udf_size)

    # plot(df, 'time_init', 'Initialization time (μs)', '../data/picture/size_time_init.pdf')
    # plot(df, 'time_warmup', 'Inference time of warmup state (μs)', '../data/picture/size_time_warmup.pdf')
    # plot(df, 'time_inference', 'Inference time of steady state (μs)', '../data/picture/size_time_inference.pdf')
    # plot(df, 'overall_memory_usage', 'Overall memory usage (MB)', '../data/picture/size_overall_memory_usage.pdf')
    plot(df, 'memory_init', 'Memory usage during initialization time (MB)', '../data/picture/size_memory_init.pdf')


if __name__ == '__main__':
    main()
