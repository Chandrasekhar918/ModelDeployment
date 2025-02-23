from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def support_form():
    # Get pre-filled values from URL parameters
    wifi_id = request.args.get("wifiid", "")
    email = request.args.get("email", "")
    description = request.args.get("description", "")

    if request.method == "POST":
        wifi_id = request.form["txtName"]
        email = request.form["txtEmail"]
        description = request.form["txtMsg"]

        return f"""
        <div class="container contact-form">
            <div class="text-center">
                <h2 style="color: green;">✅ Ticket raised successfully!</h2>
                <p><strong>WiFi ID:</strong> {wifi_id}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Message:</strong> {description}</p>
                <a href="/" style="text-decoration: none;">
                    <button style="padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px;">Raise Another Ticket</button>
                </a>
            </div>
        </div>
        """

    return render_template_string(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Raise a Support Ticket</title>

        <!-- Bootstrap CSS -->
        <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet">
        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

        <style>
            body {{
                background: url('https://t3.ftcdn.net/jpg/08/57/67/90/360_F_857679043_h9mry2jV7jCKJgUHYPF5eXPso7lizS5E.jpg') no-repeat center center fixed;
                background-size: cover;
            }}
            .contact-form {{
                background: #fff;
                margin-top: 10%;
                padding: 20px;
                width: 50%;
                border-radius: 10px;
            }}
            .contact-form h3 {{
                text-align: center;
                color: #0062cc;
            }}
            .contact-form .btnContact {{
                width: 100%;
                border: none;
                border-radius: 1rem;
                padding: 1.5%;
                background: #dc3545;
                font-weight: 600;
                color: #fff;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>

    <div class="container contact-form">
        <h3>Submit a Ticket</h3>
        <form method="post">
            <div class="form-group">
                <input type="text" name="txtName" class="form-control" placeholder="WiFi ID *" value="{wifi_id}" required />
            </div>
            <div class="form-group">
                <input type="email" name="txtEmail" class="form-control" placeholder="Email *" value="{email}" required />
            </div>
            <div class="form-group">
                <textarea name="txtMsg" class="form-control" placeholder="Description *" required>{description}</textarea>
            </div>
            <div class="form-group">
                <input type="submit" class="btnContact" value="Submit" />
            </div>
        </form>
    </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
