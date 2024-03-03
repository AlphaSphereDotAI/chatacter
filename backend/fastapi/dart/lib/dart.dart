import 'dart:convert';

import 'package:http/http.dart' as http;

Future<Map<String, dynamic>> getResponse(String query) async {
  final response = await http.post(Uri.parse("http://localhost:8000/predict?query='$query'"));
  if (response.statusCode == 200) {
    Map<String, dynamic> data = jsonDecode(jsonDecode(response.body));
    return data;
  } else {
    throw Exception('Failed to load data');
  }
}

void main() async {
  final response = await http.post(Uri.parse("http://localhost:8000/predict?query='What is the meaning of life?'"));

  if (response.statusCode == 200) {
    // If the server returns a 200 OK response, parse the JSON.
    Map<String, dynamic> data = jsonDecode(jsonDecode(response.body));
    for (var item in data.keys) {
      print('key: ${data[item]}');
    }
  } else {
    // If the server did not return a 200 OK response, throw an exception.
    throw Exception('Failed to load data');
  }
}
