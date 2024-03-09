<h1>Sign Language Detection</h1>
Sign language is an essential form of communication for individuals with hearing impairments. This project focuses on developing a sign language detection model that can recognize and interpret various sign language gestures.  <br>
This project aims to detect hand signs for sign language using two different models - one based on LSTM and another using Teachable Machine. The LSTM model is implemented in <b>`app.py`</b>, allowing real-time hand sign detection through your computer's camera. The second model, based on Teachable Machine, is implemented in <b>`testlstm.py`</b>. This model utilizes a pre-trained model generated using your custom dataset of hand sign images. Both models are capable of real-time sign language detection.

<h2>Features</h2>
<ol>
    <li><b>Real-time Detection:</b> Both models provide real-time sign language detection using the computer's camera, enabling instant communication through gestures.</li>
    <li><b>Customizable Models:</b> The LSTM model allows users to train and customize the system for specific sign language gestures by using their own datasets.</li>
    <li><b>Fine-tuning Capability:</b> The Teachable Machine model, based on a pre-trained model, can be fine-tuned on custom datasets, providing adaptability to different sign language variations.</li>
    <li><b>Adaptability:</b> The Teachable Machine model is adaptable to different sign language variations, enabling users to create models for specific contexts.</li>
    <li><b>Extensibility:</b> The codebase is open for exploration and modification, allowing users to extend the functionality, integrate additional features, or experiment with different architectures.</li>
</ol>

<h2>Requirements</h2>
<ul>
    <li>Python 3.6 or later</li>
    <li>TensorFlow 2.x</li>
    <li>OpenCV</li>
    <li>Other dependencies can be installed using <b>`requirements.txt`</b></li>
</ul>

<h2>Installation</h2>
To run the Sign language detector locally, follow these steps:
<ol>
  <li>Clone or download this repository to your local machine.</li>
  <li>Install the required dependencies: <code>pip install -r requirements.txt</code></li>
  <li>Download the pre-trained models or train your own.</li>
</ol>

<h2>Usage</h2>
<h3>LSTM Model (app.py)</h3>
<ol>
    <li>Run the following command to start the application: <code>python app.py</code></li>
    <li>The camera will open, and you can perform hand signs in front of it. The application will detect and display the corresponding sign.</li>
</ol>
<h3>Teachable Machine Model (testlstm.py)</h3>
<ol>
    <li>Run the following command to test the LSTM model using Teachable Machine: <code>python testlstm.py</code></li>
    <li>The camera will open, and you can perform hand signs in front of it. The application will detect and display the corresponding sign.</li>
</ol>
<h2>Custom Dataset</h2>
The models were trained using a custom dataset of hand sign images, located in the <b>dataset</b> directory. The dataset includes diverse examples to improve the model's accuracy and generalization.
<h2>Note</h2>
Make sure your camera is properly configured and accessible for real-time sign language detection.
<br>
Feel free to explore and modify the code according to your requirements. If you encounter any issues or have suggestions for improvement, please create an issue in the repository.
<h2>Contributions</h2>
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
<ul>
    <li>Fork the repository.</li>
    <li>Create a new branch.</li>
    <li>Make your changes and commit them.</li>
    <li>Push your changes to your forked repository.</li>
    <li>Submit a pull request describing the changes you've made.</li>
</ul>
