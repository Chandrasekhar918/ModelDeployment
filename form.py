from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/support-form", methods=["GET", "POST"])
def support_form():
    if request.method == "POST":
        wifiid= request.form["txtName"]
        email = request.form["txtEmail"]
        phone = request.form["txtPhone"]
        description = request.form["txtMsg"]

        return f"""
        <div class="container contact-form">
            <div class="text-center">
                <h2 style="color: green;">✅ Ticket raised successfully!</h2>
                <p><strong>Wifi-Id:</strong> {wifiid}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Message:</strong> {description}</p>
                <a href="/support-form" style="text-decoration: none;">
                    <button style="padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px;">Raise Another Ticket</button>
                </a>
            </div>
        </div>
        """

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Raise a Support Ticket</title>

        <!-- Bootstrap CSS -->
        <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
        <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

        <style>
           
            body {
                  background: url('https://t3.ftcdn.net/jpg/08/57/67/90/360_F_857679043_h9mry2jV7jCKJgUHYPF5eXPso7lizS5E.jpg') no-repeat center center fixed;
                  background-size: cover;
                  }

            .contact-form {
                background: #fff;
                margin-top: 10%;
                margin-bottom: 5%;
                width: 70%;
            }
            .contact-form .form-control {
                border-radius: 1rem;
            }
            .contact-image {
                text-align: center;
            }
            .contact-image img {
                border-radius: 6rem;
                width: 11%;
                margin-top: -3%;
               
            }
            .contact-form form {
                padding: 14%;
            }
            .contact-form form .row {
                margin-bottom: -7%;
            }
            .contact-form h3 {
                margin-bottom: 8%;
                margin-top: -10%;
                text-align: center;
                color: #0062cc;
            }
            .contact-form .btnContact {
                width: 50%;
                border: none;
                border-radius: 1rem;
                padding: 1.5%;
                background: #dc3545;
                font-weight: 600;
                color: #fff;
                cursor: pointer;
            }
        </style>
    </head>
    <body>

    <div class="container contact-form">
        <div class="contact-image">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUya-24WmnajoU5o9rngS5XsBs0X14MKupTg&s" alt="rocket_contact"/>
        </div>
        <form method="post">
            <h3>Submit a ticket</h3>
            <div class="row">
                <div class="col-md-6">
                    <div class="form-group">
                        <input type="text" name="txtName" class="form-control" placeholder="Wifi_ID *" required />
                    </div>
                    <div class="form-group">
                        <input type="text" name="txtEmail" class="form-control" placeholder="Email *" required />
                    </div>
                    <div class="form-group">
                        <input type="text" name="txtPhone" class="form-control" placeholder="Phone Number *" required />
                    </div>
                    <div class="form-group">
                        <input type="submit" name="btnSubmit" class="btnContact" value="Submit" />
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group">
                        <textarea name="txtMsg" class="form-control" placeholder="Description *" required style="width: 100%; height: 150px;"></textarea>
                    </div>
                </div>
            </div>
        </form>
    </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
