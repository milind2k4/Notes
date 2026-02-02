Links: [[02 Operating System Structure]]
___
# System Calls and Linux Commands

A **System Call** is the programmatic mechanism through which a user's application (running in **User Mode**) requests a service from the Operating System's kernel (running in **Kernel Mode**).

This is the only way for a user program to perform privileged operations like accessing hardware, managing files, or creating new processes.

[[02 Operating System Structure#Kernel Mode vs. User Mode]]

A system call is essentially a controlled, protected "jump" from user mode to kernel mode and back.

#### How System Calls Work (The Flow)

1.  **Application Call:** A user program calls a standard C library function (e.g., `fopen()`, `read()`, `fork()`).
2.  **Library Stub:** This library function is a "stub." It sets up the system call parameters (e.g., putting a specific system call number into a CPU register).
3.  **Trap:** The stub function executes a special `TRAP` (or `INT` for interrupt) instruction. This is a software interrupt that tells the CPU to switch to kernel mode.
4.  **Interrupt Handler:** The CPU, now in kernel mode, finds the kernel's interrupt handler.
5.  **System Call Handler:** The handler uses the system call number (from the register) to look up the correct kernel function in a "system call table."
6.  **Kernel Executes:** The kernel's function (e.g., the _real_ code for `read()`) runs, performing the requested operation (e.g., accessing the disk driver).
7.  **Return:** The kernel places the result (e.g., the data read) into a register.
8.  **Switch Back:** The kernel executes a special `RTI` (Return from Interrupt) instruction.
9.  **User Mode Resumes:** The CPU switches back to user mode, and the C library function returns the result to the application.

### Types of System Calls

System calls are grouped by the services they provide:

- **Process Control:**
  - `fork()`: Creates a new child process.
  - `exec()`: Replaces the current process's code with a new program.
  - `wait()`: A parent process waits for a child process to terminate.
  - `exit()`: Terminates the current process.
- **File Management:**
  - `open()`: Opens a file for reading or writing.
  - `read()`: Reads data from an open file.
  - `write()`: Writes data to an open file.
  - `close()`: Closes an open file.
- **Device Management:**
  - `ioctl()`: (Input/Output Control) A general-purpose call to manage device parameters.
- **Information Maintenance:**
  - `getpid()`: Get the current Process ID.
  - `getppid()`: Get the Parent Process ID.
  - `gettimeofday()`: Get the current time.
- **Communication (Inter-Process Communication - IPC):**
  - `pipe()`: Creates a simple communication channel between two processes.
  - `socket()`: Creates a network communication endpoint.
  - `shmget()`: Allocates a shared memory segment.

## Elementary Linux Commands

The **shell** (like `bash`) is the command-line interpreter that reads and executes these commands.

#### File and Directory Navigation

- `pwd` (Print Working Directory): Shows your current location.
- `ls` (List): Lists files and directories.
  - `ls -l`: Long-listing (shows permissions, owner, size, date).
  - `ls -a`: Lists all files, including hidden ones (starting with `.`).
- `cd` (Change Directory): Moves you to a different directory.
  - `cd /home/user`: Go to an absolute path.
  - `cd Documents`: Go to a relative path (a folder inside your current one).
  - `cd ..`: Go up one directory.
  - `cd ~` or `cd`: Go to your home directory.

#### File and Directory Manipulation

- `touch <filename>`: Creates a new, empty file.
- `mkdir <dirname>`: Creates a new directory.
- `cp <source> <destination>`: Copies a file.
  - `cp file.txt file_backup.txt`
  - `cp -r <dir_source> <dir_dest>`: Copies a directory recursively.
- `mv <source> <destination>`: Moves or renames a file/directory.
  - `mv oldname.txt newname.txt` (Rename)
  - `mv file.txt ../` (Move to parent directory)
- `rm <filename>`: Removes (deletes) a file.
- `rmdir <dirname>`: Removes an _empty_ directory.
- `rm -r <dirname>`: Removes a directory and all its contents (Recursive). **Use with caution!**

#### Viewing Files

- `cat <filename>`: Concatenates and prints the entire file to the screen.
- `less <filename>`: Shows the file page-by-page. (Use `q` to quit, arrows to scroll).
- `head <filename>`: Shows the first 10 lines of a file.
- `tail <filename>`: Shows the last 10 lines of a file.
  - `tail -f <logfile>`: "Follows" the file, showing new lines as they are added.

#### Process Management

- `ps` (Process Status): Lists your current processes.
  - `ps aux`: Shows all processes running on the system.
- `top`: Shows a real-time, interactive list of running processes (like Task Manager).
- `kill <PID>`: Sends a signal to a Process ID to terminate it.

#### User and System

- `whoami`: Prints your current username.
- `man <command>`: Shows the manual (help page) for a command.
- `chmod <options> <filename>`: Changes the permissions of a file.
  - `chmod u+x script.sh`: Adds "execute" permission for the "user".
- `sudo <command>`: Runs a command as the "superuser" (administrator).

## Shell Scripting

A shell script is simply a text file containing a list of Linux commands. It's used to automate repetitive tasks.

#### "Hello World" Script

1.  Create a file `hello.sh`:

    ```sh
    #!/bin/bash

    # This is a comment
    echo "Hello, World!"
    ```

    - `#!/bin/bash`: This first line is called a **shebang**. It tells the OS which interpreter (`/bin/bash`) to use to run the script.

2.  Make it executable:

    ```sh
    chmod u+x hello.sh
    ```

3.  Run the script:
    ```sh
    ./hello.sh
    ```
    _Output:_ `Hello, World!`

### Basic Syntax

#### Variables

- **Assignment:** `VARNAME="Value"` (No spaces around the `=`)
- **Access:** `$VARNAME`

```sh
#!/bin/bash
NAME="Alice"
echo "Hello, $NAME"
```

#### Control Flow Example (If-Else & Loop)

```sh
#!/bin/bash

# Check if a directory exists
if [ -d "backup" ]; then
    echo "Backup directory exists."
else
    mkdir backup
    echo "Created backup directory."
fi

# Loop through files and copy them
for file in *.txt; do
    cp "$file" "backup/$file.bak"
    echo "Backed up $file"
done
```
