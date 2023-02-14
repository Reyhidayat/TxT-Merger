import os
import time
from multiprocessing import Process

def combine_files(files, output_file):
    with open(output_file, "w", encoding="utf-8") as f_out:
        for file in files:
            with open(file, "r", encoding="utf-8") as f_in:
                f_out.write(f_in.read())

def sort_file(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines = list(set(lines))
    lines.sort()
    with open(file, "w", encoding="utf-8") as f:
        f.writelines(lines)

def run_processes(processes):
    for p in processes:
        p.start()
    for p in processes:
        p.join()

def show_loading():
    for i in range(101):
        print(f"Loading: {i}%")
        time.sleep(0.05)

if __name__ == "__main__":
    files = [f for f in os.listdir() if f.endswith(".txt")]
    output_file = "new.txt"
    combine_process = Process(target=combine_files, args=(files, output_file))
    sort_processes = [Process(target=sort_file, args=(f,)) for f in files]

    loading_process = Process(target=show_loading)
    loading_process.start()
    run_processes([combine_process] + sort_processes)
    loading_process.terminate()

    print("Process Completed")
