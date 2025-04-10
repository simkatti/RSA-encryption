## Instruction for use

### Installation
1. `git clone git@github.com:simkatti/RSA-encryption.git`
2. `cd RSA-encryption`
3. `pip install poetry`
4. `poetry install`
5. `poetry run python3 src/app.py`
6. `poetry run pytest src/tests` (for running tests)

### Running the program and inputs
Run the program from terminal with `poetry run python3 src/app.py`. 

The program allows user to input 1-190 character message. The program will display a warning message if the input is empty or exceeding 190 characters. After the user has input the message, user can then generate keys by pressing `GENERATE KEYS` button (this can take a few seconds). 

The public and private key will be displayed on the screen. The program will also create a `keys.txt` file where user can find the keys. The file can be found in the src folder. User can then encrypt the message by pressing `ENCRYPT MESSAGE` button. 

This will show the message input and allow user to input the public key. The public key has to be in format `n, e`, like it was previously displayed on the screen or in the generated file. If the key or format is wrong, a warning message will display on the screen. The public key input field can also be empty if the user doesn't want to go through the hassle of copy pasting the keys. 

`ENCRYPT MESSAGE` button will reveal the encrypted message. This is a large int. User can then decrypt the message by pressing the button `DECRYPT MESSAGE`.

The encrypted message will be displayed again on the screen and below it is a user input field for the private key. The private key must be in format `n, d` or it can be empty. Wrong private key values will display a warning and won't allow uesr to continue. 

`DECRYPT MESSAGE` will show the decrypted message which should be the original message that the user input. Below the decrypted message is `Write a new message` button which takes user back to the start.

User can exit the program by closing the window.
