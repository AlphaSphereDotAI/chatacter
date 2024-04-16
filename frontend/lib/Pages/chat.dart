import 'dart:async';
import 'dart:convert';

import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Chat extends StatefulWidget {
  const Chat({super.key});
  @override
  State<Chat> createState() => _ChatState();
}

Future<List> getResponse(String query) async {// https://8000-01hqrk1qr2p3w6cc5np0wk0ys5.cloudspaces.litng.ai
  final response = await http.post(Uri.parse("http://127.0.0.1:8000/predict?query='$query'"));
  if (response.statusCode == 200) {
    List data = jsonDecode(response.body);
    return data;
  } else {
    throw Exception('Failed to load data');
  }
}

class _ChatState extends State<Chat> {
  late String _message;
  late List _response = [];
  bool isVisible = true;
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
        _response = response;
        _message = '';
      });
    });
  }

  @override
  void initState() {
    super.initState();
    startTimer();
  }

  void startTimer() {
    const oneSec = Duration(seconds: 10);
    // Adjust the duration based on the speed of the typewriter animation
    Timer.periodic(oneSec, (Timer timer) {
      if (mounted) {
        setState(() {
          isVisible = false;
        });
        timer.cancel();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        elevation: 50,
        leading: IconButton(
          onPressed: () {
            print('Back to home');
            Navigator.pop(context);
          },
          icon: Icon(Icons.arrow_back, color: Theme.of(context).colorScheme.primary),
        ),
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: const Text('Chatting'),
      ),
      body: SingleChildScrollView(
        scrollDirection: Axis.vertical,
        child: Center(
          child: Row(
            children: [
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Visibility(
                    visible: isVisible,
                    child: AnimatedTextKit(
                      animatedTexts: [
                        TypewriterAnimatedText(
                          'Chatacter Alpha Version\nYou are now chatting with Napoleon\nType your message below and\npress send to get a response\nIt may take time due to server starting\n',
                          textStyle: const TextStyle(
                            fontWeight: FontWeight.bold,
                            fontSize: 30,
                          ),
                          textAlign: TextAlign.center,
                        ),
                      ],
                      isRepeatingAnimation: false,
                    ),
                  ),
                  Container(
                    margin: const EdgeInsets.fromLTRB(10, 10, 10, 10),
                    width: MediaQuery.of(context).size.width * 0.8,
                    child: Text(
                      'Napoleon Bonaparte: $_response',
                      style: const TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 20,
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
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
                    border: OutlineInputBorder(),
                  ),
                  onChanged: updateMessage,
                ),
              ),
              TextButton(
                onPressed: () => submitValue(_message),
                onHover: (value) {
                  print('Hovering over the button');
                },
                child: const Icon(
                  Icons.send,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
