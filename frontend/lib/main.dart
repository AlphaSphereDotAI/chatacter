import 'dart:convert';

import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';
// import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

Future<Map<String, dynamic>> getResponse(String query) async {
  final response = await http.post(Uri.parse("https://8000-01hqrk1qr2p3w6cc5np0wk0ys5.cloudspaces.litng.ai/predict?query='$query'"));
  if (response.statusCode == 200) {
    Map<String, dynamic> data = jsonDecode(jsonDecode(response.body));
    return data;
  } else {
    throw Exception('Failed to load data');
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a purple toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.
        colorScheme: const ColorScheme(
          primary: Colors.black,
          secondary: Colors.red,
          surface: Colors.white,
          background: Color.fromARGB(255, 255, 255, 255),
          error: Colors.red,
          onPrimary: Colors.white,
          onSecondary: Colors.white,
          onSurface: Colors.black,
          onBackground: Colors.black,
          onError: Colors.white,
          brightness: Brightness.light,
        ),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Chatacter Alpha Version'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.
  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  late String _message;
  late String _response = '';
  updateMessage(String value) {
    print('The value is: $value');
    setState(() {
      _message = value;
    });
  }

  submitValue(String value) {
    print('submit: $value');
    getResponse(value).then((response) {
      print(response);
      setState(() {
        _response = response['response'];
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        elevation: 50,
        leading: IconButton(
          onPressed: () => print('Menu button pressed'),
          icon: Icon(Icons.menu, color: Theme.of(context).colorScheme.primary),
        ),
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            AnimatedTextKit(
              animatedTexts: [
                TypewriterAnimatedText(
                  'Chatacter Alpha Version\nYou are now chatting with Napoleon AI\nType your message below and press send to get a response\n\n$_response',
                  textStyle: const TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Colors.black,
                    // fontFamily: GoogleFonts.jetBrainsMono().fontFamily,
                  ),
                  speed: const Duration(milliseconds: 100),
                ),
              ],
              repeatForever: false,
              isRepeatingAnimation: false,
            ),
            Text(
              _response,
              style: const TextStyle(
                fontWeight: FontWeight.bold,
                fontFamily: 'JetBrainsMono',
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: Padding(
        padding: EdgeInsets.only(bottom: MediaQuery.of(context).viewInsets.bottom),
        child: Container(
          margin: const EdgeInsets.all(10),
          child: Row(
            children: [
              Expanded(
                child: TextField(
                  decoration: const InputDecoration(
                    hintText: 'Message...',
                    hintStyle: TextStyle(color: Color.fromARGB(255, 0, 0, 0)),
                    border: OutlineInputBorder(borderSide: BorderSide(color: Colors.black)),
                  ),
                  onChanged: updateMessage,
                ),
              ),
              TextButton(
                onPressed: () => submitValue(_message),
                onHover: (value) {
                  print('Hovering over the button');
                },
                // elevation: 0,
                child: const Icon(
                  Icons.send,
                  color: Color.fromARGB(255, 0, 0, 0),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
