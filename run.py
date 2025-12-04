from argparse import ArgumentParser 
import os
from importlib import import_module
import logging

logger = logging.getLogger("AoC")
logging.basicConfig(level=logging.ERROR, format='[%(name)s] %(levelname)s: %(message)s') 


COLOR_ERROR = '\033[91m'
COLOR_WARNING = '\033[93m'
COLOR_END = '\033[0m'

def get_available_days():
    for dirpath, _, filenames in os.walk("tasks"):
        dir = os.path.basename(dirpath)
        for filename in filenames:
            if filename.endswith(".py"):
                yield f"{dir}/{filename[:-3]}"
def main():
    parser = ArgumentParser(
        prog="run.py",
        description="Test runner for Advent of Code solutions",
        epilog="Enjoy the challenge!"
    )

    parser.add_argument("mode", choices=["test", "run","full"] , help="Test solution on examples or run command on samples")
    parser.add_argument("task", type=str, choices=list(get_available_days()), help="Which day's solution to execute")
    parser.add_argument("-v", "--verbosity", action="count", help="Increase output verbosity", default=0)
    args = parser.parse_args()

    module_path = f"tasks.{args.task}".replace("/", ".")
    

    logger.setLevel(level=logging.ERROR - max(0, 10 * args.verbosity))

    module = import_module(module_path)
    module.logger = logger

    data_dir = f"tasks/{args.task}"

    test_count, errors = 0, 0
    if args.mode == "test" or args.mode == "full":
        for file in os.listdir(data_dir):
            if file.startswith("input"):
                output_file = file.replace("input", "output")
                if not os.path.isfile(f"{data_dir}/{output_file}"):
                    logger.warning(f"{COLOR_WARNING}No output file found for {file}{COLOR_END}")
                    continue

                logger.info(f"Testing {file} against {output_file}.")
                with open(f"{data_dir}/{output_file}", "r") as f:
                    expected_output = f.read().strip()
                
                output =  module.run(f"{data_dir}/{file}")
                if output != expected_output:
                    logger.error(f"{COLOR_ERROR} failed! Expected: {repr(expected_output)}, Got: {repr(output)}{COLOR_END}")
                    errors += 1
                else:
                    logger.info("Passed!")
                test_count += 1
                
        print(f"Tests run: {test_count}, \tErrors: {errors}")
    if args.mode == "run" or args.mode == "full":
        datapath = f"{data_dir}/data"
        if os.path.isfile(datapath) == False:
            higher_level_path =  f"tasks/{args.task[0:args.task.index("/")]}/data"
            if os.path.isfile(higher_level_path) == False:
              logger.error(f"{COLOR_ERROR}No data file found at {datapath}{COLOR_END}")
              return
            else:
                datapath  = higher_level_path
        
        if errors > 0:
            logger.error("Do not starting work on full data due to errors in test runs")
            return
        output =  module.run(datapath)
        print(f"Response: {output}")

if __name__ == "__main__":
    main() 