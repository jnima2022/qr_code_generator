# QR Code Generator

This project is a simple QR Code Generator web app built with Flask for the backend and HTML/CSS/JavaScript for the frontend. Users can input text or URLs, customize the size and background color, and generate a downloadable QR code. It also features a dark mode toggle for a better user experience.

## Demo
[Click here to watch the demo](https://private-user-images.githubusercontent.com/121528869/413193370-b25c8221-a3f6-4bc2-a2b6-9a11f99c83ef.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk1MTYzMzQsIm5iZiI6MTczOTUxNjAzNCwicGF0aCI6Ii8xMjE1Mjg4NjkvNDEzMTkzMzcwLWIyNWM4MjIxLWEzZjYtNGJjMi1hMmI2LTlhMTFmOTljODNlZi5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMjE0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDIxNFQwNjUzNTRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mMjk5MjFjNTVlYTg5OWEyYTBmZjdhZmU5Mzk1OGMyZTc3NGIyOWVlZmIzMjk2NzJkNWViODViZTAyOTNiNDA0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Sfr1FVGbYacmhNDFmlpc7Z6yljtE6lBQXlWWy8UZQdM)

## Features

- Generate QR codes from URLs or text.
- Customize QR code size and background color.
- Choose between different file formats (PNG, SVG).
- Toggle between Light and Dark modes with a stylish button.
- Reset the form to clear input and QR code preview.
- Responsive: Works on both desktop and mobile devices.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: python, Flask, QRCode library (for generating QR codes)

## How to Use

1. Enter a URL or text in the input field.
2. Select the desired QR code size (Small, Medium, Large).
3. Choose a background color using the color picker.
4. Pick a QR code format (PNG or SVG).
5. Click on "Generate QR Code" to generate the QR code.
6. Optionally, download the QR code by clicking the download link.
7. Toggle between Light and Dark modes using the button.

## Setup Instructions

1. Clone this repository to your local machine:
    git clone <https://github.com/jnima2022/qr_code_generator.git>

2. Navigate to the project folder:
    cd qr-code-generator

3. Install the required dependencies:
    pip install -r requirements.txt

4. Run the app.py file

5. Open your browser and navigate to http://127.0.0.1:5000/ to access the app.

## Skills Shown

- Flask: Creating a backend with Flask to serve the QR code generation functionality.
- HTML: Structuring the webpage with forms, buttons, and images.
- CSS: Styling the page with responsive design and implementing dark mode toggle.
- JavaScript: Managing dynamic content, handling button events, and interacting with an external API for QR code generation.
- Responsive Design: Ensuring the website is mobile-friendly using flexible layouts.
- User Interface Design: Creating an intuitive and clean UI with interactive features.
- Dark Mode: Implementing a toggle for switching between light and dark modes to enhance user experience.

## Future Improvements

- File Upload Support: Add the ability for users to upload files (images, videos, audio files, etc.) and generate a QR code that links to the uploaded file. This will require integration with cloud storage services (e.g., AWS S3, Google Cloud Storage, etc.) to store and retrieve files securely.
- Add Foreground Color Customization: Allow users to customize the color of the QR code foreground.
- File Format Options: Allow the user to choose multiple formats for the QR code download (e.g., JPG, PDF).