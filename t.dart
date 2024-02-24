import 'dart:convert';
import 'package:http/http.dart' as http;
import 'dart:io';

String hfKey = Platform.environment['HUGGINGFACE_KEY']!;

Future<String> query(String Q, String model) async {
  Map<String, String> envVars = Platform.environment;
  print(envVars.values);
  var client = http.Client();
  try {
    var response = await client.post(
      Uri.https('api-inference.huggingface.co', '/models/$model'),
      headers: {
        "Authorization": "Bearer $hfKey",
        "Content-Type": "application/json",
      },
      body: jsonEncode({"inputs": Q}),
    );
    var r = jsonDecode(response.body);
    return r[0]['generated_text'];
  }  finally {
    client.close();
  }
}

main() async {
  print(await query("I love you", "google/gemma-7b-it"));
}
