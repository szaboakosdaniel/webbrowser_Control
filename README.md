# Socket Communication Android App and Server

This project includes both an Android application and a server script that demonstrate simple socket communication. The Android app sends different messages to the server using buttons, establishing a socket connection and sending messages over it.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project showcases how to establish a socket connection between an Android application and a server. The Android app sends messages to the server through different buttons, while the server receives and processes these messages.

## Installation

1. Clone or download the repository to your local machine.
2. For the Android app:
   - Open the project in Android Studio.
   - Build and run the application on an Android emulator or physical device.
   - Enter the appropriate IP address and port of the server in the `serverIP` and `serverPort` variables in the `MainActivity` class.
3. For the server script:
   - Run the server script on a machine with the appropriate IP address and port configuration.

## Usage

### Android App

1. Launch the application on your Android device.
2. Enter the server's IP address and port in the app.
3. The app contains three buttons - "Send Hello", "Send Korte", and "Send Alma". Each button sends a specific message to the server upon clicking.

### Server Script

1. Run the server script on a machine with Python installed.
2. The server script binds to a specified IP address and port and waits for incoming connections.
3. Upon receiving messages from the Android app, the server processes and responds to these messages.

## Functionality

- The Android app establishes a socket connection to the server using a separate network thread.
- Buttons on the app UI allow you to send different messages to the server.
- The networking operations are carried out on separate threads to prevent blocking the main UI thread.
- The server script listens for incoming connections, receives and processes messages, and responds to the client.

## Contributing

Contributions to this project are welcome. Feel free to submit issues and pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or discussions, you can reach out to the author at [szaboakosdaniel@gmail.com](mailto:your_email@example.com).

---

Feel free to customize the content and details as needed for your specific project. This combined README provides a comprehensive overview of both the Android app and the server components of your project.