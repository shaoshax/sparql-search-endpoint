from flask import Flask, request, jsonify
from owlready2 import *
from flask_cors import CORS

# 將本體加載到owlready2
onto = get_ontology("ar.owl").load()

# 初始化Flask應用
app = Flask(__name__)
CORS(app)

@app.route('/sparql', methods=['POST'])
def sparql_endpoint():
    query = request.form.get('query')
    print(query)
    if not query:
        return jsonify({"error": "No SPARQL query provided"}), 400

    try:
        # 使用owlready2執行SPARQL查詢
        results = list(default_world.sparql(query))
        flag = results[0][1] == "owl.NamedIndividual"
        print(flag)
        # 將查詢結果格式化為JSON
        json_results = []
        if flag:
            for result in results:
                json_results.append([str(item) for item in result])
                print(result)
        else:
            for result in results:
                json_results.append([str(item).split("#")[1] for item in result])
                print(result)
            
        print(json_results)
        return jsonify({"results": json_results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



