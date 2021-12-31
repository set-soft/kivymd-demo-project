import configparser
from dataclasses import dataclass
import argparse


@dataclass
class ReplaceAndroidArch:
    arch: str
    spec_file: str = "buildozer.spec"

    def replace(self):
        config = configparser.ConfigParser()
        config.read(self.spec_file)
        config["app"]["android.arch"] = self.arch

        with open(self.spec_file, "w") as f:
            config.write(f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Get the target android architecture")
    parser.add_argument("--arch", type=str)
    args = parser.parse_args()

    # Replace
    ReplaceAndroidArch(arch=args.arch).replace()
