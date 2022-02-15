class Adventure(Checks):
    def spawn_tiny(self):
        return self.spawn("python3 adventure.py Tiny")

    def spawn_small(self):
        return self.spawn("python3 adventure.py Small")

    def spawn_crowther(self):
        return self.spawn("python3 adventure.py Crowther")

    @check()
    def exists(self):
        """Checking if all files exist."""
        self.require("adventure.py", "room.py")

        # self.add can't create directories :(
        # give v3 pls
        cwd = os.getcwd()
        dest = os.path.join(cwd, "data")
        if os.path.exists(dest):
            os.rename(dest, dest + str(uuid.uuid4()))
        os.mkdir(dest)
        with check50.cd(check50.config.check_dir):
            data_files = [os.path.join("data", data_file) for data_file in os.listdir("data")]
            for path in data_files:
                check50.copy(path, dest)

    @check("exists")
    def handles_argument(self):
        """Starting adventure with command line argument 'Tiny'."""
        try:
            self.spawn_tiny().stdout(re.escape(room_1_description), str_output=room_1_description)
        except Error as error:
            raise Error(rationale=f"Expected the description of initial "
                                  f"room when Adventure starts.\n    {error}")

    @check("handles_argument")
    def rejects_incorrect_arguments(self):
        """Rejects incorrect amount of arguments or wrong filename."""
        try:
            self.spawn("python3 adventure.py").exit(1)
        except Error as error:
            raise Error(rationale=f"Expected an exit code of 1. Not {error}")

        try:
            self.spawn("python3 adventure.py Tiny CS50").exit(1)
        except Error as error:
            raise Error(rationale=f"Expected an exit code of 1. Not {error}")

        try:
            self.spawn("python3 adventure.py CS50").exit(1)
        except Error as error:
            raise Error(rationale=f"Expected an exit code of 1. Not {error}")

    @check("handles_argument")
    def move_once(self):
        """Starting Adventure then moving once to the WEST."""
        try:
            self.spawn_tiny().stdout(re.escape(room_1_description), str_output=room_1_description)
        except Error as error:
            raise Error(rationale=f"Expected the description of initial "
                                  f"room when Adventure starts.\n    {error}")

        self.spawn_tiny().stdin("WEST").stdout(re.escape(room_2_description), str_output=room_2_description)
