# Parallel Factorial Calculation using Python and gmpy2

## Project Description

This project demonstrates the use of multiprocessing to accelerate the calculation of the factorial of a large number (in this case, 10 million). The program divides the task into 15 parts, each processed by a separate Python worker file. After all processes are complete, the intermediate results are combined to produce the final result.

## Project Structure

- **`main.py`**: The main program file. Manages the execution of 15 processes, each of which calculates the factorial of its part of the sequence. Once all workers have completed, it collects the results and combines them.
- **`worker_0.py` ... `worker_14.py`**: Worker files. Each worker computes the factorial for a given range of numbers and writes the result to a text file.
- **Result files**: Each worker saves its result in a separate file, for example, `result_part_0.txt`, `result_part_1.txt`, and so on.

## Requirements

To run the project, the following dependencies are needed:

- **Python 3.8+**
- **gmpy2**: A library for working with large numbers and optimizing mathematical operations.

Install the `gmpy2` library using pip:

```bash
pip install gmpy2
```

## How to Run

1. Ensure you have created all 15 worker files: `worker_0.py`, `worker_1.py`, ..., `worker_14.py`. The code in each worker file should be identical, except for the file name.

   Example contents of `worker_0.py`:
   ```python
   import sys
   import gmpy2

   def multiply_range(start, end):
       result = gmpy2.mpz(1)
       for number in range(start, end + 1):
           result *= number
       return result

   if __name__ == '__main__':
       start = int(sys.argv[1])
       end = int(sys.argv[2])
       output_file = sys.argv[3]

       result = multiply_range(start, end)

       with open(output_file, 'w') as f:
           f.write(str(result))
   ```

2. Run the main program file `main.py`:

```bash
python main.py
```

3. The program will create 15 processes, each of which will calculate the factorial for its assigned range of numbers. After all processes complete, the results will be combined, and the final factorial of the number 10 million will be printed to the console.

## Sample Output

```
Factorial of 5_000_000 computed!
Execution time: 50.23 seconds
```

## Configuration

- **Number of workers**: In the current version of the project, 15 workers are used, each processing its portion of the number sequence. You can change the number of workers by modifying the `num_files` variable in `main.py`.
- **Chunk sizes**: The number ranges for each worker are automatically divided based on the total number of elements and the number of workers.

## Notes

- The program uses the file system to exchange results between processes. Depending on the size of the number you're computing, the result files can be very large. Ensure there is enough free disk space to store the intermediate results.
- The program's performance may depend on the number of CPU cores and available memory. Ensure your system supports the parallel execution of a large number of processes.
