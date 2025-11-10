import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import os





# scraping Bee api:
# 4OP91TAOK2RYQGWVKQCRK22H463I802KWM6PNWFLA4KTLQG9VB1S05RM4CWPHASK963L9YUCC5MGOD49
#


def extract():
    response = requests.get(
        url='https://app.scrapingbee.com/api/v1',
        params={
            'api_key': '2APHXZKJ7S7TPTZCN2WTUKNLMD9M5BZV3FI6HFU6H4V6MEZQJMFMZQTWRTIEFOQ1LVCCL8W4NKWYC9IP',
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

ZENROWS_API_KEY = "3eda5c89e7981954492cf01ca8eb4943b976c671"  # Replace with your ZenRows key

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