<h1>Wall API</h1>

<h2>a real world open source example of django-rest-framework (DRF)</h2>

<h2>Some Features</h2>
<ul>
    <li>Compliance with the principles of test writing DRF</li>
    <li>Compliance with the principles of clean coding</li>
    <li>Documented and visualized by Swagger</li>
</ul>

<h2>Getting Started</h2>

<p>To get a local copy of the project up and running, follow these simple steps:</p>

<h3>1. Clone the Repository</h3>
<p>Open your terminal and run the following command to clone the repository:</p>
<pre><code>git clone https://github.com/realsoli/wall-api.git</code></pre>

<h3>2. Navigate to the Project Directory</h3>
<p>Change into the project directory where <code>manage.py</code> is located:</p>
<pre><code>cd wall-api</code></pre>

<h3>3. Set Up a Virtual Environment</h3>
<p>Create and activate a virtual environment:</p>
<ul>
    <li><strong>On Windows:</strong></li>
    <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
    <li><strong>On Linux/macOS:</strong></li>
    <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>
</ul>

<h3>4. Install Dependencies</h3>
<p>Install the required dependencies using <code>pip</code>:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>5. Collect Static Files</h3>
<p>Run the following command to collect static files:</p>
<pre><code>python manage.py collectstatic</code></pre>

<h3>6. Run the Development Server</h3>
<p>Start the Django development server with:</p>
<pre><code>python manage.py runserver --settings=wall.settings.dev</code></pre>

<h3>7. Access API Documentation</h3>
<p>Visit the following URL to view the API documentation:</p>
<p><a href="http://127.0.0.1:8000/swagger/">http://127.0.0.1:8000/swagger/</a></p>

<h2>Contributing</h2>
<p>Contributions are welcome! To gain a deeper understanding of API and DRF, fork the project and participate in its development.</p>

