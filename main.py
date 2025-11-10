import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import os



def extract():
    response = requests.get(
        url='https://app.scrapingbee.com/api/v1',
        params={
            'api_key': 'YOUR_SCRAPPING.BEE_API_HERE',
            'url': 'https://www.pbte.edu.pk/result.aspx',
            'premium_proxy': 'true',
            'country_code': 'pk',
            'render_js': 'false'
        },
    )
    with open('output.html', 'w') as f:
    	f.write(response.text)
print('html saved successfully')


app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True  #  Enables formatted JSON output

@app.route("/pbte_result", methods=["GET"])
def get_courses():
    try:
        print("HTML Extracted by ScrapingBee;")
        extract()

        #  Read saved HTML and parse
        with open("output.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, "html.parser")
        select_tag = soup.find("select", id="cmbcat")
        if not select_tag:
            return jsonify({"error": "Course dropdown not found"}), 404

        courses_dict = {
            opt["value"]: opt.get_text(strip=True)
            for opt in select_tag.find_all("option")
        }
        courses_list = list(courses_dict.values())

        result_status = ("Your result has been announced!" if "DAE" in courses_list  else "Your Result is NOT announced yet!")

        return jsonify({
            "courses_dict": courses_dict,
            "courses_list": courses_list,
            "total_courses": len(courses_list),
            "result_status": result_status,
            "html_saved_to": os.path.abspath("output.html")
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080)
